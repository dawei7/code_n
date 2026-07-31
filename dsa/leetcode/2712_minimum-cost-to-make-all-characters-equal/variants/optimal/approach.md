## General

Only boundaries between unequal adjacent characters matter. If `s[i - 1] != s[i]`, the final string cannot be uniform until one operation changes the parity of inversions on exactly one side of that boundary.

A prefix operation can affect this boundary without affecting any boundary to its right only by ending at index $i-1$; its cost is $i$. The corresponding suffix operation must start at index $i$ and costs $n-i$. Thus every unequal boundary requires at least $\min(i,n-i)$ cost.

These lower bounds can be achieved simultaneously. For each unequal boundary, choose its cheaper prefix or suffix operation. Inversion operations combine by parity and commute: characters within an interval may be flipped several times, but crossing an unequal boundary changes parity exactly once, while crossing an originally equal boundary changes it an even number of times. Consequently all adjacent characters become equal, and summing the cheaper cost at every transition is optimal.

A single left-to-right scan detects all unequal neighbors and accumulates `min(index, length - index)`.

## Complexity detail

Let $n$ be the length of `s`. The algorithm examines each adjacent pair once, taking $O(n)$ time and $O(1)$ auxiliary space. The returned integer requires no input-sized storage. The benchmark uses `size` as $n$ and compares the scan with independently recomputing the costs around every possible pivot.

## Alternatives and edge cases

- **Prefix and suffix dynamic-programming arrays:** Computing the cost to align each prefix and suffix is also $O(n)$ time, but stores $O(n)$ values that the boundary sum does not need.
- **Recompute around every pivot:** Trying every character as an unchanged anchor and rescanning both sides is correct, but takes $O(n^2)$ time.
- **Breadth-first search over strings:** Treating every binary string as a state becomes exponential in $n$ and is infeasible under the input limit.
- A length-one string is already uniform and costs zero.
- A string with no unequal adjacent pair also costs zero.
- At an exact middle boundary, prefix and suffix operations have equal cost.
- The final common bit need not be chosen in advance; the transition argument covers both possible outcomes.

