## General

**Treat the permutation as a one-to-one matching**

Every original occurrence `nums[i]` is a target that would like to receive a strictly larger occurrence from the same multiset. Each value used in `perm` can occupy only one index, so the problem is to form as many disjoint pairs

$$
(\textit{target},\textit{replacement})
$$

as possible with `replacement > target`.

Original index order does not constrain which occurrence may replace which, so sorting the values exposes a standard greedy matching problem.

**Meaning of the pointer**

After `nums.sort()`, pointer `i` identifies the smallest target value that has not yet been successfully matched. The loop visits every sorted value `x` as a possible replacement, also from smallest to largest.

If `x > nums[i]`, this replacement beats the current smallest unmatched target. The algorithm forms that pair and increments `i`.

If `x <= nums[i]`, `x` cannot beat the smallest unmatched target. Since all other unmatched targets are at least as large, it cannot beat any of them. The candidate is skipped as a replacement.

At the end, `i` equals the number of successful pairs and therefore the maximum number of indices where `perm[i] > nums[i]` can hold.

**Why using the smallest feasible replacement is safe**

Suppose candidate $x$ is the first scanned value large enough to beat smallest unmatched target $a$. Matching them uses the weakest currently feasible replacement.

If an optimal matching leaves $x$ unused but matches $a$ with a later value $y\ge x$, replace $y$ by $x$ for target $a$. The pair remains valid and the number of matches is unchanged, while $y$ becomes available.

If the optimal matching uses $x$ for a larger target $b\ge a$, while $a$ is matched by $y\ge x$ or left unmatched, swap so $x$ matches $a$. If $b$ was also matched, give it $y$; the ordered structure preserves feasibility whenever that original larger replacement existed. This exchange produces an equally large matching agreeing with greedy.

Repeating the argument at each successful scan proves immediate matching cannot reduce the final cardinality.

**Why a failed candidate is useless**

When `x <= nums[i]`, current target `nums[i]` is the smallest unmatched value. Every remaining target is greater than or equal to it. Therefore $x$ is not strictly greater than any unmatched target and can never create a future successful position.

Discarding it is forced, not a heuristic.

**Trace the first example**

Sorting `[1,3,5,2,1,3,1]` produces `[1,1,1,2,3,3,5]`. Start with target pointer at the first $1$.

- Replacement candidates $1,1,1$ fail the strict comparison.
- Candidate $2$ matches the first target $1$.
- Candidate $3$ matches the second target $1$.
- The next $3$ matches the third target $1$.
- Candidate $5$ matches target $2$.

Four pairs are formed, so greatness four is achievable. The unmatched occurrences can fill the remaining permutation positions arbitrarily; they do not add to greatness.

**Why the pointer access stays in bounds**

Before processing the loop's $t$th element, at most $t$ earlier candidates could have produced matches, so `i <= t`. The current loop index is still within the array, making `nums[i]` valid.

The pointer can become $n$ only after the final iteration succeeds. There is then no later access.

**Connection to the maximum-frequency formula**

The manifest summary states that the answer is $n$ minus the highest value frequency. That is another characterization: the most frequent equal block creates an unavoidable number of non-winning positions in any cyclic value assignment, and an appropriate rotation attains the bound.

The exact checked-in solution does not count frequencies. It sorts and greedily matches, producing the same optimum with a different runtime.

**From matches back to a permutation**

Each successful target-replacement pair uses distinct occurrences because each target pointer advances once and each loop candidate is considered once. Assign those replacement occurrences to their matched target indices. Place all unused occurrences into remaining indices in any order.

This constructs a complete permutation with exactly the successful strict inequalities, proving the greedy count is attainable rather than only an abstract matching bound.

## Complexity detail

Let $n$ be the array length. Sorting takes $O(n\log n)$ time, and the scan takes $O(n)$. The exact total is $O(n\log n)$, not the manifest's $O(n)$ frequency-based bound.

Python's in-place Timsort may use $O(n)$ temporary memory, matching the manifest's space bound. The pointer and loop variables use $O(1)$ additional space. Sorting mutates the input order.

## Alternatives and edge cases

- **Maximum-frequency formula:** Count occurrences and return $n-\text{maxFrequency}$ in expected $O(n)$ time and $O(n)$ space, matching the manifest summary.
- **Two explicit pointers:** Scan a small-target pointer and a large-candidate pointer over the sorted array; it is equivalent to the compact loop.
- **Try permutations:** There are $n!$ arrangements, far beyond feasible.
- **All values equal:** No strict comparison can succeed, and the answer is zero.
- **Strictly increasing values:** Every value except the largest can be matched with its successor, giving $n-1$.
- **Duplicates:** Occurrences remain distinct pairing resources even though their values compare equal.
- **Strict inequality:** Equal candidates must be skipped; using `>=` would solve a different problem.
- **Single element:** It cannot be greater than itself after permutation, so the result is zero.
- **Input mutation:** `nums.sort()` destroys original ordering.
- **Manifest distinction:** The code is sorting-based $O(n\log n)$ matching, not linear frequency counting.
