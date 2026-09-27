# Guided Example: Longest Subarray With Maximum Bitwise AND

The representative instance is `nums = [1, 2, 3, 3, 2, 2]`, whose required answer is `2`. It is chosen because the array contains two adjacent copies of its maximum value and several smaller values around them, so the instance forces the solver to explain *why* the smaller neighbours cannot be part of an optimal subarray even though they sit immediately next to the maximum.

## 1. The Instance and the Two Questions It Asks

The task has a two-stage shape that is easy to blur:

1. Determine the maximum bitwise AND achievable by **any** non-empty subarray. Call that value $k$.
2. Among all subarrays whose bitwise AND equals $k$, return the length of the **longest** one.

For the traced array the elements in binary are short enough to inspect directly:

| Index $i$ | `nums[i]` | Binary (`b2 b1 b0`) | Set bits |
|:---:|:---:|:---:|:---|
| 0 | `1` | `001` | bit 0 |
| 1 | `2` | `010` | bit 1 |
| 2 | `3` | `011` | bits 0 and 1 |
| 3 | `3` | `011` | bits 0 and 1 |
| 4 | `2` | `010` | bit 1 |
| 5 | `2` | `010` | bit 1 |

The largest value in the array is `3`, and the only subarrays that could plausibly reach an AND of `3` are the ones whose elements all retain both bits — that is, the neighbourhood of the two `3`s. The next two sections turn that intuition into a proof, because the rest of the method depends on it completely.

## 2. Bitwise AND Can Only Remove Set Bits

For any two non-negative integers, $x \,\&\, y$ has a set bit exactly where *both* operands have a set bit. It follows that $x \,\&\, y$ has no set bits outside $x$'s set bits, so

$$
x \,\&\, y \le x \quad \text{and} \quad x \,\&\, y \le y .
$$

Extending a subarray by one more element therefore can never increase its AND; it can only clear bits. This monotonicity is the engine of the whole lesson: **the AND of a subarray is non-increasing as the subarray grows**, and it is bounded by the smallest element in the subarray.

The table records the AND of every subarray that starts at a fixed index and extends to the right, which makes the descent visible. Each row is a chain of AND values, and each chain begins at the single-element value.

| Start index $i$ | AND chain as the end moves right | Largest AND in the chain | Reaches the global maximum `3`? |
|:---:|:---|:---:|:---:|
| 0 | `1` → `0` → `0` → `0` → `0` → `0` | 1 | no |
| 1 | `2` → `2` → `2` → `2` → `2` | 2 | no |
| 2 | `3` → `3` → `2` → `2` | 3 | yes, at lengths 1 and 2 |
| 3 | `3` → `2` → `2` | 3 | yes, at length 1 |
| 4 | `2` → `2` → `2` | 2 | no |
| 5 | `2` → `2` | 2 | no |

Two structural facts are readable straight off this table.

- Every chain is non-increasing, confirming that no extension can raise an AND.
- The first entry of each chain is the element `nums[i]` itself, so the best AND available from any start index is at least `nums[i]` and never more, because the singleton subarray `[nums[i]]` already achieves `nums[i]`.

## 3. The Maximum AND Equals the Maximum Element

Combining the two facts gives the first result.

**Upper bound.** For any subarray $S$, the AND is at most every element of $S$, hence

$$
\text{AND}(S) \le \min(S) \le \max(\text{nums}) .
$$

**Achievability.** Let $M = \max(\text{nums})$ and let $p$ be any index with `nums[p] = M`. The single-element subarray at $p$ has AND equal to $M$, so the maximum over all subarrays is at least $M$.

The two bounds meet, so

$$
k = \max(\text{nums}) .
$$

For the traced instance, $k = 3$ because `nums[2] = nums[3] = 3`.

The second result characterizes exactly which subarrays reach $k$. Suppose $\text{AND}(S) = k = M$. Since the AND is at most each element and each element is at most the global maximum,

$$
M = \text{AND}(S) \le e \le M \quad \text{for every } e \in S,
$$

so every $e$ must equal $M$. Conversely, a subarray consisting entirely of copies of $M$ has AND equal to $M$ by the identity $M \,\&\, M = M$ applied repeatedly. Therefore:

> **Characterization.** A subarray has AND equal to the maximum achievable value exactly when every one of its elements equals $\max(\text{nums})$. Consequently, the longest such subarray is the longest contiguous run of elements equal to the maximum.

The proof also explains why a *near*-maximum neighbour ruins a candidate: appending `2` (binary `010`) to a `3` (`011`) clears bit 0 and yields `2`, which is below $k$. In the traced array, the subarray at indices 2–3 is the only one of length two with AND `3`; every longer subarray that includes index 4 drops to `2`.

## 4. The Run Decomposition of the Instance

Because the answer is a longest run of maxima, the array can be read as a sequence of candidate runs, of which only those equal to the maximum are admissible.

| Run | Index range | Values | Length | Contains the maximum `3`? | Admissible for the answer? |
|:---:|:---|:---|:---:|:---:|:---|
| 1 | 0–0 | `1` | 1 | no | no |
| 2 | 1–1 | `2` | 1 | no | no |
| 3 | 2–3 | `3, 3` | 2 | yes | **yes — length 2** |
| 4 | 4–5 | `2, 2` | 2 | no | no |

Run 4 is the trap: it is exactly as long as the admissible run, so a method that returned the *longest run of equal values* rather than the longest run of the *maximum* value would still return `2` here by luck. The boundary table in Section 6 provides instances where those two quantities differ, which is why the distinction has to be stated rather than assumed.

## 5. Step-by-Step Scan

The method needs one pass to learn the maximum and one pass to measure the longest run of maxima. The state is the current maximum, the length of the run currently being counted, and the best run length seen so far.

| Step | Index | `nums[i]` | Equals the maximum `3`? | `cnt` before | `cnt` after | `ans` after |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 | 0 | `1` | no | 0 | 0 | 0 |
| 1 | 1 | `2` | no | 0 | 0 | 0 |
| 2 | 2 | `3` | yes | 0 | 1 | 1 |
| 3 | 3 | `3` | yes | 1 | 2 | 2 |
| 4 | 4 | `2` | no | 2 | 0 | 2 |
| 5 | 5 | `2` | no | 0 | 0 | 2 |

The final value `ans = 2` matches the expected output. Three details of the trace carry pedagogical weight.

- **`cnt` resets to zero, not to one.** A non-maximum element is not the start of a new admissible run; only a maximum element opens a run. Setting `cnt = 0` on a failure is what makes the next maximum element begin a fresh count.
- **`ans` never decreases.** After step 3 it stays at `2` even though the run ends, because the answer is a maximum over completed runs.
- **The maximum is known before the run scan begins.** Both passes are linear, so the two-pass structure costs nothing asymptotically compared with a single fused pass, and it keeps each pass's invariant simple.

## 6. Invariant and Correctness

**First pass, maximum invariant.** After index $i$ is read, the stored maximum equals $\max(\text{nums}[0..i])$: the base case reads `nums[0]`, and each step replaces the stored value only when the new element is larger. At the end the stored maximum is $M$, and by Section 3 the maximum achievable AND is exactly $M$.

**Second pass, run invariant.** After index $i$ is processed, `cnt` is the length of the longest suffix of `nums[0..i]` all of whose elements equal $M$ (that is, the current run length, or `0` when `nums[i] ≠ M`), and `ans` is the length of the longest contiguous block of $M$'s in `nums[0..i]`.

*Base.* At index `0` either `nums[0] = M`, so the maximal all-`M` suffix has length `1`, or it does not, so the suffix is empty and has length `0`; in both cases `ans` matches the longest block seen.

*Step.* Assume the invariant after $i - 1$. If `nums[i] = M` it extends the maximal all-`M` suffix by one, so `cnt` becomes `cnt + 1` and the best block becomes the larger of the previous `ans` and the new `cnt`. Otherwise no all-`M` suffix ends at $i$, so `cnt` becomes `0` and the best block is unchanged. The invariant is restored either way. $\square$

**Completeness.** Every contiguous block of $M$'s ends at some index $i$, where `cnt` equals that block's length; since `ans` is the maximum of `cnt` over all indices, it is at least the longest block's length.

**Soundness.** Every value in `ans` is a realized `cnt`, hence the length of a genuine all-`M` block, which by the characterization of Section 3 is a subarray whose AND equals $M = k$; so `ans` never exceeds a valid length. The two bounds meet at the true answer.

**Uniqueness is not required.** Several subarrays may tie — `[3]` at index 2, `[3]` at index 3, and `[3,3]` at indices 2–3 all reach $k$ — and since only a length is requested, the maximum over `cnt` resolves the ties.

## 7. Boundaries and Traps

The constraints are $1 \le n \le 10^{5}$ and $1 \le \text{nums}[i] \le 10^{6}$, so the range is strictly positive and the array is never empty.

| Instance | Maximum $M$ | Longest run of $M$ | Answer | What it exposes |
|:---|:---:|:---:|:---:|:---|
| `[1]` | 1 | 1 | `1` | the minimum-size array; the answer is `1`, never `0` |
| `[1, 2, 3, 4]` | 4 | 1 | `1` | a strictly increasing array leaves a single maximum, so the best subarray is the singleton |
| `[7, 7, 7, 7]` | 7 | 4 | `4` | the whole array is one run of maxima |
| `[5, 5, 1, 5, 5, 5, 2, 5]` | 5 | 3 | `3` | smaller values separate runs of maxima; only the middle run is longest |
| `[9, 9, 9, 8, 9]` | 9 | 3 | `3` | the best run may be at the start |
| `[4, 6, 1, 6, 6]` | 6 | 2 | `2` | the best run may be at the end |
| `[1000000, 1000000, 999999]` | 1000000 | 2 | `2` | the largest legal value is an ordinary element; `999999` still breaks the run |
| `[2, 2, 3, 3]` | 3 | 2 | `2` | a long run of a non-maximum value loses to a short run of the maximum |

Two traps are specific to this problem.

- **Confusing "longest run of equal values" with "longest run of the maximum".** In `[2, 2, 3, 3]` the two runs tie, and in `[5, 5, 1, 5, 5, 5, 2, 5]` a shorter run of maxima is surrounded by longer runs of smaller values. The proof in Section 3, not the traced instance, is what rules out every such candidate.
- **Assuming a longer subarray is better.** Growing a subarray only clears bits, so a subarray containing both a maximum and a smaller element has AND below $k$ and is rejected regardless of its length.

A milder trap is bit width: with `nums[i] ≤ 10^{6} < 2^{20}` every value fits in twenty bits and the AND cannot truncate. The argument of Section 3 never uses the width, so the reasoning holds at any magnitude.

## 8. Alternative Formulations

| Alternative | Work performed | Cost | Trade-off against the run scan |
|:---|:---|:---|:---|
| Enumerate every subarray, compute its AND, and track the best | $\binom{n+1}{2}$ subarrays, each with an inner loop over its elements | time $O(n^{3})$ naively, $O(n^{2})$ with running ANDs | directly mirrors the definition and is useful for verifying small instances, but quadratic enumeration is far too slow for $n = 10^{5}$ |
| Maintain the set of distinct AND values of subarrays ending at $i$ | at most one entry per bit, so at most twenty here | time $O(n \cdot B)$, auxiliary space $O(B)$ | the standard tool when the question is "which AND values are achievable"; it computes all of them, while the simple maximum already reveals the largest |
| Divide and conquer: crossing subarrays plus two halves | recursive split with a merge over crossing subarrays | time $O(n \log n)$ | correct but strictly worse than linear, and it answers a harder question than the one asked |
| Find the maximum value, then measure the longest run of that value | one linear maximum pass plus one linear run pass | time $O(n)$, auxiliary space $O(1)$ | chosen: the characterization of Section 3 removes the need to evaluate any subarray's AND at all |

The distinct-AND-set alternative is worth studying precisely because it is the standard tool for AND-subarray problems. It is the right answer when the question is "which AND values are achievable"; here the question is "which AND value is largest", and the monotonicity argument settles that in one pass without a set.

## 9. Complexity Derivation

**First pass.** Comparing each element with the running maximum costs $n - 1$ constant-time comparisons: $O(n)$.

**Second pass.** One equality test, at most one increment of `cnt`, one reset, and one comparison for the running best per element, all $O(1)$: $O(n)$.

**Total time.** $O(n)$. Because an adversary can change the answer by altering a single element, every correct method must read all $n$ elements, so $O(n)$ is optimal.

**Auxiliary space.** Three scalars — the maximum, the current run length, and the best run length — regardless of $n$: $O(1)$. No subarray is materialized. The quadratic enumeration alternative trades $O(n^{2})$ time for no space saving, and the distinct-AND trade uses $O(B)$ space and $O(nB)$ time; neither improves on the run scan's constant space.

**Summary.** The maximum subarray AND equals the maximum element, and the answer is the longest contiguous run of elements equal to that maximum — found in $O(n)$ time with $O(1)$ auxiliary space, using nothing beyond a maximum pass and a run-length scan.