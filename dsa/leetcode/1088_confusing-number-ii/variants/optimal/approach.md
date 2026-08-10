## General

**Generate only numbers whose digits can be rotated**

A number can be confusing only if every one of its digits has a valid rotated form. The valid digits are `0`, `1`, `6`, `8`, and `9`. Rather than checking every integer from one through `n`, the solution builds only numbers made from those five digits.

The list `d` is a direct lookup table indexed by an ordinary digit. Its values encode the rotation: zero maps to zero, one to one, six to nine, eight to eight, and nine to six. Every invalid digit has value `-1`. The condition `d[i] != -1` is therefore both a validity test and permission to append digit `i`.

**Use a digit prefix to stay at or below the upper bound**

The decimal text `s = str(n)` fixes the number of positions to the number of digits in `n`. The recursive function `dfs(pos, limit, x)` fills those positions from left to right.

The parameter `pos` is the position currently being chosen. The integer `x` contains the valid digits chosen so far. Appending digit `i` uses `x * 10 + i`, exactly the usual decimal place-value rule.

The Boolean `limit` records whether the chosen prefix is still identical to the corresponding prefix of `n`. If it is true, the next digit cannot exceed `int(s[pos])`. If it is false, an earlier digit was already smaller, so any digit through nine is safe: no choice in later positions can make the completed number exceed `n`.

After choosing `i`, the next call remains limited only when the old prefix was limited and `i == up`. In a limited call, `up` is the current digit of `n`, so equality preserves the tie. Choosing a smaller digit makes the new limit false. In an already-unlimited call, the left side of the `and` is false, so it can never become limited again.

This prefix rule proves that the DFS never produces a value greater than `n`. Conversely, take any integer at most `n` whose digits are all rotatable and pad it on the left with zeros to the length of `s`. At every position, its digit is among the DFS choices and respects the upper-bound prefix rule, so the DFS reaches it.

Leading zeros are useful here. They let one fixed-depth tree represent numbers with fewer digits. For example, when `n` has three digits, choices `0, 1, 6` construct integer `16`. Each integer has exactly one fixed-length padded representation, so this does not double count it.

**Rotate one completed candidate**

At a leaf, `pos` equals `len(s)` and `check(x)` decides whether the valid candidate actually changes under rotation. Validity alone is not enough: `1` and `8` rotate to themselves and are not confusing.

Inside `check`, `t` is a disposable copy of `x` and `y` is the rotated result under construction. `divmod(t, 10)` returns the remaining prefix and the current rightmost digit. Looking up `d[v]` rotates that digit, and `y = y * 10 + d[v]` appends it to the right of `y`.

Reading original digits from right to left automatically reverses their positions, which is exactly what a 180-degree rotation does. For `16`, the loop reads six first and appends nine, then reads one and appends one, producing `91`. Since the DFS admitted only valid digits, `check` never encounters a `-1` entry.

Integer construction also handles leading zeros in the rotated view. Rotating `10` produces written digits `01`, but building them as an integer leaves `y` equal to one. No string cleanup is necessary.

Finally, `x != y` is true exactly for a confusing number. Converting that Boolean with `int` contributes one to the count for a confusing leaf and zero for an unchanged leaf. The padded candidate zero also reaches a leaf, but `check(0)` leaves `y` at zero and returns false, so the forbidden value outside `[1,n]` is not counted.

## Complexity detail

Let $D$ be the number of decimal digits in `n`, and let $V$ be the number of fixed-length, valid-digit candidates at most `n`, including padded zero. The package manifest records $O(D^2)$ time and $O(D)$ space, describing a combinatorial method that counts rotatable numbers and subtracts unchanged rotations without enumerating all candidates.

The exact protected Python code shown here is an unmemoized digit DFS, so its precise time bound is different. Its tree has at most five branches per position, producing at most $5^D$ leaves. Each leaf runs `check`, which processes at most $D$ digits. A direct bound is therefore $O(V D)$, or $O(D5^D)$ in the unrestricted worst case. Internal DFS nodes add a geometric total smaller than the same dominant bound.

The active recursion has depth $D$. Apart from stack frames, it carries only integers and the $D$-character representation of `n`, so auxiliary space is $O(D)$. It does not store the generated candidates or their rotated forms.

For the official limit $n \le 10^9$, $D$ is at most ten, which bounds the enumeration in practice. Nevertheless, the exact code should not be described as achieving the manifest’s $O(D^2)$ time. Reaching that bound requires additional decimal combinatorics for the valid count and the strobogrammatic, unchanged count.

## Alternatives and edge cases

- **Count valid numbers minus unchanged rotations:** Every confusing number is rotatable but not strobogrammatic. Decimal-prefix combinatorics can count all valid numbers no greater than `n` and subtract those equal to their rotation, achieving the package’s stated polynomial-in-$D$ bound with more intricate boundary logic.
- **Enumerate by arithmetic DFS without digit limit state:** Start from each nonzero valid leading digit, append valid digits, and stop a branch once its value exceeds `n`. This avoids padded zeros and is often easier to visualize, but still enumerates every valid candidate.
- **Check every integer through `n`:** Rotating each integer is straightforward but costs $O(nD)$ and wastes most work on numbers containing invalid digits.
- **Memoization warning:** Caching only `(pos, limit)` would be incorrect because different prefixes `x` can rotate differently at the leaf. A polynomial digit DP must track enough relational information or count valid and unchanged numbers separately.
- **Single-digit fixed points:** `1` and `8` are valid rotations but remain unchanged, so they contribute zero.
- **Single-digit confusing values:** `6` rotates to `9` and `9` rotates to `6`, so each contributes one when it is within the bound.
- **Invalid digits in `n`:** Digits of the bound do not need to be rotatable. They only restrict the prefix; the DFS itself skips invalid candidate digits.
- **Numbers ending in zero:** A value such as `10` rotates to integer one after the leading rotated zero is ignored, so it is confusing.
- **Padded leading zeros:** They represent shorter integers uniquely and do not create alternative representations because the DFS always uses exactly $D$ positions.
- **Candidate zero:** It is generated as all leading zeros but rejected as unchanged, preserving the inclusive domain beginning at one.
- **Upper-bound equality:** When all chosen digits match `n` and are valid, the candidate `n` itself is checked because the interval is inclusive.
- **Maximum digit length:** The recursion depth is at most ten under the stated constraint, so Python recursion limits are not a concern.
