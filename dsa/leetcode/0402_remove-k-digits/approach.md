## General

**Minimize the earliest possible digit**

Removing exactly `k` digits preserves the relative order of all remaining digits. Every candidate therefore has the same raw length `len(num) - k` before leading-zero normalization. Among equal-length decimal strings, the first position where they differ determines which number is smaller.

This gives the greedy priority: improve a digit as far to the left as possible, even if that means sacrificing a larger digit immediately before it.

When a new digit `c` is smaller than the last kept digit, retaining that larger digit would place it earlier in the final number. If one deletion remains, removing the larger previous digit and allowing `c` to move left creates a smaller result than keeping the larger digit and deleting something later.

The exact solution implements this rule with a monotonically non-decreasing stack.

**What the stack represents**

`stk` contains the digits provisionally kept from the processed prefix. Before appending a new digit, the method repeatedly checks:

```text
while k and stk and stk[-1] > c:
```

All three conditions are necessary:

- `k` must be positive because no more than the requested number of deletions is allowed;
- the stack must be nonempty because there must be a previous digit to remove;
- `stk[-1] > c` means replacing that earlier larger digit with the current smaller digit improves the number at the first affected position.

Each successful iteration pops one kept digit and decrements `k`. Repeating rather than checking once is important: one small incoming digit may be better than several preceding digits.

After no further beneficial deletion is possible, the method appends `c`.

**Why equal digits are not popped**

The condition uses strict `>` rather than `>=`. Removing an equal previous digit does not improve the current prefix. Keeping the earlier equal digit preserves more future deletion flexibility, while either choice begins with the same digit.

For example, with `112` and one deletion, popping the first `1` when the second `1` arrives provides no advantage. The later decision should remove the final `2`, yielding `11`.

**A local exchange argument**

Suppose the processed digits end with kept digit `x`, the new digit is `y`, and `x > y`. Compare two strategies that still have a deletion available:

- keep `x` and delete `y` or some later digit;
- delete `x` and keep `y` in the earlier position.

Both final strings have the same number of digits. They share the same prefix before `x`, but at the next position the second strategy has smaller digit `y` while the first has `x`. No choice in later positions can overcome that earlier difference. Therefore some optimal answer deletes `x`, and the greedy pop is safe.

After popping `x`, the same argument applies to the new stack top. This justifies the repeated while loop.

**Why remaining deletions come from the right**

The greedy loop may finish with `k > 0`. This happens when the kept digits never present another descent worth fixing—for example, when the number is non-decreasing.

In a non-decreasing sequence, deleting an earlier digit would expose an equal or larger digit in its place. Deleting the rightmost digits preserves the smallest possible prefix, so all leftover removals must come from the tail.

The exact source handles this without another pop loop. Before mutating `k`, it saves

```text
remain = len(num) - original_k
```

Every valid raw result must contain exactly `remain` digits. After the scan, `stk[:remain]` keeps the first required number of greedy-stack digits and discards any tail beyond that length.

Suppose the while loops used `p` deletions. The mutated `k` is `original_k - p`, and stack length is `len(num) - p`. Slicing it to `len(num) - original_k` removes exactly `original_k - p`, the number of deletions still owed. Thus the slice is equivalent to popping the remaining `k` tail digits.

**Tracing `1432219` with three deletions**

The original target length is four.

1. Read `1`: stack becomes `[1]`.
2. Read `4`: no descent; stack becomes `[1,4]`.
3. Read `3`: `4 > 3`, so pop `4` and spend one deletion; append `3`, giving `[1,3]`.
4. Read `2`: pop `3`; append `2`, giving `[1,2]`.
5. Read the next `2`: equal top is not popped; stack becomes `[1,2,2]`.
6. Read `1`: pop one `2`, using the final deletion; append `1`, giving `[1,2,1]`.
7. Read `9`: no deletions remain, so append it.

The first four stack digits are `1219`, which is the minimum possible result.

**Leading zeros are a representation issue, not a selection issue**

For `num = "10200"`, `k = 1`, the digit `0` pops the leading `1`, producing a kept sequence beginning `0`. That is correct numerically: deleting `1` gives raw digits `0200`, which represent integer 200.

After joining the selected digits, `.lstrip('0')` removes representation-only leading zeros. It does not remove zeros inside or at the end of the number.

If every selected digit is zero, stripping produces the empty string. If all digits were removed, joining also produces empty. The final `or '0'` converts both cases to the required normalized representation `"0"`.

**The stack invariant**

After processing a prefix, the stack is the lexicographically smallest sequence obtainable from that prefix using exactly the deletions already spent, subject to retaining all processed digits not yet removed and preserving enough flexibility for the suffix. Any descent that can improve the earliest retained position has been eliminated while deletions remain.

The exchange argument proves every pop is compatible with an optimum. If deletions remain after scanning all digits, the stack is non-decreasing with respect to all available greedy choices, and removing its suffix is optimal. Therefore the first `remain` digits form the smallest raw fixed-length result. Normalization changes only its textual leading zeros, not its numeric value.

## Complexity detail

Let $n$ be the length of `num`.

Every digit is appended to the stack once. A digit can be popped at most once. Although the while loop is nested inside the for-loop, total pop iterations across the full run are at most $n$. Joining, slicing, and stripping each inspect at most $n$ characters. Total time is $O(n)$.

The stack can hold all $n$ digits, and the joined result creates another string of up to $n$ characters. Auxiliary space is $O(n)$. The input may contain up to $10^5$ digits, so the algorithm never converts the complete value to a fixed-width integer.

## Alternatives and edge cases

- **Enumerate deletion combinations:** There are $\binom{n}{k}$ choices, which is exponential in the worst case. Greedy monotonicity avoids exploring them.

- **Repeatedly remove the first descent from a string:** Applying the same rule directly is correct but repeated string deletion and rescanning can cost $O(kn)$ time. The stack performs all deletions in one pass.

- **Non-decreasing input:** No stack pop occurs. The prefix slice removes the largest rightmost digits, which is optimal.

- **Strictly decreasing input:** Each new smaller digit pops earlier digits until `k` reaches zero. This moves the smallest available digits as far left as allowed.

- **`k == len(num)`:** `remain` is zero, the slice is empty, and the method returns `"0"`.

- **Result begins with zeros:** `lstrip('0')` normalizes them away after digit selection.

- **Result contains internal zeros:** Only leading zeros are stripped; values such as `1002` remain unchanged.

- **All remaining digits are zero:** Stripping empties the string, and `or '0'` returns the canonical zero.

- **Repeated equal digits:** Strict comparison preserves them until a genuinely smaller digit or tail deletion determines which occurrences are removed.

- **Original `num = "0"`:** The constraints force `k = 1`, so all digits are removed and the result is `"0"`.

- **Mutated `k`:** The saved `remain` uses the original deletion request. This is why slicing still removes the correct total after greedy pops decrement `k`.

- **String comparison rationale:** Raw candidates all have equal length before normalization, so lexicographic minimization of their digits is equivalent to numeric minimization.
