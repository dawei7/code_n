## General

**Assign every subarray to one minimum**

Instead of enumerating subarrays, treat each `strength[i]` as the minimum and
sum the contribution of every subarray assigned to it. A monotonic stack finds
`left`, the nearest index with a strictly smaller value, and `right`, the
nearest index with a smaller-or-equal value. Then index $i$ is the designated
minimum exactly for subarrays whose left endpoint is in $(\text{left},i]$ and
right endpoint is in $[i,\text{right})$.

The strict comparison on one side and non-strict comparison on the other is
essential: when equal strengths occur, it assigns each subarray to exactly one
of them rather than omitting or double-counting it.

**Aggregate all sums in the assigned rectangle**

Let $P[k]$ be the sum of the first $k$ strengths, and let

$$
Q[k]=\sum_{t=0}^{k-1}P[t].
$$

For a fixed left endpoint $a$ and right endpoint $b$, the subarray sum is
$P[b+1]-P[a]$. Summing this expression over all assigned endpoint pairs
separates into a right-prefix term repeated for every left choice and a
left-prefix term repeated for every right choice:

$$
\bigl(Q[\text{right}+1]-Q[i+1]\bigr)(i-\text{left})
-
\bigl(Q[i+1]-Q[\text{left}+1]\bigr)(\text{right}-i).
$$

Multiplying that aggregate by `strength[i]` gives the total strength of all
subarrays assigned to $i$. Summing these contributions modulo $10^9+7$ covers
every subarray once. Stack entries are pushed and popped at most once, and all
prefix and contribution work is constant per index.

## Complexity detail

Let $n$ be the array length. Both monotonic-stack passes, both prefix levels,
and the contribution pass take $O(n)$ total time. Boundary arrays, stacks, and
prefix storage use $O(n)$ auxiliary space. Modular reduction keeps accumulated
values bounded without changing the required residue.

## Alternatives and edge cases

- **Direct subarray enumeration:** Maintaining each growing subarray's sum and minimum is correct but takes $O(n^2)$ time.
- **Segment trees per endpoint:** Range minima and sums can accelerate individual queries, but enumerating all endpoint pairs still leaves too many subarrays.
- **Equal strengths:** One boundary must be strict and the other non-strict so every tied-minimum subarray has one owner.
- **One wizard:** The only group contributes the square of that wizard's strength.
- **Increasing or decreasing arrays:** Boundary spans become one-sided, but the same formulas apply.
- **Large strengths:** Contributions can far exceed ordinary integer ranges in fixed-width languages, so multiplication and modular reduction require wide intermediates.
- **Modulo subtraction:** Intermediate prefix differences may be negative after modular reduction; normalize the final residue.
