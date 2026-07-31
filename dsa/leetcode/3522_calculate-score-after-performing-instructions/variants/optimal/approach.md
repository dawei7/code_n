## General

There is only one possible next instruction from every executed index, so simulate that single path. Keep the current `index`, the running `score`, and a set containing every index whose instruction has already been executed.

At the start of each iteration, require both that the index is in bounds and that it is absent from the visited set. Mark it visited before applying its operation. For `"add"`, add `values[index]` and increment the index by one. For `"jump"`, add `values[index]` to the index and leave the score unchanged. These transitions exactly reproduce the program rules, while the loop condition ensures an out-of-bounds target or a repeated target terminates before execution.

Because an index enters the set before its only execution, no instruction can contribute to the score twice. Conversely, the loop continues whenever the contract permits another instruction, so the returned score includes precisely all executed add operations.

## Complexity detail

Let $n$ be the common array length and $k \le n$ the number of executed instructions. Each executed index is processed once, with expected $O(1)$ hash-set lookup and insertion, so the simulation takes expected $O(k)$ time and $O(k)$ space. The required worst-case bounds in terms of the input are $O(n)$ time and $O(n)$ space.

The benchmark size is $n$. Every instruction is `"add"`, so the legal execution path visits all indices before leaving the array. The reference set performs expected constant-time revisit checks, while the calibrated slower implementation stores visited indices in a list and scans that growing list on every step, producing quadratic work.

## Alternatives and edge cases

- **Boolean visited array:** Also gives deterministic $O(n)$ time and space and can be faster than hashing, but the set directly represents only the indices actually reached.
- **Visited list with membership tests:** Functionally correct, but `index in visited` scans up to $O(n)$ entries per step and makes the full simulation $O(n^2)$.
- **Zero jump:** The current index is already marked, so the next loop check detects the revisit and stops.
- **Negative jump:** The target may be an earlier unvisited instruction, an already visited instruction, or a negative out-of-bounds index.
- **Large positive jump:** Execution stops without accessing the target if it is at least $n$.
- **Negative add value:** It decreases the score but still advances exactly one index.
- **Revisited add instruction:** Its value is not added again because termination occurs before repeated execution.
- **Single instruction:** It either adds once and exits or jumps, possibly directly back to itself.
