## General

The task has two parts: identify strings present in both lists, then keep every common string whose two indices have the smallest possible sum. Comparing every pair of positions would work, but it would repeat many unnecessary string comparisons. A hash map turns one list into a direct string-to-index lookup.

**Indexing the second list**

The dictionary comprehension:

```python
d = {s: i for i, s in enumerate(list2)}
```

stores each `list2` string as a key and its index as the value. The contract guarantees all strings within a list are unique, so no later duplicate overwrites an earlier index.

After this preprocessing, checking whether a `list1` string is common takes expected constant-time dictionary membership, and retrieving its second-list index takes expected constant time.

The exact source maps `list2` and scans `list1`. Reversing those roles would be equally correct because $i+j$ is symmetric, as long as the correct stored and scanned indices are added.

**Maintaining the best sum seen so far**

`mi` starts at positive infinity, meaning no common string has been found. `ans` starts empty.

For each `list1[i] = s`:

- if `s` is absent from `d`, it is not common and contributes no candidate;
- otherwise, `j = d[s]` is its unique index in `list2`, and `i + j` is its candidate sum.

There are three possible comparisons:

1. If `i + j < mi`, this string is strictly better than all earlier common strings. The source updates `mi` and replaces the result with `[s]`. Replacement is necessary: every old answer had a larger sum and no longer qualifies.
2. If `i + j == mi`, this string ties the optimum, so it is appended.
3. If `i + j > mi`, it is worse and ignored.

This is a standard streaming-minimum pattern: keep the smallest value seen and all items attaining it.

**Tracing the tie example**

For `list1 = ["happy","sad","good"]` and `list2 = ["sad","happy","good"]`, the dictionary is:

```text
"sad" -> 0
"happy" -> 1
"good" -> 2
```

Scanning `list1` finds `"happy"` at sum $0+1=1$, so `mi` becomes one and the answer becomes `["happy"]`. `"sad"` also has sum $1+0=1$, so it is appended. `"good"` has sum four and is ignored. The result order is allowed to be arbitrary.

**Why scanning the complete first list is safe**

One might try to stop after indices exceed `mi`, because every second-list index is nonnegative. Such an optimization is possible once a finite minimum exists: if $i>\textit{mi}$, no later `i + j` can tie or improve it. The exact source simply scans all entries. This keeps the loop straightforward and remains linear.

At least one common string is guaranteed, so `mi` eventually becomes finite and `ans` is nonempty. The implementation would still return an empty list gracefully if the guarantee were removed.

**Why the algorithm is correct**

The dictionary contains exactly the strings in `list2` and their exact indices. Therefore, during the scan, a string is treated as a candidate if and only if it occurs in both lists, and the computed value is its true index sum.

Maintain the invariant that after processing the first $k$ entries of `list1`, `mi` is the minimum index sum among common strings in that prefix, and `ans` contains exactly all prefix strings attaining `mi`. The invariant initially describes an empty prefix. A noncommon or larger-sum string changes nothing; a smaller sum replaces the previous minimum and answers; an equal sum adds exactly one tied answer. Thus, each loop step preserves the invariant.

After the full scan, the prefix is all of `list1`, so `ans` contains exactly every common string with globally minimum index sum.

Uniqueness within each list is important to this simple representation. If duplicates were allowed, a string could have several possible indices, and the map would need to retain its smallest relevant index rather than blindly storing the last.

## Complexity detail

Let $m=\lvert\texttt{list1}\rvert$, $n=\lvert\texttt{list2}\rvert$, and let string hashing/comparison length be bounded by $L$. Building the dictionary costs expected $O(nL)$, and scanning `list1` costs expected $O(mL)$. Because strings have maximum length 30, $L$ is bounded and the conventional result is expected $O(m+n)$ time.

The dictionary stores $n$ string-to-index entries. Excluding returned strings, auxiliary space is $O(n)$ for this exact orientation. The manifest writes $O(m)$ using a generic mapped-list symbol; accurately, the bound is the size of whichever list is placed in the hash map. The output can contain up to $\min(m,n)$ tied strings.

Hash lookup is expected/amortized constant time. Theoretical collision behavior can be worse, but standard analysis uses expected hash-table performance.

## Alternatives and edge cases

- **Map the shorter list:** Can reduce auxiliary entries, but the implementation must preserve each list’s actual index when adding sums.
- **Nested loops:** Compare every pair in $O(mnL)$ time and track the same streaming minimum. Simple but unnecessarily slow.
- **Enumerate sums diagonally:** Try index sums from zero upward and stop at the first diagonal containing matches. Avoids a map but can do quadratic comparison work.
- **Sort strings with indices:** Merge two sorted name/index lists to find common names, then minimize sums. Costs sorting time and extra records.
- **Several tied strings:** Reset on a strictly smaller sum, append on equality, and return all ties.
- **Only one common string:** It becomes the answer regardless of how large its indices are.
- **Common string found late:** Infinity initialization allows its sum to establish the first minimum.
- **No common string:** Outside the contract, but the exact source would return `[]`.
- **Unique strings:** Ensures one index per string in each list. Duplicates would require minimum-index handling.
- **Any answer order:** Scan order from `list1` is valid; no result sorting is needed.
- **Spaces and letter case:** Strings are dictionary keys compared exactly. Spaces and uppercase/lowercase differences remain significant.
- **Early termination:** Once `i > mi`, later sums cannot improve because `j\ge0`, but omitting this optimization does not change asymptotic time.
