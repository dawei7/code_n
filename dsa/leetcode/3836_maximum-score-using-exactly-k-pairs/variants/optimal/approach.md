## General

**A prefix state enforces both index orders**

After processing a prefix of one array, let a state for pair count `t` and right-prefix length `j` store the best score obtainable with exactly `t` pairs, using only the processed left values and the first `j` right values. Count-zero states equal zero. Positive counts that cannot yet be formed use a true negative sentinel; initializing them to zero would incorrectly allow fewer than `k` pairs when every legal score is negative.

For the next left value and right position, a state has three possibilities:

- skip the new left value, retaining the corresponding state from the previous left-prefix layer;
- skip the current right value, retaining the state immediately to the left in the current layer;
- pair these two values, adding their product to the previous layer's state with one fewer pair and one shorter right prefix.

The pairing transition comes only from the diagonal previous-prefix state. It therefore uses neither current index earlier and makes both newly chosen indices larger than every index in the preceding pairs.

**Roll the left-prefix dimension**

Only the previous and current left-prefix layers are needed. Each layer contains all pair counts from `0` through `K` and all right-prefix lengths. The two input arrays may be swapped because transposing every selected pair preserves products and both strict chains; place the shorter array on the stored right-prefix dimension to minimize memory.

Every legal selection either omits the newest left value, omits the newest right value, or uses them together after a legal selection of one fewer pair. The recurrence examines all three mutually exhaustive endings and takes their maximum. Induction over both prefixes and the exact pair count therefore shows that the final state is the best legal score using exactly `K` pairs.

## Complexity detail

There are $N$ left-prefix layers, $M$ right-prefix positions, and $K$ positive pair counts, with constant work per state. The time complexity is $O(N M K)$. Storing two layers after placing the shorter array on the right uses $O(K\min(N,M))$ auxiliary space.

The benchmark defines workload size as $W=NMK$ on square all-one arrays. The accepted rolling DP and an independent full three-dimensional prefix DP have the required $O(W)$ growth. The slower endpoint formulation rescans every possible predecessor for each selected endpoint and adds another principal factor.

## Alternatives and edge cases

- **Full three-dimensional prefix DP:** Store every left-prefix layer. This follows the recurrence directly and has the same $O(N M K)$ time, but uses $O(N M K)$ space.
- **Recursive memoization:** A top-down version can express skip and pair choices naturally, yet recursion overhead and a large state graph make the iterative prefix order more reliable at the maximum dimensions.
- **Rescan all predecessors:** Define states by the exact final pair and search every earlier pair for the previous optimum. This is correct but adds a principal predecessor factor and is too slow.
- **Exactly `k` pairs:** Negative answers are valid. Unreachable positive-count states must never default to zero.
- **Strict independent order:** A large product obtained by crossing the two index chains is illegal even when each index is used once.
- **Zeros:** Zero products can be optimal, but they do not remove the obligation to select exactly `k` pairs.
- **Unequal lengths:** Either array may be the shorter one; swapping their DP roles does not change the answer.
- **Large products:** One product can have magnitude $10^{12}$ and the total can reach $10^{14}$, so fixed-width implementations need signed 64-bit arithmetic.

