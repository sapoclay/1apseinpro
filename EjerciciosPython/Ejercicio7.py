from collections import Counter

def analyze_logs(filename):
    with open(filename) as f:
        ips = [line.split()[0] for line in f if line.strip()]
    count = Counter(ips)
    suspicious = {ip: c for ip, c in count.items() if c > 50}
    print("IPs sospechosas (más de 50 accesos):")
    for ip, c in suspicious.items():
        print(f"{ip} -> {c} accesos")

if __name__ == "__main__":
    analyze_logs("access.log")
