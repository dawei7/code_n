## General

**Parse each record but preserve its original index**

Every transaction string is split into `name`, `time`, `amount`, and `city`. Time and amount are converted to integers for arithmetic comparisons.

The original index `i` is retained because the required output contains the original strings. It also distinguishes two separate input entries that happen to have identical text.

The set `idx` stores indices known to be invalid. A set prevents the same transaction from being added repeatedly when it violates both rules or conflicts with several other transactions.

**Apply the amount rule independently**

If `amount > 1000`, the current index is inserted into `idx` immediately. The inequality is strict: an amount exactly equal to 1000 is allowed by this rule.

This check does not depend on any other transaction. A record may later also be marked by a city-time conflict, but set insertion remains idempotent.

**Group earlier records by customer name**

`d[name]` is a list of parsed triples `(time, city, index)` for transactions of that name seen so far in input order.

The current tuple is appended before the comparison loop. The loop therefore includes the current transaction itself, but it cannot conflict with itself because its city equals its own city. The `c != city` condition rejects the self-comparison.

Grouping by name avoids comparing transactions belonging to different people. The invalidity rule requires the same name, so cross-name pairs can never matter.

**Check the symmetric city-and-time conflict**

For every stored transaction `(t, c, j)` of the same name, the condition requires:

- `c != city`, meaning the cities differ;
- `abs(time - t) <= 60`, meaning their timestamps differ by at most 60 minutes, including exactly 60.

When both hold, *both* transactions are possibly invalid. The code adds both `i` and `j` to `idx`.

Although records are processed in input order rather than time order, absolute difference makes the test symmetric. Every unordered pair of same-name transactions is examined when the later input entry is processed. It does not matter which timestamp is earlier.

**Why marking both indices is necessary**

The rule does not say only the later transaction is invalid. If Alice has transactions at times 20 and 50 in different cities, each one has another same-name, different-city transaction within 60 minutes. Both must appear.

Adding only the current index would miss the earlier member of a newly discovered conflicting pair.

**Return original strings in any order**

The final comprehension maps every invalid index back to `transactions[i]`. Iterating a Python set does not promise input or sorted order, but the contract permits any order.

If two identical transaction strings occupy different invalid indices, the output can contain that identical text twice because the comprehension iterates indices, not unique strings. This preserves transaction entries rather than deduplicating by textual content.

**Why the algorithm is correct**

Every index placed in `idx` has a direct witness: either its amount exceeds 1000, or it belongs to a checked pair with the same name, different cities, and time difference at most 60. Thus every returned transaction satisfies at least one invalidity condition.

Conversely, consider any invalid transaction. If its amount is too high, it is marked during its own iteration. Otherwise, it has a conflicting partner. Whichever of those two entries appears later in the input causes the pair to be compared, because the earlier one is already stored under the same name. The condition succeeds and adds both indices, including the transaction under consideration.

Therefore, all and only possibly invalid entries are returned.

**The exact source does not use the manifest's sorting strategy**

The local manifest states `O(n log n)` time, but the exact implementation does not sort transactions or use a bounded moving window. For every transaction, it scans all previously stored transactions with the same name.

If all `n` transactions share one name, the number of comparisons is

`1 + 2 + ... + n = O(n^2)`.

The approach must document that actual nested-scan behavior rather than attribute a sorting bound to code that does not implement it.

## Complexity detail

Parsing all transaction strings is linear in their total text length; field lengths are bounded by the contract. The dominant work is the same-name comparison loops.

If name group `g` contains `n_g` transactions, it performs `O(n_g^2)` pair work. Summed across groups, the worst case is `O(n^2)` when one group contains every transaction.

The dictionary lists store every parsed transaction once, and `idx` can store every index, so auxiliary space is `O(n)`.

The manifest's `O(n log n)` bound would require a different implementation, such as sorting each name's transactions by time and using a carefully maintained 60-minute neighborhood. It is not the bound of this source.

## Alternatives and edge cases

- **Sort by name and time:** Grouped sorting can organize nearby comparisons, but differing-city conflicts within a 60-minute window still need data structures or bounded scanning to avoid quadratic work.
- **Compare every global pair:** This is also `O(n^2)` but wastes comparisons across different names. The dictionary limits scans to potentially relevant pairs.
- **Mark only the later transaction:** Both members of a qualifying pair are invalid, so both indices must be added.
- **Use `< 60` instead of `<= 60`:** The rule includes exactly 60 minutes, so the comparison must be inclusive.
- **Amount exactly 1000:** It is not invalid by amount, though another transaction may invalidate it.
- **Same name and time but same city:** The city condition fails, so the pair alone is valid.
- **Same name and time in different cities:** The time difference is zero and both entries are invalid.
- **Different names:** They never conflict regardless of city and time.
- **One transaction violates both rules:** A set keeps one index and produces one output entry for that input position.
- **Duplicate textual records:** Separate indices remain separate transactions and can both appear in the returned list.
- **Any output order:** Set iteration is acceptable because ordering is explicitly unrestricted.
- **Manifest mismatch:** The exact nested same-name scans are quadratic in the worst case, not `O(n log n)`.
