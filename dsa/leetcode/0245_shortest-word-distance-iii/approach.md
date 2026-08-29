## General

This variant has one semantic complication that changes the state needed by the scan: `word1` and `word2` may be the same string. If they are different, one occurrence of each forms a pair. If they are equal, the answer must use **two distinct occurrences** of that one word; pairing an occurrence with itself and reporting distance zero would be invalid.

The exact solution handles these cases in separate branches. This is clearer than trying to make one set of index variables mean two different things:

- for different targets, track the latest occurrence of each target;
- for equal targets, track the immediately previous occurrence of their shared word.

`ans` begins as `len(wordsDict)`. Any valid distance between two distinct indices in an array of length $n$ is at most $n-1$, so every real candidate is smaller than this initial sentinel. The contract guarantees a valid pair exists, including two individual occurrences when the words are equal, so the sentinel will be replaced before return.

**Case 1: the target words are different**

The variables `i` and `j` start at `-1`, meaning their targets have not yet appeared. During the left-to-right scan, `i` is replaced whenever `word1` occurs, and `j` is replaced whenever `word2` occurs. Once both are valid, `abs(i - j)` is a candidate distance.

Keeping only the latest indices is sufficient. When a new `word1` appears at index `k`, every seen `word2` is on or before `k`, and the greatest such index is closest to `k`. Any older `word2` is farther left. The symmetric statement holds when a new `word2` appears. Thus every new target occurrence needs to be compared only with the latest occurrence of the opposite target.

Consider

```text
["practice", "makes", "perfect", "coding", "makes"]
```

with `word1 = "makes"` and `word2 = "coding"`.

- Index `1` records the first `makes` in `i`; no `coding` exists yet.
- Index `3` records `coding` in `j`, producing distance `abs(1 - 3) = 2`.
- Index `4` replaces `i` with the newer `makes`, producing distance `abs(4 - 3) = 1`.

The minimum is `1`.

The source uses two separate `if` conditions. In this branch the words are known to differ, so a single array element can update at most one target index. Checking the distance on a non-target position only repeats an unchanged candidate and is harmless.

**Case 2: both target names are equal**

Now two “latest target” variables cannot both be assigned the current index, because that would treat one occurrence as both endpoints and yield zero. Instead, `j` means the index of the previous occurrence of the shared word.

When the scan finds another occurrence at index `i`:

1. If `j != -1`, compute `i - j`, the distance from the previous occurrence.
2. Update `j = i`, making this occurrence the previous one for the future.

The comparison must happen before replacing `j`; otherwise the subtraction would use the same index twice.

For the example array with both targets equal to `"makes"`, the first occurrence at index `1` merely sets `j = 1`. The next occurrence at index `4` creates the valid pair `(1, 4)` with distance `3`, then becomes the stored previous occurrence. The method returns `3`.

**Why consecutive equal occurrences are sufficient**

Suppose the shared word appears at sorted positions

$$
p_0<p_1<\cdots<p_{r-1}.
$$

For a fixed later occurrence $p_b$, the closest earlier occurrence is $p_{b-1}$, because every $p_a$ with $a<b-1$ is smaller and therefore farther away. Equivalently, any nonconsecutive gap decomposes into positive consecutive gaps:

$$
p_b-p_a=(p_{a+1}-p_a)+\cdots+(p_b-p_{b-1}).
$$

That sum cannot be smaller than each positive component. Hence the minimum distance between any two distinct occurrences must appear between consecutive occurrences. The single stored index `j` is all the history needed.

**Why the branch as a whole is correct**

For different words, take a globally closest valid pair and focus on its later endpoint. When the scan processes that endpoint, the stored latest opposite occurrence is either the pair's earlier endpoint or a still later compatible occurrence, which cannot be farther away. The candidate considered then is therefore at most the global optimum and, since no valid distance can be below the optimum, equals it.

For equal words, the consecutive-gap argument proves that evaluating every adjacent occurrence pair includes a globally minimum pair. The scan evaluates exactly those pairs after the first occurrence. In both branches, `ans` retains the minimum of all candidates encountered, so the returned value is the required shortest distance.

Separating the branches is more than an implementation detail. “Different words” requires compatibility between two labels; “same word” requires distinctness between two occurrences of one label. The explicit condition prevents the most common error on this problem: returning zero when the targets are equal.

## Complexity detail

Let $n$ be the number of strings in `wordsDict`. Exactly one branch runs, and that branch scans the list once. With word length bounded by `10`, each equality comparison is constant time under the problem constraints, giving $O(n)$ total time.

If string comparison cost is written explicitly, let $L$ be the maximum number of characters examined in a comparison. The detailed bound is $O(nL)$, which simplifies to $O(n)$ here because $L\le10$.

The different-word branch stores two indices, a loop index, the current word reference, and the current minimum. The equal-word branch stores one previous index plus similar scalar state. Neither allocates a list of occurrences, so auxiliary space is $O(1)$.

The time bound is worst-case optimal: a closer pair can occur near the end, so the algorithm may need to inspect the entire array. The valid-pair guarantee means `ans` is always replaced by an integer at most $n-1$.

## Alternatives and edge cases

- **One unified “previous interesting index” scan:** Record the latest index holding either target. When another interesting word appears, compare if the labels differ or if the requested targets are equal. This also achieves $O(n)$ time and $O(1)$ space, but the exact source's branch structure makes the distinct-occurrence rule more explicit.
- **Store occurrence lists:** Collect positions for the targets, then merge two lists for different words or inspect consecutive gaps for equal words. It is correct and linear time but uses $O(n)$ extra space unnecessarily for a single query.
- **Binary search between occurrence lists:** Each occurrence from one list can search for neighboring positions in the other. This costs $O(n\log n)$ in the worst case and needs stored lists, so the streaming scan is stronger.
- **Compare every pair:** Testing all target occurrence pairs is simple but can require $O(n^2)$ time.
- **Equal targets:** Two different occurrences are mandatory. The separate branch deliberately never compares an index with itself.
- **Exactly two occurrences of an equal target:** The first initializes `j`, the second supplies the only valid distance, and the guarantee ensures that candidate exists.
- **Adjacent occurrences:** Distance `1` is the smallest possible valid distance. The source could return early when it finds `1`, but completing the scan does not change correctness or asymptotic complexity.
- **First target appears much earlier:** Sentinels prevent a distance calculation until a compatible second endpoint has actually appeared.
- **Repeated runs of the same word:** In the equal-target branch, every consecutive pair in the run is checked. In the different-target branch, repeated copies replace the latest same-label index so the next opposite word uses the nearest one.
- **A target missing from the array:** The contract says both target names exist and, when equal, represent two individual words. Outside that contract, `ans` might remain `n`, so a broader API would need defined missing-pair behavior.
- **Initialization with `n`:** Since the greatest legal distance is $n-1$, `n` is a safe finite sentinel. It avoids depending on floating-point infinity while still being replaced by any valid candidate.
- **Independent `if` statements in the different branch:** They are safe because that branch runs only when `word1 != word2`. Moving the equal-word case into the same code without adjustment would make both indices equal and incorrectly create a zero distance.
