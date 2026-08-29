## General

**Replace the round-by-round story with a question about one bulb.**

Simulating the switches is tempting: round `1` touches every bulb, round `2` touches bulbs `2, 4, 6, ...`, and so on. That view follows the statement literally, but it hides the useful pattern and would perform far too much work when $n$ can be as large as $10^9$. Instead, fix one bulb position $k$ and ask exactly which rounds toggle that bulb.

Round $i$ toggles every bulb whose position is a multiple of $i$. Therefore, it toggles bulb $k$ precisely when $i$ divides $k$. For example, bulb `12` is touched in rounds `1`, `2`, `3`, `4`, `6`, and `12`, because those are exactly the positive divisors of `12`. This gives a direct translation:

- the number of times bulb $k$ is toggled equals the number of positive divisors of $k$;
- a bulb that starts off ends on after an odd number of toggles;
- a bulb that starts off ends off after an even number of toggles.

The final state of bulb $k$ therefore depends only on whether $k$ has an odd or even number of positive divisors. We no longer need to model the individual rounds.

**Why almost every divisor has a partner.**

Whenever $d$ divides $k$, the quotient $k/d$ is also a divisor, and the two values multiply to $k$. Thus divisors naturally form pairs

$$
(d, k/d).
$$

For `12`, the pairs are `(1, 12)`, `(2, 6)`, and `(3, 4)`. Every pair contains two different divisors, so there are six divisors in total—an even count. Pairing is exactly what matters because each two-member pair contributes two toggles, and two toggles cancel: off becomes on and then off again, or on becomes off and then on again.

There is only one way for such a pair not to contain two different values. Its two members are equal when

$$
d = k/d,
$$

which is equivalent to

$$
d^2 = k.
$$

That happens precisely when $k$ is a perfect square. For example, the divisor pairs of `16` are `(1, 16)`, `(2, 8)`, and `(4, 4)`. The first two pairs contribute four distinct divisors, while the last pair contributes only the single divisor `4`. Consequently, `16` has five positive divisors and is toggled five times. It finishes on.

If $k$ is not a perfect square, no divisor can be paired with itself. Every divisor belongs to a distinct two-member pair, so the divisor count is even and bulb $k$ finishes off. If $k$ is a perfect square, exactly one divisor—$sqrt{k}$—is self-paired. All other divisors still cancel in pairs, leaving one unpaired toggle, so bulb $k$ finishes on. This proves the complete characterization:

> After all rounds, the bulbs that remain on are exactly the bulbs at perfect-square positions.

**Count squares instead of examining bulbs.**

The remaining problem is simply to count perfect squares in the inclusive interval from `1` through `n`. They are

$$
1^2, 2^2, 3^2, \ldots, m^2,
$$

where $m$ is the largest nonnegative integer satisfying $m^2 \le n$. By definition,

$$
m = \lfloor \sqrt{n} \rfloor.
$$

There is one square for every integer base from `1` through $m$, so there are exactly $m$ surviving bulbs. This is why the method returns the integer part of `sqrt(n)` directly. It is not estimating how many bulbs survive; it is counting the square positions through a one-to-one correspondence between bases $j$ and positions $j^2$.

For `n = 10`, the integer square root is `3`. The square positions are `1`, `4`, and `9`, so three bulbs remain on. Bulb `1` is toggled in round `1`; bulb `4` is toggled in rounds `1`, `2`, and `4`; bulb `9` is toggled in rounds `1`, `3`, and `9`. Each has an odd toggle count. A nonsquare such as bulb `10` is toggled in rounds `1`, `2`, `5`, and `10`, an even count, and ends off.

The boundary between consecutive answers is also useful for understanding the floor. If `n = 24`, then $\lfloor\sqrt{24}\rfloor = 4$, accounting for `1`, `4`, `9`, and `16`. At `n = 25`, the answer increases to `5` because `25 = 5^2` becomes available. It remains `5` for every `n` from `25` through `35`, then increases at `36 = 6^2`. The answer changes only when the range gains another perfect square.

**Why the single return statement is sufficient.**

The exact optimal source computes `sqrt(n)` and converts the result to an integer. For the nonnegative inputs allowed by the contract, integer conversion discards the fractional part, which has the same effect as taking the mathematical floor. No array of bulb states, set of divisors, loop over rounds, or perfect-square test for every position is needed. All of that repeated behavior has already been summarized by the divisor-pair argument.

The `n = 0` case fits the same reasoning without a special branch. There are no bulb positions in the range, `sqrt(0)` is `0`, and the returned count is `0`. For `n = 1`, the only position is $1 = 1^2$, so the method returns `1`.

## Complexity detail

Let $n$ be both the number of bulbs and the number of rounds described by the problem. The implementation performs one square-root operation and one conversion to an integer. Under the problem's bounded integer domain, $0 \le n \le 10^9$, these are fixed-size machine-number operations, so the time complexity is $O(1)$. The running time does not grow by iterating through the $n$ bulbs or the $n$ rounds; there is no such iteration in the source.

The method uses only the input, the temporary numeric result of `sqrt(n)`, and the returned integer. It allocates no collection and performs no recursion, so its auxiliary space complexity is $O(1)$.

The constant-time statement depends on the contract's fixed-size numeric range. For arbitrary-precision integers with an unbounded number of digits, computing an exact integer square root would have a cost depending on the input's bit length. That distinction does not change this problem's declared complexity because the input is at most $10^9$ and the source uses the language's ordinary square-root operation.

The mathematical reduction is what produces the improvement. A literal simulation can touch roughly

$$
n + \lfloor n/2 \rfloor + \lfloor n/3 \rfloor + \cdots + 1
$$

bulbs across all rounds, which is $O(n \log n)$ work. Even an approach that independently tests each of the $n$ positions for being a square still takes $O(n)$ time. Counting the possible square bases through $\lfloor\sqrt{n}\rfloor$ removes all per-position work.

## Alternatives and edge cases

- **Direct round simulation:** Store `n` Boolean bulb states and toggle every `i`-th entry during round `i`. This mirrors the statement and can help discover the pattern on tiny examples, but it requires $O(n \log n)$ total toggles and $O(n)$ storage. It is infeasible near $n = 10^9$ and ignores the divisor structure.

- **Count divisors for every bulb:** For each position $k$, enumerate divisors up to $\sqrt{k}$ and decide whether the divisor count is odd. This eventually identifies the same perfect squares, but repeats work for every bulb and is much slower than using the proven square characterization directly.

- **Check every candidate square:** Increment `j` while $j^2 \le n$ and count the iterations. This uses $O(1)$ space and is easy to reason about, but it takes $O(\sqrt{n})$ time. The count reached by that loop is exactly $\lfloor\sqrt{n}\rfloor$, which the optimal source obtains in one fixed-size numeric operation.

- **Binary search for the integer square root:** Search for the greatest integer $j$ with $j^2 \le n$. This avoids reliance on floating-point flooring and is useful for very large arbitrary-precision inputs, but it takes $O(\log n)$ comparisons and is unnecessary under the stated limit. If implemented, multiplication should be arranged carefully in languages where `mid * mid` could overflow; this problem's bound is small enough for common wider integer types.

- **`n = 0`:** There are no bulbs and no rounds. Zero perfect-square positions occur in the empty range from `1` through `0`, and `int(sqrt(0))` correctly returns `0`.

- **Perfect-square upper boundary:** When $n = q^2$, bulb $q^2$ must be included, so the answer is exactly $q$. The use of a floor after taking the square root preserves this inclusive boundary.

- **Just below the next square:** When $q^2 \le n < (q+1)^2$, the answer remains $q$. Nonsquare positions added after $q^2$ all have paired divisors and therefore finish off.

- **Bulb numbering starts at one:** Position `0` is not a bulb and is not counted as an additional square. Although $0$ is mathematically a perfect square, the relevant positions are `1` through `n`; $\lfloor\sqrt{n}\rfloor$ counts the positive square bases `1` through that value.

- **Floating-point interpretation:** Converting `sqrt(n)` to an integer is correct for the stated range because these values are small enough for the language's standard floating-point square root to distinguish adjacent relevant integers reliably. For a substantially larger, different contract, an exact integer-square-root routine could avoid rounding near square boundaries.
