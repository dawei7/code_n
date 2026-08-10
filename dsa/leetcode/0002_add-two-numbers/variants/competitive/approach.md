## General

**Why reverse-order digits make one-pass addition possible**

The head of each input list stores the least-significant digit. Moving through `.next` visits the tens digit, hundreds digit, and later powers of ten. For example, `[2, 4, 3]` represents

$$
2 + 4 \cdot 10 + 3 \cdot 100 = 342.
$$

Ordinary written addition starts with the ones column for a reason: a column can create a carry into the next more-significant column, but it never depends on a column to its left. Because the lists use the same least-to-most-significant order, the method can add one column, append one answer node, and advance both pointers in a single forward pass.

For each column, the method needs three contributions:

1. the carry left by the preceding column;
2. the current digit from `l1`, if that list still has one;
3. the current digit from `l2`, if that list still has one.

Their sum is stored in `val` temporarily. The name later gets reused for the result digit after division by ten; following that change in meaning is important when reading the compact competitive implementation.

**The dummy node and output tail**

The method begins with

```python
dummy = ListNode(0)
current, carry = dummy, 0
```

`dummy` is a construction aid, not a digit in the returned number. `current` always points to the last node currently in the output chain. Starting it at `dummy` means the first real result digit and every later digit can be attached with the same two lines:

```python
current.next = ListNode(val)
current = current.next
```

After all digits are appended, `dummy.next` is the first real node. This avoids a separate branch for creating the head and reduces the risk of losing the beginning of the list while the tail pointer moves.

**Accumulate only the digits that exist**

The main loop continues while at least one input pointer is non-null:

```python
while l1 or l2:
```

At the beginning of an iteration, the code initializes

```python
val = carry
```

so the previous column's carry is included exactly once. It then handles each list independently:

```python
if l1:
    val += l1.val
    l1 = l1.next
```

and likewise for `l2`. If a list still has a node, its digit is added and its pointer advances immediately. If the list is already exhausted, the branch does nothing, which is mathematically the same as adding zero for that column.

Using two independent `if` statements, rather than requiring both nodes to exist, is what allows different-length numbers to work. Once the shorter list ends, the longer list continues to contribute digits together with any carry.

**Split a column sum with `divmod`**

After all available contributions have been accumulated, the method executes

```python
carry, val = divmod(val, 10)
```

For any non-negative integer `column_sum`, `divmod(column_sum, 10)` returns

$$
(\lfloor \texttt{column\_sum}/10 \rfloor,\; \texttt{column\_sum} \bmod 10).
$$

The quotient is the carry into the next column, and the remainder is the single decimal digit stored in the current result node. Although the variable `val` held the whole sum immediately before this line, it holds only the remainder immediately afterward.

The largest possible total is $9 + 9 + 1 = 19$, so `carry` is always `0` or `1`. This fact is established in the first iteration, when the incoming carry is `0`, and remains true in every later iteration.

**The final carry is handled after the loop**

Unlike the Optimal variant, this implementation does not put `carry` in the loop condition. Its loop stops as soon as both input lists are exhausted. It then explicitly checks

```python
if carry == 1:
    current.next = ListNode(1)
```

Only `1` can remain, so a single node is sufficient. There is no need to advance `current` afterward because no more nodes will be attached.

This arrangement and `while l1 or l2 or carry` are two equivalent control-flow choices. One writes the final carry inside the normal loop; this competitive version writes it in a short post-loop branch.

**Trace addition across unequal lengths**

Consider `l1 = [9, 9, 9]` and `l2 = [1]`, representing $999 + 1$.

| Iteration | Existing digits | Incoming `carry` | Whole `val` before `divmod` | Appended digit | New `carry` |
|---:|---|---:|---:|---:|---:|
| 1 | `9` and `1` | `0` | `10` | `0` | `1` |
| 2 | `9` and no `l2` digit | `1` | `10` | `0` | `1` |
| 3 | `9` and no `l2` digit | `1` | `10` | `0` | `1` |

Both pointers are now `None`, so the loop ends. `carry == 1`, and the post-loop branch appends the final node. The result is `[0, 0, 0, 1]`, representing $1000$.

**Why the constructed prefix is always accurate**

Before any iteration, no input columns have been processed, no result digits have been appended, and the carry is zero. Suppose that after processing `k` columns, the output chain contains the correct `k` least-significant digits and `carry` is exactly the amount transferred into column `k`.

The next iteration begins with that carry, adds each operand's digit for column `k` when present, and splits the total into a remainder and quotient. The remainder is exactly the required digit for $10^k$; the quotient is exactly the carry for $10^{k+1}$. Appending the remainder therefore makes the output correct through one additional column.

When the loop ends, all operand digits have been consumed. If the carry is zero, the list is complete. If it is one, the explicit final node records the only remaining most-significant digit. In both cases, `dummy.next` begins a list whose digits represent the full sum in the required reverse order.

The method constructs new nodes rather than reusing input nodes. Moving the local `l1` and `l2` pointers does not alter the original links, so the operands remain unchanged.

## Complexity detail

Let $n$ and $m$ be the lengths of the two input lists, and define $L = \max(n,m)$.

- **Time complexity: $O(L)$.** Each loop iteration advances every non-empty input pointer once. The loop therefore runs exactly $L$ times, after which the final-carry check takes constant time. Arithmetic on two digits and a carry, `divmod`, pointer assignments, and node construction are all constant-time operations per column.
- **Space complexity: $O(L)$ including the result.** The returned chain contains $L$ nodes when there is no final carry and $L+1$ nodes when there is one. Both sizes are $O(L)$. Excluding the required output, the method uses a dummy node, the `current` pointer, two input pointers, `carry`, and `val`, so its auxiliary working space is $O(1)$. The `# Space: O(1)` source comment follows the common convention of excluding output; the variant manifest includes the constructed result and therefore records $O(\max(n,m))$.

The implementation is iterative and allocates no arrays, stacks, or recursive frames. Each output node is allocated once and linked once.

## Alternatives and edge cases

- **Carry in the loop condition:** `while l1 or l2 or carry` can process a final carry as one ordinary iteration by treating missing digits as zero. That removes the post-loop `if`; the competitive version instead keeps the main loop tied exactly to input nodes and appends the final `1` explicitly.
- **Integer conversion:** Reconstructing full integers before adding is less portable because fixed-width languages may overflow, and it ignores the linked-list structure the problem asks the algorithm to handle. Per-column addition has no whole-number overflow dependency.
- **Recursion:** A recursive call per digit can express the same recurrence, but it consumes $O(L)$ stack space and makes the final carry and unequal lengths less visible. The iterative method needs only constant auxiliary state.
- **Reusing operand nodes:** Mutating and relinking input nodes could save some allocations, but it would change caller-owned data and complicate the case where the result needs a new leading node. Fresh nodes provide simple ownership and predictable behavior.
- **One list is longer:** The two independent `if` blocks allow the longer list to continue after the shorter pointer becomes `None`; the missing side contributes zero automatically.
- **Final carry exists:** The maximum residual carry is exactly `1`, so `if carry == 1` appends the one possible extra node. `[9] + [1]` becomes `[0, 1]`.
- **Final carry does not exist:** If the last `divmod` produces carry zero, the post-loop branch does nothing. This prevents an extra leading zero from being added.
- **Both operands are zero:** `[0] + [0]` enters the loop once, appends `0`, leaves `carry = 0`, and returns a one-node zero representation.
- **Runs of nines:** Repeated carries such as `[9, 9, 9] + [1]` are propagated one column at a time and finish with exactly one extra node.
- **No leading zeros in the inputs:** The contract's representation guarantee makes each operand canonical. The algorithm would still add lists containing redundant most-significant zeros, but its output could then inherit a redundant final zero, so the guarantee matters for canonical representation.
- **Input lists are non-empty:** The Reference promises both heads exist. The loop would nevertheless handle one missing head by copying the other number through new nodes, which follows the same zero-contribution rule.
- **Forward-order digits:** If the head stored the most-significant digit, carry information would be discovered too late for immediate output. Stacks, recursion, or reversal would be needed; those costs are unnecessary for this reversed-order contract.
