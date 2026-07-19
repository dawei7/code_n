## General
**Earliest finish as a DAG recurrence**

For each course `v`, its earliest start is the latest finish among all its prerequisites. Therefore its earliest finish equals its own duration plus that maximum; a course without prerequisites simply finishes after its own duration. This is a longest-path dynamic program on a DAG, where course durations are vertex weights.

**Processing prerequisites before dependents**

Build outgoing adjacency lists and indegrees. Initialize each course's finish value to its own duration and enqueue all zero-indegree courses. When a processed course reaches a dependent, use its finish time to improve the dependent's candidate finish, then decrement the dependent's indegree. An indegree of zero proves every prerequisite contribution has arrived, so the dependent can safely enter the queue.

Every feasible schedule must wait for the longest prerequisite chain ending at each course. Conversely, starting each course at the maximum prerequisite finish realizes exactly the computed time because unlimited parallel work is allowed. The maximum finish over all courses is thus both a lower bound on any schedule and an achievable completion time.

## Complexity detail
Each of the $n$ courses enters the queue once, and each of the $m$ relations is examined once, giving $O(n+m)$ time. The adjacency lists, indegrees, finish values, and queue use $O(n+m)$ space.

## Alternatives and edge cases
- **Memoized depth-first search:** Computing the longest path from prerequisites gives the same bound, but a long chain risks recursion-depth failure in Python.
- **Repeated edge relaxation:** Relaxing every relation until no value changes is correct for a DAG but may require $O(nm)$ time when edges are ordered against a long chain.
- With no prerequisite relations, every course starts immediately and the answer is `max(time)`, not the sum.
- Multiple prerequisites require the maximum of their finish times because they run in parallel; their durations are not added together.
- Course labels are one-based, whereas `time` and the implementation's graph arrays are zero-based.
