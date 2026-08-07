## Function Contract

**Inputs**

- `nums`: A list of non-negative integers. Deletions preserve the relative order of every retained element.

Let $n=\lvert\texttt{nums}\rvert$. An element originally at index $i$ can become a fixed point only if enough earlier elements can be deleted to move it to index `nums[i]`.

**Return value**

Return the largest possible number of indices `i` satisfying `nums[i] == i` in the array remaining after any number of deletions. Return `0` if no retained element can be made a fixed point.
