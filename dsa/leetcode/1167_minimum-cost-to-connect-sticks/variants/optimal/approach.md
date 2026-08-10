## General

**A merged length may be paid again**

When two sticks of lengths `x` and `y` are connected, their sum `z = x + y` is added to the total cost and becomes a new stick. If that combined stick participates in later connections, all `z` units are charged again.

Therefore, making a large combined stick early is dangerous: its length may be included in several later costs. The greedy objective is to keep intermediate sticks as small as possible by always merging the two smallest current lengths.

This is the same structure as optimal merge patterns and Huffman coding.

**Use a min-heap for the current smallest sticks**

`heapify(sticks)` rearranges the input list in place into a min-heap. The smallest current length is then available at the root and can be removed with `heappop` in logarithmic time.

Each loop iteration:

1. removes the two smallest current lengths;
2. adds them to obtain `z`;
3. adds `z` to `ans` because this connection costs that amount;
4. pushes `z` back because the merged stick must participate in future connections.

Two sticks disappear and one replaces them, so the collection size decreases by exactly one. Starting with `n` sticks, the loop performs exactly `n - 1` merges and stops when one final stick remains.

**Why the two smallest should be connected first**

Any complete sequence of connections can be represented as a full binary merge tree. Original sticks are leaves. Each internal node is the sum of its two children and represents one paid connection.

An original stick's length contributes once for every ancestor connection above it. If its leaf depth is `d`, its length is included `d` times in the total. Thus total cost can be viewed as

`sum(stick_length * leaf_depth)`.

In some optimal merge tree, consider a pair of sibling leaves at maximum depth. The labels assigned to these deepest leaves can be chosen as the two smallest stick lengths without increasing total cost: moving a smaller weight to a depth at least as large as a bigger weight cannot make the weighted depth sum worse.

Those two sibling leaves are combined with each other before either result combines upward. Contracting them into one leaf of weight equal to their sum leaves a smaller instance of the same problem. If the remaining contracted tree were not optimal for that smaller instance, replacing it with a better tree would improve the original, contradicting optimality.

Therefore, there exists an optimal solution whose first merge joins the two smallest sticks, and after that merge the same argument applies recursively to the new multiset. The heap algorithm follows exactly this optimal greedy choice at every step.

**Trace the first example**

For lengths `[2, 4, 3]`, the heap exposes two and three first. Their merge costs five, and five is inserted back alongside four.

The remaining two sticks four and five must be joined, costing nine. Total cost is `5 + 9 = 14`.

If two and four were merged first, that cost would be six and the remaining merge with three would cost nine, totaling 15. The earlier larger intermediate sum produces the worse result.

**Why merely sorting once is insufficient**

The new merged length can belong anywhere among the remaining values. After merging one and three into four, that four may need to be selected before an original length eight. A one-time sorted order cannot simply consume original elements in pairs.

The heap dynamically restores access to the two smallest values after every insertion, including both original and newly merged sticks.

**Why the algorithm is correct**

The exchange-and-contraction argument proves that an optimal sequence may begin with the two smallest current lengths. The algorithm makes that merge and adds its unavoidable cost.

The replacement stick creates a smaller valid problem. Reapplying the argument at every iteration shows that every greedy choice can be part of an optimal completion. When one stick remains, all required merges have been made and `ans` is the minimum total cost.

Positive input lengths ensure all costs and combined lengths behave as weights. No operation can reduce a future cost by introducing a negative stick.

## Complexity detail

Let `n` be the number of sticks. In-place heap construction takes `O(n)` time. There are `n - 1` iterations, each with two heap removals and one insertion, each `O(log n)` in the worst case. Total time is `O(n log n)`.

The exact code transforms and reuses the input `sticks` list as heap storage. Apart from that existing list, it stores only `ans` and `z`, so auxiliary space is `O(1)` under the in-place-input convention used by the manifest.

The input list is mutated and ends with only the final combined length. If preserving caller-owned input were required, copying it before `heapify` would use `O(n)` extra space.

## Alternatives and edge cases

- **Repeatedly sort the list:** Selecting two smallest values after a full sort works, but sorting after each merge can raise time to roughly `O(n^2 log n)`. A heap maintains just enough order.
- **Sort once and pair adjacent originals:** New sums must reenter the ordering, so a fixed original pairing can miss the optimum.
- **Merge the two largest first:** Large intermediate sticks are charged repeatedly and generally produce a much higher cost.
- **Two-queue optimal merge:** With an initially sorted list, one queue for originals and one for generated sums can achieve `O(n log n)` due to sorting and linear merging afterward. It needs additional indexing structure.
- **One stick:** No connection is needed, the loop does not run, and the result is zero.
- **Two sticks:** They are popped once, their sum is the only cost, and the process ends.
- **Equal lengths:** Any two equal minima are interchangeable; the heap may choose either without affecting optimality.
- **Large combined stick:** It is pushed back and selected only when it becomes one of the two smallest current values.
- **Positive lengths:** The greedy proof relies on nonnegative weight behavior, and the contract supplies strictly positive values.
- **Input mutation:** `heapify` and subsequent heap operations reorder and shrink `sticks`. Callers needing the original array must copy it explicitly.
- **Cost growth:** `ans` may exceed any individual input length because each stick can contribute at multiple merge depths.
