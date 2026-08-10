## General

**Represent the surviving list as an arithmetic progression**

Materializing the list is impossible for the largest input, where `n` can be $10^9$. Fortunately, after every elimination pass, the survivors remain evenly spaced and sorted. They can be described using only:

- `a1`: the first surviving value;
- `an`: the last surviving value;
- `step`: the difference between adjacent survivors;
- `cnt`: the number of survivors.

Initially the list is `1, 2, 3, ..., n`, so `a1 = 1`, `an = n`, `step = 1`, and `cnt = n`.

After one pass, every other element survives. The distance between neighboring survivors doubles, and the number of survivors becomes its integer half. The exact identities of the new endpoints depend only on the direction and whether the old count is odd or even.

This compressed representation is the central idea: update four integers instead of deleting up to a billion list elements.

**What one left-to-right pass does**

Index the current progression’s positions from one. A left-to-right pass deletes positions `1, 3, 5, ...` and keeps positions `2, 4, 6, ...`.

The first position is always deleted, so the new first survivor is the old second value. Since adjacent values differ by `step`, the exact code always executes

```text
a1 += step
```

on a left-to-right pass.

The fate of the old last value depends on `cnt`:

- if `cnt` is even, the final position is even and survives, so `an` stays unchanged;
- if `cnt` is odd, the final position is odd and is deleted, so the new last value is one step smaller: `an -= step`.

This is why the even-direction branch contains an unconditional update of `a1` and a conditional update of `an` when `cnt % 2` is true.

**What one right-to-left pass does**

From the right, the rightmost position is deleted first, so `an` always moves one step inward:

```text
an -= step
```

Again, parity decides what happens at the opposite endpoint.

- If `cnt` is even, deletions counted from the right remove the positions that are even when numbered from the left; the original first position survives, so `a1` does not move.
- If `cnt` is odd, the alternating deletion pattern reaches the original first position, so it is removed and `a1 += step`.

The odd-direction branch of the code therefore updates `an` unconditionally and `a1` only for an odd count.

**Direction tracking**

The variable `i` counts completed passes. When `i % 2 == 0`, the pass goes left to right; when `i % 2 == 1`, it goes right to left. The code tests `if i % 2` first, so the true branch is the right-to-left case and the `else` branch is left-to-right.

After every pass, `i += 1` alternates the direction. A Boolean such as `left_to_right` could encode the same state, but the parity counter makes the alternation explicit.

**Why the count halves and the step doubles**

Every pass keeps exactly the elements in every other old position. Therefore the number of survivors is

$$
\left\lfloor \frac{\texttt{cnt}}{2} \right\rfloor.
$$

The statement always removes the first visited element, so for either parity the number kept is `cnt // 2`. The implementation performs this division with `cnt >>= 1`.

Two adjacent survivors were separated by one deleted element in the old progression. Their numeric difference is therefore twice the old difference. The implementation doubles it with `step <<= 1`.

Those bit shifts are exact for positive integers: shifting right one position is floor division by two, and shifting left one position is multiplication by two.

**Tracing `n = 9` in full state**

Initially, the progression is `[1,2,3,4,5,6,7,8,9]`:

| Pass | Direction | Before `(a1, an, step, cnt)` | Endpoint changes | After progression |
|---:|---|---|---|---|
| `0` | left to right | `(1, 9, 1, 9)` | first always moves to `2`; odd count moves last to `8` | `[2,4,6,8]` |
| `1` | right to left | `(2, 8, 2, 4)` | last always moves to `6`; even count keeps first `2` | `[2,6]` |
| `2` | left to right | `(2, 6, 4, 2)` | first moves to `6`; even count keeps last `6` | `[6]` |

After the third pass, `cnt` becomes one and both endpoints describe the same sole survivor. The method returns `a1 = 6`.

**The progression invariant**

At the beginning of every loop iteration, the conceptual remaining list contains exactly `cnt` values forming

$$
\texttt{a1},
\texttt{a1}+\texttt{step},
\texttt{a1}+2\cdot\texttt{step},
\ldots,
\texttt{an}.
$$

The initial state plainly satisfies this. During either directional pass, the endpoint rules remove exactly the endpoints that belong to deleted parity positions. Keeping alternating positions doubles the common difference and leaves floor-half as many values. Thus the updated four variables describe exactly the next conceptual list, preserving the invariant.

When `cnt == 1`, the progression contains one value. Its first and last values are equal, so `a1` is the required last remaining number. The loop condition `while cnt > 1` stops at precisely that state.

**Why parity is sufficient**

It may seem that eliminating from the right requires knowing all positions. It does not. An alternating pattern’s effect on the far endpoint is determined entirely by whether the number of positions is odd or even.

For an odd count, starting deletion at either end also deletes the opposite endpoint. For an even count, starting deletion at one end preserves the opposite endpoint. Interior survivors are automatically represented by the doubled step. No other property of the full list affects the next compressed state.

**The role of `an` in the exact source**

The final code returns only `a1`, and a more compact standard formulation can update the head without explicitly storing the tail. The exact implementation keeps `an` anyway, maintaining a symmetric and easy-to-audit description of the progression. Its updates help make endpoint parity behavior concrete, even though the final numeric answer could be derived with fewer variables.

## Complexity detail

Each pass replaces `cnt` with `cnt // 2`. Starting from $n$, the number of passes before one survivor remains is $O(\log n)$.

Every pass performs only constant-time arithmetic, parity checks, and assignments. Total time is therefore $O(\log n)$. This is exponentially faster than simulating deletions one element at a time for large `n`.

The algorithm stores five integers—`a1`, `an`, `i`, `step`, and `cnt`—regardless of input size. Auxiliary space is $O(1)$. No list, recursion stack, queue, or set of survivors is allocated.

Python integers handle all intermediate values safely. Under the stated bound, fixed-width 32-bit signed integers are also sufficient for the represented values and step, but using the language’s usual integer type is appropriate.

## Alternatives and edge cases

- **Explicit list simulation:** Build `[1, ..., n]`, keep every other value, reverse direction, and repeat. It is intuitive but requires $O(n)$ memory and substantial element-copying work, which is infeasible for $n = 10^9$.

- **Recursive recurrence:** The game has a compact mathematical recurrence relating the left-to-right result for `n` to a reflected result on `n // 2`. This yields $O(\log n)$ time and $O(\log n)$ call-stack space. The iterative endpoint model avoids recursion and is easier to trace operationally.

- **Head-only iterative model:** Track the first value, gap, remaining count, and direction. The head moves on every left pass and on a right pass only when the count is odd. This is equivalent and slightly smaller; the exact solution additionally maintains the tail.

- **`n = 1`:** The initial count is already one, so the loop never runs and `a1 = 1` is returned.

- **Even count on a left pass:** The first endpoint is deleted, but the last endpoint survives. Only `a1` moves.

- **Odd count on a left pass:** Both endpoints occupy deleted odd positions, so both move inward by one old step.

- **Even count on a right pass:** The last endpoint is deleted, but the first survives. Only `an` moves.

- **Odd count on a right pass:** Both endpoints are deleted, so both move inward.

- **Count becomes one after a pass:** The endpoint updates make `a1 == an`; subsequent doubling of `step` is harmless because no further iteration reads it.

- **Large `n`:** Runtime depends on the number of bits in `n`, not on the number of initial elements. For values near $10^9$, only about thirty passes are needed.

- **Bit-shift readability:** `cnt >>= 1` and `step <<= 1` mean integer halving and doubling. Replacing them with `cnt //= 2` and `step *= 2` would preserve the algorithm exactly.
