## General

**Read decimal digits arithmetically**

The task removes zero digits while preserving the relative order of every nonzero digit. The exact Optimal source does this without converting the number to a string. It repeatedly extracts the least significant decimal digit with

`x = n % 10`

and removes that digit from `n` with

`n //= 10`.

This scan visits digits from right to left. Because the desired answer must keep their original left-to-right order, each retained digit must be placed in front of the nonzero digits already processed from its right.

**Meaning of `ans` and `k`**

After some least significant digits have been removed from the working `n`:

- `ans` is the integer formed by the nonzero processed digits in their original order.
- `k` is the next decimal place value immediately to the left of all digits currently stored in `ans`.

Initially, no digit has been retained. The empty constructed suffix is represented by `ans = 0`, and the first nonzero digit encountered should occupy the ones place, so `k = 1`.

When extracted digit `x` is nonzero, the update

`ans = k * x + ans`

places `x` at the decimal position immediately before the previously retained digits. Then `k *= 10` advances the next insertion place one position farther left.

When `x` is zero, the source performs neither update. This is exactly the removal operation: the zero contributes no digit position to the result, so `k` must not advance.

**Trace a number with several zero groups**

Consider `n = 1020030`. The digits are processed in this order:

| Extracted `x` | Action | `ans` afterward | `k` afterward |
| ---: | --- | ---: | ---: |
| 0 | Skip | 0 | 1 |
| 3 | Keep in ones place | 3 | 10 |
| 0 | Skip | 3 | 10 |
| 0 | Skip | 3 | 10 |
| 2 | Place before 3 | 23 | 100 |
| 0 | Skip | 23 | 100 |
| 1 | Place before 23 | 123 | 1000 |

The zeros disappear because they never change either constructed value or place. The nonzero digits one, two, and three remain in their original relative order even though they were discovered in reverse order.

If `k` were multiplied by ten for a skipped zero, the algorithm would preserve an empty decimal position and effectively keep the zero. For instance, advancing `k` after the zero between one and two would build 102 rather than 12. Updating `k` only for retained digits is therefore essential.

**Why prepending with place values preserves order**

Suppose the invariant holds after processing a suffix of the original decimal representation. Let that suffix contain `r` nonzero digits. Then `ans` has at most `r` decimal positions corresponding to those retained digits, and `k = 10^r`.

If the next digit to the left is zero, removing it leaves the retained sequence unchanged, so keeping both `ans` and `k` preserves the invariant.

If the next digit is nonzero `x`, the correct filtered sequence is `x` followed by the `r` retained digits from the processed suffix. Multiplying `x` by `10^r` places it immediately to their left, and adding `ans` supplies the suffix:

$$
\text{new answer}=x\cdot10^r+\text{old answer}.
$$

Then the result contains `r + 1` retained digits, so the next place value must be `10^{r+1}`, obtained by multiplying `k` by ten. The invariant continues to hold.

Once `n` becomes zero, every original digit has been processed. The invariant then says `ans` is exactly the original nonzero digits in their original order, which is the required result.

**Why the result cannot be empty**

The input integer is positive. Its ordinary decimal representation therefore contains at least one nonzero digit. Even if every other digit is zero, the loop eventually extracts that nonzero digit and adds it to `ans`. The method never needs to define what an empty digit sequence should parse to.

For `n = 1`, the sole digit is retained in the ones place and the loop returns one. For `n = 1000`, all trailing zeros are skipped, then one is retained, also returning one.

**Why no string parsing is needed**

Modulo ten and integer division by ten are the arithmetic equivalents of reading and removing the final decimal character. The place-value construction is the arithmetic equivalent of concatenating retained digits. It avoids a character list and explicit integer parsing while following the same filtering rule.

The exact source also changes only its local parameter variable `n`. Repeated division does not mutate any external object; integers are immutable values in Python.

## Complexity detail

Let `D` be the number of decimal digits in the input. Every loop iteration removes exactly one digit with `n //= 10`, so there are `D` iterations. Under the standard fixed-width arithmetic model appropriate to `n <= 10^15`, modulo, division, multiplication, and addition are constant-time operations, giving $O(D)$ time.

The source uses a constant number of integer variables. In a word-RAM description its auxiliary working space is $O(1)$. The manifest states $O(D)$ space, which is also a safe bound when counting the digit storage of the growing arbitrary-precision result and place value: `ans` and `k` can each contain $O(D)$ decimal digits. No separate array, string, or recursion stack is allocated.

For the stated constraint, `D <= 16`, so all quantities remain small. The symbolic $O(D)$ bounds describe how the digit scan scales if the decimal-length limit is viewed as variable.

## Alternatives and edge cases

- **Convert to a string and filter characters:** `int("".join(c for c in str(n) if c != "0"))` is direct and also takes $O(D)$ time and $O(D)$ string space. The arithmetic method avoids conversion while preserving the same order.
- **Build the result while scanning left to right:** A string naturally supports this. Arithmetically, one could first reverse digits or use a highest power of ten; the exact right-to-left scan instead prepends retained digits with `k`.
- **Multiply `ans` by ten when a digit is retained:** That pattern appends digits and is appropriate when reading left to right. Used during this right-to-left scan, it would reverse the retained digit order.
- **Advance `k` for zero digits:** This would keep zero positions rather than remove them. `k` counts retained digits only.
- **Trailing zeros:** They are encountered first and skipped while `ans = 0` and `k = 1`, so they leave no trace.
- **Zeros between nonzero digits:** They do not advance `k`, allowing the nonzero digit on their left to be placed directly beside the retained suffix.
- **No zeros:** Every digit is retained, and the invariant reconstructs the original number exactly.
- **Only one nonzero digit:** All zeros are skipped and that digit is placed in the ones position, producing a positive one-digit result.
- **Input equal to zero:** The contract excludes it. If allowed, the loop would return zero, but no extra semantics are needed for the stated positive input.
- **Leading zeros:** A positive integer's decimal representation has none. The algorithm operates on the canonical numeric representation automatically.
- **Maximum input `10^15`:** The one followed by fifteen zeros is processed safely and reduces to one.
- **Relative order:** Prepending each newly discovered left-side nonzero digit is the crucial step. Sorting or merely summing digits would violate the required sequence.
