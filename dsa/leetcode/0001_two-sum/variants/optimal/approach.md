## General

**Turn the required sum into a lookup question**

For every value `x` in `nums`, there is exactly one value that could form the required sum with it:

$$
y = \texttt{target} - x.
$$

The value `y` is the **complement** of `x`. For example, if `target = 9` and the current value is `x = 7`, then the complement is `y = 2`, because $7 + 2 = 9$.

This observation changes the question from “Which two elements should be tried together?” into the simpler question “Have we already seen the complement of the current element?” That change is the key to the optimal solution.

A brute-force solution compares every index with every later index. It may inspect

$$
\frac{n(n-1)}{2}
$$

pairs, which is $O(n^2)$ work. Most comparisons repeat the same kind of search: given one value, scan for its complement. A hash table removes that repeated scan by remembering values that have already been visited.

**What the dictionary stores**

The solution creates `d = {}`. Each dictionary entry has a precise meaning:

- the key is a value already encountered in `nums`;
- the associated value is an index at which that number occurred.

Immediately before the loop processes index `i`, `d` contains only values from indices smaller than `i`. The dictionary therefore represents the already-processed prefix `nums[0:i]`; it never contains the current element or a future element.

This meaning makes the distinct-index rule easy to enforce. If the current complement is found in `d`, its saved index must be different from `i`, because every saved index is earlier than `i`. The same array element can never be selected twice.

**Process the array from left to right**

The loop

```python
for i, x in enumerate(nums):
```

visits every element once. `i` is the current index and `x` is the value `nums[i]`. On each iteration, the algorithm performs three logical steps:

1. Compute the only value that could complete the pair: `target - x`.
2. Ask whether that complement is a key in `d`.
3. If it is not present, save the current value and index for later iterations.

The implementation combines the first two steps here:

```python
if (y := target - x) in d:
```

The expression `y := target - x` is Python's assignment expression. It first calculates the complement and stores it in `y`; the surrounding `in d` then checks whether that value is already a dictionary key. It is equivalent in meaning to:

```python
y = target - x
if y in d:
```

Using `:=` makes the code shorter, but it does not change the algorithm.

If `y` is present, `d[y]` is an earlier index whose value equals `y`. The current value is `x`, so

$$
\texttt{nums[d[y]]} + \texttt{nums[i]} = y + x = (\texttt{target} - x) + x = \texttt{target}.
$$

The solution can immediately return `[d[y], i]`.

If `y` is absent, no earlier element can pair with the current one. The line `d[x] = i` records the current value so that a later element can use it as its complement.

**Why lookup happens before insertion**

The order of the dictionary operations is essential: the solution checks for `y` first and inserts `x` second.

Suppose `target = 6` and the current value is the first `3` in `nums = [3, 3]`. Its complement is also `3`. At index `0`, the dictionary is empty, so the lookup fails and the algorithm stores `d[3] = 0`. At index `1`, the lookup finds that earlier `3` and returns `[0, 1]`.

If the current element were inserted before the lookup, the first `3` could find the index just inserted for itself. Returning `[0, 0]` would violate the rule that the same element cannot be used twice. Checking first makes the distinct-index requirement automatic instead of requiring a separate index comparison.

**A complete walkthrough**

Consider `nums = [2, 7, 11, 15]` and `target = 9`.

| Iteration | `i` | `x` | Complement `y = target - x` | Dictionary before lookup | Result |
|---:|---:|---:|---:|---|---|
| 1 | `0` | `2` | `7` | `{}` | `7` is absent, so store `d[2] = 0` |
| 2 | `1` | `7` | `2` | `{2: 0}` | `2` is present at index `0`, so return `[0, 1]` |

The later values `11` and `15` are never visited. Once a valid pair is found, the contract says there is exactly one solution, so continuing cannot improve or change the answer.

**Why no valid pair can be missed**

Let the unique solution use indices `a` and `b`, with $a < b$. When the loop reaches `a`, it may not find its complement because index `b` is still in the future. The algorithm then stores `nums[a]` in the dictionary.

When the loop later reaches `b`, every earlier processed value—including `nums[a]`—is represented in `d`. Because the solution values satisfy

$$
\texttt{nums[a]} + \texttt{nums[b]} = \texttt{target},
$$

the complement calculated at `b` is

$$
\texttt{target} - \texttt{nums[b]} = \texttt{nums[a]}.
$$

The lookup must therefore succeed by the time the second solution index is processed. The returned indices are distinct, both are valid, and their values sum to `target`. Thus every returned answer is valid, and the promised answer will be found.

The function has no explicit return after the loop because the problem guarantees exactly one valid pair. Under that contract, execution always returns from inside the loop. If the guarantee were removed, a deliberate “not found” result or exception would be needed after the loop.

## Complexity detail

Let $n$ be `len(nums)`.

- **Time complexity: $O(n)$ expected.** The loop visits at most $n$ elements. Each iteration performs one subtraction, one expected-$O(1)$ dictionary membership test, and at most one expected-$O(1)$ insertion. An early match may finish sooner, but the worst legal traversal processes all $n$ elements. Python dictionaries are hash tables, so their operations are expected constant time under normal hashing behavior. A deliberately adversarial collision pattern could make an operation slower and produce a theoretical $O(n^2)$ worst case, but the conventional algorithmic model—and the branch's required bound—uses expected hash-table performance.
- **Space complexity: $O(n)$.** If the pair is found near the end, the dictionary may contain values from almost the entire preceding prefix. It stores at most $n$ keys and indices. Variables such as `i`, `x`, and `y` use constant space, so the dictionary determines the auxiliary-space bound.

Duplicate values do not increase the dictionary beyond $O(n)$. Assigning `d[x] = i` again replaces the saved index for the same key. Keeping one earlier index is sufficient: if a later value needs `x`, any earlier occurrence produces a valid distinct pair. The exactly-one-answer promise means replacement cannot discard another answer that must be returned.

## Alternatives and edge cases

- **Brute-force pair enumeration:** Try every pair with two nested loops. This uses $O(1)$ auxiliary space but takes $O(n^2)$ time because it repeatedly searches for complements that a dictionary can remember.
- **Two-pass hash table:** First store every value and index, then scan again for complements. This is expected $O(n)$ time and $O(n)$ space, but it needs a separate `d[y] != i` check. The one-pass version returns sooner and enforces distinct indices through operation order.
- **Sorting plus two pointers:** Sorting allows two pointers to approach the target sum in $O(n \log n)$ time. Original indices must travel with the sorted values, however, and the method is slower than expected-$O(n)$ hashing.
- **Duplicate complement values:** `nums = [3, 3]`, `target = 6` works because the first `3` is inserted after its lookup; the second `3` finds a genuinely earlier index.
- **A value equal to half the target:** Seeing one value `x` with $2x = \texttt{target}$ is not enough. Two occurrences are required, and lookup-before-insert makes the algorithm wait for an earlier one.
- **Negative values and targets:** Subtraction and dictionary keys work identically for negative, zero, and positive integers; no sign-specific branch is needed.
- **Zeros:** `nums = [0, 4, 0]`, `target = 0` returns the two zero indices because the later zero finds the earlier zero in `d`.
- **Repeated non-solution values:** Replacing a saved index for a repeated key is safe. Only one earlier occurrence is needed to construct a valid pair.
- **Return order:** The saved earlier index is returned before the current index. The contract permits either order, so no sorting is required.
- **Exactly-one-solution guarantee:** This promise justifies both the immediate return and the absence of a fallback after the loop. A different API would need to define behavior for zero or multiple matches.
