## General

**The competitive entry point uses the one-pass hash-table method**

The `Solution` class contains two methods, but LeetCode calls `twoSum`. That primary method is the variant's $O(n)$ solution. The additional `twoSum2` method is a slower comparison implementation; it is not the method selected by the platform contract. Understanding that distinction prevents the complexity of unused helper code from being confused with the complexity of the submitted entry point.

The main method starts from the equation required for a valid pair:

$$
\texttt{nums[i]} + \texttt{nums[j]} = \texttt{target}.
$$

If the current number is `num = nums[i]`, rearranging the equation tells us exactly what earlier value is needed:

$$
\text{complement} = \texttt{target} - \texttt{num}.
$$

There is no reason to test the current number against every earlier number individually. The algorithm instead stores earlier values in a dictionary named `lookup`. A dictionary can answer “Was this complement seen?” in expected $O(1)$ time.

**The meaning of `lookup`**

Every entry in `lookup` maps an already-seen number to an index where it occurred:

```text
number -> earlier index
```

Before the iteration for index `i` begins, all indices stored in `lookup` are strictly smaller than `i`. Nothing from the unprocessed suffix is present, and the current element has not been inserted yet.

This is more than an implementation detail; it is the central invariant that explains the algorithm. If `target - num` is a key, its stored index is automatically distinct from `i`. If it is not a key, no already-processed element can pair with `num`, so saving `num` for future iterations is the only useful action.

**Follow the exact control flow**

The loop

```python
for i, num in enumerate(nums):
```

produces the current index `i` and value `num`. The condition

```python
if target - num in lookup:
```

calculates the complement and checks whether it appeared earlier. When the condition is true, the method evaluates the same complement again to retrieve its index:

```python
return [lookup[target - num], i]
```

The first returned index comes from the processed prefix; the second is the current index. Their values satisfy

$$
\begin{aligned}
\texttt{nums[lookup[target - num]]} &= \texttt{target} - \texttt{num}, \\
\texttt{nums[i]} &= \texttt{num}.
\end{aligned}
$$

Adding the equations gives exactly `target`, so returning immediately is safe.

When the condition is false, the line

```python
lookup[num] = i
```

adds the current value to the remembered prefix. The next iteration then begins with the invariant restored: every saved index is earlier than the next current index.

**Why the lookup comes first**

Checking before inserting is what enforces “do not use the same element twice.” Consider `nums = [3, 3]` and `target = 6`.

- At `i = 0`, `lookup` is empty. The required complement is `3`, so the check fails and `lookup[3] = 0` is stored.
- At `i = 1`, the required complement is again `3`. This time `lookup[3]` refers to index `0`, so the result is `[0, 1]`.

If `lookup[num] = i` happened before the membership test, index `0` could match itself and produce `[0, 0]`. The chosen order avoids this invalid state without a separate `lookup[complement] != i` condition.

**Trace a pair that is not adjacent**

Take `nums = [3, 2, 4]` and `target = 6`.

| `i` | `num` | Needed value `target - num` | `lookup` before the check | Action |
|---:|---:|---:|---|---|
| `0` | `3` | `3` | `{}` | Not found; store `3 -> 0` |
| `1` | `2` | `4` | `{3: 0}` | Not found; store `2 -> 1` |
| `2` | `4` | `2` | `{3: 0, 2: 1}` | Found `2 -> 1`; return `[1, 2]` |

Notice that the dictionary is not searching forward. It only remembers the past. That is sufficient because every pair has a later index; when that later endpoint is reached, the earlier endpoint is already available in `lookup`.

**Why the promised pair must be found**

Let the unique valid indices be `a` and `b`, where $a < b$. If the method has not returned before reaching `a`, it eventually executes `lookup[nums[a]] = a`. When it later reaches `b`, the needed complement is

$$
\texttt{target} - \texttt{nums[b]} = \texttt{nums[a]}.
$$

That value is in `lookup`, so the condition succeeds. The method cannot pass index `b` without finding the promised pair. Conversely, it returns only after a dictionary membership test proves that the earlier stored value and current value sum to the target. The method therefore neither misses the guaranteed solution nor returns an invalid pair.

There is no explicit result after the loop. This relies on the problem's guarantee that exactly one valid pair exists. Under the stated contract, the successful branch must execute.

**Why the second method is not the chosen algorithm**

`twoSum2` also computes a complement, but it repeatedly calls `nums.index`, creates a suffix slice, and searches that slice. `list.index` and `in` on a list are linear searches, while slicing copies elements. Repeating these operations for many values makes the method quadratic in the worst case. It is useful as a contrast with hashing, but `twoSum` is the direct, conventional, complexity-compliant entry point described by this variant.

## Complexity detail

Let $n$ be the number of elements in `nums`.

- **Time complexity: $O(n)$ expected for `twoSum`.** `enumerate(nums)` visits each element at most once. Each iteration performs constant arithmetic, one expected-$O(1)$ dictionary membership check, and either one expected-$O(1)$ lookup plus return or one expected-$O(1)$ insertion. Calculating `target - num` twice in the successful iteration changes only a constant factor. Python dictionary operations have expected constant time under the standard hash-table model. Pathological collisions can produce a theoretical $O(n^2)$ worst case, but the conventional and manifest bound is expected $O(n)$.
- **Space complexity: $O(n)$ for `twoSum`.** Before the answer is found, `lookup` may store an index for nearly every previously visited value. At most $n$ distinct keys are present. The loop variables and temporary arithmetic require $O(1)$ additional space.

Repeated numbers share a dictionary key, so a later assignment replaces the earlier index. This does not hurt the algorithm: any earlier occurrence of the required value is sufficient to form a pair with the current index. The dictionary size remains bounded by the number of input elements.

For comparison, `twoSum2` is $O(n^2)$ time in the worst case because its loop repeatedly performs linear list searches and suffix copies. A suffix slice can itself require $O(n)$ temporary space on an iteration, although that temporary storage is released and recreated. Those costs belong to the unused alternative method, not to the `twoSum` entry point or the branch's declared complexity.

## Alternatives and edge cases

- **Bundled `twoSum2` method:** This method searches a newly sliced suffix for each value. It avoids matching the exact current position by searching only later positions, but repeated `index`, slicing, and list membership operations make it $O(n^2)$ and less direct than `twoSum`.
- **Nested-loop brute force:** Checking every `i < j` pair uses $O(1)$ auxiliary space but $O(n^2)$ time. It makes the distinct-index rule explicit, yet repeats work that `lookup` eliminates.
- **Two-pass dictionary:** Building the complete mapping first and searching second also takes expected $O(n)$ time and $O(n)$ space. Because the current index is already in the completed map, it needs an explicit distinct-index check. The one-pass method avoids that extra condition.
- **Sorted values with original indices:** Sorting `(value, index)` pairs permits a two-pointer search in $O(n \log n)$ time. It retains correct original positions but is slower than expected linear hashing.
- **Two equal numbers form the pair:** For `nums = [3, 3]`, `target = 6`, the first occurrence is stored and the second retrieves it. Dictionary keys being unique does not prevent using two different array occurrences.
- **One occurrence of half the target:** A single `3` cannot solve `target = 6` by itself. Because insertion follows lookup, the current index is never available to its own membership test.
- **Negative integers:** A complement may be negative, positive, or zero. Integer dictionary keys and subtraction require no special handling for signs.
- **Zero target:** Two zeros are handled like any duplicate pair. The first zero is remembered; the second finds it.
- **Repeated values that are not the answer:** Reassigning `lookup[num]` keeps a valid earlier index for subsequent iterations. It cannot create an out-of-range or current index, because the reassignment occurs only after the current membership test.
- **Allowed output order:** The method returns the stored earlier index followed by `i`. Since the contract accepts any order, no final reordering is necessary.
- **Guaranteed existence:** Omitting a fallback is correct only because the Reference promises exactly one answer. Code reused outside that contract should explicitly define what happens when no pair exists.
