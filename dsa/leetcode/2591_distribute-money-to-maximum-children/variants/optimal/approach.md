## General

First reserve one dollar for every child. If this already exceeds `money`, no distribution can satisfy the minimum and the answer is `-1`. After the reservation, upgrading one child from one dollar to exactly eight costs seven additional dollars.

Use as many complete seven-dollar upgrades as possible, capped by the number of children. This greedy count is an upper bound because every eight-dollar recipient necessarily consumes those same seven extra dollars. Usually it is attainable by assigning all remaining money to children who are not counted as eight-dollar recipients.

Two configurations need repair:

- If every child was upgraded but money remains, somebody must receive more than eight. Reduce the count by one so that child can absorb the leftover.
- If all but one child were upgraded and exactly three extra dollars remain, the last child would receive `1 + 3 = 4`, which is forbidden. Reduce the count by one; the reclaimed seven dollars and the three-dollar remainder can then be split between two non-eight recipients without assigning four.

No other remainder prevents a valid distribution, so the corrected greedy count is maximal.

## Complexity detail

The method performs a fixed number of integer arithmetic operations and conditional checks, taking $O(1)$ time and $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Try every possible number of eights:** Checking candidates from `children` downward is correct but takes $O(\texttt{children})$ time when the arithmetic identifies the answer directly.
- **Dynamic programming over recipients and money:** This can model every valid allocation but is unnecessary for two bounded scalar inputs.
- **Insufficient total:** When `money < children`, giving everyone at least one dollar is impossible.
- **All-eight leftover:** Extra money cannot disappear, so an otherwise all-eight allocation must sacrifice one counted child.
- **Forbidden four:** The special three-dollar remainder matters only when exactly one non-eight child remains.
- **Amounts above eight:** They are legal and provide a place to absorb surplus money.
