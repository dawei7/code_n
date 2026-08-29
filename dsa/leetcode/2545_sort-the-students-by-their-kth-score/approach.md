## General

**Treat each row as one indivisible student record**

Each row stores all exam scores for one student. Sorting students must move entire rows together; sorting individual columns would destroy the relationship between a student and their other scores.

The selected key for row `x` is `x[k]`, the score in the requested zero-indexed exam.

**Reverse order through a negative key**

Python's `sorted` orders keys from smallest to largest. The lambda returns:

`-x[k]`.

If one student has a larger exam score, its negative is smaller and appears earlier.

For scores 11, 9, and 3, keys are $-11$, $-9$, and $-3$, producing the required descending score order.

An equivalent implementation could use `reverse=True` with key `x[k]`. The exact source chooses negation.

**Return whole rows**

`sorted(score,...)` returns a new outer list containing the original row objects in reordered sequence.

No row's internal exam-score order changes. Column `k` remains the ranking exam, and every other exam score travels with the same student row.

**Trace the first sample**

For:

`[[10,6,9,1],[7,5,11,2],[4,8,3,15]]`

with `k=2`, selected scores are 9, 11, and 3. Negative keys are $-9$, $-11$, and $-3$.

Ascending key order places:

1. row with score 11;
2. row with score 9;
3. row with score 3.

The returned rows match the sample.

**Why distinctness removes tie questions**

The matrix contains distinct integers globally, so in particular no two students share the same score in exam `k`. Every sort key is unique.

No secondary key is required, and stable-sort behavior cannot affect the result.

Even without this guarantee, Python's stable sort would preserve original student order for tied keys, but the problem never needs to specify that outcome.

**Index `k` is always valid**

Every row has `n` exam scores and constraint `0<=k<n`. The lambda can safely access `x[k]` for every row.

The matrix is rectangular, so no row is shorter than another.

**Why this is comparison sorting**

There can be up to 250 students and scores up to $10^5$. General sorting compares derived integer keys and needs no special counting array.

Key extraction is constant time. Python caches each key during sorting rather than repeatedly invoking the lambda for every comparison, so it computes one key per row.


For any two rows `A` and `B`:

- if `A[k]>B[k]`, then `-A[k]<-B[k]`, so `A` precedes `B`;
- if `A[k]<B[k]`, `B` precedes `A`.

Thus every row pair is ordered exactly according to descending kth-exam score. A total order satisfying all pairwise requirements is the required sorted matrix.

**Input and output identity**

The outer input list is not sorted in place because the built-in `sorted` creates a new list. The row objects themselves are shared, but the method never mutates them.

This is sufficient because only row ordering changes in the answer.

**Why sorting by a copied column would be dangerous**

Extracting kth scores into a separate list and sorting those numbers loses the mapping back to complete student rows unless indices are carried along. Sorting rows directly keeps each record intact automatically.

For the sample, returning only `[11,9,3]` would rank exam results but would not return the required matrix. The lambda is a key extractor, not a transformation of the output rows.

**Descending order is encoded once**

The key function is evaluated for every row, and standard sort compares those stored keys. Negating inside the key is preferable to negating matrix entries themselves: the latter would mutate or copy data and would require restoring values afterward.

Only the temporary keys are negative. Every score in every returned row retains its original positive value.

**Shallow-copy consequence**

Because rows are reused, changing a row through one matrix after the function returns could also be visible through the other reference in ordinary Python code. The challenge does not mutate results afterward, so deep copying would be unnecessary overhead.

The important contract is that the returned row order is correct at return time.

## Complexity detail

Let $m$ be the number of students. Computing keys costs $O(m)$. Comparison sorting costs $O(m\log m)$ time.

The returned outer list stores $m$ row references, and Python's sorting machinery may use $O(m)$ temporary space. Auxiliary/result outer storage is $O(m)$.

Rows are not deep-copied, so there is no additional $O(mn)$ score duplication.

## Alternatives and edge cases

- **`reverse=True`:** `sorted(score,key=lambda row:row[k],reverse=True)` avoids negating keys.
- **In-place `sort`:** It would mutate the outer input list instead of returning a separately ordered list.
- **One student:** The only row is returned.
- **One exam:** `k` must be zero and rows sort by their sole value.
- **Distinct scores:** No tie-breaker is needed.
- **Whole-row movement:** Never sort just the kth column.
- **Zero-indexed exam:** Use `x[k]` directly.
- **Large scores:** Negation is exact in Python.
- **Other columns:** They do not affect rank but remain attached to the student.
- **Row sharing:** The returned outer list references original unmodified rows.
