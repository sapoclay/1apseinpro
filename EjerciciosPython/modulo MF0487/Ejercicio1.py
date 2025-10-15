import socket  # módulo para operaciones de red con sockets

def scan_ports(host: str, ports):
    """
    Escanea una secuencia de puertos en el host indicado.

    Parámetros:
    - host: nombre de dominio o dirección IP a escanear.
    - ports: iterable de puertos (ej. range(20, 1025)).

    Retorna:
    - lista de puertos que respondieron a la conexión (abiertos).
    """
    open_ports = []  # aquí vamos guardando los puertos abiertos detectados

    # Recorremos cada puerto del rango proporcionado
    for port in ports:
        
        # Creamos un socket TCP (AF_INET = IPv4, SOCK_STREAM = TCP)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Establecemos un timeout pequeño para que la operación no bloquee demasiado.
        # Si el host no responde en este tiempo, se lanza socket.timeout.
        s.settimeout(0.5)

        try:
            # Intentamos conectar al host:puerto. Si la conexión se establece,consideramos el puerto como "abierto".
            s.connect((host, port))
            open_ports.append(port)

        except (socket.timeout, ConnectionRefusedError):
            # socket.timeout: no hubo respuesta en el tiempo establecido.
            # ConnectionRefusedError: la máquina respondió pero rechazó la conexión (puerto cerrado).
            # En ambos casos ignoramos y seguimos con el siguiente puerto.
            pass

        finally:
            # Cerramos el socket en cualquier caso para liberar recursos.
            s.close()

    # Devolvemos la lista de puertos abiertos encontrados.
    return open_ports


if __name__ == "__main__":
    try:
        # Solicitamos al usuario el host a escanear. El strip() elimina espacios accidentales al inicio/final.
        host = input("Host o IP a escanear: ").strip()
        if not host:
            # Si no se proporciona host, salimos con un mensaje.
            raise SystemExit("No se proporcionó host. Saliendo...")

        # Definimos el rango de puertos por defecto a escanear. Esto es modificable según necesidades.
        ports = range(20, 1025)

        try:
            # Llamamos a la función de escaneo. socket.gaierror se lanza si el nombre de host no se puede resolver (DNS)
            open_ports = scan_ports(host, ports)
        except socket.gaierror:
            # Mensaje claro si la resolución DNS falla
            raise SystemExit(f"No se pudo resolver el host '{host}'. Revisa el nombre o la conexión.")

        # Si la lista de puertos abiertos no está vacía, la mostramos formateada.
        if open_ports:
            print(f"Se han encontrado los siguientes puertos abiertos en {host}:")
            # Unimos los puertos con coma para una lectura más agradable
            print(", ".join(str(p) for p in open_ports))

        else:
            # Mensaje personalizado cuando no se detecta ningún puerto abierto
            print(f"No se han detectado puertos abiertos en {host}.")
            print("Posibles causas:")
            print("- El host está fuera de línea o inaccesible.")
            print("- Un firewall filtra las conexiones entrantes.")
            print("- El rango de puertos escaneado no incluye servicios expuestos.")
            print()
            print("Sugerencias:")
            print("- Verifica que el host esté en línea (ej. haciendo ping).")
            print("- Prueba con un rango de puertos más amplio o específico.")
            print("- Asegúrate de tener autorización para realizar el escaneo.")

    except KeyboardInterrupt:
        # Capturamos Ctrl+C para terminar de manera elegante
        print("\nEscaneo interrumpido por el usuario.")
