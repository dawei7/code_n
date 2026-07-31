def solve(s: str) -> str:
    if "@" in s:
        name, domain = s.lower().split("@")
        return name[0] + "*****" + name[-1] + "@" + domain

    digits = "".join(character for character in s if character.isdigit())
    country_length = len(digits) - 10
    local_mask = "***-***-" + digits[-4:]
    if country_length == 0:
        return local_mask
    return "+" + "*" * country_length + "-" + local_mask
