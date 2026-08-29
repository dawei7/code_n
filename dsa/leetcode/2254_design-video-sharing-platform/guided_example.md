# Guided Example: Design Video Sharing Platform

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"operations": ["VideoSharingPlatform", "upload", "upload", "remove", "remove", "upload", "watch", "watch", "like", "dislike", "dislike", "getLikesAndDislikes", "getViews"], "arguments": [[], ["123"], ["456"], [4], [0], ["789"], [1, 0, 5], [1, 0, 1], [1], [1], [1], [1], [1]]}`
- **Required output:** `[null, 0, 1, null, null, 0, "456", "45", null, null, null, [1, 2], 2]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You have a video sharing platform where users can upload and delete videos. Each `video` is a **string** of digits, where the $i^{\text{th}}$ digit of the string represents the content of the video at minute `i`. For example, the first digit represents the content at minute `0` in the video, the second digit represents the content at minute `1` in the video, and so on. Viewers of videos can also like and dislike videos. Internally, the platform keeps track of the **number of views, likes, and dislikes** on each video.

The objective is to compute `[null, 0, 1, null, null, 0, "456", "45", null, null, null, [1, 2], 2]` from `{"operations": ["VideoSharingPlatform", "upload", "upload", "remove", "remove", "upload", "watch", "watch", "like", "dislike", "dislike", "getLikesAndDislikes", "getViews"], "arguments": [[], ["123"], ["456"], [4], [0], ["789"], [1, 0, 5], [1, 0, 1], [1], [1], [1], [1], [1]]}` while avoiding redundant calculations and unnecessary overhead.

A naive or brute-force exploration risks evaluating infeasible states or repeating subproblem computations. The optimal method establishes a clear invariant that advances deterministically toward the goal.

---

## 2. Conceptual Foundation & Invariants

We maintain the core conceptual parameters and state variables:

| State Parameter | Role & Purpose | Initial State |
|---|---|---|
| Primary State | Tracks active elements, frontier indices, or DP table cells | Initialized at boundary |
| Accumulator | Preserves confirmed optimal sub-answers or counts | Empty / Neutral |

> **Invariant.** At every processing step, all previously evaluated subproblems strictly satisfy the problem constraints, and no viable candidate solution has been omitted.

---

## 3. Step-by-Step Worked Execution

### Step 1: Store each active video and its counters together

`videos` maps each active `videoId` to a four-entry mutable record:

`[videoText, views, likes, dislikes]`.

Keeping all state for one ID together makes successful operations expected constant-time dictionary lookups, aside from copying watched substring content.

Deleted IDs are absent from this dictionary. Membership is therefore the authoritative existence check for every method.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"operations": ["VideoSharingPlatform", "upload", "upload", "remove", "remove", "upload", "watch", "watch", "like", "dislike", "dislike", "getLikesAndDislikes", "getViews"], "arguments": [[], ["123"], ["456"], [4], [0], ["789"], [1, 0, 5], [1, 0, 1], [1], [1], [1], [1], [1]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Maintain the smallest reusable ID

Two fields coordinate allocation:

- `next_id` is the smallest ID that has never been assigned;
- `available_ids` is a min-heap of IDs that were assigned and later removed.

On upload, if the heap is nonempty, `heapq.heappop` returns its smallest deleted ID. Otherwise, the method uses `next_id` and increments it for the future.

This always gives the globally smallest available ID. Every heap entry is below `next_id` because it was previously assigned. If any deleted ID exists, the heap minimum is smaller than every never-used ID. If none exists, all IDs below `next_id` are active, making `next_id` the smallest available.

The new dictionary record initializes views, likes, and dislikes to zero. Reusing an ID does not inherit the deleted video's statistics.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Removal releases an ID exactly once

`remove` first checks whether `videoId` is active. If so, it deletes the dictionary entry and pushes the ID into the reusable heap.

Calling `remove` again on the same absent ID does nothing, so duplicate heap entries cannot be created. This matters because duplicate reuse entries could assign one ID to multiple uploads.

Removing an unknown ID has no effect on any state.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[null, 0, 1, null, null, 0, "456", "45", null, null, null, [1, 2], 2]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"operations": ["VideoSharingPlatform", "upload", "upload", "remove", "remove", "upload", "watch", "watch", "like", "dislike", "dislike", "getLikesAndDislikes", "getViews"], "arguments": [[], ["123"], ["456"], [4], [0], ["789"], [1, 0, 5], [1, 0, 1], [1], [1], [1], [1], [1]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[null, 0, 1, null, null, 0, "456", "45", null, null, null, [1, 2], 2]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Scan upward from ID zero on every upload:** It finds the smallest free ID but can take linear time per upload; the heap retrieves released minima efficiently.
- **Use only a monotonically increasing ID:** Deleted IDs would never be reused, violating the contract.
- **Reuse IDs with a stack or queue:** Neither guarantees the smallest available ID; a min-heap does.
- **Push on every remove call:** Repeated removal would duplicate heap entries. Membership guarding is essential.
- **Mutate counters before existence check:** Invalid operations must have no effect.
- **Watch beyond video end:** Python slicing truncates automatically at the correct final character.
- **Inclusive end minute:** `endMinute + 1` converts the inclusive contract to Python's exclusive slice endpoint.
- **Removed then queried:** All query methods return their specified missing-ID sentinel.
- **Reused ID:** New counters start at zero and old content is gone.
- **Duplicate videos:** Text equality does not matter; each upload receives its own ID and record.
- **Repeated arrival of same call:** Every successful watch increments views once; every valid like or dislike increments its own counter once.
- **Returned likes list:** Slicing produces only the two requested values, not the internal video record.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. Let `A` be the number of reusable IDs currently in the heap and `L` the length of a returned watch substring. Upload with reuse and successful removal take `O(\log A)` heap time; upload without reuse is `O(1)` apart from storing the video reference.
- **Auxiliary Space Complexity:** $O(U + Q)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
