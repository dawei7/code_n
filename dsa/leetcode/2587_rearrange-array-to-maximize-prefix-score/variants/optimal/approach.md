## General

**Larger values should appear earlier**

A value placed early contributes to many prefix sums. A value placed late contributes to only a few. To maximize how many prefixes stay positive, the most helpful values should be used first.

The solution sorts `nums` in descending order, then accumulates its running sum. It returns the number of positive prefixes before the first nonpositive one.

The critical reasoning is not merely that “positives come first.” Among all values, descending order never gives a smaller prefix sum at any length than another permutation.

**Exchange proof for descending order**

Suppose a permutation contains adjacent values $a<b$ in that order. Swap them to place $b$ first.

Every prefix ending before the pair is unchanged. The prefix ending after the first position of the pair increases by $b-a>0$. Every prefix containing both values is unchanged because their sum is the same.

Therefore swapping an ascending inversion cannot turn any positive prefix nonpositive and may turn one nonpositive prefix positive. Repeatedly removing all such inversions produces descending order without decreasing the score.

Hence some optimal arrangement is the descending sort used by the code.

**Pointwise maximum-prefix interpretation**

For any length $t$, the first $t$ elements of descending order are the $t$ largest values in the array. Their sum is the greatest total any $t$ chosen elements can have. Thus the sorted prefix sum is an upper bound on the prefix sum at position $t-1$ in every other permutation.

This gives another view of optimality: descending order makes every prefix as large as possible simultaneously.

**Why the first failure ends all later successes**

The loop adds values in nonincreasing order. Suppose the running sum first becomes nonpositive after including `nums[i]`.

At this point `nums[i]` cannot be positive. If it were positive, every earlier sorted value would also be positive, and their sum would be positive. Therefore `nums[i] <= 0`, and every later value is no larger, hence also nonpositive.

Adding later elements can only keep the running sum unchanged when they are zero or decrease it when they are negative. No later prefix can become positive again. The number of positive prefixes is exactly $i$, corresponding to indices zero through $i-1$.

That is why the function can return immediately rather than finish scanning.

**Why sacrificing early prefixes cannot help**

One might wonder whether placing a negative value early could create fewer early positives but allow more later positives after large values arrive. The exchange argument rules this out: moving every larger later value ahead of a smaller earlier one cannot reduce the total number of positive prefixes.

Descending order concentrates all available positive contribution as early as possible. Once even this maximum possible accumulated sum is nonpositive at some length, rearranging cannot create more total positive prefixes by delaying helpful values.

**Trace the first sample**

Sorting `[2,-1,0,1,-3,3,-3]` descending gives

`[3,2,1,0,-1,-3,-3]`.

The running sums are $3,5,6,6,5,2,-1$. The first six are positive. At the final value, the sum becomes nonpositive, so the loop returns index six.

The statement shows a different arrangement with the same score. The optimal ordering need not be unique; descending order is a canonical one justified by the exchange proof.

**Zeros are useful when a positive balance exists**

A zero does not increase the sum, but if the running sum is already positive, appending zero creates another positive prefix at no cost. Descending order places zeros after positive values and before negatives, exactly where they can contribute most safely.

If all values are zero or negative, the first sorted value is at most zero, so the first prefix fails and the score is zero.

**Following the exact return values**

Variable `i` is the zero-based position of the first nonpositive prefix. Exactly `i` earlier prefixes exist, so returning `i` is the desired count.

If no failure occurs, every one of the `len(nums)` prefixes is positive, and the function returns that length after the loop.

The call `nums.sort(reverse=True)` mutates the caller's array into descending order.

## Complexity detail

Let $n$ be the array length. Sorting takes $O(n\log n)$ time, and the single running-sum scan takes $O(n)$ in the worst case. Total time is $O(n\log n)$.

Python's Timsort may use $O(n)$ temporary memory, matching the manifest. Beyond sorting workspace, only the running sum and loop variables use $O(1)$ space. The input order is changed.

## Alternatives and edge cases

- **Try every permutation:** There are $n!$ orders; the adjacent-swap proof collapses the search to one sorted arrangement.
- **Put only positive values first:** This is directionally correct, but full descending order also optimally orders positives, zeros, and negatives.
- **Priority queue:** Repeatedly extracting the maximum reproduces descending order in $O(n\log n)$ time with explicit $O(n)$ heap space.
- **All negative:** The largest value still makes a nonpositive first prefix, so the answer is zero.
- **All zero:** Every prefix equals zero, and “positive” is strict, so the answer is zero.
- **Zeros after positive sum:** Each preserves positivity and increases the score by one.
- **Total sum positive:** Descending order keeps every prefix positive, so the score is $n$.
- **Duplicate values:** Their relative order is irrelevant and sorting handles them naturally.
- **Strict positivity:** The stopping test is `s <= 0`; a zero prefix does not count.
- **Input mutation:** Sort a copy when original ordering must be retained.
