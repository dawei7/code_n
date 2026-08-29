## General

**Read the linked lists as columns of a written addition problem**

Each node stores one decimal digit, but the digits appear in reverse order. The head is the ones digit, the next node is the tens digit, then the hundreds digit, and so on. If the nodes are `[2, 4, 3]`, the represented number is

$$
2 \cdot 10^0 + 4 \cdot 10^1 + 3 \cdot 10^2 = 342.
$$

This reversed representation is helpful because ordinary addition also begins at the least-significant column. The algorithm can read both lists from their heads, produce one result digit, and move forward. It never needs to walk backward or know either list's length in advance.

For one decimal column, let `a` be the digit from `l1`, `b` the digit from `l2`, and `carry` the amount brought from the preceding, less-significant column. The full column sum is

$$
s = a + b + \texttt{carry}.
$$

Only the ones digit of `s` belongs in the current result node. The tens digit becomes the carry for the next column. Python's `divmod` calculates both parts at once:

```python
carry, val = divmod(s, 10)
```

This is equivalent to

```python
carry = s // 10
val = s % 10
```

so `val` is the digit to append and `carry` is what must be added to the next column.

**Why the carry is always either zero or one**

Each input digit lies between `0` and `9`. Once the process starts, the incoming carry is at most `1`. Therefore the largest possible column sum is

$$
9 + 9 + 1 = 19.
$$

Dividing any possible column sum by `10` gives a quotient of only `0` or `1`. This establishes the same fact for the next iteration, so the carry can never become `2` or larger.

That small bound also explains why the result needs at most one more node than the longer input list: after all input digits have been consumed, there can be only one remaining digit, namely `1`.

**Use a dummy node to make every appended digit look the same**

The output list does not exist before its first digit is computed. Without a dummy node, the code would need one branch for creating the head and another branch for every later node.

Instead, the solution starts with

```python
dummy = ListNode()
carry, curr = 0, dummy
```

`dummy` is a temporary node that is not part of the numerical answer. `curr` always points to the last node in the constructed chain. At first, the last constructed node is the dummy itself. Every result digit can then be attached uniformly with

```python
curr.next = ListNode(val)
curr = curr.next
```

The first real digit becomes `dummy.next`. Later digits are linked after it. Returning `dummy.next` skips the temporary node and gives the caller the true head.

**Why the loop has three continuation conditions**

The loop is

```python
while l1 or l2 or carry:
```

Each condition covers a different reason that another output digit may be necessary:

- `l1` means the first number still has an unprocessed digit;
- `l2` means the second number still has an unprocessed digit;
- `carry` means both lists may be finished, but a final leading `1` still has to be written.

The lists are allowed to have different lengths. When one pointer has reached `None`, that number contributes `0` to all remaining columns. The expression

```python
l1.val if l1 else 0
```

implements exactly that rule for the first list, and the corresponding expression does the same for `l2`. This zero is not appended to an input list and does not modify it; it is only the mathematical value used for the missing column.

The full line

```python
s = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
```

therefore works for all three states: both digits present, only one present, or neither present with a final carry.

**Advance each input only when its node exists**

After appending the new result digit, the algorithm moves to the next column:

```python
l1 = l1.next if l1 else None
l2 = l2.next if l2 else None
```

The conditional expressions prevent access to `.next` on `None`. Once a list ends, its pointer stays `None` while the other list continues. The input nodes themselves are never relinked or overwritten; only the local pointers move. The returned list is built entirely from new `ListNode` objects.

**A walkthrough that creates a final carry**

Consider `l1 = [9, 9, 9]` and `l2 = [1]`, representing $999 + 1$.

| Column | Digit from `l1` | Digit from `l2` | Incoming `carry` | `s` | Output `val` | Next `carry` |
|---:|---:|---:|---:|---:|---:|---:|
| Ones | `9` | `1` | `0` | `10` | `0` | `1` |
| Tens | `9` | missing $\to 0$ | `1` | `10` | `0` | `1` |
| Hundreds | `9` | missing $\to 0$ | `1` | `10` | `0` | `1` |
| Thousands | missing $\to 0$ | missing $\to 0$ | `1` | `1` | `1` | `0` |

The constructed list is `[0, 0, 0, 1]`, which represents $1000$. The fourth iteration happens only because `carry` is still `1` after both input pointers become `None`.

**Why every generated digit belongs in the answer**

After `k` iterations, the output list contains exactly the lowest `k` digits of the mathematical sum, in reverse order. The variable `carry` contains everything from those processed columns that still belongs in the next column.

This is true before the first iteration: no columns have been processed, the output is empty, and `carry = 0`. During an iteration, the algorithm adds the two digits for the current power of ten and the carry from the preceding column. `s % 10` is exactly the digit for this column, while `s // 10` is exactly the amount transferred to the next one. Appending `val` and updating `carry` therefore extends the statement by one column.

When the loop stops, neither input has a remaining digit and `carry` is zero. Nothing remains to be written. Consequently, the nodes after `dummy` contain every digit of the sum and no extra digit. This also explains why returning `dummy.next` is sufficient.

## Complexity detail

Let $n$ be the number of nodes in `l1`, let $m$ be the number in `l2`, and let $L = \max(n,m)$.

- **Time complexity: $O(L)$.** Each iteration consumes one node from every input list that has a node remaining. The loop runs $L$ times for the input columns and at most once more for a final carry. Since $L + 1$ and $L$ have the same asymptotic growth, the time bound is $O(\max(n,m))$. Every iteration performs only constant-time arithmetic, pointer checks, and one node allocation.
- **Space complexity: $O(L)$ including the returned list.** The answer has either $L$ or $L+1$ nodes, so the output itself occupies $O(\max(n,m))$ space. Apart from that required output, the algorithm uses only the dummy node, two moving input pointers, `curr`, `carry`, `s`, and `val`; its auxiliary working space is $O(1)$. The manifest counts the constructed answer, which is why its declared space bound is $O(\max(n,m))$ even though some analyses describe the extra working space as constant.

The algorithm is iterative, so it does not consume recursion-stack space. It also never copies either input list into an array or converts the complete numbers into large integers.

## Alternatives and edge cases

- **Convert both lists to integers:** One could reconstruct each entire number, add them, and convert the sum back into nodes. That hides the digit-by-digit reasoning, may rely on arbitrary-precision integers unavailable in another language, and uses extra storage for whole-number representations. Direct column addition works under the linked-list contract alone.
- **Recursive column addition:** Recursion can process one pair of nodes per call, but it adds $O(L)$ call-stack space and still needs careful handling for unequal lengths and the last carry. The iterative loop is more direct and keeps auxiliary space constant.
- **No dummy node:** The first result node could be created separately and later nodes appended normally. This saves one temporary node but introduces special-case control flow for head initialization. The dummy node makes every output digit follow one safe attachment path.
- **Digits stored in forward order:** If the head were the most-significant digit, the next output digit would depend on carries discovered farther down the lists. Stacks, recursion, or list reversal would then be useful. This problem's reversed order is precisely what permits a single forward pass.
- **Unequal list lengths:** A finished list contributes zero while the other pointer continues. The guarded digit expressions and guarded pointer advances handle this without padding nodes or a second loop.
- **A carry after both lists end:** Inputs such as `[9, 9]` and `[1]` require an extra node. Including `carry` in the loop condition ensures that the leading `1` is not lost.
- **No final carry:** For `[2, 4, 3] + [5, 6, 4]`, the last column produces less than `10`. Both pointers become `None` with `carry = 0`, so the loop stops without appending an unnecessary leading zero.
- **Zero plus zero:** `[0] + [0]` performs one iteration, appends one zero, and stops. The answer is `[0]`, not an empty list.
- **Input preservation:** The algorithm reassigns local variables `l1` and `l2`, but it never changes an input node's `val` or `next`. The caller's lists remain structurally unchanged.
- **Fresh output nodes:** Every digit is placed in a newly allocated node. The result does not share nodes with either input, so later mutation of the result cannot corrupt an operand.
- **Non-empty-input guarantee:** The Reference promises at least one node in each list. The loop is also naturally tolerant of a missing list because it treats that side as zeros, but that robustness is not needed to satisfy the stated contract.
