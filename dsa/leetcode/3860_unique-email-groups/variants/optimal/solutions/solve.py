def solve(emails: list[str]) -> int:
    normalized = set()

    for email in emails:
        local, domain = email.split("@")
        local = local.split("+", 1)[0].replace(".", "").lower()
        normalized.add(f"{local}@{domain.lower()}")

    return len(normalized)
