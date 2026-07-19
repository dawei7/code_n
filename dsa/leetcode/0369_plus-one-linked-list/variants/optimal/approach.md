## General
**Locate the rightmost digit that can absorb the carry**

Scan the list once and remember the last node whose digit is not nine. Any nodes after that position are all nines; adding one will turn exactly that suffix into zeroes. If such a node exists, increment it and overwrite every following digit with zero.

**Handle an all-nine number by reusing the original nodes**

When no non-nine node exists, every original digit becomes zero and the result needs a new leading one. Create that one node, link it before the original head, zero the full original list, and return the new head. In the app adapter, constructing `type(head)(1)` preserves the runner-provided node type without defining a competing linked-list class.

**Why no other digit changes**

Decimal addition of one stops at the first digit from the right that is less than nine: that digit increases by one, every trailing nine becomes zero, and every earlier digit remains unchanged. The remembered node is precisely that stopping point. If it does not exist, the carry crosses the entire number and creates a new most-significant one. These are the only two possible carry patterns, so the transformation is complete.

## Complexity detail
The first scan finds the rightmost non-nine node, and the second scan zeroes at most the suffix after it. Each of the `n` nodes is visited a constant number of times, giving $O(n)$ time. Only node references are stored, so auxiliary space is $O(1)$; the all-nine case allocates the one required output node.

## Alternatives and edge cases
- **Reverse, add, and reverse back:** is also $O(n)$ time and $O(1)$ space but rewires the list twice.
- **Recursive carry propagation:** follows the arithmetic naturally but uses $O(n)$ call-stack space.
- **Repeated predecessor search from the head:** avoids reversal but becomes $O(n^2)$ when a long suffix of nines carries.
- A final digit below nine changes without affecting earlier nodes.
- A suffix of several nines becomes the same number of zeroes.
- An all-nine input increases the list length by one.
- The single digit zero increments to one, while the single digit nine becomes `[1,0]`.
