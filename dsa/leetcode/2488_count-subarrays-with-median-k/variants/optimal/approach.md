## General

**Every qualifying range crosses one fixed pivot.** Because all values are distinct and `k` occurs exactly once, a subarray can have median `k` only if it contains `k`'s index. The task is therefore to choose a left endpoint at or before that pivot and a right endpoint at or after it.

**Replace values by their relation to `k`.** Give every value greater than `k` weight $+1$, every value smaller than `k` weight $-1$, and `k` weight $0$. The sum of a range containing `k` is the number of greater values minus the number of smaller values. For an odd-length qualifying range those counts are equal, so the balance is $0$. For an even-length range, `k` is the left middle element exactly when there is one more greater value than smaller values, so the balance is $1$.

**Pair the two sides instead of enumerating ranges.** Starting immediately left of the pivot, accumulate balances while moving outward and count their frequencies. Include balance zero once to represent choosing the pivot itself as the left endpoint. Then scan from the pivot toward the right while maintaining a right-side balance $b$.

A left balance $a$ forms a valid range when $a+b$ is $0$ or $1$. The needed left balances are therefore $-b$ and $1-b$, and their stored frequencies give the number of new valid subarrays ending at the current right endpoint. Every possible pair of endpoints crossing the pivot is considered exactly once, while the two balance equations accept exactly the odd- and even-length ranges whose median is `k`.

## Complexity detail

Let $n = \lvert\texttt{nums}\rvert$. Finding the pivot and scanning the two sides take $O(n)$ time in total. The balance-frequency map can contain $O(n)$ distinct keys, so the auxiliary space is $O(n)$ under expected constant-time hash-table operations.

## Alternatives and edge cases

- **Enumerate all pivot-crossing ranges:** Updating the balance for every left/right endpoint pair avoids sorting but still takes $O(n^2)$ time.
- **Sort every subarray:** Generating all ranges and sorting each one is much slower and repeats nearly all comparison work.
- **Prefix balances over the whole array:** Prefix sums alone do not ensure a counted range contains the unique `k`; anchoring both endpoints around its pivot makes that requirement explicit.
- **Single element:** The range `[k]` has balance zero and contributes one.
- **Even-length ranges:** They require balance $1$, not $0$, because the problem chooses the smaller left-middle value.
- **`k` is the maximum:** No range containing another value can balance enough greater elements, so only `[k]` qualifies.
- **Pivot at an endpoint:** The empty choice on the missing side is represented by the initial zero balance and the same pairing logic still applies.
