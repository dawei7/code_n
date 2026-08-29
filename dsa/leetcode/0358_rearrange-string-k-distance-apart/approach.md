## General

Placing a character at output index $p$ makes that character unavailable until index $p+k$. The solution therefore treats rearrangement as a scheduling problem with two groups:

- A max-heap `pq` contains characters eligible to be placed now, prioritized by greatest remaining frequency.
- A FIFO deque `q` contains recently used characters still passing through their cooldown period.

At each position, the algorithm schedules the most frequent eligible character, decreases its remaining count, and places its record into cooldown. When a record has waited long enough, it returns to the heap if more copies remain.

**Why frequency determines priority.**

High-frequency characters are the hardest to separate. Each copy after the first needs enough other positions between it and the preceding copy. If scarce separator characters are consumed while a frequent character remains unscheduled, the final copies may become impossible to place.

Choosing the eligible character with the greatest remaining count handles the most constrained work first. A less frequent eligible character has no greater future placement pressure. Swapping it later with the more frequent choice does not create an advantage: both are legal now, while delaying the character with more copies can only leave at least as much repeated work for fewer remaining positions.

The heap implements a max-priority rule using Python's min-heap. Each entry is `(-remaining_count, character)`. A larger remaining count produces a more negative number, which is popped first. When counts tie, tuple comparison uses the character as a deterministic secondary key. That lexicographic tie-break affects which valid answer is produced, not whether the distance rule is satisfied.

**Building the initial eligible heap.**

`Counter(s)` records how many copies of every distinct lowercase letter are required. The list comprehension converts each `(character, count)` pair to `(-count, character)`, and `heapify` creates the priority queue. Initially every character is eligible because nothing has yet been placed.

`ans` stores output characters in order. The deque starts empty because no character is cooling down.

**One scheduling iteration.**

The loop runs while at least one character is eligible in the heap. It pops `(v, c)`, appends `c` to the answer, and appends `(v + 1, c)` to the cooldown queue.

Because `v` is the negative remaining count before use, adding one consumes one copy. For example, a count of three is stored as `-3`; after placing one copy, the record becomes `-2`, meaning two remain. A value of zero means all copies have been scheduled.

The record enters the queue even when its new count is zero. This is intentional in the exact implementation: queue length represents how many output positions have elapsed, so every placed character contributes one chronological slot. An exhausted record will later leave the queue but will not return to the heap.

**Why queue length enforces the exact distance.**

After adding the newly used record, the source checks `len(q) >= k`. If true, it removes the oldest record. If that record has a nonzero remaining count, it is pushed back into the eligible heap.

Suppose a character was placed at index $p$. Immediately after that placement, it is the newest queue entry. After the algorithm places through index $p+k-1$, there have been $k$ queue entries from positions $p$ through $p+k-1$; the old record is released at the end of that iteration. It becomes eligible for the next iteration, whose index is $p+k$. Thus two placements of that character differ by at least $k$.

Release occurs after choosing the current position, not before. This ordering prevents a character from reappearing at index $p+k-1$, whose distance would be only $k-1$.

**What happens when no eligible character exists.**

The loop condition is `while pq`, so it stops when the heap becomes empty. There are two possibilities.

If every character occurrence has been placed, `len(ans) == len(s)` and joining `ans` returns a valid rearrangement. The queue may still contain exhausted records, but they require no further action.

If the answer is shorter than the input, some cooldown record has a nonzero remaining count but no different eligible character is available to fill the current gap. The algorithm cannot insert idle positions because the output must be a permutation of `s`, so construction is impossible. The final length comparison returns `""`.

For `s = "aaabc"` and `k = 3`, the algorithm can begin with `a`, then use `b` and `c`, and release `a` after the required gap. After placing the second `a`, however, no other characters remain to occupy two more intervening positions before the final `a`. The heap empties with the answer incomplete, so the method correctly returns an empty string.

**A successful trace.**

For `s = "aabbcc"` and `k = 3`, all three counts tie. The heap chooses `a`, then `b`, then `c`. After `c` is placed, the first `a` record has spent three positions in the queue and returns to the heap. Subsequent releases make `b` and `c` eligible in turn, producing `abcabc`. Equal letters occur at indices separated by three.

**Why the greedy schedule is complete.**

The heap always contains exactly the characters whose previous placements are at least $k$ positions behind, while the queue contains those that are temporarily forbidden. Therefore every appended character is legal.

Among legal choices, selecting a maximum remaining frequency never gives a less urgent character priority over a more urgent one. Consider any feasible completion that chooses another eligible character first. The maximum-frequency character can be moved to that earlier position, and the displaced character can occupy the later position where the maximum-frequency character first appeared; both were eligible at the earlier point, and the character with fewer remaining copies does not acquire a tighter spacing burden from being delayed. Repeating this exchange aligns a feasible schedule with the greedy choice. Thus if a completion exists, the greedy process can continue to a full-length answer. If it stalls, no eligible separator exists for the remaining cooldown copies, so no permutation can fill the next position legally.

The final answer uses exactly the original frequencies because one counter unit is consumed on every append and no character is invented or discarded. Combined with the cooldown guarantee, a full-length result satisfies the contract.

## Complexity detail

Let $n$ be the string length and let $a$ be the number of distinct characters. Here $a\le26$.

Counting takes $O(n)$ time, building and heapifying $a$ entries takes $O(a)$ time, and each scheduled character causes one heap pop plus at most one later heap push. Those operations cost $O(\log a)$ each. The general running-time bound is $O(n\log a)$. Since the alphabet is fixed to 26 lowercase letters, $\log a$ is a constant and the bound simplifies to $O(n)$, matching the manifest.

The counter and heap each contain at most $a$ entries. A character cannot have two live cooldown records because it cannot be selected again before its earlier record is released. The queue consequently contains at most $a$ records and also at most $k$ chronological records, for $O(\min(a,k))$ space. Auxiliary storage excluding output is $O(a)$, which is $O(1)$ for the fixed alphabet. The answer list and final string require $O(n)$ output space.

The heap's character tie-break makes results deterministic for the same Python behavior, but the problem accepts any valid ordering and the complexity does not depend on which tied character is chosen.

## Alternatives and edge cases

- **Repeatedly scan all 26 counts:** At every position, choose the most frequent character whose next-allowed index has arrived. This costs $O(26n)=O(n)$ under the fixed alphabet and may be simpler than a heap, though less general for large alphabets.

- **Sort counts once without updates:** This is insufficient because remaining frequencies and eligibility change after every placement. The priority structure must reflect those changes.

- **Segment construction by maximum frequency:** Distribute the most frequent letters among frequency-sized segments and verify that all but the last reach length `k`. This can run in linear time but requires careful handling of ties and segment filling.

- **`k = 0`:** There is no separation restriction. The source enqueues and immediately releases each used record because `len(q) >= 0`, allowing any frequency-prioritized permutation.

- **`k = 1`:** Equal characters may be adjacent because their index distance is one. Immediate release after each placement correctly permits this.

- **`k` larger than the string length:** Any repeated character makes completion impossible because there are not enough positions for a second copy at the required distance. A string of all distinct characters remains valid.

- **One distinct character:** It succeeds for `k <= 1`. For larger `k` and more than one copy, the heap empties while copies remain cooling down, yielding `""`.

- **Exhausted cooldown entries:** They still occupy their chronological queue slot but are discarded when released because their stored count is zero.

- **Output order:** Lexicographic heap tie-breaking may produce a different answer from the examples. Correctness depends only on character multiplicities and distances, not on matching an example string.

- **No idle placeholders:** When the heap is empty, the algorithm cannot wait for cooldown by adding blank positions; the result must contain exactly the input characters. An incomplete schedule is therefore genuinely impossible.
