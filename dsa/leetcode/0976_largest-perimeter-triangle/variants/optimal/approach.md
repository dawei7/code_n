## General
**Reduce validity to one inequality:** For sorted positive sides $a\le b\le c$, the inequalities $a+c>b$ and $b+c>a$ hold automatically. Only $a+b>c$ needs to be tested.

**Inspect consecutive descending triples:** Sort all lengths from largest to smallest. Consider three consecutive values `nums[i]`, `nums[i + 1]`, and `nums[i + 2]`. If the two smaller values sum to more than the largest, they form a triangle. Return their perimeter immediately.

**Why the first valid triple is optimal:** At a fixed largest side `nums[i]`, the next two entries are the greatest available companions. If even they cannot exceed the largest side when added, replacing either with a later, no-larger value cannot help, so no triangle using that largest side exists. When a consecutive triple does satisfy the inequality, it has the greatest perimeter possible with its largest side. Every later triple has each component no larger, so none can produce a greater perimeter. Thus the first valid consecutive triple is globally optimal.

If the scan finishes without finding one, every possible choice fails: for each potential largest side, its two greatest remaining companions were already insufficient.

## Complexity detail
Sorting $N$ lengths costs $O(N\log N)$ time, and the subsequent scan is $O(N)$. Python's sorted copy uses $O(N)$ space. The scan itself uses constant additional space.

## Alternatives and edge cases
- **Enumerate all triples:** Testing every three-index combination is direct but costs $O(N^3)$ time.
- **Frequency counting:** Because lengths are bounded, a frequency array can avoid comparison sorting, but it uses space proportional to the value range and complicates selecting repeated sides.
- **Degenerate equality:** Sides satisfying $a+b=c$ have zero area and must be rejected because the inequality is strict.
- **Repeated lengths:** Equal sides are valid when backed by distinct entries, including equilateral triangles.
- **No valid triple:** Exhausting the descending scan proves that no selection works, so the required result is `0`.
