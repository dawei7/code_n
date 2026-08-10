## General

**Only two choices matter at each index**

At position `i`, the constructed array `nums3` must choose either `nums1[i]` or `nums2[i]`. The goal concerns a contiguous non-decreasing subarray, so when extending a candidate ending at `i - 1`, only two facts are needed:

- how long the best valid ending is when position `i - 1` chose `nums1[i - 1]`;
- how long it is when position `i - 1` chose `nums2[i - 1]`.

The exact solution stores those lengths in `f` and `g`, respectively. It does not need to remember the entire constructed array or which choices occurred earlier, because non-decreasing validity across the new boundary depends only on the previous chosen value and the current chosen value.

**Define the two dynamic-programming states precisely**

After processing index `i`:

- `f` is the maximum length of a non-decreasing subarray ending at `i` when `nums3[i] = nums1[i]`;
- `g` is the corresponding maximum length when `nums3[i] = nums2[i]`.

For index zero, either choice by itself forms a non-empty subarray of length one, so `f = g = 1`. The global answer also begins at one.

This state tracks subarrays ending at the current position, not necessarily starting at zero. If no previous state can extend, a new length-one subarray starts at the current index.

**Compute all four transitions**

At a later index `i`, new variables `ff` and `gg` start at one.

To end with `nums1[i]`, there are two possible previous choices:

- If `nums1[i] >= nums1[i - 1]`, the state represented by `f` can extend, giving `f + 1`.
- If `nums1[i] >= nums2[i - 1]`, the state represented by `g` can extend, giving `g + 1`.

`ff` takes the maximum of its initial one and every allowed extension.

Similarly, to end with `nums2[i]`:

- compare it with `nums1[i - 1]` and potentially extend `f`;
- compare it with `nums2[i - 1]` and potentially extend `g`.

The best allowed value becomes `gg`.

These four comparisons cover every combination of choosing one of two values at the previous position and one of two at the current position.

**Why separate temporary variables are necessary**

Both new states must be computed from the old states at index `i - 1`. The code calculates `ff` and `gg` first, then assigns `f, g = ff, gg` simultaneously.

If it overwrote `f` before calculating `gg`, the second calculation might use a length that already includes index `i` as though it ended at `i - 1`. That would combine incompatible transitions and could overcount. Temporaries preserve the layer-by-layer dynamic-programming meaning.

**A walkthrough**

Consider `nums1 = [1, 3, 2, 1]` and `nums2 = [2, 2, 3, 4]`.

At index zero, both states are one. At index one:

- choosing 3 can extend either previous 1 or 2, so `ff = 2`;
- choosing 2 can also extend either, so `gg = 2`.

At index two:

- choosing 2 from `nums1` cannot follow 3 but can follow the previous chosen 2, so its state remains extendable to length three through `g`;
- choosing 3 from `nums2` can follow both previous choices and also reaches length three.

At index three, choosing 4 from `nums2` extends the length-three state to four. The solution finds the construction `[1, 2, 3, 4]` over the full interval, even though its choices come from different source arrays.

**Why choices outside the best subarray are irrelevant**

The problem asks for the longest non-decreasing subarray in some complete `nums3`. Once the algorithm identifies compatible choices over an interval, positions before and after that interval can be assigned arbitrarily; they do not invalidate the interval's internal order.

That is why a failed extension resets a state to one rather than making it impossible. The current element can always begin a new candidate subarray, regardless of what was chosen earlier in `nums3`.

**Keep a global maximum**

`f` and `g` describe only intervals ending at the current index. A longest interval might end before the final position. After every update, `ans = max(ans, f, g)` preserves the best length seen at any endpoint and under either current choice.

Returning only `max(f, g)` after the loop would miss a long earlier run followed by values that force both ending states to restart.

**Why the recurrence is correct**

For a state ending with `nums1[i]`, any non-decreasing interval of length greater than one must have chosen either source value at `i - 1`. Those are exactly the two comparisons used to build `ff`. By the previous-state definition, `f` and `g` are the longest valid intervals for those respective endings, so extending the larger compatible one is optimal. If neither is compatible, only the one-element interval remains. The same reasoning proves `gg`.

Induction from index zero therefore establishes both state meanings at every index. The global maximum visits every endpoint and both final-value choices, so it equals the maximum achievable non-decreasing subarray length.

## Complexity detail

Let `n` be the common array length. The loop visits each index once. Every iteration performs four comparisons, a constant number of maximum operations, and constant assignments. Time complexity is `O(n)`.

The algorithm stores only `n`, the old states `f` and `g`, the new states `ff` and `gg`, the answer, and the loop index. No array proportional to `n` is allocated, so auxiliary space is `O(1)`.

A full table with two entries per index would use `O(n)` space, but each transition depends only on the immediately preceding pair. Rolling those two values is what yields the constant-space bound.

## Alternatives and edge cases

- **Two-row or full DP table:** Storing both states for every index makes reconstruction easier but is unnecessary when only the maximum length is requested. The exact rolling version uses constant space.
- **Construct one greedy `nums3`:** Choosing the smaller value at every index may block a later extension, while choosing the larger may also be wrong. Both ending choices must remain available as separate states.
- **Try all `2^n` constructions:** It captures every choice but is exponential and repeats the same ending-state information.
- **Longest non-decreasing subsequence algorithm:** The target is a subarray, so indices must remain contiguous. Subsequence techniques solve a different problem.
- **Length-one input:** Initialization returns one without entering the loop.
- **Equal adjacent values:** Non-decreasing means equality is allowed, and every transition correctly uses `>=`.
- **Neither previous value can precede the current choice:** That state stays one, starting a new subarray.
- **Only one source transition works:** The maximum uses that precise predecessor state and ignores the incompatible one.
- **Both source values are equal at an index:** Keeping two states is harmless; they may have different histories even when their current value matches.
- **Best interval ends early:** `ans` retains it after later states restart.
- **Very large values:** Only comparisons are performed, so magnitude does not affect storage or indexing.
- **Input arrays remain unchanged:** The solution models choices through state lengths and never constructs or mutates `nums3`.
