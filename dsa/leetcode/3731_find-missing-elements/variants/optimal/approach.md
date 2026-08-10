## General

**The surviving endpoints reveal the original range**

The contract guarantees that the smallest and largest integers of the original consecutive range are still present. Therefore,

$$
L=\min(\texttt{nums})
\quad\text{and}\quad
H=\max(\texttt{nums})
$$

are exactly the original endpoints. Every required missing value lies strictly between them, because `L` and `H` themselves are present.

The input order is arbitrary, so neighboring array positions provide no useful range information. The source first computes `mn` and `mx` by scanning all values.

**Use a set for presence tests**

The statement asks which values do not occur, not where existing values occur. Converting `nums` to `s = set(nums)` provides expected constant-time membership checks. Input values are guaranteed unique, but the set would preserve the same presence information even without that guarantee.

The list comprehension then examines

`range(mn + 1, mx)`.

Python's upper range endpoint is excluded, so this generates precisely

$$
L+1,L+2,\ldots,H-1.
$$

It keeps `x` exactly when `x not in s`.

The candidates are generated in strictly increasing order, so the returned list is automatically sorted. No separate output sort is required.

For `nums = [1,4,2,5]`, the endpoints are one and five. The scan tests two, three, and four. Only three is absent, producing `[3]`.

For `nums = [5,1]`, all interior candidates two, three, and four are absent, so all are returned. For `[7,8,6,9]`, each candidate seven and eight is present, so the comprehension produces an empty list.

**Why this returns every and only missing range element**

Take any value missing from the original range. It cannot be below `mn` or above `mx` because those are the range boundaries, and it cannot equal either endpoint because both survive. Thus it appears in `range(mn+1,mx)`. Because it is missing, the set test succeeds and includes it.

Conversely, every returned `x` lies strictly between the known endpoints and is absent from the input. The original array once contained every integer in this inclusive range, so such an `x` is genuinely one of the removed elements. Increasing enumeration provides the requested order.

The approach does not need to infer how many values were removed. The range scan naturally returns zero, one, or many missing values.

The endpoint guarantee also prevents ambiguity about values outside the scan. An absent integer smaller than `mn` or larger than `mx` was never part of the stated original range, so it must not be reported. Without the guarantee that both original endpoints survived, the current minimum and maximum might be interior survivors and the original range could not be reconstructed uniquely from `nums` alone. The source correctly uses that contract fact as the boundary of all work.

Because the input values are unique, the number of present integers in the range is exactly `n`. One could derive the number of missing values as `mx - mn + 1 - n`, but that number would not identify which values to return. The membership scan both identifies them and emits them in the required order.

## Complexity detail

Let `n` be the input length and let

$$
R=H-L
$$

be the endpoint difference. Computing minimum and maximum takes $O(n)$ time. Building the set takes expected $O(n)$ time. The range contains $R-1$ interior integers, so filtering takes expected $O(R)$ time. Total expected time complexity is $O(n+R)$.

The membership set requires $O(n)$ auxiliary space. The returned list may contain $O(R)$ integers, so including output storage the space bound is $O(n+R)$, matching the manifest. Excluding the required output, auxiliary space is $O(n)$. Hash-set membership supplies the expected-time qualification.

Under the given values from one through 100, `R` is at most 99, but naming it makes the relationship between numeric range width and work explicit.

## Alternatives and edge cases

- **Sort and enumerate gaps:** Sorting followed by expanding every adjacent gap takes $O(n\log n+R)$ time and can use less explicit membership storage. The hash-set method avoids sorting and is linear expected time.
- **Boolean array over values:** With the bound 100, a fixed presence table works in $O(n+R)$ time. A set generalizes without allocating by the maximum value.
- **Check membership in the original list:** Each candidate would require an $O(n)$ scan, producing $O(nR)$ time. The set removes that repeated work.
- **Scan from zero or one:** The original range need not begin there. Only values between the surviving minimum and maximum belong in the answer.
- **Include endpoints in the candidate loop:** They are guaranteed present, so testing them is harmless but unnecessary. The exact range excludes both.
- **No missing integers:** Every membership test fails the filter and the list comprehension returns `[]` naturally.
- **All interior integers missing:** The returned list is the complete increasing interior range.
- **Input already sorted:** The method remains correct and does not rely on or exploit that incidental order.
- **Exactly two endpoint values:** Every integer strictly between them is missing, which the range comprehension returns.
- **Adjacent endpoints:** `range(mn+1,mx)` is empty, correctly showing that there is no integer available to be missing.
- **Uniqueness guarantee:** It ensures `n` reflects distinct survivors, but the presence-based logic would also tolerate duplicates.
- **Sorted output requirement:** Iterating the numeric range in increasing order satisfies it without a final sort.
