## General

Let $n$ and $m$ be the lengths of `nums1` and `nums2`.

**View a solution as one global interleaving**

All chosen integers are distinct, so sort them globally. Reading which array owns each value produces an interleaving that preserves the original order of both arrays, because each replaced array must be increasing. Conversely, any such interleaving defines a valid construction if every next integer has its position's required parity.

For a previous value `x` and required parity `p`, the smallest legal next value is `x + 1` when that value has parity `p`, otherwise `x + 2`. Choosing anything larger cannot help a later transition, so only this smallest extension matters.

**Store the best last value for two prefixes**

Define the state for prefixes of lengths `i` and `j` as the minimum possible last assigned integer after interleaving those positions. Its final assignment must come from exactly one of two choices:

- append `nums1[i - 1]` after an optimal state for `(i - 1, j)`; or
- append `nums2[j - 1]` after an optimal state for `(i, j - 1)`.

Advance each predecessor to the smallest larger integer with the appended parity and keep the smaller result. The empty state has last value zero. The top row and left column simply extend one array alone.

Every valid interleaving ends with one of these two transitions, so the recurrence examines all possibilities. Replacing any prefix by another with a no-larger last value never restricts future parity choices, establishing optimal substructure. The state at `(n, m)` is therefore the minimum possible global maximum.

**Roll the table by rows**

Each state uses only the previous row and the current row's preceding cell. Retain those two rows instead of the full table.

## Complexity detail

There are $(n+1)(m+1)$ prefix states and each transition uses constant arithmetic, giving $O(nm)$ time. Two rows of $m+1$ integers use $O(m)$ space. When `nums1` is empty, only the initialized top row is needed.

## Alternatives and edge cases

- **Enumerate all interleavings:** Trying every merge of the two arrays is correct but can require $\binom{n+m}{n}$ paths.
- **Construct each array independently:** This may reuse the same integer across arrays and violates global uniqueness.
- **Greedily choose the array with the smaller next value:** Equal local choices can affect later parity runs, so a single greedy path can miss the best interleaving.
- An empty `nums1` reduces to assigning the smallest increasing parity-compatible sequence to `nums2`.
- Two positions with the same parity cannot use the same integer; one must advance to the next positive integer of that parity.
- Odd replacements begin at 1, while even positive replacements begin at 2.
- Long runs of one parity advance by two within the owning array.
- The two arrays may have different lengths or identical parity patterns.
- Strict increase is required inside each array, while values across arrays need only be distinct.
