## General

**Each round consumes the two smallest remaining values**

Alice removes the minimum remaining value first, then Bob removes the new minimum. Bob appends his removed value before Alice appends hers. If the two removed values are $a \le b$, the round contributes `[b, a]` to the result.

The implementation models the changing minimum with a min-heap. `heapify(nums)` rearranges the input list in place so that `nums[0]` is the smallest value and the heap property supports efficient repeated removal.

During each loop iteration, `a = heappop(nums)` removes Alice’s minimum. The next `heappop` removes Bob’s minimum `b` from what remains. The code appends `b` and then `a`, exactly reversing their removal order as the game requires. Because the input length is even, two pops are always available until the heap becomes empty.

**Why heap extraction reproduces the rules exactly**

A Python min-heap guarantees that `heappop` returns a smallest element currently stored. Before the first pop of a round, the heap contains precisely all values not removed in earlier rounds, so `a` is Alice’s required choice. After that pop, the heap contains precisely the values Bob is allowed to choose from, so `b` is Bob’s required minimum.

Appending Bob’s value first and Alice’s second matches the distinct append rule; it is not enough merely to return values in sorted order. Repeating the same exact simulation until the heap is empty produces the unique result array.

For `nums = [5, 4, 2, 3]`, heap extraction yields two and then three, so the first output pair is `[3, 2]`. The remaining values are four and five; extraction yields them in that order and appending reverses them to `[5, 4]`. The complete answer is `[3, 2, 5, 4]`.

**Relationship to sorting**

If all values were sorted as

`x0 <= x1 <= x2 <= x3 <= ...`,

the removal sequence would be exactly that sorted sequence. The game’s append sequence swaps every adjacent pair, producing

`[x1, x0, x3, x2, ...]`.

The manifest summary describes that sort-and-swap perspective, but the exact protected solution does not call `sort`. It uses `heapify` followed by repeated `heappop` operations. Both approaches produce the same result, but their data flow and some implementation-space details differ.

**Duplicates cause no ambiguity**

When several equal minima exist, Alice or Bob may conceptually remove any occurrence of that value. Since the output stores values rather than original indices, all choices are equivalent. A heap is free to choose any equal entry, and the resulting array remains correct.

**Why the game has no strategic choices**

Although Alice and Bob are named participants, neither optimizes an objective or chooses among nonminimum values. Each action is prescribed: remove the current minimum, then append in the required order. This is a deterministic simulation problem, not minimax game theory.

The heap lets the code follow those rules without searching for a minimum by scanning the entire remaining list every time. A repeated linear minimum search plus deletion would become quadratic.

**Exact mutation and output behavior**

`heapify(nums)` modifies `nums`, and successive pops empty it completely. After the function returns, the caller-provided input list is empty. This is more substantial mutation than merely sorting it. The output `ans` contains every original value exactly once because each heap entry is popped once and appended once.

The result length therefore equals the original even length. Every adjacent output pair corresponds to one game round and has the larger-or-equal removed value first.

## Complexity detail

Let $N$ be the original number of elements. `heapify` takes $O(N)$ time. There are $N$ heap pops, each costing $O(\log N)$ in the worst case as the heap shrinks. Appends are amortized $O(1)$. The total time is $O(N\log N)$.

The heap reuses the input list, so excluding the output, the algorithm’s explicit auxiliary storage is $O(1)$ under the usual in-place heap accounting. The required result list uses $O(N)$ output space. Some manifests state $O(N)$ space because the returned array is included; it is useful to distinguish output space from extra working space.

## Alternatives and edge cases

- **Sort and swap adjacent pairs:** Sorting once and emitting `nums[1], nums[0], nums[3], nums[2], ...` is equally correct and also takes $O(N\log N)$ time. It matches the manifest summary more literally than this heap source.
- **Repeated linear minimum search:** Removing the minimum twice per round from an ordinary list can take $O(N^2)$ time.
- **Counting frequencies:** Since values have a small stated range, a counting array can generate minima in $O(N+V)$ time, but it relies on that bound and needs extra range storage.
- **Duplicate minima:** Equal values can be popped in any internal order because only values, not identities, appear in the answer.
- **Two elements:** The heap pops the smaller for Alice and the larger for Bob, then returns them as `[larger, smaller]`.
- **Even-length guarantee:** It ensures the second pop of every round exists. Without it, the rules would leave an unmatched value.
- **Input mutation:** The exact implementation empties `nums`. Copying before `heapify` would preserve the caller’s list but require $O(N)$ additional space.
- **No adversarial strategy:** Names of players do not imply choices; both minimum removals are mandatory.
- **Pair order:** Appending `a` before `b` would return the removal order, not the required Bob-before-Alice append order.
