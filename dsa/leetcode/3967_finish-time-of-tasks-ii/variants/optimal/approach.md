## General

Choosing a root gives every undirected edge a direction away from that root. A task then treats its farther neighbors as children, and its finish time is computed from those children's finish times.

For child finish values `x_1,x_2,\ldots,x_c`, define

$$
\operatorname{combine}(u;x_1,\ldots,x_c)
=
\begin{cases}
\texttt{baseTime}[u], & c=0,\\
2\max_j x_j-\min_j x_j+\texttt{baseTime}[u], & c>0.
\end{cases}
$$

The second line is exactly the statement's rule:

$$
\text{latest}
+(\text{latest}-\text{earliest})
+\texttt{baseTime}[u].
$$

A direct solution could choose each of the `n` tasks as root and recompute the whole tree, but that would take `O(n^2)` time. The source instead computes reusable information for both directions of every edge. This technique is called tree rerooting.

**The message carried along a directed edge**

For adjacent tasks `u` and `v`, imagine cutting edge `\{u,v\}`. Define the message

$$
F(u\to v)
$$

as the finish time of `u` when `v` is treated as `u`'s parent. Equivalently, `u` combines information from every neighbor except `v`.

If a candidate root is `u`, then every neighbor `v` is a child and contributes `F(v\to u)`. Once all incoming neighbor messages are known, the finish time for root `u` is simply

$$
\operatorname{combine}\bigl(u;\{F(v\to u):v\text{ adjacent to }u\}\bigr).
$$

The whole algorithm is therefore about producing both directed messages for every undirected edge without recomputing complete components.

**Building one temporary orientation**

The source first stores both directions of every edge in `graph`. It then temporarily roots the tree at task zero solely to establish parent-child order:

```python
parent = [-1] * n
parent[0] = 0
order = [0]
for task in order:
    for neighbor in graph[task]:
        if neighbor != parent[task]:
            parent[neighbor] = task
            order.append(neighbor)
```

Python's list iterator continues to see items appended during this loop. Consequently, `order` grows until it contains every task. A parent is appended before any of its children.

Checking only `neighbor != parent[task]` is sufficient because the input is a tree. After excluding the one edge back to the parent, every remaining edge leads to an unvisited child; there are no cycles or cross edges.

Assigning `parent[0]=0` gives the temporary root a harmless self-marker. Task zero is not its own graph neighbor because tree edges connect distinct tasks.

**Bottom-up messages from child side to parent side**

The array `downward` stores messages following the temporary orientation. For a non-root task `u`,

$$
\texttt{downward}[u]=F(u\to\texttt{parent}[u]).
$$

Since parents precede children in `order`, traversing `reversed(order)` processes every child before its parent. The source gathers `downward` values only from neighbors whose recorded parent is the current task.

If there are no such children, `u` is a leaf in the temporary orientation, so its message is `baseTime[u]`. Otherwise, applying the combine rule to the child messages gives

```python
downward[task] = (
    2 * max(child_values)
    - min(child_values)
    + baseTime[task]
)
```

This completes every message directed from a node toward its temporary parent. It also computes a value for task zero using all its temporary children, although zero has no parent that needs that particular message.

**Top-down messages provide the missing direction**

For a non-root task `u`, `upward[u]` stores the message coming from the parent side:

$$
\texttt{upward}[u]
=
F(\texttt{parent}[u]\to u).
$$

The second pass processes `order` forward, so a parent's upward-side information is ready before messages are sent to its children.

At a task `u`, the source creates `incoming` in exactly the same order as `graph[u]`:

- for the neighbor equal to `parent[u]`, use `upward[u]`;
- for a temporary child `v`, use `downward[v]`.

Thus each entry corresponding to neighbor `v` is exactly `F(v\to u)`. These are the finish times that `u` would see if `u` itself were selected as the root.

For temporary root zero, no graph neighbor equals `parent[0]=0`, so every entry correctly comes from a child's `downward` value.

**Evaluating the current task as root**

If `incoming` is empty, the tree has one task and its root finish is `baseTime[task]`. Otherwise, the source finds the minimum and maximum incoming messages and computes

```python
root_finish = 2 * maximum - minimum + baseTime[task]
```

This is the complete finish time for choosing the current task as root. The algorithm compares it with `answer`, so after the pass `answer` is the minimum over all `n` possible roots.

**Producing an outgoing message without rescanning neighbors**

To send a message from `u` to one temporary child `v`, task `u` must treat `v` as its parent. It must therefore combine the incoming messages from every neighbor except `v`:

$$
F(u\to v)
=
\operatorname{combine}
\bigl(u;\{F(w\to u):w\ne v\}\bigr).
$$

If `u` has only that one neighbor, removing `v` leaves no children. The outgoing value is simply `baseTime[u]`. This is the source's `len(incoming) == 1` branch.

For a larger neighbor set, the combine formula needs only the minimum and maximum after one selected value is excluded. Rescanning all other neighbors for every child would cost quadratic time at a high-degree node. The source instead finds:

- the smallest and second-smallest incoming values;
- the largest and second-largest incoming values.

These four order statistics are stored in the exact variables `minimum`, `second_minimum`, `maximum`, and `second_maximum`. The “second” variables mean the next occurrence in sorted order, not necessarily a different numerical value.

When excluding a value:

- if it equals the current minimum, use the second minimum; otherwise keep the minimum;
- if it equals the current maximum, use the second maximum; otherwise keep the maximum.

The resulting extrema are substituted into the combine formula and stored as `upward[v]`. Because the current task is processed before `v`, this message is ready when the forward pass later reaches `v`.

**Why ties are handled correctly**

The extrema loop uses a strict comparison followed by an `elif`. If two incoming messages both equal the minimum, the first becomes `minimum` and the second becomes `second_minimum` with the same value. Excluding either minimum therefore leaves the other equal copy available.

The same behavior holds for duplicate maxima. This matters because the exclusion code compares values rather than remembering one distinguished index. With duplicates, the second order statistic equals the first, which is exactly the correct remaining extreme.

For two unequal incoming values `a<b`:

- excluding `a` leaves both new minimum and maximum equal to `b`;
- excluding `b` leaves both equal to `a`.

The tracked second extrema produce these results as well.

**Why every candidate root receives complete information**

The bottom-up pass computes all messages pointing from a temporary child toward its parent. The top-down pass computes the reverse message for each edge by using every already-known incoming message except the destination child's message.

Inductively, when task `u` is reached in the top-down order, `upward[u]` summarizes the entire component on the other side of its parent edge, and every `downward[v]` summarizes the component below each temporary child `v`. These components partition all tasks other than `u`.

Therefore `incoming` contains exactly one complete child-component finish time for every neighbor under the rooting at `u`. Applying the given formula evaluates that rooting exactly. Since every task appears once in `order`, every legal choice of root is evaluated once, and the minimum retained in `answer` is the requested result.

**A three-task path as messages**

For path `0-1-2`, the temporary root is zero. The downward pass first gives task two its base time, then computes `F(1\to0)` from task two, and finally computes zero's temporary-root value.

During the top-down pass, zero computes `F(0\to1)`. At task one, `incoming` now contains both `F(0\to1)` and `F(2\to1)`. Combining both evaluates task one as root. Excluding the task-two entry produces `F(1\to2)`, which lets task two later be evaluated as root. No subtree is recursively recomputed for a new root.

## Complexity detail

Let `n` be the number of tasks. A tree has `n-1` edges, so the undirected adjacency lists contain `2(n-1)` neighbor entries.

Building `graph`, `parent`, and `order` takes `O(n)` time. The reversed pass scans each adjacency list to collect temporary children; summed across all tasks, this is `O(n)`.

In the forward pass, each task performs a constant number of scans over its own neighbors: one to form `incoming`, one to compute the first and second extrema, and one to create messages for temporary children. Although a single high-degree task can cost `O(n)`, the sum of all degrees is `2(n-1)`, so all these scans together remain `O(n)`.

Total time complexity is therefore `O(n)`. This improves on evaluating each root separately, which can require `O(n^2)` total work.

The adjacency lists, parent array, traversal order, downward array, and upward array each use `O(n)` space. The transient `child_values` and `incoming` lists for one task use at most `O(n)` at a time and are discarded before moving far beyond that task. Total auxiliary space is `O(n)`.

The implementation is iterative and therefore does not consume `O(n)` interpreter call-stack frames on a chain. This is important for the declared `n\le10^5` constraint.

The method does not change `edges` or `baseTime`. All orientation and message state is stored in new arrays.

## Alternatives and edge cases

- **Recompute from every root:** Running a complete postorder evaluation `n` times is easy to conceptualize but costs `O(n^2)` in the worst case. Directed edge messages reuse the unchanged component results.

- **Recursive rerooting:** Two recursive DFS passes can express the same message equations, but a chain of length `10^5` can exceed Python's recursion limit. The stored iterative order avoids that failure mode.

- **Rescan all other neighbors for every child:** At a star center, excluding each child and scanning the remaining `O(n)` messages would make that one node cost `O(n^2)`. First and second extrema make every exclusion constant time after one scan.

- **Prefix and suffix extrema:** Arrays of prefix/suffix minima and maxima can also support exclusions in constant time. They require additional per-node arrays; keeping two extrema is sufficient because only one value is removed.

- **Use only downward values:** That evaluates root zero correctly but omits the component above a task when considering another root. `upward` supplies precisely that missing side.

- **One task:** There are no incoming messages. The only possible root is a leaf, so the answer is `baseTime[0]`.

- **One neighbor after rerooting:** Excluding that neighbor leaves a node with no children, so its outgoing message must be its base time. Using infinite extrema here would be invalid; the source has an explicit branch.

- **A chain:** Every internal node has at most two incoming messages. The algorithm remains linear and iterative, regardless of chain length.

- **A star:** The center has many neighbors, but its list is scanned only a constant number of times. Leaves use the degree-one branch when sending back toward the center.

- **Equal incoming minima or maxima:** The second-extreme update records duplicate occurrences. Excluding one tied extreme correctly leaves the same numerical extreme.

- **Negative infinity initialization:** `float("-inf")` and positive infinity are only sentinels while scanning a nonempty list. Actual integer values replace them before arithmetic.

- **Index alignment:** `incoming` is constructed by iterating `graph[task]` in order, and the child-message loop enumerates that same list. Therefore `incoming[index]` always belongs to the neighbor being considered.

- **Temporary root marker:** `parent[0]=0` does not create an artificial incoming parent value because task zero cannot be adjacent to itself in a valid tree.

- **Appending during list iteration:** Python's list iterator observes appended tasks, so `for task in order` traverses the growing list. Replacing `order` with an iterator type that does not expose appended elements would change this behavior.

- **Arbitrary edge input order:** Adjacency-list order affects only traversal order, not any minimum, maximum, message value, or final answer.

- **Integer growth:** Python integers preserve exact arithmetic for the recurrence. No floating-point operation is applied to actual finish values; infinities are comparison sentinels only.
