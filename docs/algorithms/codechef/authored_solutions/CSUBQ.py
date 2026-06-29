import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, q, low_limit, high_limit = data[0], data[1], data[2], data[3]
    size = 1
    while size < n:
        size <<= 1

    seg_len = [0] * (2 * size)
    for i in range(size, 2 * size):
        seg_len[i] = 1 if i - size < n else 0
    for i in range(size - 1, 0, -1):
        seg_len[i] = seg_len[i << 1] + seg_len[i << 1 | 1]

    lp = [0] * (2 * size)
    ls = [0] * (2 * size)
    lc = [0] * (2 * size)
    hp = [0] * (2 * size)
    hs = [0] * (2 * size)
    hc = [0] * (2 * size)
    for i in range(size, size + n):
        lp[i] = ls[i] = lc[i] = 1
        hp[i] = hs[i] = hc[i] = 1
    for i in range(size - 1, 0, -1):
        length_left = seg_len[i << 1]
        length_right = seg_len[i << 1 | 1]
        left = i << 1
        right = left | 1

        lp[i] = lp[left] if lp[left] < length_left else length_left + lp[right]
        ls[i] = ls[right] if ls[right] < length_right else length_right + ls[left]
        lc[i] = lc[left] + lc[right] + ls[left] * lp[right]

        hp[i] = hp[left] if hp[left] < length_left else length_left + hp[right]
        hs[i] = hs[right] if hs[right] < length_right else length_right + hs[left]
        hc[i] = hc[left] + hc[right] + hs[left] * hp[right]

    def pull(i: int) -> None:
        left = i << 1
        right = left | 1
        length_left = seg_len[left]
        length_right = seg_len[right]
        lp[i] = lp[left] if lp[left] < length_left else length_left + lp[right]
        ls[i] = ls[right] if ls[right] < length_right else length_right + ls[left]
        lc[i] = lc[left] + lc[right] + ls[left] * lp[right]
        hp[i] = hp[left] if hp[left] < length_left else length_left + hp[right]
        hs[i] = hs[right] if hs[right] < length_right else length_right + hs[left]
        hc[i] = hc[left] + hc[right] + hs[left] * hp[right]

    def update(pos: int, value: int) -> None:
        idx = size + pos - 1
        low_ok = 1 if value < low_limit else 0
        high_ok = 1 if value <= high_limit else 0
        lp[idx] = ls[idx] = lc[idx] = low_ok
        hp[idx] = hs[idx] = hc[idx] = high_ok
        idx >>= 1
        while idx:
            pull(idx)
            idx >>= 1

    def merge(a_len: int, a_p: int, a_s: int, a_c: int, b_len: int, b_p: int, b_s: int, b_c: int):
        length = a_len + b_len
        pref = a_p if a_p < a_len else a_len + b_p
        suff = b_s if b_s < b_len else b_len + a_s
        count = a_c + b_c + a_s * b_p
        return length, pref, suff, count

    def query(prefix: list[int], suffix: list[int], count: list[int], left_pos: int, right_pos: int) -> int:
        left_pos += size - 1
        right_pos += size - 1
        llen = lpref = lsuff = lcnt = 0
        rlen = rpref = rsuff = rcnt = 0
        while left_pos <= right_pos:
            if left_pos & 1:
                llen, lpref, lsuff, lcnt = merge(
                    llen, lpref, lsuff, lcnt,
                    seg_len[left_pos], prefix[left_pos], suffix[left_pos], count[left_pos],
                )
                left_pos += 1
            if not (right_pos & 1):
                rlen, rpref, rsuff, rcnt = merge(
                    seg_len[right_pos], prefix[right_pos], suffix[right_pos], count[right_pos],
                    rlen, rpref, rsuff, rcnt,
                )
                right_pos -= 1
            left_pos >>= 1
            right_pos >>= 1
        return merge(llen, lpref, lsuff, lcnt, rlen, rpref, rsuff, rcnt)[3]

    idx = 4
    out: list[str] = []
    for _ in range(q):
        typ, a, b = data[idx], data[idx + 1], data[idx + 2]
        idx += 3
        if typ == 1:
            update(a, b)
        else:
            out.append(str(query(hp, hs, hc, a, b) - query(lp, ls, lc, a, b)))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
