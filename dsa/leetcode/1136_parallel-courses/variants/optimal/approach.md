## General

**Turn the prerequisite rules into a directed graph**

Each course is a vertex. A relation `[prev, next]` is a directed edge from `prev` to `next` because completing `prev` is a condition for taking `next`. The important value for a course is its *indegree*: the number of prerequisite edges currently pointing into it. An indegree of zero means that none of its prerequisites remain unfinished, so the course is available in the next semester.

The solution stores outgoing edges in `g`. For every relation, it converts the one-based course labels to zero-based indices, appends `nxt` to `g[prev]`, and increments `indeg[nxt]`. The queue is then initialized with every course whose indegree is zero. Those courses have no prerequisites at all, so they are exactly the courses that can be taken in semester one.

**Why taking every available course is always optimal**

There is no upper bound on the number of courses taken in one semester. Therefore, postponing an available course cannot create any advantage. Taking it now does not compete for a limited seat, time slot, or course allowance. On the other hand, postponing it may postpone every course that depends on it. Consequently, an optimal schedule may take all currently available courses together.

This observation turns Kahn's topological-sort algorithm into a semester simulation. One queue layer represents one semester. At the start of the `while q` iteration, every course already in `q` is eligible for the semester about to begin. The code increments `ans` once, records the layer size through `range(len(q))`, and removes exactly that many courses.

Capturing the queue length is essential. While a course is processed, each outgoing edge is removed conceptually by decrementing the destination's indegree. If that indegree becomes zero, the destination is appended to the queue. It cannot be taken in the current semester because one of its prerequisites was completed only during this semester, whereas the contract requires prerequisites to have been taken in a previous semester. Since the loop processes only the queue's original length, newly appended courses remain for the following `while` iteration and therefore for the following semester.

**What the mutable counter means**

The parameter `n` initially holds the total number of courses. The solution reuses it as a count of courses not yet processed. Whenever a course is removed from the queue, `n -= 1` marks that course as completed. This mutation does not affect the graph indices or any loop bound; after graph construction, the original total is no longer needed. At the end, `n == 0` means every course appeared in some valid semester. A positive value means some courses were never eligible.

**Why an unfinished course proves a cycle**

Suppose the queue becomes empty while `n` is still positive. Every remaining course has positive indegree within the remaining graph. Starting from any such course and repeatedly following one of its remaining prerequisite dependencies must eventually revisit a course because only finitely many courses remain. That repetition is a directed cycle. Every course on the cycle waits for another course on the same cycle, so no course in that cycle can ever become available. Courses downstream of the cycle may also remain blocked. Returning `-1` is therefore necessary.

Conversely, if the graph has no directed cycle, every nonempty remaining subgraph has at least one zero-indegree vertex. Thus the queue cannot become permanently empty before all courses are processed. The algorithm will remove every course and return the number of layers.

**Why the returned semester count is minimal**

Consider the queue at the beginning of semester `s`. By construction, it contains precisely the uncompleted courses whose prerequisites were all removed in earlier layers. Every one of them is legally available, so the algorithm takes all of them. Any legal schedule must delay a course until all of its prerequisites have been taken in earlier semesters; it cannot place a course in a layer earlier than the layer assigned by this dependency process.

This can also be viewed through prerequisite chains. Along a chain of `k` courses, each course must occupy a later semester than the preceding course, so at least `k` semesters are required. Layered Kahn processing assigns each course to the earliest semester permitted by all incoming dependencies. Its last occupied layer therefore matches the length of the longest prerequisite chain in an acyclic graph. No legal schedule can use fewer layers, and the constructed schedule uses exactly that many.

For the first example, courses `1` and `2` begin with indegree zero and form the first queue layer. Processing both removes the two incoming edges of course `3`. Course `3` becomes zero-indegree only after those removals, is left in the queue for the next layer, and is taken in semester two. In the cyclic example, every course begins with positive indegree, so the initial queue is empty, no course is processed, and the remaining count correctly causes `-1` to be returned.

## Complexity detail

Let `n` denote the number of courses and let `r` denote `len(relations)`.

Building `g` and `indeg` examines each relation once, taking `O(r)` time. Initializing the indegree array and scanning it to seed the queue take `O(n)` time. During the breadth-first traversal, each course enters and leaves the queue at most once. Each directed edge is examined exactly once when its source course is processed, and its destination indegree is decremented once. The total time is therefore `O(n + r)`. Grouping vertices into semester layers does not multiply this cost: all layer iterations together still process only `n` vertices and `r` edges.

The adjacency lists hold one entry per relation and up to one list per course that has outgoing edges. The indegree array holds `n` integers, and the queue can hold at most `n` course indices. The total auxiliary space is `O(n + r)`.

The code changes the local variable `n`, but that is constant-sized bookkeeping and does not add another linear structure. The returned integer `ans` also occupies constant space.

## Alternatives and edge cases

- **Depth-first search with three visitation states:** A DFS can detect a cycle and memoize the longest path beginning at every course, also achieving `O(n + r)` time and space. It is a valid optimal alternative, but the layered breadth-first method maps semesters directly to queue layers and avoids recursion-depth concerns for as many as 5,000 courses.
- **Repeatedly scan all courses for newly available ones:** This can simulate semesters without a queue, but rescanning every course after each layer can require quadratic time on a long prerequisite chain. Maintaining indegrees and a queue records exactly what changed.
- **Take only one available course per semester:** That is legal but not generally minimal. Because there is no per-semester course limit, all eligible courses should be taken together.
- **No initial zero-indegree course:** With at least one course, this means every course has a remaining prerequisite. The graph contains a directed cycle, the loop never starts, and the result must be `-1`.
- **A cycle in only one component:** Other components may be processed completely, but the courses in or below the cyclic component remain unprocessed. Checking the final remaining count catches this case even when the initial queue was nonempty.
- **Several prerequisites for one course:** The course is appended only when the last incoming edge is removed. Earlier decrements leave a positive indegree, so it cannot be scheduled prematurely.
- **Several outgoing relations from one course:** Processing that course decrements every dependent course independently. Any of them whose final prerequisite has now been completed becomes eligible for the next layer.
- **Independent courses:** Every course begins in the queue, all are processed in the first layer, and the answer is `1`.
- **A single long chain:** Exactly one course becomes available per layer. The algorithm returns `n`, which is unavoidable because every course after the first depends on a course from the preceding layer.
- **Unique relations:** The input guarantee prevents duplicate edges from artificially inflating indegrees. The implementation relies on the relations representing distinct prerequisite requirements.
