## General

**Model each in-range integer as a graph state**

An operation may be started only while the current value `x` lies between zero and one thousand inclusive. These 1,001 integers are the reusable states of an implicit graph.

From one such `x` and each `num`, there are three possible next values:

- `x + num`;
- `x - num`;
- `x ^ num`.

Each transition costs exactly one operation, so breadth-first search finds the minimum number of operations.

**Why out-of-range values are terminal**

An operation producing a value below zero or above one thousand is legal. If that value equals `goal`, the search must accept it.

If it does not equal `goal`, no further operation may begin from it. The source therefore checks `nx == goal` before checking the allowed range, but enqueues `nx` only when `0 <= nx <= 1000`.

This order faithfully handles goals far outside the reusable state interval.

**Queue states by operation count**

The queue begins with `(start,0)`. For a popped pair `(x,step)`, every generated neighbor is reachable in `step+1` operations.

Breadth-first order guarantees all states at smaller step counts are processed before states at larger counts. The first generated value equal to `goal` therefore uses the minimum possible number of operations, and the source returns immediately.

**Generate all three operations uniformly**

The source creates three small functions for addition, subtraction, and XOR and stores them in `ops`.

For every `num`, the inner loop calls each function. This covers every legal action from the problem statement. The same `num` can be used again later because nothing removes it from the array or records per-number usage.

Distinctness of `nums` avoids duplicate input entries, although different operations or different numbers may still reach the same next state.

**Use a visited table for reusable states**

`vis` has one Boolean for each integer zero through one thousand. When an unseen in-range `nx` is enqueued, it is marked immediately.

Marking at enqueue time prevents several queued parents from adding the same value before it is processed. Since future behavior depends only on the current integer and not on the path used to reach it, processing a later occurrence cannot improve on the first breadth-first arrival.

**The initial state is not marked immediately**

The exact source leaves `vis[start]` false when seeding the queue. If some operation later returns to `start`, that value may be enqueued once more and then marked.

This creates at most one redundant processing of the start state. After that generation, `vis[start]` is true like every other state. It does not harm correctness: the original queue entry already explores start at distance zero, while the later revisit has a larger step count and cannot create a shorter route that BFS missed.

Marking `vis[start]=True` initially would avoid the redundant revisit but is not required for the result.

**Trace an out-of-range final step**

For `nums=[3,5,7]`, `start=0`, and `goal=-4`, BFS can reach three in one step.

From three, subtraction by seven produces negative four. The goal comparison succeeds before the range check, so the source returns two. Negative four is never enqueued, correctly reflecting that no further move could start there.

**Why each in-range state needs to be processed once**

Suppose the first BFS discovery of value `v` uses `d` operations. Any later discovery has at least `d` operations because of queue level order.

All outgoing values from `v` depend only on `v` and `nums`. Repeating them from a later copy cannot yield a shorter goal route. The visited table therefore removes only redundant work.

**Why failure returns negative one**

There are only 1,001 reusable states. After all reachable ones have been processed, the queue becomes empty.

Every legal multi-operation sequence must remain among those states until its final operation. BFS tried every operation from every reachable reusable state, including terminal results outside the range. If none equaled `goal`, conversion is impossible and `-1` is correct.

**XOR and negative numbers**

`nums` may contain negative integers. The exact Python `^` operator applies Python's signed integer bitwise semantics, and its result may lie far outside the reusable interval. The same goal-first, range-second handling applies.

The method does not rely on numerical closeness to the goal; BFS treats addition, subtraction, and XOR transitions equally.

## Complexity detail

Let $R=1001$ be the reusable state count and $M=len(nums)$. Each reusable state is processed at most once, except for the possible single redundant revisit of `start`. Processing one state tries three operations for every input number.

Time is $O(3RM)=O(RM)$. The visited array and queue store at most $O(R)$ states, so auxiliary space is $O(R)$. Under the fixed range, $R$ is a constant 1,001, but retaining it in the bound explains the algorithm.

## Alternatives and edge cases

- **Mark start immediately:** Set `vis[start]=True` when enqueuing it to remove the one possible redundant revisit.
- **Depth-first search:** Does not naturally guarantee the minimum operation count and may explore long cycles.
- **Bidirectional search:** Difficult because inverse transitions, especially signed XOR interactions and terminal goals, require care.
- **Goal outside zero through one thousand:** Can be reached only as the final generated value and is checked correctly.
- **Generated out-of-range non-goal:** Discarded because no next operation is legal.
- **Repeated use of one number:** Allowed; visited state, not number usage, controls search.
- **Different paths reach the same state:** Only the first breadth-first arrival needs expansion.
- **Start equals goal outside the stated contract:** The exact source has no zero-step precheck; the contract guarantees they differ.
- **Negative input numbers:** Addition and subtraction reverse intuitive directions, but both are explicitly generated.
- **XOR result:** May be negative or large and is treated by the same terminal rule.
- **Unreachable goal:** Finite state exhaustion returns `-1`.
- **Input preservation:** Neither `nums` nor the scalar inputs are modified.
