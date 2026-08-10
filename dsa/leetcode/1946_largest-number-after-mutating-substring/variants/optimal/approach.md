## General

**Compare equal-length numbers from left to right**

Every mutation replaces one digit with one digit, so the result always has the same length as `num`. Among equal-length digit strings, numeric order is lexicographic order: the first position where two strings differ determines which number is larger.

Therefore the best mutation should start at the earliest position where the mapped digit is strictly larger than the original. Any improvements later cannot compensate for voluntarily making an earlier digit smaller, and equal earlier digits do not affect the comparison.

The solution converts `num` to a mutable character list `s` and scans left to right. For current digit character `c`, it computes mapped character `d = str(change[int(c)])`.

**Delay the substring until a strict improvement**

While `changed` is false:

- if `d < c`, mutating here would worsen the first differing digit, so the algorithm skips it;
- if `d == c`, including or excluding this position produces the same visible result, so it also skips it;
- if `d > c`, this is the earliest profitable start. The code sets `changed = True` and stores `d`.

Starting later than this first strict improvement would preserve the smaller original digit at this decisive position and could never yield a larger final number.

**Continue through neutral or improving positions**

Once mutation has started, all changed positions must form one contiguous substring. A mapped digit larger than the original should be written. A mapped digit equal to the original can remain physically unchanged, but the chosen conceptual substring may pass through it; the output is identical either way.

The exact code writes only strict improvements. When `d == c` after starting, neither the break nor assignment executes, `changed` remains true, and the scan continues. This correctly allows a later improvement within the same substring.

At the first position where `d < c` after mutation began, the code breaks. Including that position would make the result worse at the earliest difference after an already fixed prefix. Ending the substring immediately before it preserves all earlier gains. Because only one substring may be mutated, no position after this break may be changed.

**Why greedy stopping is optimal**

Fix the earliest profitable position selected by the algorithm. All candidate results that start there share the same improved prefix until they make different decisions later.

At a later position with `d>c`, including it increases the result while keeping the prior prefix identical. At `d=c`, including it has no effect and preserves the option to improve later positions. At `d<c`, including it makes the number smaller at that position; ending before it is strictly better, and the single-substring rule prevents restarting afterward. These local decisions are forced by lexicographic order.

If no position has `d>c`, every possible mutation either leaves leading digits equal or introduces a decrease at its first effective change. Choosing no mutation is then optimal, and the method returns the original string.

For `num = "021"` with mappings $0\mapsto9$, $2\mapsto3$, and $1\mapsto4$, mutation starts at the first digit and continues through all three strict improvements, producing `"934"`. For a mapping that improves one digit, leaves the next equal, then improves another, the unchanged middle character does not split the conceptual interval.

## Complexity detail

Let $N$ be the number of digits.

Creating `list(num)` takes $O(N)$ time. The loop examines each position at most once and may stop early. `"".join(s)` scans all $N$ characters to build the return string. Total time is $O(N)$.

The mutable list and returned string each contain $N$ characters, so peak space is $O(N)$. The algorithm otherwise uses constant scalar state. A new string must be materialized for the result because Python strings are immutable.

## Alternatives and edge cases

- **Try every substring:** Mutate each of $O(N^2)$ intervals and compare results, leading to at least quadratic and often cubic work with string construction.
- **Dynamic programming states:** States for “not started,” “inside,” and “finished” can model the rule, but lexicographic greed makes the transitions deterministic.
- **Start on an equal mapping:** It is harmless but unnecessary. Delaying the recorded start until the first strict improvement leaves the output and future options unchanged.
- **Equal mapping after start:** It must not end the interval; the code continues so later improvements remain reachable.
- **First harmful mapping after start:** The method stops before it and never mutates later digits because a second substring is forbidden.
- **No improving digit:** `changed` remains false and the original number is returned.
- **Single digit:** It is replaced only if its mapped digit is larger.
- **Leading zero:** It is treated like any digit. Mapping it upward can create the most important possible improvement.
- **Mapped digit smaller before start:** It is skipped because the chosen substring can start later.
- **Same-length comparison:** The greedy proof relies on every mapping producing exactly one digit, which the length-ten change array guarantees.
- **Input preservation:** `num` is immutable; the result is built through a separate list.
