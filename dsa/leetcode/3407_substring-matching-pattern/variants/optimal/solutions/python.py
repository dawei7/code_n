def solve(s: str, p: str) -> bool:
    prefix, suffix = p.split("*")
    prefix_start = s.find(prefix)
    return prefix_start != -1 and s.find(suffix, prefix_start + len(prefix)) != -1
