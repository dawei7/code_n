## General

**Use the sorted order to recognize an excessive copy.** Equal values form one contiguous run. Maintain `write`, the length of the valid prefix already compacted into `nums[0:write]`, and inspect each original value from left to right.

The first $k$ retained values always fit because no value can yet have more than $k$ retained copies. After that, compare the current value with `nums[write - k]`:

- if they are equal, the valid prefix already ends with at least $k$ copies of this value, so the current occurrence must be skipped;
- if they differ, fewer than $k$ copies of the current value have been retained, so write it at `nums[write]` and advance `write`.

Why does one comparison suffice? If `nums[write - k]` equals the current value, sortedness makes every retained entry from that position through the end of the prefix equal to the current value, giving at least $k$ copies. Conversely, if it differs, the current value occupies fewer than the last $k$ retained positions and therefore has fewer than $k$ retained copies. The rule accepts exactly the first $k$ occurrences of every run and every occurrence of a shorter run, preserving order automatically.

Assignments never overwrite an unread value: `write` cannot exceed the current scan position. Once the scan finishes, delete the suffix beginning at `write` and return the resized input list.

## Complexity detail

Let $n=\lvert\texttt{nums}\rvert$. The scan examines every input element once, so it takes $O(n)$ time. Apart from the output storage represented by the resized input list, it uses only the write index and current value, giving $O(1)$ auxiliary space.

For scaling evidence, the three benchmark tiers use $n=20$, $50$, and $100$ distinct sorted values with `k = 1`. The accepted compaction remains linear. A correct generic method that scans the retained prefix to count every value performs

$$
1+2+\dots+(n-1)=\frac{n(n-1)}{2}
$$

comparisons on these inputs and therefore exposes its $O(n^2)$ growth while remaining within the legal source limit.

## Alternatives and edge cases

- **Track the current run length:** Remembering the previous value and its accepted count is also $O(n)$ time and $O(1)$ space, but the distance-$k$ comparison expresses the capacity test with less state.
- **Count each value in the retained prefix:** This is correct even without using sortedness, but repeated prefix scans take $O(n^2)$ time.
- **Fixed frequency table:** The legal values `1..100` permit 101 counters, giving another $O(n)$-time and $O(1)$-auxiliary-space implementation under this contract. It is independently benchmarked, but it relies on the fixed numeric range rather than the sorted-array structure.
- **Single element:** Since $k\ge1$, the only value is always retained.
- **Limit at least as large as every run:** No occurrence is removed, and the returned values equal the input values.
- **All values equal:** Exactly the first `k` copies remain.
- **Limit one:** The procedure retains one representative of each distinct value, equivalent to ordinary sorted-array deduplication.
