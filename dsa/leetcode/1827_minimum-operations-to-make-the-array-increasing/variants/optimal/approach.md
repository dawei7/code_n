## General
**Commit to the smallest legal value at each position**

Keep the previous value after all required increments. For the current original value, strict increase requires at least `previous + 1`. Its optimal adjusted value is therefore the larger of its original value and that threshold. Add the difference from the original to the operation count and carry the adjusted value forward.

**Why no earlier choice should be made larger**

Only increments are allowed, so the first value is optimally unchanged. At every later position, raising it above the smallest legal value spends extra operations immediately and can only raise—not relax—the minimum required value for the following position. Thus the locally smallest feasible adjustment is compatible with every optimal suffix.

**Why the complete greedy construction is optimal**

Inductively, after each position the algorithm has built the componentwise smallest strictly increasing prefix obtainable by increments. Any valid transformed array must make the current value at least `previous + 1`, and the algorithm pays exactly the necessary difference. Summing these individually unavoidable increments yields the global minimum.

## Complexity detail
The scan visits each of the $n$ values once and performs constant work, so time is $O(n)$. The operation total and previous adjusted value use $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Increment one unit in a loop:** It produces the same adjusted values but can execute $\Theta(n^2)$ individual loop iterations on a flat array.
- **Modify `nums` in place:** It is also $O(n)$ and correct, but tracking only the adjusted predecessor avoids changing the input.
- **Already strictly increasing:** Every value exceeds the predecessor and the answer remains zero.
- **Equal neighbors:** The later value must be raised by at least one.
- **Decreasing input:** Earlier forced increases propagate and may require increasingly large changes.
- **Single element:** Return zero without any adjacent comparison.
- **Large adjusted values:** The transformed values may exceed the original $10^4$ bound; that bound applies only to input.
