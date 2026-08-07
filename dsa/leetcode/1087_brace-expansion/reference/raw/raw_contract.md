## Function Contract

**Input**

- `s`: a valid string made from lowercase English letters, curly braces, and commas.

A lowercase letter outside braces is fixed. The distinct letters within one brace group are alternatives for a single output position, and different groups are chosen independently. Brace groups do not nest.

Let $n$ be the length of `s`, $L$ the number of output positions after each brace group is treated as one position, and $R$ the number of words represented by the expression.

**Return value**

- A list containing all $R$ possible words, sorted in lexicographical order.
- Every returned word has length $L$.
