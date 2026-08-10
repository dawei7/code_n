## General

Mountain `i` is stable based solely on mountain `i-1`. Its own height and all other mountains are irrelevant. Mountain zero has no predecessor and is explicitly excluded.

The list comprehension iterates `i` from one through `len(height)-1`. For each candidate, it tests `height[i - 1] > threshold`. When true, it emits the current index `i`.

The strict greater-than comparison is essential. A predecessor exactly equal to the threshold does not make the next mountain stable.

For `[1,2,3,4,5]` with threshold two, candidate indices one and two look back at heights one and two and fail. Indices three and four look back at three and four and pass, producing `[3,4]`.

For `[10,1,10,1,10]` with threshold three, high predecessors at indices zero and two make following indices one and three stable. The mountains of height ten at indices two and four are not themselves selected merely for being tall; stability looks backward.

With threshold ten, even predecessors of height ten fail because the relation is strict, yielding an empty output.

**Why the returned order is valid.** The statement accepts any order. The comprehension naturally returns ascending indices, which is deterministic and needs no extra sorting.

**Why index zero is never considered.** Starting `range` at one both prevents invalid access to a conceptual predecessor and enforces the explicit rule. In Python, accidentally using `height[-1]` for index zero would compare the last mountain and create a false circular interpretation.

The loop invariant is simple: after considering candidate indices through `i`, the result contains exactly those among one through `i` whose immediate predecessor exceeds the threshold. The predicate appends precisely the next qualifying index, so the final list is complete and contains no false positives.

No mountain heights are modified, and no additional structural information is needed.

## Complexity detail

Let $n$ be the number of mountains. The comprehension evaluates $n-1$ candidates with constant work, taking $O(n)$ time.

The returned list can contain up to $n-1$ indices and therefore uses $O(n)$ required output space. Excluding output, the iterator and current index use $O(1)$ auxiliary space. The manifest's $O(1)$ space should be understood as auxiliary space excluding the answer.

## Alternatives and edge cases

- **Explicit loop:** Append qualifying indices in a standard loop. It is equivalent and may be easier to instrument, but the comprehension directly expresses filtering.
- **Compare the current mountain:** This is incorrect; stability depends on the previous mountain's height.
- **Use greater-than-or-equal:** It would wrongly include predecessors equal to `threshold`.
- **Start at zero:** Python negative indexing would compare mountain zero against the last mountain, violating the non-circular definition.
- **All predecessors high:** Every index one through $n-1$ is returned.
- **No predecessor high:** The output is empty.
- **Alternating high and low:** Each high mountain affects only the immediately following index.
- **Last mountain high:** It affects no output if there is no mountain after it.
- **First mountain high:** It can make index one stable even though index zero itself is never stable.
- **Minimum length two:** Exactly one candidate index is tested.
- **Duplicate heights:** They are evaluated independently against the threshold; uniqueness is irrelevant.
- **Output space:** A list is required by the contract, so a potentially linear result does not contradict constant auxiliary working memory.
- **Current height can be small:** A mountain of height one is stable if its predecessor exceeds the threshold. Stability does not describe the current mountain's own strength.
- **Current height can be large:** A very tall mountain is not stable when its predecessor fails the test. Looking at `height[i]` would reverse the relationship.
- **Threshold at maximum constraint:** When threshold is one hundred and heights are at most one hundred, strict comparison guarantees an empty result.
- **Threshold at minimum constraint:** With threshold one, every predecessor of height at least two qualifies, while height one still fails equality.
- **Consecutive stable indices:** If several consecutive predecessor heights exceed the threshold, their following indices can all be stable; there is no exclusivity rule.
- **Why no state carries between candidates:** Each predicate reads one fixed predecessor independently. Whether index `i-1` was itself stable has no bearing on index `i`.
- **Result contains indices, not heights:** The comprehension emits `i`. Emitting `height[i]` would lose location information and violate examples with repeated values.
- **Any-order allowance:** Ascending order is still a valid “any order” result and is helpful for deterministic testing.
- **No circular predecessor:** The row of mountains is linear. Explicitly excluding zero prevents Python's negative indexing from inventing a wraparound neighbor.
- **Read-only behavior:** The comprehension reads `height` without sorting or changing it, so predecessor relationships remain those of the original row.
- **Why every possible answer is examined:** Every stable index must lie between one and `n-1`, exactly the range traversed. The predicate is the definition itself, so there is no hidden candidate outside the scan.
- **One-pass optimality:** A correct method may need to inspect every predecessor height because any unchecked value could independently determine whether its following index belongs in the result. Linear time is therefore asymptotically optimal.
