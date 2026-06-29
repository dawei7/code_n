def min_window(s, t):
    from collections import Counter
    need = Counter(t)
    window = {}
    have, need_total = (0, len(need))
    res, resLen = ([-1, -1], float('inf'))
    l = 0
    for r, ch in enumerate(s):
        window[ch] = window.get(ch, 0) + 1
        if ch in need and window[ch] == need[ch]:
            have += 1
        while have == need_total:
            if r - l + 1 < resLen:
                res = [l, r]
                resLen = r - l + 1
            window[s[l]] -= 1
            if s[l] in need and window[s[l]] < need[s[l]]:
                have -= 1
            l += 1
    return res if resLen != float('inf') else None

def solve():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])
    s = data[2]
    t = data[3]
    from collections import Counter
    s_count = Counter(s)
    t_count = Counter(t)
    for ch in t_count:
        if s_count.get(ch, 0) < t_count[ch]:
            sys.stdout.write('IMPOSSIBLE')
            return
    res = min_window(s, t)
    if res:
        l, r = res
        substring = s[l:r + 1]
        sys.stdout.write(str(len(substring)) + '\n' + substring)
    else:
        sys.stdout.write('IMPOSSIBLE')


if __name__ == "__main__":
    solve()
