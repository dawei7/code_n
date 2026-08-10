## General

**Model prerequisites as a directed acyclic graph**

Each course is a vertex. Relation `[a,b]` creates a directed edge from prerequisite `a` to dependent course `b`.

The source converts one-based labels to zero-based indices, appends `b-1` to `g[a-1]`, and increments `indeg[b-1]`. The indegree records how many prerequisites of each course have not yet been topologically processed.

The graph is guaranteed acyclic, so every course can eventually enter a topological order.

**Unlimited parallelism turns the objective into a critical path**

Courses with satisfied prerequisites can run simultaneously. A dependent course cannot start until all its prerequisites finish, so its earliest start is the latest completion time among them.

Define `f[i]` as the earliest possible completion month of course `i`. For a source course with no prerequisites, it can start at month zero and finishes at `time[i]`.

For an edge from `i` to `j`, completing `j` through that prerequisite chain would take

`f[i] + time[j]`.

Because all prerequisites must be finished, `f[j]` is the maximum of this value over every incoming prerequisite.

**Initialize all immediately available courses**

The source scans `zip(indeg, time)`. Every course whose indegree is zero is placed in queue `q`, assigned `f[i]=time[i]`, and considered for global `ans`.

All such courses can begin together at month zero. The queue order among them does not affect completion times because their dependency subgraphs are handled through maxima.

**Propagate completion times in topological order**

When course `i` is removed from the queue, its `f[i]` is final: all of its prerequisites were already processed before its indegree became zero.

For every dependent `j`, the source performs

`f[j] = max(f[j], f[i] + time[j])`.

This considers the critical path reaching `j` through `i`. It then decrements `indeg[j]`. Once that indegree reaches zero, every incoming prerequisite has contributed its candidate finish time, so `f[j]` is final and `j` enters the queue.

**Why maximum, not sum, combines prerequisites**

If three prerequisite courses finish at months two, five, and seven, the dependent course can begin at month seven. The earlier two finish while the longest one is still running.

Adding all three completion times would incorrectly assume prerequisites must be taken sequentially. The unlimited-parallelism rule makes their maximum the required start time.

Course duration itself is then added once, producing finish time.

**Trace the first example**

Courses one and two have no prerequisites, so they finish at months three and two.

Both point to course three, whose duration is five. Processing course one proposes finish `3+5=8`. Processing course two proposes `2+5=7`, which does not replace the larger value.

After both incoming edges are processed, course three's indegree reaches zero with final `f[2]=8`. The answer is eight.

**Track the global completion time**

`ans` is updated for every initialized source and after every dependent relaxation. It therefore records the largest earliest finish time discovered.

Completing all courses requires waiting until the last course finishes, so the project duration is `max(f)`. Maintaining `ans` incrementally is equivalent and avoids a final scan.

**Why the schedule is achievable**

Start every indegree-zero course at month zero. Whenever a course's prerequisites have all completed, start it immediately.

The recurrence assigns each course exactly that earliest start plus its duration. Unlimited capacity means concurrently active courses never block one another. Thus all `f[i]` finish times can be realized in one schedule.

**Why no faster schedule exists**

For every directed prerequisite path ending at a course, those courses must be completed sequentially along the path. The sum of durations on that path is a lower bound on the course's finish time.

`f[i]` is the maximum duration sum among paths ending at `i`, so no schedule can finish `i` earlier. The achievable schedule meets these lower bounds, and the maximum `f` is the minimum possible time to finish everything.

**Mutation and graph guarantees**

The source decrements its newly allocated `indeg` array, not the input relations. It reads `time` without modification.

If a cycle existed, some vertices would never reach indegree zero. The problem explicitly guarantees a DAG, so no cycle-detection branch is needed.

## Complexity detail

Let $N$ be the number of courses and $M$ the number of prerequisite relations. Graph construction takes $O(N+M)$ initialization time. Kahn's process enqueues each course once and scans each directed edge once, so total time is $O(N+M)$.

The adjacency lists store $O(N+M)$ structure, while `indeg`, `f`, and the queue each use $O(N)$ space. Overall auxiliary space is $O(N+M)$.

## Alternatives and edge cases

- **Memoized DFS:** Compute the longest duration path starting or ending at each course; also $O(N+M)$ but recursion depth can be large.
- **Ordinary shortest path:** Wrong objective; prerequisites impose a longest critical path, not a shortest route.
- **Sum all prerequisite finishes:** Incorrect because prerequisites run concurrently.
- **No relations:** Every course starts at zero and the answer is the largest individual duration.
- **One course:** Its own duration is the answer.
- **Several source courses:** All are initialized and run in parallel.
- **Several prerequisites:** Their maximum finish controls the dependent start.
- **Several outgoing edges:** One completed course can unlock timing updates for many dependents.
- **Duplicate relations:** Excluded by the contract; otherwise indegree and adjacency would both duplicate consistently but unnecessarily.
- **Cycle:** Excluded by the DAG guarantee.
- **Independent components:** They execute in parallel, and the slower component determines `ans`.
- **Input preservation:** Only new graph and state arrays are mutated.
