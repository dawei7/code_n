## General

**Simulate gifts in their natural order**

Gift number `i + 1` is intended for person `i % num_people` when turns are zero-indexed. The modulo operation wraps from the last person back to the first without needing a separate round counter.

`ans` starts with one zero per person, and `i` starts at zero. During each loop, the current person receives `min(candies, i + 1)`. If enough candies remain, this is the full scheduled gift. Otherwise it is every remaining candy, which implements the special final partial gift.

The same amount is subtracted from `candies`, then `i` advances. Because at least one candy is removed whenever the loop runs, the remaining amount strictly decreases and the loop terminates at zero.

**Why modulo assigns the right person**

For turns zero through `num_people - 1`, the remainder equals the turn index, so people receive gifts one through `num_people` in order. On the next turn, the remainder returns to zero and the scheduled amount is `num_people + 1`. Every later block behaves the same way.

Thus the expression simultaneously represents row position and repeated rounds. A person may receive several gifts, and `+=` accumulates them in that person’s final total.

**Handle the last gift without a special branch**

Suppose the next scheduled amount is seven but only three candies remain. `min` returns three, adds all three to the correct person, and subtraction makes `candies` zero. The loop then ends. No following person receives anything, exactly matching the statement.

Calling `min` twice produces the same amount because `candies` is not changed between the addition and subtraction. Storing it in a local variable would avoid repeated evaluation but would not change behavior.

**Why the distribution is correct**

Before each iteration, `i` is the number of gifts already processed and `candies` is the unallocated remainder. The code chooses the required recipient for turn `i` and gives the smaller of the scheduled amount and all remaining candies. This is exactly the next rule in the process. Subtraction and increment restore the same statement for the next turn.

When no candies remain, every original candy has been added once to exactly one answer slot. Therefore, the answer sum equals the original amount and every person’s entry matches the prescribed sequence.

The loop also preserves nonnegativity. The chosen gift never exceeds the remaining supply, so subtraction cannot make `candies` negative. Every answer entry starts at zero and only receives nonnegative additions. These facts make the final array a valid distribution in addition to following the required recipient order.

## Complexity detail

Let $C$ be the initial candy count and $P$ the number of people. If $T$ full or partial gifts are made, the loop takes $O(T)$ time. Scheduled full gifts grow as one, two, three, and so on, whose first $T$ terms total $T(T+1)/2$. Therefore $T = O(\sqrt{C})$, and the exact protected simulation takes $O(\sqrt{C})$ time.

Creating the result array takes $O(P)$ time and space. The exact total time is $O(P+\sqrt{C})$ and output space is $O(P)$, with $O(1)$ additional scalar space beyond the returned array.

The package manifest records $O(P)$ time, which corresponds to a closed-form arithmetic solution that computes complete rounds and the final partial round per person. The shown simulation does not achieve that bound when $C$ grows independently of $P$, though at $C \le 10^9$ it performs only on the order of tens of thousands of iterations.

## Alternatives and edge cases

- **Closed-form complete rounds:** Solve the triangular-number inequality to find how many gifts are fully paid, then use arithmetic-series formulas for each person and distribute the remaining candies. This can achieve the manifest’s $O(P)$ time.
- **Binary-search the number of full gifts:** Find the greatest $T$ with $T(T+1)/2 \le C$, compute per-person progressions, and place the remainder. This avoids floating-point square-root concerns.
- **Round-by-round nested loops:** Iterate people inside rounds and stop on exhaustion. It is equivalent but requires more bookkeeping than a single turn index with modulo.
- **Fewer candies than people:** The first few people receive increasing gifts until a partial gift consumes the remainder; later entries stay zero.
- **Exactly a triangular number:** The final full scheduled gift consumes the last candies, and no partial gift occurs.
- **One person:** Every gift wraps to index zero, so the sole answer entry becomes the entire original candy count.
- **Partial final gift:** `min` ensures it never exceeds the scheduled amount or remaining supply.
- **Large candy count:** The simulation is far smaller than $C$ iterations because gifts increase, but it is still not strictly $O(P)$.
- **Answer sum:** Each subtraction has an equal addition to one slot, preserving the total until the remainder reaches zero.
- **Positive inputs:** Both candy count and people count are at least one, so modulo is valid and the loop initially runs.
