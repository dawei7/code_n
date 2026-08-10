## General

**Count valid numbers without enumerating every integer**

Testing every integer from `1` through `n` would require work proportional to `n`, which can be about two billion. Digit dynamic programming instead constructs decimal representations one position at a time and counts many valid completions as one cached state.

The string `s = str(n)` supplies the upper-bound digits. Every counted candidate is represented with exactly `len(s)` positions by permitting leading zeros. For example, integer `57` under a three-digit bound is conceptually represented as `057`. These leading zeros are formatting only and must not consume the digit zero or create duplicate-digit violations.

**Meaning of the four state values**

The helper `dfs(i, mask, lead, limit)` returns how many valid positive integers can be formed from position `i` onward under the prefix already chosen.

- `i` is the current digit position.
- `mask` is a ten-bit integer recording which real digits have already appeared. Bit `d` is one exactly when digit `d` has been used after the number started.
- `lead` is true while every selected position has been a leading zero, meaning the positive number has not started.
- `limit` is true when the chosen prefix exactly matches `n`'s prefix. In that case, the current digit cannot exceed `s[i]`. If the prefix is already smaller, any digit through nine is allowed.

These values contain all information future choices need. The exact earlier prefix is irrelevant except for its used digits, whether it has started, and whether it remains tight to the bound.

**Choose the allowed upper digit**

The current maximum digit is:

```python
up = int(s[i]) if limit else 9
```

The loop tries every `j` from zero through `up`. If bit `j` is already set in `mask`, choosing it would repeat a real digit, so that branch is skipped.

When `lead` is true and `j == 0`, this zero is still padding. The recursive call keeps the same mask and keeps `lead` true:

```python
dfs(i + 1, mask, True, limit and j == up)
```

Not setting bit zero here is essential. Otherwise, a number such as `5` represented as `005` would appear to repeat zero and be rejected, even though those zeros are not part of its ordinary decimal representation.

For every other choice, the number has started. The call sets bit `j` and changes `lead` to false. This includes a zero chosen after a nonzero digit: in `105`, the zero is a real digit and must be recorded.

**Maintain the bound correctly**

The next state remains limited only if the current state was limited and `j` equals the current upper digit. Under a limited state, `up` is precisely `n`'s digit at this position, so equality preserves the matching prefix. Choosing less makes every remaining suffix safe to range through `0` to `9`.

When `limit` is already false, the conjunction remains false. Although `up` is then nine, choosing nine does not somehow restore equality with the bound; a previously smaller prefix stays smaller.

**Exclude the number zero**

When `i` reaches the length of `s`, all positions have been chosen. The expression:

```python
int(lead ^ 1)
```

returns one if `lead` is false and zero if it is true. Since Boolean true XOR one becomes zero, the all-leading-zero path is excluded. Every other path represents one positive number and contributes one.

This is how the method counts interval `[1, n]` rather than `[0, n]`.

**Why the digit mask guarantees distinctness**

Before placing a real digit `j`, the algorithm rejects the branch if `mask >> j & 1` is one. If accepted, it records the digit with `mask | 1 << j`. Therefore, every constructed positive representation uses each digit at most once.

Conversely, any positive integer with distinct digits follows one unblocked path: take padding zeros until its first decimal digit, then take its actual digits. None of their bits is already set, and because the number is at most `n`, none violates the tight upper bound.

There is thus a one-to-one correspondence between successful terminal paths and special integers in the requested interval.

**Why caching is valid**

Different prefixes can lead to the same state tuple. Once `i`, `mask`, `lead`, and `limit` match, the set of legal suffix choices is identical, so their counts are identical. `@cache` stores that result and prevents rebuilding the same suffix search.

For example, two already-smaller prefixes that used the same set of digits need exactly the same count of completions; their numeric prefix values no longer matter after `limit` is false.

**A small conceptual example**

For `n = 20`, the search counts all one-digit values `1` through `9`. Among two-digit values within the bound, it counts `10`, `12` through `19`, and `20`. The path for `11` tries to use digit one a second time, sees its mask bit, and is rejected. This leaves nineteen total special integers.

## Complexity detail

Let $L$ be the number of decimal digits in `n`. There are at most $L\cdot2^{10}\cdot2\cdot2$ cached states, and each tries at most ten digits. Time is $O(L\cdot2^{10}\cdot10)$ and cache space is $O(L\cdot2^{10})$.

Because decimal alphabet size ten is fixed, these simplify to $O(L)=O(\log n)$ time and $O(L)$ state layers. Under the concrete constraint `n <= 2 * 10^9`, $L$ is at most ten, so all state storage is bounded by a fixed constant; this is why the manifest reports $O(1)$ space.

The recursion depth is exactly $L$, also at most ten here.

## Alternatives and edge cases

- **Combinatorial prefix counting:** Count all shorter lengths with permutations, then scan `n`'s digits and count smaller unused choices at each prefix. It achieves the same $O(\log n)$ behavior with less state machinery but requires careful case handling.
- **Enumerate every number:** Checking digit uniqueness individually takes roughly $O(n\log n)$ time and is infeasible near two billion.
- **`n` below ten:** Every integer `1` through `n` has one distinct digit, and the DP counts all of them.
- **Repeated digit in `n`:** Tight traversal stops when it would repeat that digit, while already-smaller branches continue normally.
- **Internal zero:** It is recorded in the mask after the number starts and cannot be reused.
- **Leading zeros:** They do not set bit zero and do not make the all-zero representation positive.
- **Number zero:** The terminal `lead` check deliberately contributes zero for it.
- **Upper bound inclusion:** A path equal to every digit of `n` is counted when `n` itself has distinct digits.
- **Ten-digit uniqueness limit:** No positive decimal integer longer than ten digits can have all distinct digits, though the given bound is shorter.
