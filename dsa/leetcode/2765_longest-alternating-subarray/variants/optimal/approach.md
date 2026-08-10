## General

**Express the pattern as alternating adjacent differences**

A valid subarray must have length at least two and look like

`a, a + 1, a, a + 1, ...`.

Its adjacent differences are therefore

$$
+1,\ -1,\ +1,\ -1,\ \ldots
$$

The exact solution uses this difference view directly. For every possible start index `i`, it sets `k = 1`, meaning the first required difference is positive one. It then advances `j` while

`nums[j + 1] - nums[j] == k`

and flips the next expectation with `k *= -1` after each successful step.

This avoids repeatedly comparing later values with the first value. The required current difference completely describes whether the next position continues the pattern.

**Why every start is examined**

An alternating subarray can begin anywhere, but it cannot begin with a decrease. Even if an index lies inside some other pattern, it might start a different valid pattern with its following value. The outer loop therefore tries each `i` independently.

For a fixed `i`, `j` begins equal to `i`. If the next difference is not positive one, the while loop performs no extension. If it does match, `j` advances and the expected difference becomes negative one. Each later success alternates that sign.

When the loop stops, one of two things is true: `j` is already the final array index, or the next adjacent difference does not match the required sign and magnitude. In either case, the interval `nums[i:j + 1]` is the longest alternating subarray beginning at this particular `i`.

**The magnitude matters, not only parity or sign**

The condition is exact equality with `1` or `-1`. A change from 2 to 5 is positive, but it is not the required increase by one. A sequence such as `[2, 3, 2, 3]` succeeds because its differences are exactly `1, -1, 1`. A sequence `[2, 3, 1]` stops before 1 because the second difference is `-2`.

Likewise, merely alternating parity is not enough. Values 2 and 5 have opposite parity but differ by three. Tracking `k` captures the full numerical pattern stated in the contract.

**A walkthrough**

For `nums = [2, 3, 4, 3, 4]`:

- At `i = 0`, the first difference `3 - 2` is 1, so the scan reaches index one and expects `-1`. The next difference `4 - 3` is 1, not `-1`, so this candidate has length two.
- At `i = 1`, `4 - 3 = 1`, then `3 - 4 = -1`, then `4 - 3 = 1`. The scan reaches the end with length four.
- Later starts cannot produce a longer result.

The answer becomes four. Notice why a failure at index two for the first start does not justify skipping index one: index one is exactly where the longest valid pattern begins.

**Reject length-one intervals**

`ans` is initialized to `-1`, the required result when no valid alternating subarray exists. After scanning one start, the code checks `j - i + 1 > 1` before updating the maximum.

This guard distinguishes “the chosen starting element exists” from “at least one required transition succeeded.” Without it, every array would produce an answer of at least one, contradicting the definition that `m` must be greater than one.

**Why the enumeration is correct**

For any fixed start `i`, the loop begins with the required first difference and flips its sign after every match. Thus every transition inside the recorded interval has exactly the mandated difference. If the interval length is at least two, it is a valid alternating subarray.

The scan continues until the first failing transition, and every longer interval with the same start would contain that failure. Hence it finds the longest valid interval for `i`.

Now take a globally longest alternating subarray. Its start is some index visited by the outer loop. At that iteration, every transition through its endpoint matches, so the inner loop reaches at least that endpoint and records a candidate no shorter than it. Taking the maximum across all starts therefore returns the global optimum. If no start achieves even one matching transition, the guarded update never runs and `-1` is correct.

**The exact code is not the one-pass method named by the manifest**

The manifest says the solution tracks the alternating run ending at each position in `O(n)` time. The exact file instead resets `k` and `j` for every start and scans forward again. These repeated scans are visible in the nested loops and can overlap heavily.

For the small constraint `n <= 100`, this straightforward enumeration is easily fast enough. However, it is important not to claim the linear bound or describe an ending-state update that the submitted code does not contain.

## Complexity detail

Let `n` be the array length. The outer loop has `n` iterations. A single inner scan can advance through nearly the rest of the array. In a long pattern such as `[a, a+1, a, a+1, ...]`, every other start has an initial positive-one difference and scans a long suffix. The total number of successful comparisons is an arithmetic series, producing `O(n^2)` worst-case time.

Thus the exact solution is `O(n^2)`, not the `O(n)` shown in `solution_variants.json`. Many inputs stop quickly at most starts and run closer to linear in practice, but worst-case analysis must use the repeated long scans.

The algorithm stores only `ans`, `n`, `i`, `j`, and `k`. It allocates no array, set, or recursion stack, so auxiliary space is `O(1)`. It only reads `nums`.

## Alternatives and edge cases

- **One-pass dynamic tracking:** Carry the length of the valid alternating run ending at each position, continue it when the expected difference matches, and restart at length two on a new `+1` pair. That yields `O(n)` time and matches the manifest, but it is not the exact implementation.
- **Compare values to the start:** Checking whether each even offset equals `nums[i]` and each odd offset equals `nums[i] + 1` is correct, but adjacent differences plus a sign flip express the same rule more directly.
- **Parity-only test:** Alternating even and odd values is insufficient because the required numerical difference must be exactly one in magnitude.
- **No `+1` adjacent pair:** No start reaches length two, so the initial `-1` is returned.
- **Exactly one valid pair:** Its length two updates `ans` even if the pattern fails immediately afterward.
- **Consecutive increases:** A second `+1` is invalid because the expected difference after the first step is `-1`.
- **Difference with magnitude greater than one:** It fails even if its sign is the expected sign.
- **Pattern reaches the final element:** The bounds check `j + 1 < n` ends the loop safely, and the full length is recorded.
- **Overlapping valid subarrays:** Each start is considered independently. Overlap causes repeated work but does not cause duplicate answer counting because only the maximum length is stored.
- **Length-one candidate:** It is deliberately ignored due to the strict `> 1` definition.
- **Minimum input length two:** One comparison decides between answer two and `-1`.
- **Input mutation:** The method never changes the array, so later starts see the original values.
