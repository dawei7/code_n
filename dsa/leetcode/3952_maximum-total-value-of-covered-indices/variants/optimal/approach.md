## General

Every token may stay at its original index or move exactly one position left, and may move at most once. Since all `nums` values are positive, an optimal plan wants the tokens to cover as many distinct indices as possible; sending two tokens to the same index would lose a positive contribution without creating a new covered position.

The source groups consecutive token positions into runs. Each run can be optimized independently.

**Why consecutive tokens form one interacting block**

Suppose `s` has a maximal run of ones from index $a$ through $b$. There are

$$
r=b-a+1
$$

tokens in the run.

A token originally at index $i$ can end only at $i$ or $i-1$. For the entire run, every possible destination lies in:

$$
[a-1,b]
$$

when $a>0$. This candidate block contains $r+1$ indices for $r$ tokens.

Tokens outside this run do not compete for these positions. Since the run is maximal, `s[a-1]` is zero when $a>0$. Any previous token run ends by index $a-2$, and its candidate positions do not extend to $a-1$. A following run similarly begins after at least one zero.

Therefore run contributions can be added.

**A run not starting at zero can omit any one candidate**

There are $r$ tokens and $r+1$ candidate indices $a-1,a,\ldots,b$. With distinct coverage, exactly one candidate must be omitted.

Every possible omission is achievable. Suppose index $q$ is to be omitted:

- tokens from $a$ through $q$ move left, covering $a-1$ through $q-1$;
- tokens after $q$ stay, covering $q+1$ through $b$.

For the special omission $q=a-1$, no token needs to move and all original run positions are covered. For $q=b$, every token shifts left. Intermediate omissions use a shifted prefix and stationary suffix.

Thus the run can cover any $r$ of the $r+1$ candidate values. To maximize their positive-value sum, include all candidates except the one with minimum `nums` value.

The source computes exactly this:

- `block_sum` begins as the sum of values at token positions $a$ through $b$;
- `block_min` tracks their minimum;
- `preceding_value = nums[a - 1]` is added;
- the minimum across all $r+1$ candidates is subtracted.

The result is the greatest attainable contribution for that run.

**A run beginning at index zero**

When $a=0$, there is no index $-1$. The leftmost token cannot move left, and the candidate set is only the $r$ original indices $0$ through $b$.

Keeping every token in place covers all $r$ candidates. Since all values are positive, dropping a covered index through a collision cannot help. The optimal contribution is simply the sum of the run's original values.

The source recognizes this with `if run_start > 0`. It performs the add-and-remove-minimum step only when a preceding index actually exists.

**Scan maximal runs once**

The outer loop skips every index whose character is zero. On a one, it records `run_start` and initializes the running sum and minimum with that position.

The inner loop advances while later characters are also one, accumulating the complete maximal run. When it stops, `index` already points at the first following zero or at the array end.

The source applies the appropriate run formula, adds `block_sum` to `total`, and resumes the outer scan. No token or value is processed in more than one run.

**Why positive values matter**

For a run with a preceding empty position, the formula deliberately covers $r$ distinct indices. If values could be negative, it might be better to make tokens collide and cover fewer indices, avoiding a negative contribution.

The contract guarantees every `nums[i] >= 1`. Covering one more distinct position always increases the total, so maximizing the number of distinct covered positions within each run is safe. Once that number is fixed at $r$, omitting only the minimum candidate maximizes value.

**Why the sum of run optima is globally feasible**

Candidate blocks for different maximal runs are disjoint, so moves chosen for one run never place a token on an index used by another run. Combine each run's shifted-prefix/stationary-suffix construction. Every token moves at most once and only left by one.

The combined covered-index sum equals the sum of the independently optimized blocks. Conversely, any global plan restricts to some feasible choice within each run and cannot exceed that run's maximum. The added `total` is therefore globally optimal.

## Complexity detail

Let $n$ be the common length of `nums` and `s`. `index` only moves forward. The inner loops collectively visit every one-character position once, while the outer loop visits intervening zeroes once. Total time is $O(n)$.

The source stores scalar indices, a block sum, a block minimum, and the accumulated total. It does not allocate run lists or modify the input, so additional space is $O(1)$.

The manifest's $O(n)$ time and $O(1)$ space bounds accurately describe the implementation.

## Alternatives and edge cases

- **Dynamic programming per token:** A two-state stay/move DP can model collisions, but run structure and positive values reduce each component to “omit its minimum.”
- **Move every token left whenever possible:** This omits the rightmost run value regardless of its weight and can be suboptimal.
- **Never move tokens:** This omits the preceding zero-position candidate even when it has a large value.
- **Choose the largest candidate positions without proving feasibility:** The run construction shows that every single omitted candidate is realizable; arbitrary subsets in more general movement problems may not be.
- **Allow multiple tokens to improve one covered index:** Coverage is binary per index. Collisions do not add the value twice and are harmful with positive values.
- **Run starts at zero:** No preceding candidate exists, so all original run values are summed and none is subtracted.
- **Single token at index greater than zero:** It can cover either its own index or the preceding one; adding both and subtracting the smaller selects the larger.
- **Single token at index zero:** It cannot move and contributes `nums[0]`.
- **All characters are zero:** No run is processed and the answer is zero.
- **All characters are one:** The sole run starts at zero, so leaving all tokens in place covers every index and returns the sum of `nums`.
- **Runs separated by one zero:** That zero is a candidate only for the following run; the previous run's candidates end before it, so independence holds.
- **Minimum candidate is inside the token run:** Shift the prefix through that token and leave later tokens stationary to omit exactly that interior position.
- **Minimum candidate is the preceding empty index:** Leave every token in place.
- **Minimum candidate is the run's final position:** Move every token in the run one step left.
- **Large sums:** Python integers safely accumulate up to the full positive array sum.
