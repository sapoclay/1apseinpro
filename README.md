# 🛡️ IFCT0109 - 1Aplicación de seguridad informática para probar

<img width="1024" height="1024" alt="AFCT0109Logo" src="https://github.com/user-attachments/assets/92c8b698-32cf-4c01-9d92-852130a8182e" />

Una aplicación educativa en Python que implementa ejercicios prácticos de seguridad informática organizados por módulos temáticos. Diseñada como herramienta de aprendizaje.

## 📋 Descripción

Esta aplicación consiste en un sistema de menús interactivo que incluye ejercicios prácticos relacionados con la seguridad informática:

- **0486**: Seguridad en equipos informáticos
- **0487**: Auditoría de seguridad informática  
- **0488**: Gestión de incidentes de seguridad informática
- **0489**: Sistemas seguros de acceso y transmisión de datos
- **0490**: Gestión de servicios en el sistema informático
- **EjerciciosPython**: Colección de scripts independientes que se listan automáticamente desde el nuevo menú de ejercicios.

## 🚀 Instalación y ejecución

### Opción 1: Ejecución automática (recomendada)
```bash
python run_app.py
```
Este script automáticamente:
- Crea un entorno virtual Python
- Instala las dependencias necesarias
- Ejecuta la aplicación principal y permite elegir entre modo CLI o GUI (con `python run_app.py --gui` puedes abrir directamente la interfaz gráfica)

### Opción 2: Instalación manual
```bash
# Crear entorno virtual
python -m venv .venv

# Activar entorno virtual
# Linux/Mac:
source .venv/bin/activate
# Windows:
.venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar aplicación en modo terminal (CLI)
python main.py --cli

# Ejecutar aplicación en modo gráfico (GUI)
python main.py --gui

# También puedes lanzar la GUI directamente
python gui_app.py
```

Tras arrancar en modo CLI encontrarás una nueva opción de menú denominada "EjerciciosPython" que lista automáticamente todos los scripts ubicados en la carpeta del mismo nombre y permite ejecutarlos directamente.

## 📦 Dependencias

Las dependencias están definidas en `requirements.txt`:
- `cryptography`: Para ejercicios de cifrado y descifrado
- `psutil`: Para monitorización de sistema

## 🔧 Estructura del proyecto

```
├── main.py                 # Menú principal de la aplicación
├── run_app.py              # Script de ejecución automática
├── requirements.txt        # Dependencias del proyecto
├── gui_app.py              # Interfaz gráfica con Tkinter
├── EjerciciosPython/       # Ejercicios individuales accesibles desde el menú
│   ├── Ejercicio1.py
│   ├── Ejercicio2.py
│   └── ...
├── mod_0486.py             # Seguridad en equipos informáticos
├── mod_0487.py             # Auditoría de seguridad informática
├── mod_0488.py             # Gestión de incidentes
├── mod_0489.py             # Sistemas seguros de acceso
└── mod_0490.py             # Gestión de servicios
```

## 📚 Módulos y funcionalidades

### 🔒 0486 - Seguridad en equipos informáticos
- **Análisis de malware EICAR**: Detecta el archivo de prueba EICAR por su hash MD5
- **Hardening del sistema**: Guías para deshabilitar servicios según el SO
- **Políticas de contraseñas**: Configuración de políticas de seguridad
- **Copias de seguridad**: Creación automática de backups comprimidos

### 🔍 0487 - Auditoría de seguridad informática
- **Escaneo de vulnerabilidades**: Integración con nmap para escaneos de red
- **Simulación de auditoría**: Creación de checklists de auditoría
- **Prueba de contraseñas débiles**: Guías para usar herramientas como John the Ripper

### 🚨 0488 - Gestión de incidentes
- **Análisis de phishing**: Detección de indicadores sospechosos en correos
- **Registro de incidentes**: Sistema de logging para documentar incidentes
- **Análisis forense básico**: Herramientas básicas de investigación

### 🔐 0489 - Sistemas seguros de acceso
- **Cifrado de archivos**: Implementación con Fernet (AES)
- **Descifrado de archivos**: Recuperación de archivos cifrados
- **Gestión de claves**: Generación y manejo seguro de claves

### 📊 0490 - Gestión de servicios
- **Monitorización de recursos**: Seguimiento en tiempo real de CPU y memoria
- **Monitorización de servicios**: Verificación del estado de servicios del sistema
- **Gestión de logs**: Creación de logs centralizados

### 🧪 EjerciciosPython - Scripts individuales
- Los archivos `.py` ubicados en `EjerciciosPython/` se muestran automáticamente en el menú "EjerciciosPython" de la aplicación.
- El listado se ordena numéricamente (Ejercicio1, Ejercicio2, ...), facilitando su ejecución secuencial.
- Cada script se ejecuta en su propio contexto y puede generar salidas específicas, como informes CSV en el caso de `Ejercicio2.py`.
- Desde este menú puedes instalar las dependencias adicionales definidas en `EjerciciosPython/requeriments.txt`.

## 🖥️ Interfaz gráfica (GUI)

La interfaz gráfica (`gui_app.py`) replica todas las opciones del menú de terminal:
- Navegación por pestañas para cada módulo (0486-0490).
- Formularios y selectores de archivos/carpetas para introducir los mismos datos que se piden por consola.
- Área de salida que muestra resultados y alertas en tiempo real.
- Monitorización de recursos con actualización automática cada 2 segundos.

Puedes lanzar la GUI directamente con `python gui_app.py` o desde el lanzador principal con `python main.py --gui`.


## 🛠️ Requisitos del sistema

- Python 3.6 o superior
- Sistema operativo: Linux, Windows o macOS
- Herramientas opcionales:
  - `nmap` (para escaneos de red)
  - `john` (para pruebas de contraseñas)

## 🤝 Contribuciones

Para contribuir al proyecto:
1. Fork el repositorio
2. Crea una rama para tu funcionalidad
3. Realiza tus cambios
4. Envía un pull request

## 📄 Licencia

Este proyecto es de uso educativo. Consulta los términos de uso de las herramientas externas utilizadas.

## 🆘 Soporte

Si encuentras problemas:
1. Verifica que tienes Python 3.6+ instalado
2. Asegúrate de que las dependencias están instaladas correctamente
3. Revisa que tienes permisos para escribir archivos en el directorio de trabajo

---

**Nota**: Esta aplicación está diseñada con fines educativos para pasar el rato. No hace nada ilegal y cumple con todas las leyes que se me han ocurrido, por lo que no sirve para hacer nada ilegal ni divertido ...
