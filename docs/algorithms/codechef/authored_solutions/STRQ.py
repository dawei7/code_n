import sys
from array import array


CHARS = "chef"
INDEX = {ch: i for i, ch in enumerate(CHARS)}
PAIRS = [(a, b) for a in range(4) for b in range(4) if a != b]
PAIR_INDEX = {pair: i for i, pair in enumerate(PAIRS)}


def main() -> None:
    buffer = sys.stdin.buffer
    text = buffer.readline().strip().decode()
    n = len(text)

    count_prefix = [array("i", [0]) for _ in range(4)]
    pair_prefix = [array("q", [0]) for _ in PAIRS]
    counts = [0] * 4
    pairs = [0] * len(PAIRS)

    for ch in text:
        current = INDEX[ch]
        for left in range(4):
            if left != current:
                pairs[PAIR_INDEX[(left, current)]] += counts[left]
        counts[current] += 1
        for i in range(4):
            count_prefix[i].append(counts[i])
        for i, value in enumerate(pairs):
            pair_prefix[i].append(value)

    q = int(buffer.readline())
    out: list[str] = []
    for _ in range(q):
        a_s, b_s, l_s, r_s = buffer.readline().split()
        a = INDEX[a_s.decode()]
        b = INDEX[b_s.decode()]
        left = int(l_s)
        right = int(r_s)
        pair_id = PAIR_INDEX[(a, b)]
        total = pair_prefix[pair_id][right] - pair_prefix[pair_id][left - 1]
        before_a = count_prefix[a][left - 1]
        inside_b = count_prefix[b][right] - count_prefix[b][left - 1]
        out.append(str(total - before_a * inside_b))

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
