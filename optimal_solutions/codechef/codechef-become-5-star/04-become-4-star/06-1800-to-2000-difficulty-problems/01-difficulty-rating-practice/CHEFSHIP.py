import sys
MOD1 = 1000000007
MOD2 = 1000000009
BASE = 911382323

def build_hash(s: bytes, mod: int):
    pref = [0] * (len(s) + 1)
    power = [1] * (len(s) + 1)
    for i, ch in enumerate(s, 1):
        pref[i] = (pref[i - 1] * BASE + ch) % mod
        power[i] = power[i - 1] * BASE % mod
    return (pref, power)

def get_hash(pref, power, left: int, right: int, mod: int) -> int:
    return (pref[right] - pref[left] * power[right - left]) % mod

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for s in data[1:1 + t]:
        n = len(s)
        half = n // 2
        pref1, pow1 = build_hash(s, MOD1)
        pref2, pow2 = build_hash(s, MOD2)
        ans = 0
        for first_len in range(1, half):
            second_len = half - first_len
            if get_hash(pref1, pow1, 0, first_len, MOD1) == get_hash(pref1, pow1, first_len, 2 * first_len, MOD1) and get_hash(pref2, pow2, 0, first_len, MOD2) == get_hash(pref2, pow2, first_len, 2 * first_len, MOD2) and (get_hash(pref1, pow1, 2 * first_len, 2 * first_len + second_len, MOD1) == get_hash(pref1, pow1, 2 * first_len + second_len, n, MOD1)) and (get_hash(pref2, pow2, 2 * first_len, 2 * first_len + second_len, MOD2) == get_hash(pref2, pow2, 2 * first_len + second_len, n, MOD2)):
                ans += 1
        out.append(str(ans))
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
