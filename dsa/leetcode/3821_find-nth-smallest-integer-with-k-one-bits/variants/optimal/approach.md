## General

**View every candidate as a fixed-width bit string**

The answer is guaranteed to be below $2^{50}$, so represent every candidate with exactly 50 bit positions, numbered 49 down to 0. Leading zeros do not change the integer or its number of one bits.

Every valid integer corresponds to choosing exactly `k` of those 50 positions for ones. When fixed-width binary strings are compared from the most significant bit downward, a 0 at the first differing position gives the smaller integer and a 1 gives the larger integer. Thus numerical order is the same as lexicographic order over the 50 bits with 0 before 1.

This makes the task a combinatorial unranking problem: construct the `n`th bit string in that order without enumerating the strings before it.

**Precompute how many suffixes contain a required number of ones**

The global table `c` is built once. Its intended meaning is

$$
\texttt{c}[i][j]=\binom{i}{j},
$$

the number of ways to place exactly $j$ ones into $i$ available bit positions.

There is one way to place zero ones, so `c[i][0] = 1`. For positive `j`, Pascal's identity gives

$$
\binom{i}{j}
=
\binom{i-1}{j-1}
+
\binom{i-1}{j}.
$$

The two terms split choices according to whether one distinguished position is 1 or 0. The source fills the table using precisely that recurrence. Entries where $j>i$ remain zero because it is impossible to place more ones than positions.

Although the table has 50 rows and 51 columns, the algorithm only asks `c[i][k]` for lower-position counts at a current bit `i`. Row `i` represents the `i` positions numbered `i - 1` down through 0.

**Count the complete block beginning with zero**

Suppose the construction is deciding bit `i` and still needs `k` one bits in positions `i` through 0.

If bit `i` is set to zero, all `k` ones must be chosen among the `i` lower positions. There are

$$
\binom{i}{k}=\texttt{c}[i][k]
$$

such valid completions.

Because 0 is smaller than 1 at the current most significant undecided position, these completions form the first contiguous block in numeric order. Every completion with bit `i = 0` comes before every completion with bit `i = 1`.

Call this zero-block size $Z$. The current `n` remains a one-based rank within the not-yet-decided possibilities:

- if `n <= Z`, the requested candidate lies in the zero block, so the source leaves bit `i` unset;
- if `n > Z`, all $Z$ zero-prefixed candidates come before the answer, so the source skips them.

The source expresses the second case as `if n > c[i][k]`. Strict `>` is essential: when `n == Z`, the requested candidate is the last member of the zero block, not the first member of the one block.

**Enter the one block and renumber the rank**

When the requested rank lies after the zero block, the current bit must be 1. The source performs three updates:

`n -= c[i][k]` removes all earlier zero-prefixed candidates from the rank.

`ans |= 1 << i` sets bit `i` in the numerical answer.

`k -= 1` records that one of the required one bits has now been placed.

The adjusted `n` is again a one-based rank, now among completions of the chosen prefix. The same decision can be repeated at bit `i - 1`.

If `k > i` before a choice, then the lower `i` positions cannot hold all remaining ones, so `c[i][k] = 0`. Since `n` is positive, the condition is automatically true and bit `i` is forced to 1. The zero table entries therefore handle impossible zero branches without a special case.

**Stop once every required one has been placed**

After setting a bit, `k` may become zero. Every remaining lower bit must then be zero; setting another one would violate the exact-count requirement. Since `ans` starts at zero, those lower bits already have the correct value.

The source breaks immediately. This is both correct and a small efficiency improvement. If it continued, every `c[i][0]` would equal 1 and the valid rank would remain within the zero block, so no more bits would be set anyway.

**Trace the fourth number with two one bits**

For `n = 4` and `k = 2`, all very high positions remain zero because their zero blocks contain far more than four completions. The first decisive position is bit 3.

If bit 3 were zero, two ones would have to fit into bits 2, 1, and 0. There are

$$
\binom{3}{2}=3
$$

such numbers: 3, 5, and 6. Since the desired rank 4 is greater than 3, the algorithm skips that block, sets bit 3, changes `n` to 1, and changes `k` to 1.

At bit 2, the zero block has $\binom{2}{1}=2$ completions, so rank 1 stays in it and bit 2 remains zero. At bit 1, the zero block has $\binom{1}{1}=1$ completion, so bit 1 also remains zero. At bit 0, the zero block has $\binom{0}{1}=0$ completions; bit 0 is forced to one.

The constructed bits are `1001`, which represent 9, the fourth valid integer.

For `n = 3` and `k = 1`, the first decisive position is bit 2. The zero block contains $\binom{2}{1}=2$ numbers, 1 and 2. Rank 3 lies after them, so bit 2 is set and `k` becomes zero. The answer is 4.

**Why the construction returns exactly the requested rank**

Before deciding a bit, the current `n` is the rank among all valid completions of the already fixed prefix. The binomial count partitions those completions into a zero block followed by a one block.

Staying in the zero block preserves the same rank. Entering the one block subtracts exactly the number of earlier completions, yielding the correct rank within that block. In both cases, the invariant continues for the next bit.

The guarantee that an answer exists below $2^{50}$ ensures the initial rank does not exceed $\binom{50}{k}$. Therefore one of the two blocks always contains the requested completion. Once all 50 decisions are resolved—or all ones are placed early—`ans` has exactly `k` original one bits and exactly the original one-based rank.

## Complexity detail

Let $B=50$. The `nthSmallest` method visits at most $B$ bit positions and performs constant-time table access, comparison, subtraction, and bit operations at each one. Its per-call time is $O(B)$ and its additional working space is $O(1)$.

The exact source also contains module-level preprocessing. Pascal's table has $O(B^2)$ entries and takes $O(B^2)$ time and space to build. That cost occurs once when the module is loaded, not once per method call.

Because $B$ is the fixed literal 50 in this problem, both the table and all bit operations are bounded constants with respect to user input. The manifest's $O(B)$ time and $O(1)$ space describe the query and treat the precomputed fixed-size table as constant shared storage. If $B$ were a variable parameter, the fuller statement would be $O(B^2)$ preprocessing space and time, followed by $O(B)$ time and $O(1)$ extra space per query.

## Alternatives and edge cases

- **Enumerate integers and count bits:** Testing positive integers in order is simple but can scan an enormous range before reaching a large rank, despite the answer being below $2^{50}$.
- **Generate combinations then sort:** There are $\binom{50}{k}$ valid bit patterns, far too many to materialize for central values of `k`.
- **Binary search with digit counting:** Count how many integers up to a candidate have exactly `k` bits, then binary-search the answer. This can work in roughly $O(B^2)$ time per query but is more involved than direct unranking.
- **Next-combination bit trick:** Starting from the smallest `k`-bit integer and repeatedly generating the next one takes time proportional to `n`, which is unsuitable for very large ranks.
- **One-based rank:** The branch uses `n > block_size`, not `>=`. Rank 1 selects the first completion in the current block.
- **k equals one:** Valid values are powers of two, and the unranking naturally returns $2^{n-1}$ within the guarantee.
- **k equals 50:** Every position is forced to one because no zero branch can fit the remaining count. There is only one valid 50-bit pattern.
- **Impossible lower suffix:** When `k > i`, `c[i][k]` is zero, forcing the current bit to one without out-of-range logic.
- **Early termination:** Once `k == 0`, every lower bit must remain zero and breaking cannot skip another valid choice.
- **Large result bits:** `1 << i` and bitwise OR construct values exactly in Python, with no floating-point conversion.
- **Existence guarantee:** Without it, an excessive `n` could exhaust all positions without placing the requested number of ones. Valid inputs exclude that situation.
