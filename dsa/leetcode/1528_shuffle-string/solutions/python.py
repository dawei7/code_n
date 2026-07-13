def solve(s, indices):
    if not s:
        return ""
    result = [""] * len(s)
    extras = []
    for i, ch in enumerate(s):
        target = indices[i] if i < len(indices) else i
        if 0 <= target < len(s) and result[target] == "":
            result[target] = ch
        else:
            extras.append(ch)
    extra_index = 0
    for i in range(len(result)):
        if result[i] == "":
            if extra_index < len(extras):
                result[i] = extras[extra_index]
                extra_index += 1
            else:
                result[i] = s[i]
    return "".join(result)
