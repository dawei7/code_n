## General

**First decide whether the requested digit sum is possible.**  A decimal digit is at most `9`. Therefore, an integer with at most `n` digits can have digit sum at most

$$
9n.
$$

If `s > 9n`, no arrangement of at most `n` digits can supply enough digit sum, and the source returns `-1` immediately.

If `s <= 9n`, a solution always exists. The required sum can be distributed across `n` positions, with each position receiving between `0` and `9`. When `s > 0`, the greedy construction's first digit will be positive, so it represents an ordinary number without a leading zero. When `s = 0`, the only possible non-negative integer is `0`.

**Maximize the most significant digit first.**  Decimal place values are not equal. Increasing an earlier digit by one is worth more than any possible arrangement of all later lower-place digits lost to keep the same digit sum. For example, at two digits, moving one unit from the ones place to the tens place changes `ab` into `(a+1)(b-1)` and increases the number by

$$
10 - 1 = 9.
$$

For positions farther apart, the advantage is even larger. Consequently, the largest number places as much of the digit sum as possible in its leftmost digit, then does the same at the next digit, and so on.

At each position, the exact source chooses

`x = min(s, 9)`.

This gives the current most significant unfinished position the largest legal digit. It appends the digit numerically with

`ans = ans * 10 + x`

and removes that contribution with

`s -= x`.

Once the remaining sum becomes zero, every later digit is zero. The loop still appends those zeros, which is important because trailing zeros make a positive number larger without changing its digit sum.

For example, with `n = 2` and `s = 9`, the first digit receives `9` and the remaining sum becomes zero. The second iteration appends `0`, producing `90`. Returning `9` after the sum was exhausted would satisfy the sum but would not be the largest number allowed by two positions.

**Why using all `n` loop positions is compatible with “at most.”**  A shorter number can be viewed as an `n`-position digit vector padded with leading zeros. The greedy distribution maximizes that fixed-width vector lexicographically. For every positive `s`, it puts a positive digit at the first position rather than leaving a leading zero, so the resulting integer genuinely uses the most valuable available positions. For `s = 0`, all `n` conceptual digits are zero and their numeric value is simply `0`.

**Why the greedy choice never makes the remaining suffix impossible.**  Suppose there are `r` positions including the current one and the remaining sum is feasible, so `s <= 9r`.

- If `s < 9`, the current digit takes all of `s`, leaving zero for the suffix.
- If `s >= 9`, the current digit takes `9`. The new remaining sum is `s - 9 <= 9(r - 1)`, so the remaining `r - 1` positions still have enough capacity.

Thus choosing the largest current digit never paints the algorithm into a corner.

**Why no other feasible number can be larger.**  Compare the greedy digit sequence with any other feasible digit sequence from left to right. At the first position where they differ, the greedy digit is as large as the remaining sum and digit limit permit. The other sequence cannot have a larger digit there. If it has a smaller digit, it must place that unused sum somewhere later, but later place values cannot compensate for losing one unit at this earlier place. Hence the alternative number is smaller.

The same idea can be expressed as an exchange. If an alternative has an earlier digit below `9` and some later positive digit, move one unit from the later digit to the earlier digit. The digit sum stays unchanged, every digit remains legal, and the integer increases. Repeating this exchange yields exactly the greedy form: a prefix of `9` digits, possibly one digit from `1` through `8`, and then zeros.

For `n = 2` and `s = 19`, the capacity is only `18`, so the source correctly returns `-1`. For `n = 5` and `s = 0`, every chosen `x` is zero and `ans` remains zero, matching the unique valid result.

The source mutates its local parameter variable `s` as “remaining digit sum.” This does not affect any caller-visible object because integers are immutable and the parameter binding is local to the method.

## Complexity detail

The loop performs exactly `n` iterations. Each iteration uses constant-time arithmetic on the bounded result: a minimum, multiplication by ten, addition, and subtraction.

- Time complexity is `O(n)`.
- Auxiliary space complexity is `O(1)`.

The result is assembled as an integer, so no digit list or string proportional to `n` is stored. Under the given constraint `n <= 5`, the result easily fits ordinary integer ranges. In a generalized version with much larger `n`, constructing an arbitrarily long integer would make arithmetic cost depend on the number of digits; the stated bound follows the problem's small fixed digit limit and the manifest's standard unit-cost arithmetic model.

## Alternatives and edge cases

- **Enumerate all numbers with at most `n` digits:** This examines up to `10^n` candidates. The place-value exchange argument identifies the unique largest digit arrangement directly.
- **Dynamic programming over positions and remaining sum:** A DP can establish feasibility, but feasibility has the simple condition `s <= 9n`, and the lexicographically largest digits follow greedily.
- **Build a digit string:** Appending characters and converting at the end is also `O(n)` time but uses `O(n)` temporary space. The exact source accumulates the integer in constant auxiliary space.
- **Requested sum zero:** The answer is `0` for every legal `n`. Leading or trailing zero representations do not create a different integer.
- **Requested sum above capacity:** If `s > 9n`, even all `9` digits are insufficient, so `-1` is the only valid response.
- **Requested sum equal to capacity:** Every digit must be `9`, and the loop produces an `n`-digit number consisting entirely of nines.
- **Sum smaller than nine:** The result is that sum as the first digit followed by `n - 1` zeros. Those trailing zeros maximize place value without changing the sum.
- **Sum divisible by nine:** The result has a prefix of `s / 9` nines and zeros afterward; there is no partial digit.
- **At most versus exactly `n` digits:** For positive sums, using a more significant available position always increases the number. The greedy result is therefore maximal among shorter candidates as well.
- **No leading-zero problem:** When `s > 0`, `min(s, 9)` is positive at the first iteration. When `s = 0`, the valid integer is the single value zero.
- **Trailing zeros after exhaustion:** The loop must continue after `s` becomes zero. Stopping early would return a smaller integer such as `9` instead of `90`.
- **Input parameter mutation:** Only the local binding `s` is reduced. The method has no mutable input collection and no external side effect.
