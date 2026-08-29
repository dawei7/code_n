## General

**Choose one occurrence of every distinct character**

The answer must preserve source order because it is a subsequence. It must contain every distinct character exactly once, and among all such choices it must be lexicographically smallest.

Choosing a smaller character earlier is desirable, but an earlier chosen character can be removed only if another copy remains later. Otherwise the final answer would lose that distinct character.

The solution maintains the current best subsequence as a stack and uses last-occurrence positions to decide which earlier choices are safely replaceable.

**Record the final opportunity for each character**

The dictionary is:

```python
last = {c: i for i, c in enumerate(s)}
```

The comprehension processes indices from left to right. Reassigning the same key overwrites its previous value, so `last[c]` ends as the final index where `c` occurs.

When processing position `i`, the condition `last[x] > i` means character `x` will appear again later. A selected `x` may be removed now without making it impossible to include `x` eventually.

**Track the current subsequence and membership**

The algorithm uses:

```python
stk = []
vis = set()
```

`stk` stores selected characters in their subsequence order. `vis` contains exactly the characters currently in `stk`.

The set makes the exactly-once rule efficient. Membership lookup avoids scanning the stack for every source character.

**Skip a character already selected**

For each indexed character:

```python
if c in vis:
    continue
```

If `c` is already in the stack, adding it would create a duplicate. The existing occurrence is earlier, which generally leaves at least as much future source available as replacing it with the later copy.

Any reason to remove that existing occurrence in favor of a smaller character is handled when the smaller character itself is processed by the pop loop. Simply seeing another copy of the same character creates no lexicographic improvement.

**Remove a larger suffix character when it can be recovered later**

The central loop is:

```python
while stk and stk[-1] > c and last[stk[-1]] > i:
    vis.remove(stk.pop())
```

Three conditions are required:

- The stack must be nonempty.
- Its final character must be lexicographically larger than current `c`.
- That final character must occur again after position `i`.

If all hold, replacing the larger stack suffix character with `c` makes the current result lexicographically smaller at the earliest changed position. The removed character is not lost permanently because a later occurrence remains available.

After popping, the new stack top becomes adjacent to `c` in the candidate subsequence, so the loop checks again. Several decreasing suffix characters may be removed.

Removing a character from `vis` is essential. It permits a later occurrence to be appended when the scan reaches it.

**Why the loop must stop in two cases**

If `stk[-1] <= c`, popping would not improve lexicographic order. A smaller top is already better, and an equal top cannot occur here because current `c` was not in `vis`.

If `last[stk[-1]] <= i`, no copy of the top remains later. Popping it would make it impossible to include every distinct character. Feasibility takes priority over placing `c` earlier.

The stack is therefore not necessarily globally increasing. A larger character may remain before a smaller one when it is the last available occurrence. The structure is best described as a greedy monotonic-stack process with a recoverability constraint.

**Append the current character**

After all safe improvements:

```python
stk.append(c)
vis.add(c)
```

Current `c` is not already selected, so adding it preserves uniqueness. Its source index is later than all characters still in the stack, so subsequence order is preserved.

Every character will eventually be selected. If earlier occurrences are popped, its last occurrence cannot be popped at or after itself for lack of a future copy. When the scan passes the final occurrence, that character must be in the stack.

**Greedy correctness**

At every step, the stack is the lexicographically smallest feasible selected prefix that can still be completed using the unprocessed suffix.

When a larger top has a later copy, keeping it before current `c` is unnecessary and lexicographically worse. Popping it is safe and improves the prefix.

When the top has no later copy, every feasible answer extending the processed prefix must retain that top before current `c`. Removing it would violate completeness, so stopping is forced.

The loop applies these decisions repeatedly to the entire replaceable suffix. Appending `c` then gives the smallest feasible prefix after processing this position.

By induction through the string, the final stack is the smallest complete subsequence containing each distinct character once.

**Example behavior**

For `"bcabc"`, the stack first becomes `["b", "c"]`. When `"a"` arrives, both `"c"` and `"b"` have later copies and are greater, so both are popped. The stack becomes `["a"]`, then later `"b"` and `"c"` are appended, producing `"abc"`.

In `"cbacdcbc"`, some larger characters cannot be popped when their final occurrence has been reached. The recoverability condition produces `"acdb"` rather than an infeasible alphabetically sorted string.

## Complexity detail

Let `n` be the string length and `A` the alphabet size.

Building `last` takes `O(n)` time. Each source character is examined once. A character can be pushed and popped only a bounded number of times associated with its occurrences, and total stack operations are `O(n)`. Total time is `O(n)`.

`last`, `vis`, and `stk` hold at most one entry per distinct lowercase letter, using `O(A)` space. Since `A = 26` is fixed, the manifest states this as `O(1)` auxiliary space.

The returned string contains at most 26 characters under the contract.

## Alternatives and edge cases

- **Remaining-count array:** Decrement a character's remaining frequency while scanning and allow a pop when that frequency stays positive. It is equivalent to comparing with the last index.
- **Recursive greedy selection:** Repeatedly choose the smallest character whose suffix still contains all remaining distinct characters. It is correct but can rescan and slice the string many times.
- **Enumerate subsequences:** Testing every subsequence is exponential and unnecessary.
- **All characters distinct and increasing:** Nothing is popped and the input is returned.
- **All characters distinct and decreasing:** No top has a later copy, so none can be popped; the input is the only valid full distinct-character subsequence.
- **Repeated one character:** The first copy is selected and all later copies are skipped, returning one character.
- **Current character already visited:** Skipping prevents duplicates without harming feasibility.
- **Larger top appears later:** It is safe to pop and reinsert from its future copy.
- **Larger top has no future copy:** It must remain even if current is smaller.
- **Multiple pops:** The loop removes the entire safely replaceable larger suffix, not only one character.
- **Last-occurrence dictionary:** Absolute positions remove the need to decrement frequency counters.
- **Lowercase constraint:** Fixed alphabet size justifies constant auxiliary-space notation.
- **Input preservation:** The immutable source is only scanned; result state is separate.
