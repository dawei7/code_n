## General

The selected competitive implementation builds the reflected binary Gray sequence one bit at a time. It starts with `[0]`, the complete sequence for zero bits. When introducing bit position $i$, it leaves the current sequence in place as the half whose new bit is `0`, then walks that sequence in reverse and appends copies with bit $i$ set to `1`.

For example, after one bit the list is `[0, 1]`, written as `[00, 01]` when preparing to build the two-bit sequence. Traversing backward sees `1` and then `0`; setting the new bit produces `11` and `10`. Appending them gives

$$
[00,01,11,10].
$$

Repeating the process for a third bit retains `[000,001,011,010]` and appends the reversed, high-bit-set half `[110,111,101,100]`.

**Why reflection is necessary**

Suppose the current list is a valid cyclic Gray sequence for $i$ bits. The first half of the enlarged list uses the same values with a leading `0`, so all neighbor relationships inside that half remain valid. The second half uses the old sequence in reverse with a leading `1`. Reversing a path does not change how many bits differ between its adjacent values, and adding the same leading bit to every value does not introduce a difference. Thus neighbors inside the second half also differ in exactly one bit.

The delicate part is the join between the halves. The last value of the first half and the first appended value have identical old $i$ bits because the second traversal begins with that same last value. Only the newly set bit differs. This is precisely why the old sequence must be reflected. If it were appended in forward order, the join would compare the old last value with the old first value while also changing the new bit; because those old endpoints already differ by one bit, the join would differ by two bits and fail.

The final wraparound is valid for a similar reason. The last appended value is based on the old first value. Since the construction begins with zero, that old first value is `0`; the new last value is therefore exactly `1 << i`. It differs from the first value, still `0`, only in the newly introduced bit.

**Why every required value appears exactly once**

Before an iteration, every current number is below $2^i$, so bit $i$ is zero in all of them. The retained first half therefore contains all values with that bit zero. The appended half computes `1 << i | value`, which sets bit $i$ while preserving all lower bits. Every appended value is consequently different from every retained value.

The old values were already unique by the induction hypothesis. Applying the same one-to-one bit-setting operation to distinct old values keeps the appended values distinct as well. The list doubles from $2^i$ entries to $2^{i+1}$ entries, and those entries cover every $(i+1)$-bit pattern exactly once.

Starting from the correct zero-bit sequence and preserving all four properties—start at zero, uniqueness and full coverage, one-bit adjacency, and one-bit wraparound—proves by induction that after `n` iterations the returned list is a valid $n$-bit Gray code sequence.

**How the two loops modify one list safely**

The outer loop `for i in range(n)` introduces bit positions $0,1,\ldots,n-1$. During each iteration, `reversed(result)` creates a reverse iterator whose initial position is the old end of the list. Each visited value causes one append.

Appending while iterating over a list can often be dangerous because a forward iterator may continue into newly appended elements. Reverse iteration avoids that problem in CPython's list iterator behavior: its index moves downward through positions that existed at the start, while every append occurs at a larger position beyond the iterator's starting index. It therefore visits exactly the prior sequence once and terminates. It also produces the required reflection without allocating a reversed copy.

The expression `1 << i | n` sets the new bit. The lower bits of `1 << i` are zero, and the old value has bit $i$ zero, so bitwise OR is equivalent here to adding $2^i$. OR states the intent more directly: preserve the old pattern and switch on one designated bit.

There is an unfortunate naming choice in the exact source: the inner loop is `for n in reversed(result)`, reusing the parameter name `n` for each old list value. This does not break this function. The outer `range(n)` iterator is created before the inner assignments, and the original bit count is not needed after that creation. Rebinding `n` is nevertheless confusing and fragile; a clearer name such as `value` would make the data roles obvious.

The file also contains a separate `Solution2` class with the direct formula `i >> 1 ^ i`. That class is an alternative implementation, not the body of the selected `Solution.grayCode` method explained here.

## Complexity detail

Let $N=2^n$, the number of integers that the answer must contain. At outer iteration $i$, the list initially contains $2^i$ values, and the inner loop visits and appends exactly those $2^i$ values. The total work is therefore the geometric sum

$$
1+2+4+\cdots+2^{n-1}=2^n-1.
$$

Each iteration performs constant-time bit operations and a list append under the standard fixed-width word model, giving $O(2^n)$ time. This matches the output-size lower bound and is optimal for returning an explicit sequence.

The manifest's $O(1)$ space bound means auxiliary space excluding the output list. The algorithm extends the same list that it ultimately returns and does not create a second reflected list, a visited set, or a recursion stack. The reverse iterator and loop variables require constant extra storage. The returned list itself occupies $O(2^n)$ space and must be counted if the convention includes output memory.

Although Python list resizing occasionally copies references into a larger backing array, appends are amortized $O(1)$. Across all $N-1$ appends, resizing remains linear in aggregate and does not change the $O(2^n)$ time bound.

## Alternatives and edge cases

- **Direct binary-to-Gray formula:** Generate position $i$ as `i ^ (i >> 1)`. It has the same $O(2^n)$ time and constant auxiliary space, is shorter, and is implemented as `Solution2` in the source file. Its proof is more algebraic, whereas reflection is often easier to derive visually.
- **Recursive reflection:** Recursively build the smaller sequence and append its reflected high-bit copies. It mirrors the same recurrence but consumes $O(n)$ stack space and offers no runtime advantage.
- **Backtracking:** Flip each possible bit from the current value and search among unseen values. It needs a visited structure of up to $2^n$ entries and obscures the deterministic structure. General Hamiltonian-cycle search can also be far more expensive.
- **Do not iterate forward while appending:** A forward traversal of the changing list may visit newly appended entries, and even a bounded forward traversal would append the old sequence in the wrong order. The reflected order is part of the correctness proof, not an implementation detail.
- **Variable shadowing:** Reusing `n` in the inner loop is safe only because the outer iterator has already captured `range(original_n)` and no later expression needs the parameter. Renaming that loop variable is preferable in maintained code, although the explanation preserves and accurately describes the selected source.
- **Minimum input:** At $n=1$, the sole iteration reflects `[0]`, sets bit zero, and returns `[0, 1]`.
- **Largest allowed input:** At $n=16$, the method returns exactly $65{,}536$ values. The running time and output memory necessarily grow exponentially in the bit count because the requested output itself does.
- **Leading zeros:** Values are returned as decimal integers, so leading binary zeros are not stored. They are conceptually present when checking the $n$-bit adjacency rule.
- **Any valid ordering is acceptable:** Reflection chooses one canonical cycle. Reversing a valid cycle or permuting bit positions can produce other valid answers, but the judge need not receive a particular example ordering.
