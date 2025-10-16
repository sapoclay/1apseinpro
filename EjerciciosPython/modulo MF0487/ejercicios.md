# Ejercicios MF0487 — Auditoría de seguridad informática

A continuación se presentan los **10 ejercicios prácticos** relacionados con MF0487 del certificado de profesionalidad IFCT0109, orientados a aplicar los conocimientos teóricos mediante scripting en Python.

---

## 🧩 Ejercicio 1 — Escáner de puertos (básico)
Desarrolla un script en Python que recorra un rango de puertos para una dirección IP o dominio y determine cuáles están abiertos.  
Debe:
- Utilizar el módulo `socket`.
- Aceptar entrada del usuario (host y rango).
- Mostrar los puertos abiertos al final.

---

## 🧩 Ejercicio 2 — Ping y traceroute automatizado
Crea un programa que realice **ping** y **traceroute** a varios hosts, guardando los resultados en un archivo CSV.  
Debe incluir:
- Ping a cada host con estadísticas.
- Traceroute para cada host.
- Registro de resultados en formato CSV.

---

## 🧩 Ejercicio 3 — Escaneo web simple
Implementa un script que detecte vulnerabilidades web básicas:  
- Inyección SQL (`' or '1'='1`).  
- XSS (`<script>alert(1)</script>`).  
- Directorios comunes (admin/, login/, robots.txt).  
Debe reportar si encuentra posibles anomalías.

---

## 🧩 Ejercicio 4 — Análisis de dependencias (Python)
Crea un analizador que lea un archivo `requirements.txt` y consulte las versiones más recientes de los paquetes en PyPI.  
Debe generar un informe indicando:
- Nombre del paquete.
- Versión instalada vs. versión más reciente.
- Indicar si hay dependencias desactualizadas.

---

## 🧩 Ejercicio 5 — Generador de plan de auditoría
Construye un script que permita generar un **plan de auditoría** interactivo en formato JSON.  
Debe solicitar al usuario:
- Alcance.  
- Criterios y normativa aplicable.  
- Recursos.  
- Fases.  
- Indicadores de éxito.

---

## 🧩 Ejercicio 6 — Auditoría integral automatizada
Integra los ejercicios anteriores en un flujo completo de auditoría:  
- Escaneo de puertos.  
- Detección de rutas web comunes.  
- Clasificación del riesgo.  
- Exportación del resultado en `informe_integral.json`.

---

## 🧩 Ejercicio 7 — Análisis de logs
Escribe un programa que analice un archivo `access.log` y detecte IPs con actividad anómala.  
Debe:
- Contar accesos por IP.  
- Considerar sospechosas las IPs con más de 50 accesos.  
- Mostrar las IPs y número de accesos detectados.

---

## 🧩 Ejercicio 8 — Comparador de configuración de firewall
Desarrolla un script que compare dos archivos de configuración (`firewall_old.txt` y `firewall_new.txt`).  
Debe:
- Detectar reglas nuevas.  
- Detectar reglas eliminadas.  
- Mostrar las diferencias por pantalla.

---

## 🧩 Ejercicio 9 — Evaluación cuantitativa de riesgo
Usando los resultados del informe integral, calcula un **índice de riesgo** según probabilidad e impacto.  
Debe:
- Leer el archivo JSON con resultados.  
- Calcular Riesgo = Probabilidad × Impacto.  
- Clasificar el nivel de riesgo (bajo, medio, alto).

---

## 🧩 Ejercicio 10 — Generador automático de informe PDF
Genera un informe de auditoría profesional en formato PDF a partir de los datos de `informe_integral.json`.  
Debe incluir:
- Título, resumen y resultados.  
- Secciones por categoría.  
- Recomendaciones finales.

---


