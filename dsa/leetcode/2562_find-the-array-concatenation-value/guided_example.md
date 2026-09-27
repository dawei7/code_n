# Guided Example: Find the Array Concatenation Value

## 1. The order the operations impose

The concatenation value starts at $0$. While at least two elements remain, the operation takes the **first** and the **last** element of the current array, forms a single number by writing their numerals back to back, adds that number to the running total, and deletes both elements. When exactly one element is left, that element is added on its own and the array is emptied.

The pairing order is therefore fixed: outermost pair first, then the next pair inward, and so on. Nothing is chosen and nothing is searched — the only question is how to compute each concatenation and where the process stops.

## 2. What concatenation does arithmetically

Writing two numerals back to back is a shift and an addition. If the right-hand operand has $d$ decimal digits, then appending it to the left-hand operand $a$ produces

$$
a \cdot 10^{d} + b
$$

For example, appending `2` to `52` gives $52 \cdot 10 + 2 = 522$, and appending `12` to `5` gives $5 \cdot 10^{2} + 12 = 512$.

The exponent is decided by the **right** operand alone — the number of digits of the element taken from the end of the array. The left operand's own width is irrelevant. This asymmetry is the one arithmetic fact the whole problem rests on, and it is why the pair order cannot be reversed: the pair `(10, 2)` yields `102` while `(2, 10)` would yield `210`.

## 3. Worked instance: the odd-length official sample

Take `nums = [5, 14, 13, 8, 12]`, whose required concatenation value is `673`. Five elements mean two full pairs plus one leftover:

| Operation | Window before the operation | First element | Last element | Digits of the last element | Concatenation | Running total |
|---|---|---|---|---|---|---|
| 1 | `[5, 14, 13, 8, 12]` | 5 | 12 | 2 | $5 \cdot 10^{2} + 12 = 512$ | 512 |
| 2 | `[14, 13, 8]` | 14 | 8 | 1 | $14 \cdot 10^{1} + 8 = 148$ | 660 |
| 3 | `[13]` | 13 | 13 | the element is the only one left | added unchanged | 673 |

The third operation is not a concatenation at all: a single remaining element is added as its own value, so `13` enters the total raw. Summing gives $512 + 148 + 13 = 673$, matching the required output.

## 4. Tracking the window with two indices

Deleting the outer elements is a description of the state, not an instruction to move memory. After $k$ operations the surviving elements are exactly the original indices

$$
k,\; k+1,\; \dots,\; n-1-k
$$

because each operation consumes one element from each end. Two indices — a left cursor $i$ starting at $0$ and a right cursor $j$ starting at $n-1$ — reproduce that window exactly, advancing $i$ by one and retreating $j$ by one per operation.

> **Invariant.** Before each operation, the elements still to be processed are precisely `nums[i]` through `nums[j]`, inclusive, and every element outside that window has already contributed its share to the running total.

The invariant starts true at $i = 0$, $j = n-1$, where the window is the whole array. Each operation pairs `nums[i]` with `nums[j]` and then moves both cursors inward, so the next window is again the untouched remainder. The process ends when $i$ reaches or passes $j$: if $i > j$ the array is empty, and if $i = j$ exactly one element sits in the window, which is the case handled by adding `nums[i]` unchanged. Distinguishing those two stopping states is what makes odd and even lengths agree without a separate branch for parity.

## 5. How the shift depends on the right operand's width

The width of the appended value decides the size of the jump, so values that straddle powers of ten behave very differently even when they look similar:

| Right operand | Decimal digits $d$ | Multiplier $10^{d}$ | Left operand `1` becomes | Left operand `9` becomes |
|---|---|---|---|---|
| `4` | 1 | 10 | 14 | 94 |
| `12` | 2 | 100 | 112 | 912 |
| `999` | 3 | 1000 | 1999 | 9999 |
| `10000` | 5 | 100000 | 100001 | 900001 |

A one-digit increase in the appended value multiplies the left operand's contribution by ten, which is why a careless fixed shift — say always multiplying by $10$ — collapses as soon as any element has more than one digit.

## 6. Boundary behaviour

| Input | Length | Pairing performed | Arithmetic | Result |
|---|---|---|---|---|
| `[1]` | 1 | no pair exists; the lone element | $1$ | 1 |
| `[7]` | 1 | no pair exists; the lone element | $7$ | 7 |
| `[10, 2]` | 2 | (10, 2) | $10 \cdot 10 + 2$ | 102 |
| `[7, 7]` | 2 | (7, 7) | $7 \cdot 10 + 7$ | 77 |
| `[1, 10, 100, 1000]` | 4 | (1, 1000) then (10, 100) | $11000 + 10100$ | 21100 |
| `[9, 99, 999]` | 3 | (9, 999), then the middle 99 | $9999 + 99$ | 10098 |
| `[10000, 10000]` | 2 | (10000, 10000) | $10000 \cdot 100000 + 10000$ | 1000010000 |

Three of these rows matter most. `[10, 2]` shows that order is not interchangeable, since the reversed reading would be `210`. `[9, 99, 999]` shows the middle element of an odd-length array being added raw after a wide pair — the middle is never shifted. `[10000, 10000]` shows the largest arithmetic the constraints permit, with a shift of five digits on each side.

## 7. Other strategies and their trade-offs

| Strategy | Work per operation | Total cost | Assessment |
|---|---|---|---|
| Physically delete the first and last element | moving the remaining elements costs $\Theta(\text{window size})$ | $O(n^2)$ | Reproduces the statement literally, but the shifting work dominates for no benefit |
| Two cursors moving inward | one comparison and two cursor updates, $O(1)$ | $O(n)$ | The method derived here; the array is read-only |
| Explicit double-ended queue | $O(1)$ amortised per removal | $O(n)$ | Equivalent cost; more state than two integer cursors need |
| Rebuilding the array each round | allocating a shorter copy costs $O(\text{window size})$ | $O(n^2)$ | Correct but allocates repeatedly |

All four produce the same total; the difference is entirely in how the shrinking window is represented. Since the operations never depend on elements in any order other than outside-in, the read-only cursor form is the natural one.

## 8. Traps this instance exposes

- **Reversing the pair.** The pair is always (first, last) in that order. `[12, 3]` gives $12 \cdot 10 + 3 = 123$, and swapping the operands would give a different number.
- **Shifting by the wrong operand's width.** The exponent counts the digits of the element taken from the **end** of the current window; using the left operand's width produces wrong concatenations whenever the two widths differ.
- **Shifting the middle element of an odd-length array.** After the final pair, exactly one element remains and it enters the total unchanged. In `[9, 99, 999]` the leftover `99` contributes $99$, not $990$ or $9900$.
- **Stopping too late or too early.** The loop belongs to the condition $i < j$. Letting it run at $i = j$ would process the middle element twice; stopping at $i \le j$ would also process a single element as though it had a partner.
- **Assuming a fixed number of digits.** Values up to $10^4$ span one to five digits, and a hard-coded multiplier breaks as soon as the appended value is not a single digit.
- **Underestimating the total.** With up to $500$ pairs whose concatenations can each approach $10^9$, the total can exceed $5 \times 10^{11}$, so a narrow 32-bit accumulator is not enough.

## 9. Time and auxiliary space

Let $n$ be the length of `nums` and $d$ the number of decimal digits of a value, with $d \le 5$ under the constraints.

- **Number of operations.** Each operation consumes two elements, so exactly $\lfloor n/2 \rfloor$ concatenations occur, plus at most one direct addition when $n$ is odd.
- **Work per operation.** Reading the two endpoint values, measuring the digit count of the right operand, forming the shifted number, and advancing both cursors are all $O(d)$, and $d$ is bounded by a constant.
- **Total time complexity.** $O(n \cdot d) = O(n)$, a single outside-in sweep with no repeated scanning.
- **Auxiliary space complexity.** $O(1)$. Only the two cursors, the running total, and the digit width of one element are stored; the array itself is never copied or modified.
