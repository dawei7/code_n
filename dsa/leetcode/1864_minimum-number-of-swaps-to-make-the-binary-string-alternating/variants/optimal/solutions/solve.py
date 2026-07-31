def solve(s: str) -> int:
    zero_count = s.count("0")
    one_count = len(s) - zero_count
    if abs(zero_count - one_count) > 1:
        return -1

    def swaps_for(start: str) -> int:
        mismatches = 0
        expected = start
        for character in s:
            if character != expected:
                mismatches += 1
            expected = "1" if expected == "0" else "0"
        return mismatches // 2

    if zero_count > one_count:
        return swaps_for("0")
    if one_count > zero_count:
        return swaps_for("1")
    return min(swaps_for("0"), swaps_for("1"))
