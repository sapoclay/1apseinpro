import requests

def check_vulnerable(package):
    url = f"https://pypi.org/pypi/{package}/json"
    try:
        r = requests.get(url, timeout=5)
        if r.status_code != 200:
            return None
        info = r.json()["info"]
        return info["version"]
    except Exception:
        return None

def analyze_requirements(file="requirements.txt"):
    with open(file) as f:
        packages = [line.strip().split("==")[0] for line in f if line.strip()]
    report = {}
    for pkg in packages:
        latest = check_vulnerable(pkg)
        report[pkg] = latest or "Desconocido"
    return report

if __name__ == "__main__":
    res = analyze_requirements()
    for pkg, ver in res.items():
        print(f"{pkg}: versión más reciente {ver}")
