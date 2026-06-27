import bisect

class FenwickTree:
    def __init__(self, n):
        self.tree = [0] * (n + 1)
    def update(self, i, delta):
        i += 1
        while i < len(self.tree):
            self.tree[i] += delta
            i += i & (-i)
    def query(self, i):
        i += 1
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & (-i)
        return s

def solve(colors, queries):
    n = len(colors)
    breaks = sorted([i for i in range(n) if colors[i] == colors[(i + 1) % n]])
    
    def get_len(i):
        idx = bisect.bisect_left(breaks, i)
        nxt = breaks[idx] if idx < len(breaks) else breaks[0] + n
        return (nxt - i) % n if (nxt - i) % n != 0 else n
    
    bit_count = FenwickTree(n + 1)
    bit_sum = FenwickTree(n + 1)
    
    for i in breaks:
        prev = breaks[breaks.index(i) - 1] if breaks.index(i) > 0 else breaks[-1] - n
        length = i - prev
        bit_count.update(length, 1)
        bit_sum.update(length, length)
        
    results = []
    for q in queries:
        if q[0] == 1:
            k = q[1]
            if not breaks:
                results.append(n if k <= n else 0)
            else:
                total = bit_sum.query(n) - bit_sum.query(k - 1) - (k - 1) * (bit_count.query(n) - bit_count.query(k - 1))
                results.append(total)
        else:
            idx, c = q[1], q[2]
            if colors[idx] == c: continue
            
            for i in [idx - 1, idx]:
                pos = i % n
                if pos in breaks:
                    prev = breaks[breaks.index(pos) - 1] if breaks.index(pos) > 0 else breaks[-1] - n
                    length = pos - prev
                    bit_count.update(length, -1)
                    bit_sum.update(length, -length)
                    breaks.remove(pos)
            
            colors[idx] = c
            for i in [idx - 1, idx]:
                pos = i % n
                if colors[pos] == colors[(pos + 1) % n]:
                    bisect.insort(breaks, pos)
            
            for i in [idx - 1, idx]:
                pos = i % n
                if pos in breaks:
                    prev = breaks[breaks.index(pos) - 1] if breaks.index(pos) > 0 else breaks[-1] - n
                    length = pos - prev
                    bit_count.update(length, 1)
                    bit_sum.update(length, length)
    return results
