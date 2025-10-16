# Ejercicios MF0488_3 — Gestión de incidentes de seguridad informática

A continuación se presentan los **10 ejercicios prácticos** relacionados con MF0488 del certificado de profesionalidad IFCT0109, orientados a la gestión de incidentes de seguridad mediante scripting en Python.

---

## 🧩 Ejercicio 1 — Detector de phishing
Desarrolla un script que analice mensajes de correo electrónico para detectar indicadores de phishing.  
Debe:
- Buscar palabras clave sospechosas (urgente, verificar cuenta, etc.).
- Detectar URLs y direcciones de email en el mensaje.
- Calcular una puntuación de riesgo.
- Clasificar el mensaje como phishing o legítimo.

---

## 🧩 Ejercicio 2 — Sistema de registro de incidentes
Crea un sistema para registrar, almacenar y listar incidentes de seguridad.  
Debe incluir:
- Registro interactivo de incidentes con campos obligatorios.
- Almacenamiento en formato JSON.
- Listado de todos los incidentes registrados.
- Clasificación por severidad (BAJA, MEDIA, ALTA, CRÍTICA).

---

## 🧩 Ejercicio 3 — Analizador de hashes (detección de malware)
Implementa un script que calcule hashes MD5 y SHA256 de archivos y los compare con una base de datos de malware conocido.  
Debe:
- Calcular hashes de archivos.
- Comparar con base de datos de hashes maliciosos.
- Identificar el archivo EICAR de prueba.
- Reportar si se detecta malware conocido.

---

## 🧩 Ejercicio 4 — Monitor de integridad de archivos
Desarrolla un sistema de monitorización de integridad basado en hashes.  
Debe:
- Crear una línea base (baseline) con hashes de archivos críticos.
- Verificar la integridad comparando con la línea base.
- Detectar archivos modificados o eliminados.
- Generar alertas cuando se detecten cambios.

---

## 🧩 Ejercicio 5 — Generador de informes HTML
Crea un script que genere informes profesionales en HTML a partir de los incidentes registrados.  
Debe incluir:
- Estadísticas agregadas (total, por severidad, por tipo).
- Diseño responsive con CSS inline.
- Detalle de cada incidente con colores según severidad.
- Generación automática de gráficos visuales.

---

## 🧩 Ejercicio 6 — Analizador de logs de acceso
Implementa un analizador de logs Apache/Nginx para detectar patrones de ataque.  
Debe detectar:
- Intentos de fuerza bruta (múltiples 401/403).
- Escaneos de vulnerabilidades (muchas rutas diferentes).
- Ataques comunes (SQL injection, XSS, path traversal).
- Top de IPs más activas.

---

## 🧩 Ejercicio 7 — Sistema de notificaciones por email
Desarrolla un sistema de notificaciones automáticas de incidentes (simulado).  
Debe:
- Generar emails formateados según severidad del incidente.
- Incluir toda la información relevante del incidente.
- Definir tiempos de respuesta según severidad.
- Simular el envío de notificaciones.

---

## 🧩 Ejercicio 8 — Simulador de respuesta a incidentes (NIST)
Crea un simulador interactivo que guíe a través de las 4 fases del framework NIST para respuesta a incidentes.  
Debe cubrir:
- Fase 1: Preparación
- Fase 2: Detección y Análisis
- Fase 3: Contención, Erradicación y Recuperación
- Fase 4: Post-Incidente (lecciones aprendidas)
- Generación de informe completo en JSON.

---

## 🧩 Ejercicio 9 — Analizador de tráfico de red
Implementa un analizador de capturas de tráfico de red para detectar anomalías.  
Debe detectar:
- Escaneos de puertos (muchos puertos contactados desde una IP).
- Volúmenes de tráfico anormalmente altos.
- Conexiones a puertos comúnmente usados por malware.
- Distribución de protocolos.
- Top de IPs más activas.

---

## 🧩 Ejercicio 10 — Dashboard interactivo de incidentes
Desarrolla un dashboard en terminal para visualizar estadísticas de incidentes de forma interactiva.  
Debe incluir:
- Gráficos de barras ASCII visuales.
- Estadísticas por severidad, estado y tipo.
- Filtros interactivos (por severidad, estado, tipo).
- Listado de incidentes recientes.
- Actualización en tiempo real de los datos.

---
