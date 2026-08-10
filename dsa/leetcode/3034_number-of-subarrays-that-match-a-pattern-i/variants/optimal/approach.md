## General

**Convert each adjacent pair into one of three signs.** The pattern does not care about the magnitudes of neighboring numbers. It records only whether the next value is larger, equal, or smaller. The helper

`f(a, b)`

returns:

- 0 when `a == b`;
- 1 when `a < b`, meaning the next value `b` is larger;
- $-1$ when `a > b`, meaning the next value is smaller.

This exactly matches the symbols allowed in `pattern`. For any candidate subarray of length $M+1$, its $M$ adjacent relationships can therefore be converted and compared position by position with the $M$ pattern entries.

**Enumerate every possible start.** If `nums` has length $N$ and `pattern` length $M$, a matching subarray uses positions $i$ through $i+M$. Its start can range from 0 through $N-M-1$, giving $N-M$ candidates. The source writes

`for i in range(len(nums) - len(pattern))`,

which enumerates exactly those starts.

For fixed `i`, the generator visits `enumerate(pattern)`. At pattern position `k`, it compares the relationship between `nums[i + k]` and `nums[i + k + 1]` with the expected pattern value `p`:

`f(nums[i + k], nums[i + k + 1]) == p`.

Every index is valid because the last tested adjacent pair is between `nums[i + M - 1]` and `nums[i + M]`, both inside the candidate length-$M+1$ subarray.

**Use `all` to require every relationship.** `all(generator)` returns true only when every generated comparison is true. One wrong relation invalidates the candidate subarray, regardless of the other positions. Python's `all` short-circuits: it stops asking the generator for values at the first false comparison. This can save work on typical nonmatching starts while preserving the worst-case bound.

The line `ans += all(...)` works because Python Booleans act as integers. A matching candidate adds one; a nonmatch adds zero. Consequently `ans` after each outer iteration equals the number of matching starts examined so far.

**A detailed example.** Take `nums = [1,4,4,1,3]` and `pattern = [1,0,-1]`. At start 0:

- `f(1,4) = 1`, matching the first pattern symbol;
- `f(4,4) = 0`, matching the second;
- `f(4,1) = -1`, matching the third.

`all` returns true, so the subarray `[1,4,4,1]` is counted.

At start 1, the first relation is `f(4,4)=0` but the pattern expects 1. `all` stops immediately and contributes zero; it does not need to inspect the other two relations.

**Why overlapping subarrays are counted separately.** Starts advance by one, not by $M+1$. Two matching windows may share most of their elements and still represent different subarrays. The outer loop examines each start independently, as the problem requires.
For a fixed start $i$, the problem defines a match by $M$ conditions, one for each $k$: greater-than when pattern is 1, equality when it is 0, and less-than when it is $-1$. Helper `f` maps the actual adjacent pair to exactly that same three-valued language. Therefore `f(...) == pattern[k]` is true exactly when condition $k$ holds. `all` is true exactly when all $M$ defining conditions hold, so it counts exactly the matching subarrays. Enumerating all $N-M$ starts and summing those truth values yields the complete answer.

**Why no transformed array is needed.** Another natural method first creates an array of $N-1$ relation signs, then searches for `pattern` within it. This source computes each needed sign on demand. For the small “I” constraints, direct candidate comparison is both clear and sufficient.

## Complexity detail

There are $N-M$ candidate starts. In the worst case, such as when every candidate matches or differs only at its last relationship, `all` examines all $M$ pattern positions for each start. Worst-case time is

$$
O((N-M)M).
$$

Short-circuiting may reduce actual work but does not improve the worst-case guarantee.

The generator expression is lazy, `all` retains only the current comparison, and the helper uses only its two arguments. No transformed relation array or substring is created. Auxiliary space is $O(1)$. The input arrays remain unchanged.

Function-call and generator overhead are constant per tested relationship. With $N\le100$, the straightforward bound is easily acceptable.

## Alternatives and edge cases

- **Precompute a comparison array:** Convert every adjacent pair of `nums` into $-1$, 0, or 1, then compare length-$M$ slices. This uses $O(N)$ space and retains the same naive worst-case time if each slice is compared directly.
- **KMP on relation signs:** It finds all pattern occurrences in $O(N+M)$ time and $O(M)$ space. That is useful for the larger version but unnecessary for $N\le100$.
- **Z-function or rolling hash:** Both can accelerate pattern matching after transformation, but they add machinery not needed by this direct implementation.
- **Materialize the generator:** Building a list of $M$ Booleans before calling `all` wastes $O(M)$ space and loses short-circuiting.
- **Pattern length one:** Every adjacent pair is one candidate, and the helper directly checks whether its relation matches the single symbol.
- **Pattern nearly as long as `nums`:** When $M=N-1$, there is exactly one candidate subarray, because `range(N-M)` has one start.
- **Equal adjacent values:** The helper returns zero, not either inequality sign.
- **Large numeric magnitudes:** Only comparisons matter, so values up to $10^9$ do not affect complexity or require subtraction that might overflow in fixed-width languages.
- **Overlapping matches:** Each start is counted independently, even when windows share elements.
- **Early mismatch:** `all` stops at the first false condition, which is a safe optimization because one failure already invalidates the whole candidate.
- **Input immutability:** The algorithm only indexes `nums` and `pattern` and does not reorder or edit either list.
