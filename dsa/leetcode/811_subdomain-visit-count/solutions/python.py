from collections import Counter


def solve(cpdomains: list[str]) -> list[str]:
    visits: Counter[str] = Counter()
    for entry in cpdomains:
        count_text, domain = entry.split()
        count = int(count_text)
        while True:
            visits[domain] += count
            dot = domain.find(".")
            if dot == -1:
                break
            domain = domain[dot + 1 :]
    return [f"{count} {domain}" for domain, count in visits.items()]
