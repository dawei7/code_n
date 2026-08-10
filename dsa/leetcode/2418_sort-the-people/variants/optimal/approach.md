## General

**Keep the two parallel arrays connected**

At every index `i`, `names[i]` and `heights[i]` describe the same person. The required output changes the order of the names according to height, so the central danger is losing that index relationship. Sorting only `heights` would reveal the correct height order but would no longer say which original name belonged to each moved value.

The solution avoids mutating either input array. It creates

`idx = list(range(len(heights)))`,

which initially contains `0, 1, ..., n - 1`. Each number is a compact reference to one person. Through that reference, both attributes remain available: the person's height is `heights[i]` and the person's name is `names[i]`. The algorithm sorts these references and then uses them to read names in the resulting order.

**Why sorting indices solves the ordering problem**

The call

`idx.sort(key=lambda i: -heights[i])`

assigns index `i` the key `-heights[i]`. Python's list sort arranges keys in ascending order. Negation reverses the desired numeric relationship: if one person is taller, then their height is larger but their negative height is smaller. For example, heights 180, 165, and 170 produce keys -180, -165, and -170. Ascending key order is -180, -170, -165, corresponding to descending height order 180, 170, 165.

The constraints guarantee that all heights are distinct. Therefore every sorting key is distinct as well, and the required order is unambiguous. No tie-breaking rule is needed. Python's sort is stable, but stability has no effect under this guarantee.

After sorting, `idx[j]` is the original position of the person who belongs at output position `j`. The list comprehension

`[names[i] for i in idx]`

visits those positions in sorted order and extracts only the requested names. It does not return heights or indices, and it does not confuse equal names: names may repeat, but each index still identifies the correct person. In the example with two people named `"Bob"`, the two Bob strings are indistinguishable as values, yet their separate indices have different heights and are placed correctly.

**Step-by-step trace**

For `names = ["Mary", "John", "Emma"]` and `heights = [180, 165, 170]`, the initial index list is `[0, 1, 2]`. The associated negative keys are -180 for index 0, -165 for index 1, and -170 for index 2. Sorting by those keys changes the index list to `[0, 2, 1]`. Reading `names[0]`, `names[2]`, and `names[1]` produces `["Mary", "Emma", "John"]`.

Notice that no association needs to be rebuilt after sorting. The association is the index itself. This is especially clean because the problem already presents the data as parallel arrays.

**Why the result is correct**

Take any two output positions `p < q`. Because `idx` is sorted by ascending negative height,

$$
-\texttt{heights[idx[p]]}
<
-\texttt{heights[idx[q]]}.
$$

Distinct heights make the inequality strict. Multiplying by -1 reverses it, giving

$$
\texttt{heights[idx[p]]}
>
\texttt{heights[idx[q]]}.
$$

Thus every earlier output position belongs to a taller person than every later position. The index list begins as every integer from 0 through $n-1$ exactly once, and sorting only permutes those integers. The final comprehension consequently returns every input person's name exactly once, in strictly descending order of that person's height. These two facts establish both completeness and the required ordering.

**Why this representation is a good fit**

A dictionary from height to name would also be valid because heights are unique, but it creates a second association that the input indices already provide. Sorting indices makes no changes to `names` or `heights`, uses no assumptions about names being unique, and mirrors the exact output request: determine an order, then project that order onto the names.

Using `-heights[i]` rather than `reverse=True` is an implementation choice, not a different algorithm. Both express descending height. The negative key is safe for the stated positive heights, and Python integers do not overflow when negated.

## Complexity detail

Let $n$ be the common length of `names` and `heights`. Creating `idx` takes $O(n)$ time. Sorting $n$ indices takes $O(n \log n)$ comparisons in the worst case relevant to the stated bound, and evaluating each simple key is constant time. Building the result examines all $n$ sorted indices once, taking another $O(n)$ time. Sorting dominates, so total time is $O(n \log n)$.

The index list occupies $O(n)$ auxiliary space. Python's sort may use $O(n)$ temporary memory, and the returned name list contains $n$ references, also $O(n)$. Therefore the implementation's overall additional storage is $O(n)$, matching the manifest. If output space is excluded by convention, the explicit index list and sorting workspace still justify $O(n)$.

The strings themselves are not copied character by character by the list comprehension; the new list stores references to the existing string objects. If one separately counted the unavoidable output text representation outside Python's object model, its total character volume would depend on the name lengths, but the algorithmic manifest uses the number of people as its primary size.

## Alternatives and edge cases

- **Pair and sort:** Construct pairs such as `(height, name)`, sort them by descending height, and extract each name. This is equally asymptotic and often concise, but the exact solution's index permutation avoids duplicating the association into tuple objects.
- **Height-to-name dictionary:** Unique heights allow a map followed by a sort of the heights. It works in $O(n \log n)$ time and $O(n)$ space, but would be invalid without the distinct-height guarantee because duplicate keys could overwrite people.
- **Sort both arrays in place:** A custom sort could swap names whenever it swaps heights. That can avoid an explicit index result but mutates the inputs and is easier to implement incorrectly because the arrays must remain synchronized.
- **Counting sort:** Heights are bounded by $10^5$, so a bucket-based method could run in $O(n + H)$ time for height range $H$. Its memory and range-scanning cost are unnecessary for $n \le 1000$, and comparison sorting is simpler.
- **Single person:** `idx` contains only zero, sorting does nothing, and the one name is returned.
- **Repeated names:** Names do not serve as keys. Separate people with the same spelling retain their separate indices and are ordered by their distinct heights.
- **Distinct heights:** This guarantee removes all tie ambiguity. If it were removed, the problem would need to specify how equal-height people should be ordered; Python's stable sort would retain their original relative order.
- **Input preservation:** Neither original list is rearranged. Only the newly allocated index and result lists change, which can be useful when callers still need the original alignment.
- **Descending versus ascending:** Omitting the minus sign would return the shortest person first. The sign inversion is the exact detail that converts Python's default ascending key order into the required descending height order.
