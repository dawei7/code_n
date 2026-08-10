## General

**First determine the minimum score, then maximize the number of pieces.** Let

$$
A=\texttt{nums[0] AND nums[1] AND \cdots AND nums[n-1]}
$$

be the bitwise AND of the whole array. Keeping the entire array as one subarray always achieves total score $A$, so the minimum total can never be greater than $A$.

For any partition, every bit set in $A$ appears in every array element. It therefore remains set in the AND score of every subarray. Each subarray score is numerically at least $A$. This separates the problem into two cases.

**If the whole-array AND is positive.** Every subarray score contains all bits of positive $A$, so every piece has score at least $A>0$. A partition into two or more pieces has score sum at least $2A>A$. It cannot match the one-piece score $A$. Consequently, the unique maximum number of pieces among minimum-score partitions is one.

**If the whole-array AND is zero.** Score zero is the absolute minimum because all scores are non-negative. A partition has total zero only when every one of its subarrays has AND zero. The task becomes cutting as many zero-AND segments as possible.

**Greedily close the earliest zero-AND prefix.** Variable `score` is the AND of the current not-yet-closed segment. It starts at `-1`. In Python, negative one behaves like an unbounded sequence of one bits for bitwise AND, so `-1 & num == num` for every non-negative input. This is a convenient identity value.

For each `num`, the code executes `score &= num`. Bitwise AND can only clear bits as a segment grows; a bit never returns after it has been cleared. As soon as `score == 0`, the current segment is a valid zero-score piece. The solution closes it immediately, resets `score = -1` for the next segment, and increments its counter.

**Why the earliest possible cut is optimal.** Suppose the current segment first reaches AND zero at position $r$. No valid zero-AND segment starting at the same left boundary can end before $r$, by definition of “first.” Any valid partition must place its first cut at $r$ or later. Cutting exactly at $r$ leaves the longest possible suffix for forming additional valid pieces. Delaying the cut cannot create more room or restore bits, so it cannot increase the number of later zero-AND segments. Repeating this argument after every reset proves the greedy cuts maximize the number of zero-score pieces.

**What happens to a trailing nonzero suffix.** After one or more zero segments have been closed, the final few elements might leave `score > 0`. They cannot stand as a separate piece in a minimum-total-zero partition. They can, however, be appended to the last closed zero-AND segment: zero AND anything remains zero. This covers every input element without reducing the number of previously counted pieces.

**Understanding the unusual counter.** The source initializes `ans = 1` and increments it for every time a zero segment is closed. If no zero is ever reached, `ans` remains one and the function returns one, matching the positive-whole-AND case. If $c\ge1$ zero segments are found, `ans = c+1` and the function returns `ans - 1 = c`. The extra initial one is only a coding device; the actual result in the zero case is the number of greedy zero cuts.

For `[1,0,2,0,1,2]`, current AND reaches zero after `[1,0]`, after `[2,0]`, and after `[1,2]`. Three zero-score segments are closed, giving the answer three. For `[5,7,1,3]`, the whole AND is one, no reset occurs, and the result is one.
When $A>0$, more than one segment necessarily raises the total above the achievable minimum $A$. When $A=0$, non-negativity forces every segment score to zero, and earliest-zero greedy cutting yields the maximum number of such segments. The source's return expression implements exactly those cases.

## Complexity detail

The loop reads every element once and performs one constant-width bitwise AND plus constant scalar work. Since `nums[i] <= 10^6`, integer width is bounded by the constraints. Time is $O(n)$.

Only `score` and `ans` are maintained, so auxiliary space is $O(1)$. The input is neither copied nor changed. The manifest's $O(n)$ time and $O(1)$ space accurately describe the checked-in implementation.

## Alternatives and edge cases

- **Compute the whole AND first:** One may explicitly branch on $A$ and then run a second greedy pass when it is zero. The source combines discovery and cutting in one pass.
- **Dynamic programming over cut positions:** It can model partitions but is unnecessary because AND only loses bits and the earliest valid cut is always optimal.
- **Whole AND positive:** Return one; every additional subarray contributes at least the same positive common-bit value.
- **Trailing nonzero remainder:** Merge it into the final zero-score segment, whose AND stays zero.
- **A zero element:** Encountering literal zero immediately makes the current segment AND zero and forces the earliest possible cut.
- **All zeros:** Every single element forms a zero-score segment, so the maximum number is $n$.
- **Single element:** The result is one whether its value is zero or positive, because at least one subarray is required.
- **Identity value `-1`:** This Python idiom is safe for non-negative inputs; a fixed-width implementation can initialize from the first element or use an all-ones mask.
