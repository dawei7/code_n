## General

**The operations depend on the most recent valid scores**

The record changes over time. A canceled score must disappear, and later `+` or `D` operations refer only to scores still valid after all earlier cancellations.

A stack represents this perfectly:

- its elements are the valid scores in chronological order;
- the top is the most recent valid score;
- the element below the top is the second most recent.

After processing each operation, `stk` is exactly the current record.

**Ordinary integer operation**

If `op` is not one of the three command strings, it represents an integer score. `int(op)` parses positive or negative text and the value is appended.

Appending places it at the end of the record and makes it available to future commands.

**The plus command**

For `+`, the new score is the sum of the previous two valid scores:

`stk[-1] + stk[-2]`.

The source guarantees at least two valid scores whenever this operation occurs. The sum is appended without removing either source score.

It is important that the expression is evaluated before the append. Both negative indices refer to the old record's last two entries.

**The double command**

For `D`, the new score is twice the previous valid score. The exact code computes:

`stk[-1] << 1`.

Left-shifting an integer by one binary position equals multiplication by two, including for negative Python integers. The doubled value is appended, while the original score remains.

Writing `2 * stk[-1]` would be more immediately recognizable but behaves equivalently.

**The cancel command**

For `C`, `stk.pop()` removes the most recent valid score. The source guarantees the stack is nonempty.

The command itself does not become a score. Once removed, that score no longer influences later `+` or `D` operations.

**A walkthrough**

For `["5", "2", "C", "D", "+"]`:

- `"5"` appends five: `[5]`;
- `"2"` appends two: `[5, 2]`;
- `"C"` removes two: `[5]`;
- `"D"` appends ten: `[5, 10]`;
- `"+"` appends fifteen: `[5, 10, 15]`.

Summing the final record gives thirty.

**Why a canceled value stays gone**

Consider later commands after `C`. Because the canceled score was physically popped, stack positions `-1` and `-2` automatically refer to the latest remaining valid scores. No separate “invalid” marker or backward search is needed.

**The stack invariant**

After processing the first `i` operations, the stack contains exactly the valid score record specified by those operations, in order.

It is true initially because both are empty. For an integer, both the rules and implementation append the value. For `+` and `D`, the stack invariant makes the referenced top entries exactly the required previous scores, and appending creates the same new record. For `C`, both rules and implementation remove the last valid score.

By induction, the invariant holds after all operations. Therefore, `sum(stk)` is exactly the requested total.

**Why the total is computed only at the end**

The exact source keeps individual scores because future commands need them, then runs `sum` once.

It could maintain a running total alongside the stack, adding on insertions and subtracting on cancellation. That would save the final pass but not change asymptotic complexity, and the direct final sum is simpler.

## Complexity detail

Let `N` be the number of operations and `V` the number of scores remaining at the end.

Each operation is processed once. Stack append, top access, and pop are amortized `O(1)`. Parsing an integer string costs time proportional to its small bounded textual length. The final `sum` scans `V <= N` entries. Total running time is `O(N)`.

In the worst case, every operation appends a score and none is canceled, so the stack holds `O(N)` values. Auxiliary space is `O(N)`.

Python integers handle negative values and the guaranteed 32-bit intermediate range safely.

## Alternatives and edge cases

- **List of records with validity flags:** Keep canceled entries and search backward for valid scores. This complicates commands and can make repeated lookups slower than stack removal.

- **Stack plus running total:** Update a total on every append and subtract the popped value on `C`. This avoids the final linear sum but still needs the stack for `+` and `D`.

- **Recompute the record from the beginning for each command:** This repeats work and is unnecessary because stack state is incremental.

- **Final record is empty:** Python `sum([])` is zero, correctly handling operations such as `["1", "C"]`.

- **Negative score:** `int` parses it, addition works normally, and left shift doubles it mathematically.

- **Consecutive cancellations:** They are safe whenever the validity guarantee says a score remains before each `C`.

- **Plus after cancellations:** The top two stack entries are the latest surviving scores, not necessarily the latest two numeric operations in the input.

- **Double after a negative score:** Left shift produces twice the negative value.

- **Command text versus integer text:** The branch order recognizes `+`, `D`, and `C` first; every other legal string is parsed as an integer.

- **Validity guarantees:** The code performs no explicit stack-length checks because the source promises every operation is valid.

- **Intermediate overflow:** The source says values fit 32-bit, and Python would handle larger values anyway. Fixed-width implementations can rely on the stated guarantee.

- **Stack order:** Scores must remain chronological. Sorting or aggregating them would destroy access to the previous two valid rounds.

- **Using `stk[-1] * 2` instead of shift:** It is equivalent and may be clearer; the exact source's shift is still correct.
