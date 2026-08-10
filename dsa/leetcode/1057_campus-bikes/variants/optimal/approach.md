## General

**Translate the repeated rule into one sortable key**

At every assignment step, the problem chooses among all currently available worker–bike pairs using three priorities:

1. Smaller Manhattan distance.
2. Smaller worker index when distances tie.
3. Smaller bike index when both distance and worker index tie.

Those priorities are exactly the lexicographic order of a tuple `(distance, worker_index, bike_index)`. Python compares tuples from left to right, moving to the next component only when the earlier components are equal.

The exact solution generates one such tuple for every possible worker–bike combination, sorts all tuples once, and scans them from smallest to largest. Availability arrays decide whether a pair is still usable.

**Generate every candidate pair**

Let `n` be the worker count and `m` be the bike count. The loop:

```python
for i, j in product(range(n), range(m)):
```

enumerates the Cartesian product of worker indices and bike indices. For every worker `i`, it visits every bike `j` exactly once. There are therefore `n * m` iterations.

For each pair, Manhattan distance is:

```python
dist = abs(workers[i][0] - bikes[j][0]) + abs(workers[i][1] - bikes[j][1])
```

The first absolute difference is horizontal distance and the second is vertical distance. Their sum is the required shortest grid-walking distance between the two coordinates.

The code appends:

```python
arr.append((dist, i, j))
```

Including both indices is not merely bookkeeping. Their order in the tuple encodes the two specified tie-breakers after distance.

All positions are unique, but distances need not be. Two different pairs can easily have the same Manhattan distance, so relying on distance alone would not reproduce the required deterministic assignment process.

**Sort once in the exact global priority order**

The statement:

```python
arr.sort()
```

sorts tuples in ascending lexicographic order. The resulting sequence is ordered first by distance, then by worker index, then by bike index. It is therefore the same order in which pairs would be considered by repeatedly searching for the smallest currently available key.

A subtle point is that some early tuples will later be unusable because their worker or bike was already assigned. They remain in `arr`, but the scan simply ignores them.

This works because availability changes only from true to false. Once a pair is unusable, it can never become usable later: assigned workers are never released, and assigned bikes are never returned. Consequently, a skipped tuple never needs to be reconsidered.

**Represent availability explicitly**

The code allocates:

```python
vis1 = [False] * n
vis2 = [False] * m
ans = [0] * n
```

`vis1[i]` records whether worker `i` already has a bike. `vis2[j]` records whether bike `j` is already taken. Although the names suggest generic visitation, their specific meaning is assignment status.

`ans[i]` will contain the bike index assigned to worker `i`. Its zeros are only initial placeholders. Since `n <= m`, enough bikes exist, and the complete candidate list includes every worker–bike pair. Every worker will eventually receive a bike, so every output slot is assigned before return.

**Scan candidates and accept only available endpoints**

The sorted tuples are processed with:

```python
for _, i, j in arr:
    if not vis1[i] and not vis2[j]:
        vis1[i] = vis2[j] = True
        ans[i] = j
```

The distance is unpacked into `_` because sorting has already used it and the scan does not need its numeric value again.

A pair is accepted only when both endpoints remain free. On acceptance, the chained assignment marks both as used, and `ans[i]` records the chosen bike.

If the worker is already assigned, that worker must not receive a second bike. If the bike is already assigned, it cannot be shared with another worker. Failing either condition is enough to skip the tuple.

The exact code continues through all pairs even after every worker has a bike. Those later checks cannot change `ans` because all workers are marked. An early counter and break could save scan work in practice, but it would not change the worst-case pair-generation and sorting costs.

**Why this scan simulates the required repeated selection**

Before the first assignment, the first tuple in sorted order is the globally smallest pair key, exactly matching the rule.

Now consider any later assignment. Every tuple earlier than the next accepted tuple has already been examined. Each was skipped because its worker or bike was unavailable. Since availability never returns, none of those earlier tuples is a legal choice now.

The next accepted tuple has both endpoints available. Every legal pair appearing later has a key greater than or equal to it because the entire list is sorted. Therefore this accepted tuple is the smallest-key pair among all currently available workers and bikes.

After accepting it, the same reasoning applies to the next assignment. By induction, every accepted pair is exactly the pair that the problem's repeated greedy rule would select at that moment.

This proof is important because sorting all original pairs might initially seem different from recomputing priorities after each removal. The monotonic loss of availability is what makes the one-pass simulation valid.

**Why every worker is eventually assigned**

There are at least as many bikes as workers. Each accepted pair consumes one worker and one bike, so after fewer than `n` assignments there are still enough unassigned bikes for all remaining workers.

For any unassigned worker, `arr` contains a tuple pairing that worker with every bike, including every still-free bike. When the scan reaches the earliest such legal tuple, it accepts it. Thus no worker can remain unassigned after the full list is processed.

The returned `ans` has length `n` and stores exactly one distinct bike index for every worker.

## Complexity detail

Let `W` be the number of workers, `B` the number of bikes, and `P = WB` the number of possible pairs.

Generating all tuples takes `O(P)` time. Sorting `P` tuples with comparison sorting takes `O(P log P)` time. The final scan examines all `P` tuples in the exact implementation and takes `O(P)` time. Sorting dominates, so the exact total is `O(WB log(WB))`.

`arr` stores `WB` triples. The two status arrays use `O(W + B)` space and the answer uses `O(W)` space. Python's sort may also use linear temporary storage. Overall auxiliary space is `O(WB)`, with the returned answer included or excluded without changing that dominant bound.

The manifest records `O(WB + D)` time and `O(WB + D)` space, where `D` is the maximum possible Manhattan distance. Under coordinates from zero through 999, `D = 1998`.

Those bounds describe distance buckets rather than the exact comparison sort. Create one bucket per distance. Generate pairs in ascending worker-index order and, inside that, ascending bike-index order. Appending pairs in that generation order means each distance bucket already respects the two tie-breakers. Scanning buckets from distance zero through `D` then produces the complete priority order in `O(WB + D)` time without comparison sorting.

The exact source and bucket version implement the same greedy assignment rule. Their difference is only how the ordered stream of candidate pairs is produced.

## Alternatives and edge cases

- **Distance buckets for the manifest target:** Group each `(worker, bike)` pair by its integer Manhattan distance and scan buckets from zero through `D`. Generate pairs in worker-major and bike-minor order so no per-bucket sort is needed. This achieves `O(WB + D)` time.
- **Global minimum heap of all pairs:** Heapifying every tuple and popping by priority reproduces the rule but uses `O(WB log(WB))` total pop time in the worst case and does not improve space.
- **One sorted bike list per worker plus a heap:** Keep each worker's bikes ordered by distance and maintain only that worker's current closest candidate in a global heap. This reduces heap size but still requires substantial preprocessing and careful replacement when a bike is taken.
- **Repeated full search:** Recompute the best available pair by scanning every worker and bike before each assignment. It directly mirrors the statement but can take `O(W^2B)` time.
- **One worker:** The first available tuple for that worker gives the globally closest bike, with bike index resolving distance ties.
- **Equal numbers of workers and bikes:** Every bike is eventually used, though assignment order still follows the global pair priority rather than independent nearest choices.
- **More bikes than workers:** Some bikes remain unused. Their tuples are harmless after all workers are marked assigned.
- **Distance ties across workers:** Tuple ordering gives the smaller worker index priority, even if the other tied worker has fewer good alternatives. The contract requires this local greedy choice.
- **Distance ties for one worker:** The smaller bike index appears first and is selected if still free.
- **Already-taken closest bike:** The tuple is skipped, and the worker remains unassigned until the scan reaches its next legal bike.
- **Parallel coordinate values are absent:** Locations are unique, but workers and bikes can still be at Manhattan distance zero only if a worker position equals a bike position. Cross-category equality is not prohibited by uniqueness wording, and the formula handles it.
- **No early break:** The exact loop scans all tuples after assignments are complete. Adding an assigned-worker counter could stop early but would not improve the asymptotic sorting bound.
- **Placeholder zeros:** Bike zero is a valid assignment, so `ans` alone cannot indicate whether a worker is assigned. `vis1` provides that separate status.
- **Input preservation:** Coordinates are only read. Sorting affects the newly built tuple list, not `workers` or `bikes`.
