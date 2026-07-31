## General

Each bench needs a collection that remembers which student identifiers have already appeared there. A hash set has exactly this behavior: inserting a repeated identifier leaves its size unchanged, while inserting a new identifier increases the size by one.

Scan the input once. For every `[student_id, bench_id]` row, obtain the set assigned to `bench_id` and insert `student_id`. After the scan, the size of a bench's set is precisely its number of unique students: every recorded student for that bench was inserted, and set uniqueness prevents any student-bench pair from being counted twice. The largest set size is therefore the requested answer. Supplying a default of zero to the maximum operation handles an empty input without a special collection entry.

## Complexity detail

Let $n$ be the number of rows in `students`. With expected $O(1)$ hash insertion, the scan takes $O(n)$ time. The sets store at most one entry for every distinct student-bench pair, so the auxiliary space is $O(n)$.

## Alternatives and edge cases

- **Set of complete pairs plus bench counts:** Deduplicating `(student_id, bench_id)` pairs first and then counting their bench identifiers is also $O(n)$ expected time, but it requires a second pass over the unique pairs.
- **Repeated linear searches:** Scanning earlier rows to decide whether each pair was already seen is correct but takes $O(n^2)$ time in the worst case.
- **Empty input:** No bench has any students, so the required result is `0`.
- **Duplicate observations:** Repeated occurrences of the same student on the same bench contribute once because the per-bench set does not grow.
- **One student on several benches:** Uniqueness is local to a bench; the student belongs to the set for every distinct recorded bench.
