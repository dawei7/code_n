def solve(s: str, t: str) -> bool:
    if len(s) > len(t):
        return False

    exact = 0
    changed = -1
    target_length = len(s)

    for character in t:
        previous_exact = exact
        previous_changed = changed

        if previous_changed >= 0 and previous_changed < target_length and s[previous_changed] == character:
            changed = previous_changed + 1

        if previous_exact < target_length:
            changed = max(changed, previous_exact + 1)
            if s[previous_exact] == character:
                exact = previous_exact + 1

        if exact == target_length or changed == target_length:
            return True

    return False
