## General

**Turn strict majority into positive balance.** Replace every occurrence of `target` conceptually by $+1$ and every other value by $-1$. For a subarray containing $f$ target values among $L$ elements, its transformed sum is $f-(L-f)=2f-L$. The required condition $2f>L$ is therefore exactly the condition that this sum is positive.

Let `balance` be the transformed prefix sum. A subarray ending at the current position has positive sum precisely when its earlier prefix balance is strictly smaller than the current one. The answer can consequently be built by adding the number of earlier prefixes below each new balance.

**Exploit the unit-step walk.** Each new array value changes `balance` by exactly $+1$ or $-1$. Maintain `smaller_prefixes`, the number of recorded prefix balances strictly below the current balance, together with the frequency of every visited balance.

- On a $+1$ step, prefixes equal to the old balance become newly smaller, so add their frequency.
- On a $-1$ step, prefixes equal to the new balance are no longer smaller, so subtract their frequency.

After that update, `smaller_prefixes` is exactly the number of valid starting prefixes for the current endpoint. Add it to the answer, record the new balance, and continue. The initial zero balance represents the empty prefix, allowing subarrays that begin at index `0` to be counted by the same rule.

## Complexity detail

Every value causes one constant-time balance update and one frequency update, so the running time is $O(n)$. Balances remain in $[-n,n]`; the frequency array for those states uses $O(n)$ auxiliary space. The answer may reach $n(n+1)/2$, so fixed-width implementations must use a 64-bit result type for the $10^5$-element limit.

## Alternatives and edge cases

- **Fenwick tree or merge-sort counting:** Counting ordered prefix pairs with smaller-left balances works in $O(n\log n)$ time, but it misses the constant-time update available because adjacent balances differ by exactly one.
- **Enumerate every subarray:** Maintaining a target count while extending each left endpoint is straightforward and correct, but $O(n^2)$ time is not viable for the II constraint.
- **Exactly half is not enough:** A zero transformed subarray sum represents a tie and must not be counted because the majority comparison is strict.
- **Target absent:** Every step is $-1$, so no later prefix exceeds an earlier one and the answer is `0`.
- **Every value equals target:** Every subarray has positive transformed sum, producing the maximum answer $n(n+1)/2$.
- **Large element values:** Only equality with `target` matters; the values up to $10^9$ are never used as frequency-array indices.
