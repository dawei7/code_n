import sys
from collections import Counter

def find_min_window(s, t):
    if not s or not t:
        return ''
    dict_t = Counter(t)
    required = len(dict_t)
    l, r = (0, 0)
    formed = 0
    window_counts = {}
    ans = (float('inf'), None, None)
    while r < len(s):
        character = s[r]
        window_counts[character] = window_counts.get(character, 0) + 1
        if character in dict_t and window_counts[character] == dict_t[character]:
            formed += 1
        while l <= r and formed == required:
            character = s[l]
            if r - l + 1 < ans[0]:
                ans = (r - l + 1, l, r)
            window_counts[character] -= 1
            if character in dict_t and window_counts[character] < dict_t[character]:
                formed -= 1
            l += 1
        r += 1
    return '' if ans[0] == float('inf') else s[ans[1]:ans[2] + 1]

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    t = int(data[0])
    index = 1
    outputs = []
    for _ in range(t):
        n = int(data[index])
        m = int(data[index + 1])
        index += 2
        s = data[index]
        index += 1
        t_str = data[index]
        index += 1
        res = find_min_window(s, t_str)
        outputs.append(res if res != '' else '-1')
    sys.stdout.write('\n'.join(outputs))


if __name__ == "__main__":
    solve()
