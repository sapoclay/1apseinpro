"""Pruebas simples de seguridad web sobre una URL proporcionada."""

import requests
from urllib.parse import urljoin, urlparse


def _normalizar_url(url: str) -> str:
    url = url.strip()
    if not url:
        return ""
    if not urlparse(url).scheme:
        return f"https://{url}"
    return url


def _safe_get(url: str, **kwargs):
    try:
        return requests.get(url, timeout=5, **kwargs)
    except requests.RequestException as exc:
        print(f"[WARN] {url} no respondió correctamente: {exc}")
        return None


def test_sql_injection(url):
    payload = "' OR '1'='1"
    resp = _safe_get(url, params={"sqli": payload})
    if not resp:
        return False
    texto = resp.text.lower()
    return "error" in texto or "sql" in texto


def test_xss(url):
    payload = "<script>alert(1)</script>"
    resp = _safe_get(url, params={"xss": payload})
    if not resp:
        return False
    return payload in resp.text


def test_common_paths(url):
    paths = ["admin", "login", "robots.txt"]
    encontrados = []
    for ruta_relativa in paths:
        destino = urljoin(url.rstrip('/') + '/', ruta_relativa)
        resp = _safe_get(destino)
        if resp and resp.status_code == 200:
            encontrados.append(ruta_relativa)
    return encontrados


if __name__ == "__main__":
    entrada = input("URL base (ej. https://ejemplo.com/): ")
    target = _normalizar_url(entrada)
    if not target:
        print("[ERROR] Debes introducir una URL válida.")
    else:
        print("Probando SQLi:", test_sql_injection(target))
        print("Probando XSS:", test_xss(target))
        print("Rutas comunes encontradas:", test_common_paths(target))
