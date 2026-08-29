## General

**The scheduling decision hidden in the story**

A rainy day fills one lake. If that lake was already full, the flood happens immediately, so any necessary drying must have occurred on an earlier zero day. A zero day can dry only one lake. The challenge is therefore to assign available zero days to repeated rains while respecting time order.

The stored solution processes days from left to right and maintains two pieces of state:

- `rainy[lake]` is the index of the most recent day on which that lake received rain.
- `sunny` is a `SortedList` containing the indices of zero days that have occurred but have not yet been assigned to dry a lake.

The answer starts as `[-1] * n`. Rainy days are required to contain minus one, so that default already suits them. Whenever the code sees a zero day, it inserts that index into `sunny` and temporarily writes `1` into the answer. Drying lake one is a valid harmless fallback if that zero day is never needed for a more urgent assignment.

**What happens on a rainy day**

For day `i` with lake number `v`, there are two cases.

If `v` has never appeared in `rainy`, it was initially empty and this rain simply fills it. No earlier zero day has to be assigned. The code records `rainy[v] = i`.

If `v` is already in `rainy`, let `rainy[v]` be the previous rain day. To prevent a flood now, lake `v` must have been dried on some day strictly after that previous rain and strictly before the current day. Every index currently in `sunny` is automatically before the current day because days are processed online. The only remaining condition is that the chosen index must be greater than `rainy[v]`.

The call `sunny.bisect_right(rainy[v])` finds the insertion position immediately after all stored indices less than or equal to the previous rain day. Therefore, `sunny[idx]` is the earliest unused zero day strictly after that rain. If `idx == len(sunny)`, no valid zero day exists. The current second rain would hit a still-full lake, so the method returns an empty list.

Otherwise, the code assigns `ans[sunny[idx]] = v`, meaning that this zero day dries lake `v`. It removes that day from `sunny` because one zero day cannot perform two drying actions. Finally, whether the rain was the first or a repeat, it updates `rainy[v] = i` so the next occurrence will search after the current rain.

**Why the earliest usable zero day is chosen**

Any unused zero day between two rains on the same lake could dry that lake. Choosing the earliest such day is the safe greedy rule because later zero days remain available for future intervals that may start later.

Suppose some valid schedule uses a later eligible day `b` to dry the current lake while the algorithm chooses an earlier eligible day `a`. If `a` was unused in that schedule, move this drying action from `b` to `a`. The lake is already full after its previous rain, and both days occur before its current rain, so drying it earlier still prevents the flood. Day `b` becomes free and can serve every future task that could have used `a`, because `b` is later. Thus replacing the schedule's choice with the greedy choice does not destroy feasibility.

Repeatedly applying this exchange argument shows that whenever a valid completion exists, there is one agreeing with each earliest-day choice made by the algorithm. If the binary search finds no available day after the previous rain, no alternative schedule can help: all processed zero days are either too early or already committed, and future zero days occur after the flood would happen.

**Why keeping only the last rain is enough**

Once lake `v` has been successfully dried between two consecutive rains, its earlier history no longer matters. The later rain fills it again, and avoiding its next flood requires a drying day after this new last rain. Therefore, one timestamp per lake summarizes exactly the boundary that the next search must cross.

The map does not delete a lake after assigning a drying day. That is intentional. It immediately replaces the old timestamp with the current rain day. Whether the lake was once dry is already captured by the assigned answer day; future reasoning begins from the latest refill.

**Why unused sunny days may dry lake one**

The result requires a positive lake choice on every zero day, even when no drying is necessary. Drying an empty lake has no effect, so the initial value one is always permitted on an otherwise unused zero day. If lake one is full, drying it is also safe. A later repeated rain on lake one does not invalidate the answer; it merely means that this unused day happened to provide useful drying in addition to being a valid default.

## Complexity detail

Let $N$ be the number of days. Each day is visited once. A zero day is inserted into `sunny` once. A zero day assigned to a repeated lake is found by binary search and removed once. With the ordered-container operations modeled as $O(\log N)$, the total time is $O(N \log N)$.

The `rainy` dictionary stores at most one entry per distinct lake that appears, which is at most $N$. The sorted collection stores at most all zero-day indices, also at most $N$. The answer contains $N$ entries. Auxiliary state is therefore $O(N)$, matching the manifest.

Dictionary access has expected constant time. `SortedList` is an external ordered-sequence implementation whose documented practical operation costs support the logarithmic algorithmic model used here; its internal blocked-list details differ from a balanced binary search tree. The important abstract operations are ordered insertion, upper-bound search, and deletion. The lake universe can be as large as one billion, but storage depends only on lakes and days that actually occur, never on the universe size.

## Alternatives and edge cases

- **Balanced binary search tree:** Store unused zero-day indices in an ordered set and ask for the successor of the previous rain day. This is the same greedy algorithm and the most direct language-independent formulation.
- **Heap of deadlines:** One can derive pending lakes and their next-rain deadlines, then dry the most urgent lake on each zero day. It can also reach $O(N \log N)$ but usually needs preprocessing and more state.
- **Linear search through zero days:** Scanning all unused zero days for every repeated rain is conceptually simple but can degrade to $O(N^2)$.
- **No zero days:** The answer is all minus ones if every lake rains at most once. A repeated lake makes the instance impossible.
- **Extra zero days:** They retain the default value one because drying an arbitrary empty or full lake is allowed.
- **Zero day before the previous rain:** It cannot help with the next repeated rain because the lake is filled again afterward. `bisect_right` excludes it.
- **Zero day exactly at a boundary:** A day cannot be both rainy and zero. The strict successor search correctly requires a zero-day index greater than the previous rain index.
- **Several lakes competing for one zero day:** Removing an assigned index from `sunny` ensures that only one lake receives that drying action.
- **Consecutive rains on the same lake:** There is no zero day between them, so the method immediately returns an empty list on the second rain.
- **Very large lake identifiers:** They are ordinary dictionary keys; no array of size $10^9$ is allocated.
- **Any valid answer is accepted:** Earliest-day assignments are a deterministic greedy choice, while unused zero days may legally name lake one.
