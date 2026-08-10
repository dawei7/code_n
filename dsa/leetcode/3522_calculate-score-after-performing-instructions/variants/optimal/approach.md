## General

**There is only one execution path**

At any in-bounds instruction index `i`, the next state is completely determined:

- `"add"` changes the score by `values[i]` and moves to `i + 1`;
- `"jump"` leaves the score unchanged and moves to `i + values[i]`.

There is no choice, branching search, or optimization decision. The correct method is to simulate this one path until one of the two stopping conditions occurs.

The only complication is that jumps can move backward or stay in place, so execution may enter a cycle. The process must stop before executing an index for a second time.

**Track whether each instruction has already executed**

The source allocates:

`vis = [False] * n`.

`vis[i]` means instruction index `i` has already been executed. A boolean array is appropriate because valid indices are the dense range zero through `n - 1`.

The loop condition is:

`0 <= i < n and not vis[i]`.

Python evaluates the left side first and short-circuits. Thus `vis[i]` is accessed only when `i` is in bounds. The loop stops safely for both a negative jump target and a target at or beyond `n`.

It also stops when `vis[i]` is already true. Since the body is not entered, the revisited instruction is not executed again, exactly matching the specification.

**Mark before applying the instruction**

At the start of each loop body, the source performs:

`vis[i] = True`.

Only then does it update the score or instruction pointer. Marking before movement is important for a self-jump. If `instructions[0] = "jump"` and `values[0] = 0`, execution stays at index zero. On the next condition check, `vis[0]` is true, so the process ends. If marking were delayed until after reaching a different index, this case could loop forever.

More generally, every executed index is recorded before any transition that may eventually return to it.

**Execute add instructions**

The source identifies an add operation with:

`instructions[i][0] == "a"`.

The contract guarantees that every instruction is exactly either `"add"` or `"jump"`, whose first letters differ. Under that guarantee, checking the first character is equivalent to comparing the whole string.

For add, it performs:

`ans += values[i]`

and then:

`i += 1`.

Values may be negative, so an add instruction can lower the score. The source uses ordinary signed addition and makes no incorrect assumption that score is monotone.

**Execute jump instructions**

If the first character is not `"a"`, the guaranteed alternative is `"jump"`. The score is unchanged, and:

`i = i + values[i]`.

The offset may be positive, negative, or zero. The new position is not clamped. If it is out of range, the next loop check terminates; if it is a previously executed valid index, that same check terminates before re-execution.

**Loop invariant and correctness**

Before each loop-condition test:

- `ans` equals the sum of `values[j]` over exactly the executed indices `j` whose instruction was add;
- `vis[j]` is true exactly for indices executed so far;
- `i` is the next instruction the process rules say to attempt.

These statements hold initially: no instruction is visited, score is zero, and index zero is next.

If `i` is invalid, the specified out-of-bounds stop condition holds and the invariant shows `ans` is the final score. If `vis[i]` is true, the attempted instruction is a revisit; the loop stops before executing it, again leaving the correct final score.

Otherwise, the body marks the newly executed index. The add branch changes score and advances exactly as specified; the jump branch changes only the index by the given offset. Thus the invariant is restored for the next test.

When the loop ends, it does so for exactly one of the required reasons, and `ans` includes every add instruction executed once and no revisited instruction. Returning `ans` is therefore correct.

**Why termination is guaranteed**

Each loop iteration marks one previously unvisited in-bounds index. There are only `n` indices. Therefore the body can execute at most `n` times. If execution has not gone out of bounds by then, the deterministic path must attempt a marked index and stop.

This finite-state argument means no separate cycle-finding algorithm is required; the visited array both detects the stop and bounds the work.

**Metadata wording versus exact source**

The Optimal manifest summary says the implementation records executed indices “in a hash set.” The protected source actually uses a boolean list. Both support membership tracking, but their mechanics and space constants differ. The dense boolean array gives direct indexed access and is the exact structure documented here.

## Complexity detail

Let `n` be the instruction count. Each valid index enters the loop at most once because it is marked on entry and any revisit stops before the body. Every iteration performs constant work: a few comparisons, one boolean assignment, one instruction check, and one arithmetic transition. Total time is `O(n)` in the worst case.

The `vis` list contains `n` booleans, so auxiliary space is `O(n)`. All other variables are scalars.

The score can have magnitude up to roughly `n \cdot 10^5`, or `10^10` under the constraints. Python integers are safe. A fixed-width implementation should use a 64-bit score even though indices and individual values fit in 32 bits.

The actual path may stop much earlier than `n`, but the source allocates the full visited array immediately. Its worst-case and allocated-space bounds remain linear.

## Alternatives and edge cases

- **Hash set of visited indices:** This matches the manifest wording and can store only reached indices. A boolean list is faster and simpler for the dense known index range, though it always allocates `O(n)` space.
- **Floyd cycle detection:** Two pointers could detect cycles with constant memory, but score accumulation and the rule to stop at the first repeated execution make bookkeeping more awkward. The direct visited array is clearer.
- **Recursive simulation:** It risks recursion-depth failure for a path of length `10^5` and provides no benefit over the loop.
- **Execute before checking visited:** That would incorrectly apply a revisited add instruction one extra time. The loop condition must reject the index first.
- **Mark after moving:** A zero jump could repeat forever. Mark the current instruction before computing its successor.
- **Jump to n:** Index `n` is out of bounds, so execution stops without indexing either input array there.
- **Jump below zero:** Negative indices must be treated as out of bounds rather than Python-style indexing from the end; the explicit `0 <= i` condition prevents accidental negative indexing.
- **Zero jump:** The current index becomes the next attempted index, is recognized as visited, and is not executed twice.
- **Backward cycle of several indices:** Every member executes once; the first attempted repeat ends the process.
- **Negative add value:** It decreases `ans` and then moves to the next index. Scores need not be nonnegative.
- **Add at the last index:** The value is included, then `i` becomes `n` and the process stops.
- **First instruction exits immediately:** A jump outside the array returns the initial score zero after executing only that jump.
- **Instruction string test:** Checking the first letter is safe only because the contract restricts values to `"add"` and `"jump"`.
- **Equal array lengths:** The source takes `n = len(values)` and indexes `instructions` with the same `i`. Correctness relies on the guaranteed equal sizes.
- **No mutation:** The source changes neither input array; all execution state lives in `i`, `ans`, and `vis`.
