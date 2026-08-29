## General

**Perform decimal addition from right to left**

The digits in `num` are stored most significant first, but ordinary addition begins with the least significant column. The algorithm therefore starts at index `len(num) - 1` and walks leftward.

Instead of separating `k` into decimal digits in advance and maintaining another carry variable, the implementation reuses `k` itself as the unprocessed addend plus carry. At every column, it adds the current digit from `num` to `k`, extracts the resulting ones digit, and carries the remaining quotient into the next column.

This compact technique is still the same schoolbook addition learned on paper; it simply combines the addend's higher digits and the carry into one integer.

**Meaning of `k` during the loop**

Before an iteration processes position `i`, `k` represents everything that must still be added to the unprocessed prefix of `num`. Initially, that is the complete input addend.

If `i >= 0`, the code executes

`k += num[i]`.

This combines the array digit in the current decimal column with the current least significant digit of the remaining addend and any carry already embedded in `k`.

If `i < 0`, no array digit remains, so the conditional expression adds zero. The loop can then continue decomposing a leftover `k` into leading result digits.

**Use `divmod` to split result digit and carry**

The statement

`k, x = divmod(k, 10)`

simultaneously computes quotient and remainder:

- `x = k % 10` is the digit that belongs in the current result column;
- the new `k = k // 10` is everything carried into columns to the left.

For example, if the current combined amount is twenty-five, the current digit is five and the remaining carry/addend is two. This is exactly the decimal relation

`25 = 10 * 2 + 5`.

All inputs are nonnegative, so the remainder is always a legal digit from zero through nine.

**Why the entire addend can be placed into the rightmost column**

Suppose the current remaining addend is `181` and the current array digit is four. Adding them gives `185`. The ones digit five belongs in the current column, while `18` remains for the columns to the left. In the next column, adding `18` to the next array digit automatically combines the original tens-and-hundreds portions with any carry from the previous column.

Repeated quotient-by-ten operations expose `k`'s digits in the same order that schoolbook addition needs them. No information is lost: the quotient retains all higher decimal places, and the remainder finalizes only the current place.

**Build digits backward, then reverse once**

Each computed digit `x` is appended to `ans` immediately. Since the algorithm processes the ones column first, `ans` is in least-significant-to-most-significant order.

The final expression `ans[::-1]` returns a reversed copy in the required left-to-right array form. Reversing once is simpler and more efficient than inserting each new digit at the front of a Python list, which would repeatedly shift existing elements.

**Loop until both sources are exhausted**

The condition `while i >= 0 or k` continues as long as either an array digit remains or the carry/addend is nonzero.

- If array digits remain after `k` becomes zero, they still have to be copied through the same arithmetic.
- If the array is exhausted while `k` remains positive, its decimal digits must become new leading digits.
- The loop stops only when neither source can contribute another result column.

Index `i` decreases after every iteration, including iterations after it becomes negative. This causes no invalid access because the conditional reads `num[i]` only when `i >= 0`.

**Trace `[2, 7, 4] + 181`**

Start with `i = 2`, `k = 181`, and an empty answer:

- Add digit four: `k = 185`. `divmod(185, 10)` gives carry/addend eighteen and digit five. Now `ans = [5]`.
- Move to digit seven: `k = 18 + 7 = 25`. The next quotient is two and digit is five. Now `ans = [5, 5]`.
- Move to digit two: `k = 2 + 2 = 4`. The next quotient is zero and digit is four. Now `ans = [5, 5, 4]`.

The index is exhausted and `k` is zero, so the loop ends. Reversal returns `[4, 5, 5]`, representing 455.

**Trace a new leading carry**

For `[9, 9, 9] + 1`:

- Each nine combines with carry one to produce digit zero and carry one.
- After all three array digits are consumed, `i < 0` but `k = 1`, so the loop runs once more.
- With no array digit to add, `divmod(1, 10)` emits leading digit one and clears `k`.

The backward list `[0, 0, 0, 1]` reverses to `[1, 0, 0, 0]`. The `or k` part of the loop condition is what preserves this extra digit.

**The column invariant**

After each iteration, the digits currently in `ans`, when read in their stored order, are the finalized result digits for all decimal columns processed so far from right to left. They will never change again. The updated `k` contains exactly the remaining higher-place addition that must be combined with the unprocessed prefix of `num`.

The invariant begins before any column is processed. Adding `num[i]` and applying `divmod` finalizes the current remainder and transfers exactly the quotient to the next column, so it is preserved. At termination, no array prefix and no carry remain. Therefore, every result digit has been finalized, and reversing `ans` gives exactly the array form of the sum.

**The input array is not mutated**

The method reads `num[i]` but stores result digits in a separate list. This preserves the caller's digit array. By contrast, some schoolbook implementations add directly into `num` and repair carries in place; both are possible, but the protected solution deliberately produces a fresh result.

## Complexity detail

Let `N` be the number of digits in `num` and `D` the number of decimal digits in the original `k`. Let `L = \max(N, D)`, allowing one additional output digit for a final carry.

Each iteration consumes one array position or one decimal place of the remaining `k`, and there are `O(L)` iterations. Reversing the result also takes `O(L)` time, so total time is `O(L)`.

The output list contains `O(L)` digits, and `ans[::-1]` creates the returned reversed list of the same order of size. Thus total space is `O(L)`. Aside from the output construction, only `i`, `k`, and `x` are stored, giving `O(1)` auxiliary scalar space.

## Alternatives and edge cases

- **Convert the digit array to an integer:** Reconstruct the number, add `k`, and split the result. It is concise in Python but ignores the intended digit-by-digit method and depends on arbitrary-precision integer conversion.
- **Split `k` into a digit array first:** Then add two arrays from right to left with an explicit carry. This is conventional but needs extra preprocessing and indices.
- **Mutate `num` in place:** Add `k` to the final digit and propagate carries leftward. It can reuse input storage but changes the caller's array and still needs space if a new leading carry appears.
- **Insert result digits at index zero:** It avoids a final reversal but every front insertion shifts the existing list, potentially making construction quadratic.
- **Array longer than `k`:** Once `k` becomes zero, remaining digits pass through `divmod(num[i], 10)` unchanged.
- **`k` longer than the array:** After `i` becomes negative, the loop continues emitting `k`'s remaining decimal digits.
- **Carry beyond the most significant digit:** The `or k` condition creates the necessary new leading digit.
- **Zeros inside the number:** A zero is processed like any other digit, and internal or result zeros are preserved.
- **Input representing zero:** The same loop adds `k` to its single zero digit and emits the proper result.
- **No leading zeros:** The input guarantee and normal carry termination ensure the returned representation has no artificial leading zero.
- **Very long `num`:** The method never constructs the represented integer, so it scales linearly to ten thousand digits.
