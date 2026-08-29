## General

Only the parity of a subsequence sum matters. Adding an even value preserves parity, while adding an odd value switches even to odd and odd to even. The solution processes the array from left to right and counts nonempty subsequences by these two parity states.

After processing some prefix, `f[0]` is the number of nonempty subsequences of that prefix with an even sum, and `f[1]` is the number with an odd sum. Both start at zero because the empty prefix has no nonempty subsequence. The empty subsequence is deliberately not stored; singleton cases are added explicitly when each element arrives.

For every existing subsequence, there are two choices for the new element `x`: exclude it and keep the old subsequence, or include it and update the sum parity. In addition, the singleton subsequence `[x]` must be counted.

**Transition for an odd value.** Including odd `x` flips parity. New even-sum subsequences consist of old even subsequences that exclude `x` and old odd subsequences that include it:

$$
E'=E+O.
$$

New odd-sum subsequences consist of old odd subsequences that exclude `x`, old even subsequences that include it, and the odd singleton:

$$
O'=O+E+1.
$$

This is implemented by the first simultaneous assignment.

**Transition for an even value.** Including even `x` preserves parity. Every old even subsequence contributes twice to the new even count, once excluding and once including `x`, and the even singleton adds one:

$$
E'=2E+1.
$$

Every old odd subsequence likewise contributes an exclude and include version, but the singleton is not odd:

$$
O'=2O.
$$

The second assignment implements these formulas.

Python evaluates the complete right-hand side of a multiple assignment before replacing either element of `f`. This matters because both new states must use the old `f[0]` and old `f[1]`. Updating one entry first with separate statements and then using it in the other formula would mix DP layers and overcount.

For `nums = [1,1,1]`, the first odd value changes the state from `[0,0]` to `[0,1]`. The second changes it to `[1,2]`: one even pair and two odd singletons. The third produces `[3,4]`. The four odd subsequences are the three singletons and the length-three subsequence.

For `[1,2,2]`, after the first one there is one odd subsequence. Each even value doubles the number of odd subsequences because it may be excluded or included without changing parity. The odd count progresses one, two, four.

**Why subsequences with equal values are still distinct.** A subsequence is determined by selected indices. Two identical values at different positions create different singleton subsequences, and the DP processes each occurrence as a distinct include/exclude decision. It must not deduplicate by value.

The modulus `10 ** 9 + 7` is applied during every transition. Modular reduction is valid because the recurrences use only addition and multiplication by two. If two exact counts are congruent modulo the modulus, applying the next recurrence preserves congruence. The final `f[1]` is therefore the required count modulo the stated number.

There is also a closed-form observation: if the array contains at least one odd value, toggling the inclusion of one fixed odd occurrence pairs every even-sum subset with exactly one odd-sum subset. Among all $2^n$ subsets, exactly $2^{n-1}$ are odd, and the empty subset belongs to the even side. If no odd value exists, the answer is zero. The exact source uses the two-state DP instead; it directly demonstrates the parity transitions and generalizes naturally.

**Why the final state is exact.** Every nonempty subsequence of the current prefix either excludes the newest index, corresponding uniquely to an old subsequence, or includes it, corresponding uniquely to an old subsequence plus `x` or to the singleton. These cases are disjoint and exhaustive. The parity rules place each in exactly one state. Induction over the array proves `f[1]` counts every odd-sum subsequence once.

## Complexity detail

Let $n$ be the length of `nums`. Each element triggers a parity test and a constant number of arithmetic operations, so time complexity is $O(n)$. Modular arithmetic keeps stored values below the modulus.

The array `f` always has two entries, and `mod` and `x` are scalars. Auxiliary space is $O(1)$. The input is read once and never modified.

Although the mathematical count can be exponential in $n$, the algorithm's work is linear because it aggregates subsequences by parity rather than enumerating them.

## Alternatives and edge cases

- **Closed-form power:** If any value is odd, return `pow(2, n - 1, mod)`; otherwise return zero. This is shorter and has $O(n+\log n)$ or effectively linear scan plus logarithmic exponentiation, but the DP makes the include/exclude logic explicit.
- **Two-dimensional DP:** Storing even and odd counts for every prefix is correct but uses $O(n)$ space. Only the previous prefix is needed, so two rolling states suffice.
- **Enumerate all subsequences:** There are $2^n-1$ nonempty subsequences, making direct generation impossible for $n=10^5$.
- **Track exact sums:** Sum magnitudes are irrelevant; only parity determines future transitions. A sum-indexed DP wastes enormous state.
- **All values even:** Odd count begins at zero and doubles as zero at every step, so the returned answer is zero.
- **Exactly one odd value:** Every odd-sum subsequence must include it, while every even value is optional. The answer is $2^{n-1}$.
- **Several identical odd values:** Positions remain distinct decisions. Choosing an odd number of those occurrences yields odd parity, and the DP counts the index combinations correctly.
- **Single odd element:** The odd singleton is added by the `+ 1` term, producing one.
- **Single even element:** Only the even singleton exists, and `f[1]` remains zero.
- **Modulo placement:** Reducing each state after every update is safe and prevents enormous intermediate counts. The returned value is already normalized.
- **Simultaneous assignment:** Both right-hand expressions need the previous states. An in-place sequential rewrite must save old values first.
