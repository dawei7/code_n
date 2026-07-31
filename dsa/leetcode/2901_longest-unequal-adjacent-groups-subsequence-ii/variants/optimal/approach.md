## General

Treat each word index as a vertex in a directed acyclic graph ordered by index. There is an edge $j\to i$ for $j<i$ exactly when the two group identifiers differ, the words have the same length, and their Hamming distance is one. A valid answer is precisely a directed path in this graph, so the task is to recover a longest path.

Let `lengths[i]` be the greatest valid subsequence length ending at index `i`. Every index alone gives the initial value $1$. For each earlier index `j`, test whether $j\to i$ is an edge. If it is and `lengths[j] + 1` improves `lengths[i]`, update the length and record `j` in `previous[i]`.

The edge test first rejects unequal groups and unequal word lengths. It then compares aligned characters, stopping as soon as more than one difference is found; the edge exists only when the final difference count is exactly one.

When index `i` is processed, every path that can end there must arrive from some earlier compatible `j`, and all `lengths[j]` values are already final. Taking the best such predecessor therefore computes the optimal path ending at `i`. Induction over increasing indices proves every state correct. The largest state is the global optimum; following its parent indices backward and reversing the collected words reconstructs one longest valid subsequence.

## Complexity detail

There are $O(n^2)$ ordered index pairs. Testing a pair compares at most $L$ characters, so the running time is $O(n^2L)$. The two dynamic-programming arrays and the reconstructed answer use $O(n)$ space.

## Alternatives and edge cases

- **Greedy next compatible word:** A locally available transition can block a longer future chain, so choosing the first compatible successor is not generally optimal.
- **Store every best subsequence explicitly:** Copying word lists during transitions remains correct but can raise the worst-case time to $O(n^3+n^2L)$ and uses substantially more memory.
- **Build the full compatibility graph:** Longest-path DP is then straightforward, but storing all $O(n^2)$ possible edges is unnecessary.
- **Different word lengths:** Such a pair has no defined equal-length Hamming distance for this contract and cannot form an edge.
- **Exactly one character:** Zero differences and two or more differences are both invalid, even when the groups differ.
- **Equal group identifiers:** They block a transition regardless of the two words.
- **Several longest paths:** Parent updates may retain any one optimum because the result is not required to be unique.
