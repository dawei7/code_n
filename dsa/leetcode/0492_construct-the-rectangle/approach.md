## General

The area condition requires `L * W = area`, so `L` and `W` must form an integer factor pair. The condition `L >= W` means `W` is the smaller factor. Among all such pairs, the one with the smallest difference lies closest to a square.

To see why, write `L = area / W` for a valid divisor `W`. As `W` grows from `1` toward `sqrt(area)`, `L` decreases while `W` increases. Their difference

$$
\frac{\textit{area}}{W} - W
$$

therefore becomes smaller. Once `W` exceeds the square root, the factors swap order and violate the chosen `L >= W` orientation. Consequently, the desired width is the largest divisor of `area` that does not exceed `sqrt(area)`.

**Start at the closest possible width.** The code computes `w = int(sqrt(area))`. For a positive number, converting the nonnegative square root to an integer truncates the fractional part, giving `floor(sqrt(area))`. No legal width satisfying `W <= L` can be greater than this value: if `W > sqrt(area)` and `L >= W`, then `L * W > area`, contradicting the required product.

If this initial `w` divides the area, it is immediately the largest divisor at or below the square root. Otherwise the loop decrements one candidate at a time until `area % w == 0`. The remainder test is exact integer arithmetic: a zero remainder means `w` is a valid width and `area // w` is its matching integer length.

The search is guaranteed to stop. Every positive integer is divisible by `1`, and the width moves downward toward one. Thus prime areas naturally reach `w = 1` and return `[area, 1]`.

**Why the first divisor is optimal.** The loop examines widths in strictly descending order beginning at the maximum possible width. The first divisor found is therefore the greatest feasible `W`. For fixed area and widths at most the square root, increasing `W` decreases `L = area / W` and increases `W` itself, bringing the dimensions closer together. No later, smaller divisor can have a smaller difference.

The returned pair is `[area // w, w]`. Its product is exactly `area` by divisibility. Because `w <= sqrt(area)`,

$$
\frac{\textit{area}}{w} \ge w,
$$

so the first returned component is a legal length `L >= W`. The maximal-width argument proves its difference is minimal among all legal factor pairs.

For `area = 4`, `sqrt(4) = 2` and two divides the area immediately, producing `[2, 2]` with difference zero. For prime `area = 37`, the candidates descend until one, producing `[37, 1]`. For `area = 122122`, the first divisor found below the square root is `286`, and the matching length is `427`.

It helps to trace a smaller non-square example. For `area = 30`, the starting width is `floor(sqrt(30)) = 5`. Because `30 % 5 == 0`, the loop stops immediately and returns `[6, 5]`. Other legal oriented pairs are `[10, 3]`, `[15, 2]`, and `[30, 1]`; their differences are seven, thirteen, and twenty-nine, all larger than one. For `area = 32`, the starting width five does not divide, so the loop tries four next. Four divides, yielding `[8, 4]`. The trace shows that the loop is not approximating dimensions with the square root: the square root only supplies the best starting boundary, and exact divisibility selects the valid pair.

There cannot be a second, better factor pair hidden above the square root. Every divisor `d > sqrt(area)` is paired with `area / d < sqrt(area)`. Orienting that same rectangle to satisfy `L >= W` simply names `d` as the length and its paired smaller divisor as the width. It is therefore already represented by the search on the lower side of the square root. Searching both sides would examine every rectangle twice.

This method avoids generating, storing, or sorting all factor pairs. Once the closest width is found, the corresponding length is uniquely determined by integer division.

One implementation detail is the use of floating-point `sqrt`. The constraint `area <= 10^7` is far below the range where ordinary double-precision square root has integer-boundary ambiguity, so `int(sqrt(area))` is reliable here. For unrestricted huge integers, an exact integer-square-root function would avoid all floating-point concerns.

## Complexity detail

The loop starts at approximately `sqrt(area)` and may decrement to one. In the worst case, such as a prime area, it performs $O(\sqrt{\textit{area}})$ divisibility tests. Each test is treated as constant-time under the standard fixed-width integer model, giving the manifest's $O(\sqrt{\textit{area}})$ time bound.

The algorithm stores only `w` and the returned two integers, so auxiliary space is $O(1)$. The output itself also has constant size.

## Alternatives and edge cases

- **Search upward from one:** Every divisor can be remembered as the latest width, but this always scans to the square root. Descending search can stop as soon as the optimal divisor appears.
- **Enumerate all factor pairs:** This is unnecessary because factor closeness is monotonic as the smaller factor approaches the square root.
- **Exact integer square root:** `math.isqrt(area)` would compute the starting width without floating point and is preferable if the numeric constraint were much larger.
- **Perfect square:** The square root divides immediately, returning equal dimensions and the minimum possible difference zero.
- **Prime area:** Only one is a feasible width below the square root, so the answer is `[area, 1]`.
- **`area = 1`:** The starting width is one and the result is `[1, 1]`.
- **Ordering requirement:** Returning `[w, area // w]` would reverse length and width for non-square areas. The source returns the larger quotient first.
- **Guaranteed termination:** Width one divides every positive area, so the decrement loop cannot pass below one under the stated constraints.
