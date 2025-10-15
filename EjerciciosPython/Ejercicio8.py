def compare_firewall_rules(file1, file2):
    with open(file1) as f1, open(file2) as f2:
        rules1 = set(f1.read().splitlines())
        rules2 = set(f2.read().splitlines())

    added = rules2 - rules1
    removed = rules1 - rules2

    print("Reglas añadidas:", added)
    print("Reglas eliminadas:", removed)

if __name__ == "__main__":
    compare_firewall_rules("firewall_old.txt", "firewall_new.txt")
