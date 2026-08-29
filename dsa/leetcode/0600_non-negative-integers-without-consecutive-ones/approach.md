## General

Enumerating every integer from 0 to $n$ is too expensive when $n$ can be $10^9$. The solution instead counts valid binary strings directly with digit dynamic programming. “Digit” here means a binary digit.

The binary representation of any number in $[0,n]$ can be padded with leading zeros to the same bit length as $n$. For example, with three bits, values 0, 1, and 2 become `000`, `001`, and `010`. Leading zeros neither change the numeric value nor create consecutive ones. This gives a one-to-one way to count the entire numeric range as fixed-length bit strings not exceeding $n$.

**The state meaning**

`dfs(i, pre, limit)` counts valid ways to choose bits from position `i` down through position 0, given:

- `i`: the next bit position, scanning from most significant toward least significant;
- `pre`: whether the previously chosen, more-significant bit was 1;
- `limit`: whether the prefix chosen so far is exactly equal to $n$’s prefix.

These three facts completely determine which next bits are legal. Earlier bit details do not matter beyond whether the previous bit was one and whether the upper bound is still tight.

**Respecting the upper bound**

If `limit` is true, the next bit cannot exceed $n$’s bit at position `i`:

```python
up = n >> i & 1
```

Shifting moves bit `i` to the least-significant position, and `& 1` extracts it. If `limit` is false, the already chosen prefix is strictly smaller than $n$’s prefix. Any remaining binary digit 0 or 1 is safe, so `up = 1`.

The loop tries every `j` from zero through `up`.

**Preventing consecutive ones**

If both `pre` and candidate `j` are one, choosing `j` would create adjacent `11`, so that branch is skipped:

```python
if pre and j:
    continue
```

Otherwise, `j` becomes the previous-bit flag for the next lower position.

The next tightness is:

```python
limit and j == up
```

When the old state is tight, staying tight requires choosing exactly the allowed bit from $n$. Choosing zero when $n$ has one makes the constructed prefix smaller, so later bits become unrestricted. When the old state is already not tight, the Boolean remains false.

**The base case counts one completed number**

When `i < 0`, all positions have been assigned without violating either rule. The function returns one for that complete bit string.

This includes the all-zero string, representing integer 0. The range explicitly starts at zero, so that contribution is necessary.

**Why memoization helps**

Different prefixes can reach the same combination of position, previous bit, and limit status. `@cache` stores each state’s answer. There are only a constant number of states per bit position: two `pre` values and two `limit` values. Each state tries at most two next bits.

The initial call uses `n.bit_length() - 1`, the index of $n$’s highest set bit, previous bit zero, and tight status true. Since $n$ is positive, this is a valid nonnegative starting position.

**Tracing $n=5$**

$5$ is binary `101`. At the first bit, choosing 0 counts every valid three-bit padded number beginning with 0; choosing 1 stays tight. Under tight prefix 1, the next bit of $n$ is 0, so only 0 can be chosen. At the last bit, either 0 or 1 is allowed. The DP counts `000,001,010,100,101` and excludes `011` because of its final `11`; values 6 and 7 are above the bound. The count is five.

**Why the algorithm is correct**

Every integer in $[0,n]$ has exactly one padded bit string of $n$’s bit length. The `limit` rule generates exactly strings lexicographically/numerically no greater than $n$: a tight prefix cannot exceed the corresponding bound bit, while a smaller prefix can choose freely afterward. The `pre` rule rejects exactly choices that would place a 1 immediately after a 1.

Each allowed complete bit string follows one unique sequence of loop choices and reaches the base case once. Each invalid or too-large string is blocked at its first offending choice. Therefore, summing all branches counts every and only nonnegative integers at most $n$ without consecutive ones.

## Complexity detail

Let $L=\lfloor\log_2 n\rfloor+1$ be the bit length. There are at most $L\cdot2\cdot2=O(L)$ memo states. Each performs at most two transitions, so time is $O(L)=O(\log n)$.

The cache stores $O(L)$ results, and recursion depth is $O(L)$. Total auxiliary space is $O(\log n)$, matching the manifest. For $n\le10^9$, $L\le30$.

Without memoization, the recursion could revisit equivalent suffix problems and branch toward a Fibonacci-size set. Caching makes cost proportional to the state space rather than the answer count.

## Alternatives and edge cases

- **Iterative Fibonacci bit scan:** Precompute counts of valid bit strings by length, scan $n$ from most significant bit, add counts when seeing a 1, and stop on `11`. It achieves $O(\log n)$ time and space or constant fixed-word space.
- **Bottom-up digit DP:** Store counts for tight/non-tight and previous-bit states while advancing through bits. Avoids recursion and cache overhead.
- **Brute-force every integer:** Takes $O(n\log n)$ bit checks and is infeasible at $10^9$.
- **Generate valid numbers recursively:** Avoids invalid strings but still takes time proportional to the potentially large output count.
- **Integer zero:** Counted by the all-leading-zero assignment.
- **$n=1$:** Padded strings `0` and `1` are both valid, yielding two.
- **$n$ contains `11`:** Tight traversal cannot continue through both ones; other branches already count all valid smaller values.
- **$n$ itself valid:** The exact tight bit sequence reaches the base case and is included.
- **Leading zeros:** They do not create consecutive ones and let shorter binary representations share one fixed length.
- **Limit transition:** Equality preserves tightness; choosing below the current bound bit releases it permanently.
- **Previous-bit state:** Only adjacency matters, so retaining the whole prefix would waste state.
- **Positive-input guarantee:** `bit_length() - 1` starts correctly. For hypothetical $n=0$, it would start at -1 and still return one.
- **Caching closure:** `n` is fixed in the enclosing method, so the arguments fully identify a state within one call.
