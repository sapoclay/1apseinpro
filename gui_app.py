import threading
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

from mod_0486 import (
    analizar_eicar_core,
    hardening_sistema_info,
    politicas_contrasenas_info,
    backup_directorio_core,
)
from mod_0487 import (
    ejecutar_nmap,
    simulacion_auditoria_info,
    prueba_contrasenas_info,
    generar_informe_auditoria,
)
from mod_0488 import (
    phishing_analisis_core,
    registro_incidente_core,
    analisis_forense_core,
    plan_respuesta_core,
)
from mod_0489 import (
    cifrar_archivo_core,
    descifrar_archivo_core,
    generar_mfa_key,
)
from mod_0490 import (
    snapshot_recursos,
    estados_servicios,
    crear_log_centralizado,
)


class SecurityAppGUI(tk.Tk):
    """Interfaz gráfica que replica las opciones del menú en terminal."""

    def __init__(self):
        super().__init__()
        self.title("Aplicación de Seguridad Informática")
        self.geometry("1000x700")
        self.resizable(True, True)

        self.monitor_activo = False
        self.monitor_lock = threading.Lock()

        self._build_widgets()

    # ------------------------------------------------------------------
    # Construcción de la interfaz
    # ------------------------------------------------------------------
    def _build_widgets(self):
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=0)

        notebook = ttk.Notebook(self)
        notebook.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        self.output = tk.Text(self, height=10, wrap="word")
        self.output.grid(row=1, column=0, sticky="nsew", padx=10, pady=(0, 10))
        self.output.configure(state="disabled")

        self._build_mod_0486_tab(notebook)
        self._build_mod_0487_tab(notebook)
        self._build_mod_0488_tab(notebook)
        self._build_mod_0489_tab(notebook)
        self._build_mod_0490_tab(notebook)

    # ------------------------------------------------------------------
    # Utilidades
    # ------------------------------------------------------------------
    def log(self, mensaje):
        self.output.configure(state="normal")
        self.output.insert("end", mensaje + "\n")
        self.output.see("end")
        self.output.configure(state="disabled")

    def limpiar_log(self):
        self.output.configure(state="normal")
        self.output.delete("1.0", "end")
        self.output.configure(state="disabled")

    # ------------------------------------------------------------------
    # Pestaña 0486
    # ------------------------------------------------------------------
    def _build_mod_0486_tab(self, notebook):
        frame = ttk.Frame(notebook, padding=10)
        notebook.add(frame, text="0486 - Seguridad equipos")

        frame.columnconfigure(1, weight=1)

        # Analizar EICAR
        ttk.Label(frame, text="Archivo a analizar (EICAR)").grid(row=0, column=0, sticky="w")
        eicar_var = tk.StringVar()
        ttk.Entry(frame, textvariable=eicar_var).grid(row=0, column=1, sticky="ew", padx=5)
        ttk.Button(frame, text="Examinar", command=lambda: self._seleccionar_archivo(eicar_var)).grid(row=0, column=2)
        ttk.Button(frame, text="Analizar", command=lambda: self._analizar_eicar_gui(eicar_var.get())).grid(row=0, column=3, padx=5)

        # Hardening
        ttk.Button(frame, text="Mostrar recomendaciones de hardening", command=self._mostrar_hardening).grid(row=1, column=0, columnspan=4, pady=(10, 0), sticky="w")

        # Políticas de contraseñas
        ttk.Button(frame, text="Mostrar políticas de contraseñas", command=self._mostrar_politicas).grid(row=2, column=0, columnspan=4, pady=(10, 0), sticky="w")

        # Backup
        ttk.Label(frame, text="Directorio a respaldar").grid(row=3, column=0, sticky="w", pady=(15, 0))
        origen_var = tk.StringVar()
        ttk.Entry(frame, textvariable=origen_var).grid(row=3, column=1, sticky="ew", padx=5, pady=(15, 0))
        ttk.Button(frame, text="Seleccionar", command=lambda: self._seleccionar_directorio(origen_var)).grid(row=3, column=2, pady=(15, 0))

        ttk.Label(frame, text="Destino backup").grid(row=4, column=0, sticky="w")
        destino_var = tk.StringVar()
        ttk.Entry(frame, textvariable=destino_var).grid(row=4, column=1, sticky="ew", padx=5)
        ttk.Button(frame, text="Seleccionar", command=lambda: self._seleccionar_directorio(destino_var)).grid(row=4, column=2)
        ttk.Button(frame, text="Crear backup", command=lambda: self._crear_backup(origen_var.get(), destino_var.get())).grid(row=4, column=3, padx=5)

    def _analizar_eicar_gui(self, ruta):
        if not ruta:
            messagebox.showwarning("Dato requerido", "Selecciona un archivo para analizar.")
            return
        try:
            resultado = analizar_eicar_core(ruta)
            if resultado["es_eicar"]:
                self.log(f"[ALERTA] {ruta} coincide con la firma EICAR. MD5: {resultado['md5']}")
            else:
                self.log(f"[OK] {ruta} no coincide con EICAR. MD5: {resultado['md5']}")
        except Exception as exc:
            messagebox.showerror("Error", str(exc))

    def _mostrar_hardening(self):
        self.log(hardening_sistema_info())

    def _mostrar_politicas(self):
        self.log(politicas_contrasenas_info())

    def _crear_backup(self, origen, destino):
        if not origen or not destino:
            messagebox.showwarning("Datos requeridos", "Selecciona el directorio de origen y destino.")
            return
        try:
            archivo = backup_directorio_core(origen, destino)
            self.log(f"[OK] Backup creado en: {archivo}")
        except Exception as exc:
            messagebox.showerror("Error", str(exc))

    # ------------------------------------------------------------------
    # Pestaña 0487
    # ------------------------------------------------------------------
    def _build_mod_0487_tab(self, notebook):
        frame = ttk.Frame(notebook, padding=10)
        notebook.add(frame, text="0487 - Auditoría")

        frame.columnconfigure(1, weight=1)

        ttk.Label(frame, text="Host/IP a auditar").grid(row=0, column=0, sticky="w")
        host_var = tk.StringVar()
        ttk.Entry(frame, textvariable=host_var).grid(row=0, column=1, sticky="ew", padx=5)
        ttk.Button(frame, text="Escanear con nmap", command=lambda: self._ejecutar_nmap(host_var.get())).grid(row=0, column=2)
        ttk.Button(frame, text="Guía OpenVAS", command=lambda: self.log("Abre OpenVAS/GVM y documenta resultados para la IP seleccionada.")).grid(row=0, column=3, padx=5)

        ttk.Button(frame, text="Checklist de auditoría", command=lambda: self.log(simulacion_auditoria_info())).grid(row=1, column=0, columnspan=4, pady=(15, 0), sticky="w")
        ttk.Button(frame, text="Prueba de contraseñas débiles", command=lambda: self.log(prueba_contrasenas_info())).grid(row=2, column=0, columnspan=4, pady=(5, 0), sticky="w")

        ttk.Button(frame, text="Generar informe de auditoría", command=self._generar_informe_gui).grid(row=3, column=0, columnspan=4, pady=(15, 0), sticky="w")

    def _ejecutar_nmap(self, host):
        if not host:
            messagebox.showwarning("Dato requerido", "Introduce un host o IP.")
            return

        def tarea():
            try:
                salida = ejecutar_nmap(host)
                self.log(salida)
            except FileNotFoundError as exc:
                messagebox.showerror("Error", str(exc))
            except Exception as exc:
                messagebox.showerror("Error", f"No se pudo ejecutar nmap: {exc}")

        threading.Thread(target=tarea, daemon=True).start()

    def _generar_informe_gui(self):
        archivo = filedialog.asksaveasfilename(title="Guardar informe", defaultextension=".txt", filetypes=[("Texto", "*.txt"), ("Todos", "*.*")])
        if not archivo:
            return
        try:
            generar_informe_auditoria(archivo)
            self.log(f"[OK] Informe creado en {archivo}")
        except Exception as exc:
            messagebox.showerror("Error", str(exc))

    # ------------------------------------------------------------------
    # Pestaña 0488
    # ------------------------------------------------------------------
    def _build_mod_0488_tab(self, notebook):
        frame = ttk.Frame(notebook, padding=10)
        notebook.add(frame, text="0488 - Incidentes")

        frame.columnconfigure(1, weight=1)

        ttk.Button(frame, text="Analizar correo phishing", command=self._analizar_phishing_gui).grid(row=0, column=0, columnspan=2, sticky="w")

        ttk.Label(frame, text="Registro de incidente").grid(row=1, column=0, sticky="w", pady=(15, 0))
        titulo_var = tk.StringVar()
        ttk.Entry(frame, textvariable=titulo_var).grid(row=1, column=1, sticky="ew", padx=5, pady=(15, 0))
        ttk.Label(frame, text="Descripción breve").grid(row=2, column=0, sticky="w")
        descripcion_var = tk.StringVar()
        ttk.Entry(frame, textvariable=descripcion_var).grid(row=2, column=1, sticky="ew", padx=5)
        ttk.Button(frame, text="Guardar incidente", command=lambda: self._registro_incidente_gui(titulo_var.get(), descripcion_var.get())).grid(row=3, column=0, columnspan=2, pady=(5, 0), sticky="w")

        ttk.Button(frame, text="Analizar logs (fallos de acceso)", command=self._analisis_forense_gui).grid(row=4, column=0, columnspan=2, pady=(15, 0), sticky="w")
        ttk.Button(frame, text="Generar plan de respuesta", command=self._plan_respuesta_gui).grid(row=5, column=0, columnspan=2, pady=(5, 0), sticky="w")

    def _analizar_phishing_gui(self):
        ruta = filedialog.askopenfilename(title="Selecciona correo", filetypes=[("Texto", "*.txt"), ("Todos", "*.*")])
        if not ruta:
            return
        try:
            alertas = phishing_analisis_core(ruta)
            if alertas:
                self.log("[ALERTA] Indicadores de phishing:")
                for alerta in alertas:
                    self.log(f"- {alerta}")
            else:
                self.log("[OK] No se detectaron indicadores obvios de phishing.")
        except Exception as exc:
            messagebox.showerror("Error", str(exc))

    def _registro_incidente_gui(self, titulo, descripcion):
        if not titulo or not descripcion:
            messagebox.showwarning("Datos requeridos", "Introduce título y descripción.")
            return
        archivo = filedialog.asksaveasfilename(title="Guardar registro", defaultextension=".txt", filetypes=[("Texto", "*.txt"), ("Todos", "*.*")])
        if not archivo:
            return
        try:
            registro_incidente_core(titulo, descripcion, archivo)
            self.log(f"[OK] Incidente registrado en {archivo}")
        except Exception as exc:
            messagebox.showerror("Error", str(exc))

    def _analisis_forense_gui(self):
        ruta = filedialog.askopenfilename(title="Seleccionar log", filetypes=[("Log", "*.log"), ("Texto", "*.txt"), ("Todos", "*.*")])
        if not ruta:
            return
        try:
            conteo = analisis_forense_core(ruta)
            if conteo:
                self.log("IPs con intentos fallidos:")
                for ip, cantidad in conteo.items():
                    self.log(f"- {ip} ({cantidad} intentos)")
            else:
                self.log("[OK] No se detectaron intentos fallidos.")
        except Exception as exc:
            messagebox.showerror("Error", str(exc))

    def _plan_respuesta_gui(self):
        archivo = filedialog.asksaveasfilename(title="Guardar plan", defaultextension=".txt", filetypes=[("Texto", "*.txt"), ("Todos", "*.*")])
        if not archivo:
            return
        try:
            plan_respuesta_core(archivo)
            self.log(f"[OK] Plan de respuesta generado en {archivo}")
        except Exception as exc:
            messagebox.showerror("Error", str(exc))

    # ------------------------------------------------------------------
    # Pestaña 0489
    # ------------------------------------------------------------------
    def _build_mod_0489_tab(self, notebook):
        frame = ttk.Frame(notebook, padding=10)
        notebook.add(frame, text="0489 - Acceso seguro")

        ttk.Button(frame, text="Cifrar archivo", command=self._cifrar_archivo_gui).grid(row=0, column=0, sticky="w")
        ttk.Button(frame, text="Descifrar archivo", command=self._descifrar_archivo_gui).grid(row=1, column=0, sticky="w", pady=(5, 0))
        ttk.Button(frame, text="Generar clave MFA", command=lambda: self.log(f"Clave MFA: {generar_mfa_key()}"))

    def _cifrar_archivo_gui(self):
        ruta = filedialog.askopenfilename(title="Archivo a cifrar")
        if not ruta:
            return
        try:
            resultado = cifrar_archivo_core(ruta)
            self.log(f"[OK] Archivo cifrado: {resultado['archivo']}")
            self.log(f"Clave: {resultado['clave']}")
        except Exception as exc:
            messagebox.showerror("Error", str(exc))

    def _descifrar_archivo_gui(self):
        ruta = filedialog.askopenfilename(title="Archivo cifrado", filetypes=[("Archivos cifrados", "*.enc"), ("Todos", "*.*")])
        if not ruta:
            return
        clave = simple_input_dialog(self, "Clave de descifrado", "Introduce la clave en base64 generada durante el cifrado:")
        if not clave:
            return
        try:
            archivo = descifrar_archivo_core(ruta, clave)
            self.log(f"[OK] Archivo descifrado: {archivo}")
        except Exception as exc:
            messagebox.showerror("Error", str(exc))

    # ------------------------------------------------------------------
    # Pestaña 0490
    # ------------------------------------------------------------------
    def _build_mod_0490_tab(self, notebook):
        frame = ttk.Frame(notebook, padding=10)
        notebook.add(frame, text="0490 - Servicios")

        ttk.Button(frame, text="Iniciar monitor de recursos", command=self._iniciar_monitor_recursos).grid(row=0, column=0, sticky="w")
        ttk.Button(frame, text="Detener monitor", command=self._detener_monitor_recursos).grid(row=0, column=1, sticky="w", padx=(5, 0))
        ttk.Button(frame, text="Estado de servicios", command=self._mostrar_servicios_gui).grid(row=1, column=0, sticky="w", pady=(10, 0))
        ttk.Button(frame, text="Crear log centralizado", command=self._crear_log_gui).grid(row=1, column=1, sticky="w", padx=(5, 0), pady=(10, 0))

    def _iniciar_monitor_recursos(self):
        with self.monitor_lock:
            if self.monitor_activo:
                return
            self.monitor_activo = True
        self.log("Monitorización de recursos iniciada.")
        self._programar_actualizacion_recursos()

    def _detener_monitor_recursos(self):
        with self.monitor_lock:
            self.monitor_activo = False
        self.log("Monitorización de recursos detenida.")

    def _programar_actualizacion_recursos(self):
        with self.monitor_lock:
            if not self.monitor_activo:
                return
        try:
            datos = snapshot_recursos(intervalo=0)
            mensaje = f"CPU: {datos['cpu']}% | Memoria: {datos['memoria']}%"
            if datos['cpu'] > 80 or datos['memoria'] > 80:
                mensaje += " -> [ALERTA] Consumo alto"
            self.log(mensaje)
        except Exception as exc:
            self.log(f"[ERROR] No se pudo obtener la métrica: {exc}")
        finally:
            self.after(2000, self._programar_actualizacion_recursos)

    def _mostrar_servicios_gui(self):
        try:
            estados = estados_servicios()
            for info in estados:
                self.log(f"Servicio {info['servicio']}: {info['estado']}")
        except Exception as exc:
            messagebox.showerror("Error", str(exc))

    def _crear_log_gui(self):
        ruta = filedialog.askdirectory(title="Seleccionar carpeta destino")
        if not ruta:
            return
        try:
            archivo = crear_log_centralizado(ruta)
            self.log(f"[OK] Log centralizado creado en {archivo}")
        except PermissionError:
            messagebox.showerror("Error", "No tienes permisos para esa ruta. Elige un directorio dentro de tu usuario o del proyecto.")
        except Exception as exc:
            messagebox.showerror("Error", str(exc))

    # ------------------------------------------------------------------
    # Helpers de selección
    # ------------------------------------------------------------------
    def _seleccionar_archivo(self, var):
        ruta = filedialog.askopenfilename(title="Seleccionar archivo")
        if ruta:
            var.set(ruta)

    def _seleccionar_directorio(self, var):
        ruta = filedialog.askdirectory(title="Seleccionar directorio")
        if ruta:
            var.set(ruta)


def simple_input_dialog(parent, title, prompt):
    dialog = tk.Toplevel(parent)
    dialog.transient(parent)
    dialog.grab_set()
    dialog.title(title)

    ttk.Label(dialog, text=prompt, wraplength=400).grid(row=0, column=0, columnspan=2, padx=10, pady=10)
    value_var = tk.StringVar()
    entry = ttk.Entry(dialog, textvariable=value_var, width=50)
    entry.grid(row=1, column=0, columnspan=2, padx=10, pady=(0, 10))
    entry.focus()

    resultado = {"value": ""}

    def aceptar():
        resultado["value"] = value_var.get().strip()
        dialog.destroy()

    def cancelar():
        dialog.destroy()

    ttk.Button(dialog, text="Aceptar", command=aceptar).grid(row=2, column=0, padx=10, pady=10, sticky="e")
    ttk.Button(dialog, text="Cancelar", command=cancelar).grid(row=2, column=1, padx=10, pady=10, sticky="w")

    parent.wait_window(dialog)
    return resultado["value"] or None


def lanzar_gui():
    app = SecurityAppGUI()
    app.mainloop()


if __name__ == "__main__":
    lanzar_gui()
