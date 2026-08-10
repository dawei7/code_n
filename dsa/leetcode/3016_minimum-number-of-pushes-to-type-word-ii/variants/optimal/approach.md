## General

**Turn the keypad layout into a collection of costs.** The important freedom in this problem is that the letters may be assigned to the eight usable keys in any way. A key can hold several letters. Its first assigned letter costs one push, its second assigned letter costs two pushes, and so on. The physical number printed on the key does not matter: every one of the eight keys offers one position costing one push, one position costing two pushes, one position costing three pushes, and so forth. Therefore the complete set of available costs begins as

$$
1,1,1,1,1,1,1,1,\;
2,2,2,2,2,2,2,2,\;
3,3,\ldots
$$

Once this is noticed, there is no need to construct an actual mapping from letters to key numbers. We only need to decide which letter frequency receives which cost.

**Count how valuable each cheap position is.** The solution first builds `Counter(word)`. If a letter occurs $f$ times and is placed in a position requiring $c$ pushes, that letter contributes $f \cdot c$ pushes to the total. Only the frequency matters; the identity of the letter does not. For example, if one letter occurs 20 times and another occurs twice, giving the first letter a one-push position and the second a two-push position costs $20 + 4 = 24$. Reversing the assignments costs $40 + 2 = 42$. Frequent letters should clearly get the cheaper positions.

The code extracts the counter's values and sorts them in descending order. Let the sorted frequencies be

$$
f_0 \ge f_1 \ge \cdots \ge f_{A-1},
$$

where $A$ is the number of distinct letters in `word`. Index $i$ receives push cost

$$
\left\lfloor \frac{i}{8} \right\rfloor + 1.
$$

Indices 0 through 7 use the eight one-push positions. Indices 8 through 15 use the eight two-push positions. Indices 16 through 23 use the eight three-push positions. The expression in the exact implementation, `i // 8 + 1`, is precisely this grouping.

**Why descending order is optimal.** Consider any assignment in which a more frequent letter, with frequency $f$, has a larger cost $c_{\text{high}}$, while a less frequent letter, with frequency $g$, has a smaller cost $c_{\text{low}}$. Here $f \ge g$ and $c_{\text{high}} > c_{\text{low}}$. Their current contribution is

$$
f c_{\text{high}} + g c_{\text{low}}.
$$

If the two letters exchange positions, their contribution becomes

$$
f c_{\text{low}} + g c_{\text{high}}.
$$

Subtracting the second quantity from the first gives

$$
(f-g)(c_{\text{high}}-c_{\text{low}}) \ge 0.
$$

Thus the exchange never makes the total worse and usually makes it smaller. Repeating this exchange removes every inversion: the largest frequencies occupy the smallest costs, the next largest frequencies occupy the next smallest costs, and so on. That is exactly the order produced by sorting the frequencies in reverse. This exchange argument proves the greedy assignment globally optimal; it is not merely a plausible heuristic.

**A concrete trace.** Suppose the distinct-letter frequencies are `[12, 9, 8, 7, 6, 5, 4, 3, 2, 1]` after sorting. The first eight values fit in one-push positions, contributing

$$
12+9+8+7+6+5+4+3=54.
$$

The remaining two values require two pushes per occurrence, contributing $2\cdot2+1\cdot2=6$. The minimum total is therefore 60. Which particular keys receive the letters is irrelevant: all eight first positions have the same price, and all eight second positions have the same price.

**What the loop accumulates.** In `for i, x in enumerate(sorted(cnt.values(), reverse=True))`, `x` is the current frequency and `i` identifies the next cheapest available position. The update

`ans += (i // 8 + 1) * x`

adds the exact contribution of that letter. The algorithm never needs to examine the original order of characters after building the counter, because typing cost is additive over occurrences and the problem permits a global remapping.

## Complexity detail

Let $N$ be the length of `word` and $A$ be its number of distinct letters. Counting frequencies takes $O(N)$ time and stores $A$ counter entries. Sorting the $A$ frequencies costs $O(A\log A)$ time and creates a list of those values. The final loop costs $O(A)$ time. The exact total is therefore

$$
O(N + A\log A)
$$

time and $O(A)$ auxiliary space.

Because `word` contains only lowercase English letters, $A \le 26$. Under that fixed-alphabet constraint, both $A\log A$ and the counter storage are bounded constants. It is consequently conventional to simplify the bounds to $O(N)$ time and $O(1)$ auxiliary space. The more explicit $A$-parameterized bounds are still useful because they explain what the Python objects actually store; “constant space” here comes from the problem's 26-letter alphabet, not from the implementation storing no data.

The returned integer is output rather than auxiliary storage. Python's arbitrary-precision integer arithmetic is harmless for the stated limits, and the maximum answer remains small enough that treating each arithmetic operation as constant time is appropriate.

## Alternatives and edge cases

- **Explicit key simulation:** One could build eight arrays of assigned letters and repeatedly select the currently shortest key, but that records layout information the answer never uses. Sorting frequencies and pairing them with the implicit cost sequence is simpler and proves the same optimum.
- **Priority queue of key depths:** A min-heap containing the next cost for each of eight keys can assign frequencies one at a time. It works, but every operation pays a heap factor and obscures the fact that the costs are simply eight copies of each positive integer.
- **Brute-force letter assignment:** Trying mappings grows combinatorially and is unnecessary because letter identities do not interact. Only the frequency-cost products matter, which is exactly the setting handled by the exchange argument.
- **Fewer than eight distinct letters:** Every used letter receives a one-push position, so the answer is just the length of `word`. The formula handles this because every relevant index has `i // 8 == 0`.
- **Exactly eight distinct letters:** All eight still cost one push. The ninth distinct letter, not the eighth, is the first one that must use a two-push position.
- **Tied frequencies:** Their relative order is irrelevant. Swapping equal frequencies leaves the total unchanged, so Python's particular ordering for ties cannot affect the answer.
- **One overwhelmingly frequent letter:** Sorting places it first and gives it a one-push position. Its particular key number is immaterial because every key has an equally cheap first slot.
- **All 26 lowercase letters:** The layout uses eight one-push slots, eight two-push slots, eight three-push slots, and two four-push slots. The expression `i // 8 + 1` naturally reaches cost four for indices 24 and 25.
- **No reconstruction:** The method returns only the minimum number of pushes, as requested. If an actual keypad mapping were required, the algorithm would also need to retain each letter beside its frequency and assign concrete keys, but that extra output is not part of this contract.
