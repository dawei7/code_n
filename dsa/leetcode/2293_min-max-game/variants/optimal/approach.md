## General

**Shrink the active prefix by half each round**

The process repeatedly replaces an array of length `n` with one of length `n/2`. The exact solution reuses the front of `nums` rather than allocating `newNums`.

`n >>= 1` divides the active length by two before building the next round. The loop over `range(n)` writes the new values into indices zero through `n-1`. Elements beyond that prefix become stale and are ignored in later rounds.

The power-of-two guarantee ensures repeated halving reaches exactly one.

**Read the prescribed source pair**

For new index `i`, the source indices are `2i` and `2i+1`. Bit shifts express these:

- `i << 1` equals `2i`;
- `i << 1 | 1` equals `2i+1`.

The values are captured as `a, b` before the destination is overwritten.

If `i` is even, the code writes `min(a,b)`. If `i` is odd, it writes `max(a,b)`. Parity belongs to the new index, exactly as the rule states; it does not depend on source-index parity beyond selecting the pair.

**Why in-place writes do not corrupt later reads**

The inner loop moves `i` upward. At index `i`, future iterations will read source positions at least `2(i+1)`, while all destinations written so far are at most `i`.

Those ranges do not overlap. For example, after writing destination zero from sources zero and one, the next iteration reads sources two and three, which are untouched. Therefore, overwriting the active prefix is safe without a temporary array.

**Trace one round**

For `[1,3,5,2,4,8,2,2]`, the new active length is four:

- new index zero is even, so it receives `min(1,3)=1`;
- index one is odd, so it receives `max(5,2)=5`;
- index two receives `min(4,8)=4`;
- index three receives `max(2,2)=2`.

The active prefix is now `[1,5,4,2]`. Stale positions after index three do not participate again.

The next two rounds produce `[1,4]` and then `[1]`.

**Why each round matches the defined new array**

Every new index reads the exact old pair before writing its destination. The parity branch applies the required operation. Safe non-overlap proves all source values are still from the previous active round when read.

Thus, after the inner loop, the first `n` positions equal the separately allocated `newNums` that the statement describes. Induction over rounds proves `nums[0]` is the same final survivor.

**Handle the base case naturally**

If the original length is one, `while n > 1` never runs and the method returns the original `nums[0]`.

No separate return branch is needed.

**Account for mutation**

The method changes `nums` in place. After completion, index zero contains the answer, some early positions contain values from recent intermediate rounds, and the suffix contains stale original or intermediate data.

Only the returned value is specified, but callers retaining the list can observe this mutation.

## Complexity detail

For original length `N`, the numbers of pair operations are

$$
\frac N2+\frac N4+\cdots+1=N-1.
$$

Total time is `O(N)`, not `O(N\log N)`, because the active length halves each round.

The exact algorithm stores only `n`, loop variables, and two pair values, so auxiliary space is `O(1)`. The manifest's `O(n)` space describes a new-array implementation, but this source deliberately reuses `nums`.

## Alternatives and edge cases

- **Allocate a new array each round:** It mirrors the statement directly and uses `O(n)` peak auxiliary space.
- **Recursive tournament:** It can express the reduction tree but adds call-stack overhead and more complex parity indexing.
- **Apply min or max by source index:** The rule uses the new index `i`, so that substitution is incorrect.
- **Single element:** The loop is skipped and the element is returned.
- **Two elements:** New index zero is even, so the result is their minimum.
- **Equal pair values:** Both `min` and `max` return the same value.
- **Power-of-two length:** It guarantees every active round consists of complete pairs and finishes at one.
- **Overwriting source zero:** It is safe because no later pair rereads positions zero or one.
- **Stale suffix:** It is intentionally ignored once `n` shrinks.
- **Input mutation:** The caller's list does not retain its original contents.
- **Large values:** Only comparisons are performed, so magnitude does not affect arithmetic safety.
- **Total operations:** The geometric series explains why several rounds still total linear work.
- **Active length versus list length:** The physical Python list never shrinks; `n` alone determines which prefix belongs to the current round.
- **Parity resets each round:** Index parity is evaluated in the newly produced prefix, so an element's operation role can differ from the role of its source position.
- **Ascending destination order:** Writing destinations from zero upward is part of the overwrite-safety argument; an arbitrary write order could destroy unread sources.
- **Pair coverage:** Source positions zero through `2n-1` are divided into disjoint consecutive pairs, so every active old value participates exactly once per round.
- **Return location:** Every reduction writes its first result to index zero, making `nums[0]` the final survivor after the last round.
- **No list slicing:** Reusing the existing buffer avoids both a half-length allocation and copying on every round.
