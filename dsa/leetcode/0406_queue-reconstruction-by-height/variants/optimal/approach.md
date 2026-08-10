## General

**Place people whose constraints are easiest to isolate first**

A person `[h, k]` cares only about people in front whose height is at least `h`. Shorter people are invisible to this constraint.

This suggests placing taller people first. When a person of height `h` is processed, everyone already in the partial queue has height at least `h`. Therefore, inserting this person at list index `k` puts exactly `k` qualifying people before them.

Later insertions involve people no taller than the current person. Strictly shorter people do not change the current person’s count, even if inserted before them. This makes the greedy decision permanent.

**The exact sorting order**

The method sorts with key

```text
(-height, k)
```

Negating height puts larger heights first. For equal height, ordinary ascending `k` order is used.

The equal-height tie rule is essential because people of the same height count one another. Processing smaller `k` first ensures that when another equal-height person with larger `k` is inserted, the equal-height people that must precede them are already available in the partial queue.

For example, among height-seven people `[7,0]` and `[7,1]`, `[7,0]` must be placed first. Inserting it at index zero gives one partial person. Inserting `[7,1]` at index one then places exactly one height-seven person before it.

**Why insertion index equals `k`**

At the moment `[h, k]` is processed, every person currently in `ans` is at least as tall as `h`. Python list index `k` means exactly `k` current entries lie before the inserted position. Since all of those entries qualify, the newly inserted person’s condition is satisfied immediately.

The input guarantee ensures reconstruction is possible, so the required insertion index is valid for the partial queue at that point.

The method performs

```text
ans.insert(p[1], p)
```

for each sorted person. The person pair itself is inserted; no new pair needs to be constructed.

**Why later shorter insertions do not break earlier work**

Suppose a previously placed person has height `H`. A later person has height `h <= H` because processing is descending by height.

If `h < H`, the new person does not count toward the earlier person’s requirement. Inserting the shorter person before the earlier one may change the earlier person’s numeric queue index, but it does not change how many preceding people have height at least `H`.

If `h == H`, the ascending-`k` ordering ensures equal-height people are inserted in the sequence required by their constraints. Once the algorithm moves to a smaller height, no future insertion can count toward any already-processed taller group.

This distinction between physical index and qualifying-person count is the heart of the greedy method.

**Tracing the first example**

The input

```text
[[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
```

sorts to

```text
[[7,0],[7,1],[6,1],[5,0],[5,2],[4,4]]
```

Insertions proceed as follows:

| Person | Insert index | Partial queue |
|---|---:|---|
| `[7,0]` | `0` | `[[7,0]]` |
| `[7,1]` | `1` | `[[7,0],[7,1]]` |
| `[6,1]` | `1` | `[[7,0],[6,1],[7,1]]` |
| `[5,0]` | `0` | `[[5,0],[7,0],[6,1],[7,1]]` |
| `[5,2]` | `2` | `[[5,0],[7,0],[5,2],[6,1],[7,1]]` |
| `[4,4]` | `4` | `[[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]` |

When `[6,1]` is inserted, only height-seven people are present, so index one gives it exactly one qualifying predecessor. Later height-five and height-four people do not count for it.

When `[5,2]` is inserted, every current person has height at least five. Its index two therefore gives exactly two qualifying predecessors. The final height-four person similarly uses index four.

**A formal invariant**

After processing the first `m` people in sorted order:

- `ans` contains exactly those `m` people;
- every person in `ans` has the correct number of preceding people among the processed set whose height is at least their own;
- every unprocessed person is no taller than the processed people at the boundary.

For the next person `[h, k]`, all current entries have height at least `h`. Inserting at index `k` gives the new person exactly `k` qualifying predecessors. For every earlier taller person, the new person is too short to affect its count. For earlier equal-height people, ascending `k` placement and the insertion position preserve their already-satisfied counts: the new equal-height person is placed according to its larger-or-equal required prefix rather than ahead of a person requiring fewer predecessors.

Thus the invariant is preserved. After all people are processed, it applies to the complete queue, proving the result satisfies every pair.

## Complexity detail

Let $n$ be the number of people.

Sorting takes $O(n\log n)$ time. However, Python’s `list.insert(index, value)` shifts every element at and after the insertion point. One insertion can cost $O(n)$, and the sum over all `n` insertions is $O(n^2)$ in the worst case. Therefore the exact solution’s total time is $O(n^2)$, not the $O(n\log n)$ time recorded in the variant manifest.

The result list holds $n$ references, so output storage is $O(n)$. Python’s sort also uses implementation-dependent temporary memory up to $O(n)$, and the input list is sorted in place. The asymptotic space bound is $O(n)$ including the returned queue and sorting workspace.

An order-statistics tree or Fenwick-tree formulation can achieve $O(n\log n)$ time, but it uses a different placement strategy than this exact source.

## Alternatives and edge cases

- **Fenwick tree over empty positions:** Sort shorter people first with an appropriate tie order and use a Fenwick tree to locate the required empty slot in $O(\log n)$. This realizes $O(n\log n)$ time but is much harder to explain and implement.

- **Balanced order-statistics sequence:** Supports insertion by rank in $O(\log n)$, preserving the same tall-first greedy idea. Python’s built-in list does not provide that bound.

- **Sort shortest first without empty-slot logic:** Direct insertion at `k` would be invalid because existing shorter people would not all count for the new person. Tall-first ordering is what makes list index equal the qualifying count.

- **Equal heights:** Ascending `k` is required because equal-height people count one another. Reversing that tie order can request an index larger than the partial group supports and disrupt counts.

- **All heights equal:** Sorting reduces to ascending `k`, and each person is inserted at the index stated by `k`, exactly reconstructing the group.

- **All `k` values zero:** Each newly processed shorter person is inserted at the front. That is valid because none of the already-processed taller people may precede it.

- **Duplicate pairs:** They represent distinct person occurrences. The sort and insert operations retain every occurrence.

- **Input mutation:** `people.sort(...)` changes the caller-provided list order. The returned `ans` is a separate list, but a defensive implementation would use `sorted(people, ...)` if input preservation mattered.

- **Any valid reconstruction:** The problem guarantees at least one solution and accepts any valid queue. This deterministic greedy order produces one such queue.

- **Physical position shifts:** Later shorter insertions can move a taller person to a larger array index, but they do not alter that taller person’s count of qualifying predecessors.
