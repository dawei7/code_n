import sys


ALPHABET = b"abcde"


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    idx = 1
    out = []
    for _ in range(t):
        n = int(data[idx])
        m = int(data[idx + 1])
        s = bytearray(data[idx + 2])
        target = data[idx + 3]
        idx += 4

        matched = 0
        for i, ch in enumerate(s):
            if ch == 63:  # ?
                best_ch = ALPHABET[0]
                best_state = m + 1
                for cand in ALPHABET:
                    nxt = matched + (matched < m and cand == target[matched])
                    if nxt < best_state:
                        best_state = nxt
                        best_ch = cand
                s[i] = best_ch
                matched = best_state
            elif matched < m and ch == target[matched]:
                matched += 1

        out.append(s.decode() if matched < m else "-1")
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
