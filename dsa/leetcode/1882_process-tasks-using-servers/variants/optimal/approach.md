## General
**Separate free and busy ordering**

Maintain an available min-heap of `(weight, index)`, exactly matching the choice rule for free servers. Maintain a busy min-heap of `(finish_time, weight, index)`. Its first field reveals the next scheduling event, while the remaining fields consistently order simultaneous releases.

**Process tasks in arrival order**

For task $j$, advance the simulated time to at least $j$ and move every server whose finish time is no later than that time into the available heap. If the available heap is nonempty, pop its best server and start the task immediately.

**Jump across a backlog**

If no server is available, jump time to the earliest busy finish. Release every server finishing then before choosing one; this is necessary because simultaneous finishers must compete by weight and index. Push the selected server back into the busy heap with finish time equal to the actual start time plus the task duration.

**Why this reproduces the queue**

Tasks are visited strictly by index, so no later arrival can pass an earlier waiting task. Before each assignment, all and only servers free at the current time have been transferred to the available heap. Its root is therefore precisely the server required by the tie rules. Each recorded assignment matches the specified event process by induction over tasks.

## Complexity detail
Each of the $N$ servers enters the available heap initially. Across $M$ tasks, every assignment performs one removal and one busy insertion, and every completion causes at most one transfer back. Heap size never exceeds $N$, giving $O((N+M)\log N)$ time. The two heaps together store $N$ servers, so auxiliary space is $O(N)$. The required output occupies $O(M)$ additional result space.

## Alternatives and edge cases
- **Scan all servers per task:** Tracking finish times in arrays is correct but selecting the best free server costs $O(NM)$ time.
- **One combined heap:** Availability time and weight have different priority orders, so a single static tuple order cannot represent both states safely.
- **Single server:** Every task receives index `0`, possibly after waiting.
- **Equal weights:** The smaller server index wins whenever both are free.
- **Simultaneous completions:** Release all servers at that time before assigning the next queued task.
- **Idle gaps:** When tasks arrive slower than completion, process each at its own arrival second.
- **Backlogged tasks:** Start time may be much larger than task index; use the simulated time, not the arrival, for the new finish time.
