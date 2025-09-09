# 🛡️ 1APSEINPRO - 1Aplicación de seguridad informática para probar

Una aplicación educativa en Python que implementa ejercicios prácticos de seguridad informática organizados por módulos temáticos. Diseñada como herramienta de aprendizaje.

## 📋 Descripción

Esta aplicación consiste en un sistema de menús interactivo que incluye ejercicios prácticos relacionados con la seguridad informática:

- **0486**: Seguridad en equipos informáticos
- **0487**: Auditoría de seguridad informática  
- **0488**: Gestión de incidentes de seguridad informática
- **0489**: Sistemas seguros de acceso y transmisión de datos
- **0490**: Gestión de servicios en el sistema informático

## 🚀 Instalación y ejecución

### Opción 1: Ejecución automática (recomendada)
```bash
python run_app.py
```
Este script automáticamente:
- Crea un entorno virtual Python
- Instala las dependencias necesarias
- Ejecuta la aplicación principal

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

# Ejecutar aplicación
python main.py
```

## 📦 Dependencias

Las dependencias están definidas en `requirements.txt`:
- `cryptography`: Para ejercicios de cifrado y descifrado
- `psutil`: Para monitorización de sistema

## 🔧 Estructura del proyecto

```
├── main.py                 # Menú principal de la aplicación
├── run_app.py             # Script de ejecución automática
├── requirements.txt       # Dependencias del proyecto
├── mod_0486.py           # Seguridad en equipos informáticos
├── mod_0487.py           # Auditoría de seguridad informática
├── mod_0488.py           # Gestión de incidentes
├── mod_0489.py           # Sistemas seguros de acceso
└── mod_0490.py           # Gestión de servicios
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
