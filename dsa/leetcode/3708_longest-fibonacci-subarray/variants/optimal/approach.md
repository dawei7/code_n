## General

Whether a Fibonacci subarray can extend through position `index` depends only on the three consecutive values ending there. If `nums[index]` equals `nums[index - 1] + nums[index - 2]`, every recurrence already satisfied by the current run remains satisfied, and the run grows by one. Otherwise, no Fibonacci subarray of length at least three can cross this failed equation.

Maintain `current` as the length of the longest Fibonacci subarray ending at the previous position. It starts at `2` because any adjacent pair qualifies. On a successful recurrence, increment `current`; on a failure, reset it to `2`, representing the new pair `nums[index - 1..index]`.

After each extension, update `best`. The reset discards exactly the subarrays that include a failed triple, while retaining the only suffix that can begin a future run. Therefore `current` is correct at every index, and the maximum value recorded in `best` is the longest Fibonacci subarray anywhere in `nums`.

## Complexity detail

Let $n=\lvert\texttt{nums}\rvert$. Each value from the third onward is inspected once, so the running time is $O(n)$. The two run lengths and loop index require $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Enumerate every subarray:** Testing all start/end pairs can require $O(n^2)$ candidates even when each failed recurrence is detected quickly.
- **Restart an extension from every position:** Growing a candidate independently from each left endpoint repeats comparisons already summarized by the current run.
- **Dynamic-programming array:** Storing the run length ending at every index also takes $O(n)$ time, but uses $O(n)$ space when only the previous length and global maximum are needed.
- **Failure at the third term:** The longest valid subarray may still have length `2`; initialization and reset both preserve that baseline.
- **Overlapping runs:** After a failure, the last two values of the failed run become the first two values of a possible new run.
- **Large positive values:** A sum may exceed $10^9$ even though each input value does not; comparing the mathematical sum with the next element still correctly marks a break.
