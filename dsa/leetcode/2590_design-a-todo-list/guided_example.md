# Guided Example: Design a Todo List

## 1. The instance and the responses it must produce

The representative instance is the official command stream, an interleaved sequence of eleven calls on a single `TodoList` object. Two users appear: user `1`, who owns every task that is added, and user `5`, who owns nothing and therefore acts as the probe for ownership handling.

| Step | Command | Summary of the arguments | Required response |
|---|---|---|---|
| 1 | `TodoList` | none | none (construction) |
| 2 | `addTask` | user `1`, `"Task1"`, due date `50`, no tags | `1` |
| 3 | `addTask` | user `1`, `"Task2"`, due date `100`, tag `"P1"` | `2` |
| 4 | `getAllTasks` | user `1` | `["Task1", "Task2"]` |
| 5 | `getAllTasks` | user `5` | `[]` |
| 6 | `addTask` | user `1`, `"Task3"`, due date `30`, tag `"P1"` | `3` |
| 7 | `getTasksForTag` | user `1`, tag `"P1"` | `["Task3", "Task2"]` |
| 8 | `completeTask` | user `5`, task `1` | none (and no state change) |
| 9 | `completeTask` | user `1`, task `2` | none (task `2` becomes complete) |
| 10 | `getTasksForTag` | user `1`, tag `"P1"` | `["Task3"]` |
| 11 | `getAllTasks` | user `1` | `["Task3", "Task1"]` |

The stream is instructive because it forces five separate design decisions to surface: a task identifier counter that is shared by all users, a per-user store that must answer in due-date order, a tag view that must reuse that same order, an ownership rule that makes step 8 a no-op, and a completion rule whose effect is visible only through the *filters* applied by the two retrieval methods.

## 2. The state model

Every user-visible answer is a projection of one underlying record set, so the first design question is what a task record must contain and which structures index it.

| Stored fact | Why it must be stored | Where it is used |
|---|---|---|
| Task identifier | Returned by `addTask`, accepted by `completeTask` | Both the creation reply and the completion lookup |
| Owning user identifier | Tasks are partitioned per user; tag names are scoped per user | Every retrieval and every completion |
| Description | It is the value that retrieval methods return | Output of `getAllTasks` and `getTasksForTag` |
| Due date | The fixed ordering key of every retrieval | Ordering of both list methods |
| Tag set | Membership in a tag query | Filtering in `getTasksForTag` |
| Completion flag | Completed tasks must vanish from both lists but must stay identifiable | Filtering in both list methods, mutation in `completeTask` |

Three structural decisions follow from the table. The identifier counter is a **single** counter for the whole object, not per user, because the statement fixes the first task at `1`, the second at `2`, and so on over the entire call stream. The records are grouped **by user**, because every query names a user and no query ever crosses users. And each user's group is kept **ordered by due date**, because both list methods must return their answers in that order; since all due dates in an instance are unique, the due date alone determines the order and no tie-breaking rule is needed.

The counter is the only piece of state that is genuinely global. Everything else is scoped: the pending-task list, the tag membership, and the completion flag are all properties of one task belonging to one user.

## 3. Building the store: the first three additions

Steps 2, 3, and 6 add three tasks for user `1`. The counter allocates identifier `1` to the first call, `2` to the second, and `3` to the third, regardless of which user made the call.

| Step | Call | Allocated identifier | Counter afterwards | Records for user `1`, in due-date order |
|---|---|---|---|---|
| 2 | `addTask(1, "Task1", 50, [])` | `1` | `2` | `Task1` (due `50`, no tags, pending) |
| 3 | `addTask(1, "Task2", 100, ["P1"])` | `2` | `3` | `Task1` (due `50`), `Task2` (due `100`, tag `P1`) |
| 6 | `addTask(1, "Task3", 30, ["P1"])` | `3` | `4` | `Task3` (due `30`), `Task1` (due `50`), `Task2` (due `100`) |

The complete record set after step 6 is the following.

| Task id | Owner | Description | Due date | Tags | Completed |
|---|---|---|---|---|---|
| `1` | `1` | `"Task1"` | `50` | none | no |
| `2` | `1` | `"Task2"` | `100` | `P1` | no |
| `3` | `1` | `"Task3"` | `30` | `P1` | no |

Note that the insertion order and the due-date order disagree: `Task3` was created last but must be reported first. This is the reason the per-user collection is maintained in due-date order rather than in insertion order — the ordering requirement belongs to retrieval, and maintaining it incrementally is what keeps retrieval cheap. The identifier order is never used as an ordering key, which is why `Task3` can legitimately come before `Task1`.

## 4. How the two retrieval methods derive their answers

Both list methods walk the *same* per-user ordered collection and apply a filter; neither of them re-sorts anything.

`getAllTasks(1)` at step 4 filters the collection of user `1` on the completion flag alone: at that moment the collection holds `Task1` (due `50`) and `Task2` (due `100`), both pending, so the ordered result is `["Task1", "Task2"]`. At step 11 the same call sees `Task3` (due `30`), `Task1` (due `50`), and the completed `Task2` (due `100`); dropping the completed record leaves `["Task3", "Task1"]`.

`getTasksForTag(1, "P1")` applies the same completion filter and additionally requires the tag to be a member of the record's tag set. The candidate table below shows exactly which records survive each predicate.

| Task id | Description | Due date | Has tag `P1`? | Completed at step 7? | In the answer at step 7? | Completed at step 10? | In the answer at step 10? |
|---|---|---|---|---|---|---|---|
| `1` | `"Task1"` | `50` | no | no | no | no | no |
| `2` | `"Task2"` | `100` | yes | no | yes | yes | no |
| `3` | `"Task3"` | `30` | yes | no | yes | no | yes |

Both predicates are applied to every record of the user in due-date order, so the surviving records come out already ordered: `["Task3", "Task2"]` at step 7, and `["Task3"]` at step 10 once `Task2` has been completed. This is the key structural insight of the problem: the tag query is a **filter over an ordered traversal**, not a separate sorted structure. A design that stored tag groups independently would have to reproduce the same due-date ordering inside each group.

Two consequences deserve emphasis. First, a task with no tags can never satisfy a tag query, because membership in an empty set is false — the plain task `"Plain"` with no tags is invisible to every tag query while remaining visible to `getAllTasks`. Second, tags are scoped to the owning user: two users may both tag a task with `"Shared"`, and the query must still return only the caller's own task, because the traversal never leaves the named user's collection.

## 5. Ownership, unknown identifiers, and repeated completion

`completeTask` is the only mutating call, and its contract is deliberately narrow: it marks the task complete **only if** the task exists, **and** it belongs to the named user, **and** it is not already complete. Failure of any condition is silently ignored, which is why the method has no return value.

| Call at step | Task found in the caller's collection? | Record state before | Record state after | Explanation |
|---|---|---|---|---|
| 8 — `completeTask(5, 1)` | no | task `1` exists but belongs to user `1` | unchanged | User `5` has an empty collection, so the lookup finds nothing; the identifier `1` is not consulted globally |
| 9 — `completeTask(1, 2)` | yes | task `2` pending | task `2` complete | Both the owner and the identifier match, and the task was pending |
| a repeat of `completeTask(1, 2)` | yes | task `2` complete | task `2` complete | The flag is already set; overwriting it with the same value leaves the state unchanged |
| `completeTask(9, 100)` | no | nothing | unchanged | No task carries identifier `100` |

Step 8 is the discriminating case: the identifier `1` is a valid identifier, but it is resolved *within the caller's own collection*. Looking the identifier up in a global table without checking ownership would complete a stranger's task and then wrongly hide `Task1` from step 11, whose required answer still contains it. Equally, the ownership check must not be inverted into an error: a wrong owner is not a failure to report, it is a request that changes nothing.

Idempotence matters for the same reason in the other direction. Since completion is a filter applied by the retrieval methods, marking an already-complete task again cannot make it reappear, and there is no path by which a completed task becomes pending again.

## 6. The complete trace

The table below condenses the eleven steps into the state that every answer is derived from. The final column tracks user `1`'s pending tasks in due-date order, which is exactly what `getAllTasks(1)` would report at that moment.

| Step | Command summary | Response | Counter afterwards | Pending tasks of user `1` in due order |
|---|---|---|---|---|
| 1 | construct | none | `1` | none |
| 2 | add `"Task1"`, due `50`, user `1` | `1` | `2` | `Task1` |
| 3 | add `"Task2"`, due `100`, tag `P1`, user `1` | `2` | `3` | `Task1`, `Task2` |
| 4 | list user `1` | `["Task1", "Task2"]` | `3` | `Task1`, `Task2` |
| 5 | list user `5` | `[]` | `3` | `Task1`, `Task2` |
| 6 | add `"Task3"`, due `30`, tag `P1`, user `1` | `3` | `4` | `Task3`, `Task1`, `Task2` |
| 7 | tag `P1` for user `1` | `["Task3", "Task2"]` | `4` | `Task3`, `Task1`, `Task2` |
| 8 | complete task `1` as user `5` | none | `4` | `Task3`, `Task1`, `Task2` |
| 9 | complete task `2` as user `1` | none | `4` | `Task3`, `Task1` |
| 10 | tag `P1` for user `1` | `["Task3"]` | `4` | `Task3`, `Task1` |
| 11 | list user `1` | `["Task3", "Task1"]` | `4` | `Task3`, `Task1` |

Every response follows mechanically from the two columns to its right: the identifier replies read the counter, the list replies read the pending projection, the tag replies read the pending projection further filtered by tag membership, and both completion calls change only the completion flags. Step 5 returns an empty list rather than failing, because a user with no records is an ordinary case: the per-user group is simply empty.

## 7. Invariants that keep the views consistent

Four invariants hold after every command, and together they explain why no retrieval ever needs to repair or re-sort the state.

1. **The identifier counter is global, strictly increasing, and never reused.** It advances by exactly one per `addTask` call, whatever the user, so identifiers are unique across the object and the returned value is exactly the counter value at the time of the call. No user identifier, description, or due date influences it.
2. **Every record sits in exactly one user group, and that group is ordered by due date.** A record never migrates between users, and its due date never changes after creation, so the ordering established at insertion remains valid forever.
3. **Completion is monotone.** A flag only ever changes from pending to complete, never back. Therefore the set of pending tasks of a user only shrinks, and a task that disappears from a list can never reappear; filtering is safe at any moment.
4. **The ordering key and the mutable field are disjoint.** Only the completion flag is ever written after creation, and the flag is not part of the ordering key. Mutating a field that the ordering depends on would invalidate the structure's internals; mutating a field that the ordering ignores is safe, which is precisely why the visible order survives every `completeTask` call.

## 8. Boundary conditions and traps

| Situation | Instance | Required behaviour | Why it matters |
|---|---|---|---|
| Query for a user with no tasks | `getAllTasks(5)` at step 5 | `[]` | Absence of a user group is a normal empty answer, not an error |
| Completion by the wrong owner | `completeTask(5, 1)` at step 8 | no change | Resolution happens inside the caller's own collection, so a valid identifier owned by someone else is invisible |
| Identifiers increase across users | user `7` adds, then user `2` adds | `1` then `2` | The counter is object-wide, so the second user's first task is *not* identifier `1` |
| Repeated completion | complete the same task twice | second call changes nothing | Completion is idempotent and monotone |
| Completion of an unknown identifier | `completeTask(9, 100)` | no change | The lookup fails and the call is silently ignored |
| A task with no tags | `"Plain"`, no tags, then a query for tag `"A"` | `[]` from the tag query, `["Plain"]` from the list | Membership in an empty tag set is false, but the task is still pending and listed |
| Equal tag names for two users | both users tag a task `"Shared"` | each query returns only its own task | Tag names are scoped by the user traversal, so no cross-user leakage can occur |
| Ordering versus insertion order | add due `90`, then due `10`, then due `50` | `["Early", "Middle", "Late"]` | Retrieval order ignores insertion order and identifier order; only the due date matters |
| One task carrying several tags | tags `A` and `B` on one task, queries for `A` and for `B` | the same task appears in both answers | Tag filtering is a membership test, and a record may satisfy many tag queries at once |
| A completed task inside a tag group | complete one of two tasks sharing tag `"X"` | only the pending one is returned | The completion filter is applied together with, not instead of, the tag filter |
| The longest permitted description | a description of $50$ characters, the maximum | returned verbatim | Descriptions are opaque payloads; nothing sorts or compares them |

The trap worth calling out explicitly is the ordering-versus-completion interaction. Ordering by due date is a property of the *store*, while hiding completed tasks is a property of the *query*; conflating them leads to either a tag query that returns completed work, or a store whose order is destroyed by a mutation. Keeping the two concerns separate is what makes all four invariants of Section 7 simultaneously maintainable.

## 9. Why the reasoning is correct

**Every answer is a projection of the stored records.** `addTask` records one tuple and returns the counter value; the counter is advanced exactly once per call, so the identifiers `1, 2, 3, …` required by the contract are produced in order and never repeat. Each list method traverses the named user's collection, which by invariant 2 is in due-date order, keeps the records that pass its predicates, and returns their descriptions in traversal order. Since a traversal preserves the stored order and the predicates are applied record by record, the returned list is sorted by due date exactly as required.

**The filters are the right ones.** `getAllTasks` keeps a record exactly when it is not complete; `getTasksForTag` keeps a record exactly when it is not complete *and* the queried tag is one of its tags. These predicates restate the contract literally, so no task that the contract excludes can be returned, and no task the contract includes can be dropped — including tasks matched by several tags, tasks with no tags, and tasks whose description merely resembles a tag name, which is irrelevant because only set membership is tested.

**The completion call is safe under all three conditions.** If the named user owns no record with that identifier, the traversal finds nothing and the state is unchanged, which is exactly the required behaviour for a wrong owner or an unknown identifier. If the record exists and is pending, the flag is set, and by invariant 3 no later call can clear it, so the task stays out of both list results permanently. If it is already complete, writing the same value leaves the state identical, so repetition is harmless. Because the flag is excluded from the ordering key (invariant 4), none of these writes can disturb the order established by invariant 2, and the next retrieval remains correct without any reordering step.

## 10. Complexity of each operation

Let $m$ be the number of records currently held for the queried user, $k$ the number of records returned, and $t$ the number of tags supplied in one call. At most $100$ calls are made to each method and every user identifier is bounded by $100$, so these quantities stay small, but the shapes below are what make the design defensible in general.

| Operation | Dominant work | Cost |
|---|---|---|
| `addTask` | Allocate from the counter and insert the record into the user's ordered collection | $O(\log m)$ with a balanced ordered container, $O(m)$ with a plain append; plus $O(t)$ to store the tag set |
| `getAllTasks` | One ordered traversal of the user's records, filtering on the completion flag | $O(m)$ traversal plus $O(k)$ to emit the answers |
| `getTasksForTag` | The same traversal with an additional constant-time tag membership test per record | $O(m + k)$ |
| `completeTask` | Locate the record with the given identifier inside the caller's collection, then write one flag | $O(m)$ for a linear scan, or $O(\log m)$ with a secondary identifier index |
| Whole object | Records, tag sets, and the per-user grouping | $O(\text{total records} + \text{total tag entries})$ auxiliary space |

Two alternatives are worth stating. Sorting each user's records at query time instead of maintaining the order incrementally costs $O(m \log m)$ per retrieval and repeatedly re-derives an order that never changes, since due dates are immutable; maintaining the order on insertion pays a logarithmic insertion cost once and then makes every retrieval linear in the user's record count. Storing an explicit per-tag index — for each user and tag, the ordered list of matching records — makes a tag query proportional to $k$ instead of $m$, at the cost of $O(t)$ extra storage per record and of keeping the index in step with completion flags; that trade is attractive only when tag queries dominate the call stream. The single ordered per-user collection chosen here keeps insertion cheap, makes both list methods share one traversal, and needs no additional bookkeeping when a task is completed.