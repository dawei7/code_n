## General

**Understand what choosing a value really does**

An operation does not choose one index or even one contiguous segment. It chooses a value `x` and updates every maximal segment currently containing that value. Those maximal segments together contain exactly all indices whose current value is `x`. Whether equal values form one segment or several separated segments therefore does not change which positions the operation updates: every current occurrence of `x` is written to its own target value at the same time.

This observation removes the apparent interval complexity. The operation can be viewed more simply as:

> Choose a current value `x`, then for every index currently equal to `x`, replace that element with `target[i]`.

The source consequently does not build segments, simulate mutations, or decide an order of operations. It scans corresponding values from `nums` and `target` and collects the distinct original values found at positions that are not already correct:

`{x for x, y in zip(nums, target) if x != y}`

The answer is the size of this set.

**Already-correct positions require no work**

If `nums[i] == target[i]`, index `i` does not force any operation. It may still be touched later when its value is selected because some other index with the same value is wrong. That is harmless: the operation writes `target[i]` to this position, which is the value already stored there, so the position stays correct.

For example, in `nums = [4,1,4]` and `target = [5,1,4]`, only index 0 is mismatched, and its original value is 4. Choosing 4 updates both maximal 4-segments. Index 0 changes to 5, while index 2 is written to its target value 4 and remains unchanged. This is why the algorithm may ignore matching positions while deciding how many different choices are necessary.

**Every distinct mismatched original value is necessary**

Consider a value `v` that appears at least once in `nums` at a mismatched position. Pick one such index `i`. Initially, the current value at `i` is `v`, but its desired value is different.

Before an operation chooses `v`, no operation choosing another value can change index `i`. An operation affects an index only when that index's current value equals the chosen value, and `i` remains `v` until it is affected for the first time. Therefore some operation must choose `v`. Otherwise index `i` can never leave its wrong initial value.

Apply that reasoning separately to every distinct value appearing at a mismatched position. If the set contains $K$ values, any successful sequence needs at least $K$ operations. One operation chooses only one integer, so it cannot serve as the required first selection for two different original values.

This lower bound explains why counting occurrences would be wrong. Ten mismatched positions that all begin with value 7 can be fixed when 7 is chosen once. Conversely, two mismatched positions beginning with different values require at least two operations even if their target values happen to be identical.

**Choosing each collected value once is sufficient**

Now take every value in the set and choose it exactly once, in any order. When a value `v` is chosen, every position still holding `v` is written to its target. In particular, every position whose original value was `v` and that was initially mismatched is fixed no later than this operation.

The subtle question is whether a later operation can break a position that was already fixed. Suppose choosing `v` changes index `i` to its target value `w`. If `w` is selected later, index `i` is indeed touched again because its current value equals `w`. However, the operation writes `target[i]`, which is also `w`. The element stays correct. Once any position has been written to its target, all later operations are idempotent at that position: they either do not touch it or write the same target value again.

This makes the order irrelevant. New occurrences of a value can be created when earlier values are processed, but selecting that value merely rewrites those newly correct positions to their existing targets. If the newly created value was already processed earlier, no further selection is needed because the position that just acquired it is already correct.

For `nums = [1,2,3]` and `target = [2,1,3]`, the mismatched original values are 1 and 2. Choosing 1 changes the first position to 2. Choosing 2 then touches both of the first two positions: the first remains at its target 2, and the second changes to 1. Exactly two operations are sufficient. Reversing the choices also works.

The set size is thus both a lower bound and an achievable upper bound. They match, so it is the minimum possible operation count.

**How the exact source expresses the algorithm**

`zip(nums, target)` creates corresponding pairs in index order. The constraints guarantee equal lengths, so every index participates. The condition `if x != y` keeps precisely the initially mismatched positions. A set comprehension inserts each retained `x`, automatically collapsing repeated values. Finally, `len(s)` returns the number of distinct required choices.

The function never mutates `nums`. Simulation is unnecessary because the proof shows that only the initial value classes at mismatched indices determine the optimum. This is a stronger simplification than merely finding a faster simulation: the complete sequence of intermediate arrays contains no additional information needed for the answer.

## Complexity detail

Let $N$ be the common array length and let $K$ be the number of distinct original values appearing at mismatched positions. `zip` and the set comprehension inspect each of the $N$ aligned pairs once. Set insertion and membership handling are expected $O(1)$ per retained value in Python, so the expected running time is $O(N)$. Computing `len(s)` is $O(1)$.

The set stores exactly $K$ integers, giving $O(K)$ auxiliary space. Since $K\le N$, the manifest's $O(N)$ space bound is correct as a worst-case statement. If every position already matches, $K=0$ and the set is empty. If all mismatched original values are different, $K$ can be $N$.

Under the stated bound `nums[i] <= 100000`, a boolean array indexed by value could provide deterministic $O(N+V)$ time and $O(V)$ space for value limit $V$, but the set naturally scales with the number of distinct required values. The result itself is a single integer and uses $O(1)$ output space.

## Alternatives and edge cases

- **Direct operation simulation:** Repeatedly scanning the array, finding maximal segments, and writing targets can reproduce a valid sequence, but it may cost $O(NK)$ time and obscures the fact that segment boundaries do not affect the count.
- **Frequency map:** Counting how many mismatched indices begin with each value also leads to the answer by taking the number of keys. The frequencies themselves are unnecessary; only distinctness matters, so a set is simpler.
- **Boolean seen array:** Because values lie between 1 and $10^5$, an indexed boolean array can mark required values. It has deterministic access but reserves space for the entire value domain even when few values occur.
- **All positions already match:** The comprehension inserts nothing, and the answer is zero. The operation may be used zero times, exactly as the statement permits.
- **One value at many separated positions:** All maximal segments of the chosen value are processed in the same operation. Separation by other values never increases the answer.
- **Matching and mismatching occurrences of one value:** Choosing that value fixes the mismatches and rewrites matching occurrences to the same values they already have, so only one operation is needed for the whole value class.
- **Different values sharing one target:** They still require separate operations because an index cannot be changed for the first time until its own current value is selected.
- **Cycles of desired values:** Transformations such as 1 becoming 2 and 2 becoming 1 do not require cycle detection. Later operations cannot damage completed positions because every write uses that position's final target.
- **Targets introducing a previously processed value:** No second operation is required. A position receiving that value has just been written to its target and is already correct.
- **Equal-length guarantee:** Python's `zip` would silently stop at the shorter array if lengths differed. The contract guarantees equal lengths, so the concise source covers every index; outside that contract, explicit length validation would be necessary.
