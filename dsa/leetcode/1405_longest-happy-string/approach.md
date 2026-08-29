## General

**The real obstacle is an overrepresented letter**

There are only three possible characters, but their allowed counts can be very uneven. Appending letters in a fixed rotation can waste available characters, and always appending the most numerous letter without checking the suffix can create `"aaa"`, `"bbb"`, or `"ccc"`. The useful greedy rule combines both concerns:

1. Prefer the letter with the largest remaining supply.
2. If that letter would make three identical characters in a row, use the largest remaining different letter for one position.
3. Stop only when no legal different letter exists.

Using a plentiful letter early reduces the imbalance that could otherwise make part of that supply unusable later. Using a second choice only when forced creates the separator needed to make the blocked letter legal again.

**How the heap represents the remaining supply**

The list `h` is used as a max-heap conceptually. Python's heap operations implement a min-heap, so the code stores each count as its negative:

```text
[-remaining_count, character]
```

A letter with ten copies is stored with priority `-10`, which is smaller and therefore pops before a letter stored with `-4`. A letter is inserted only if its input count is positive. Consequently, the heap contains at most three entries, and every entry represents a letter that is still available.

The entries are mutable two-element lists because the code updates the negative count in place. After consuming one copy, `entry[0] += 1` moves a negative count one step toward zero. For example, `-5` becomes `-4`. The condition `-entry[0] > 1` is evaluated before that update: if more than one copy existed, at least one remains after consumption, so the updated entry is pushed back. If exactly one existed, it is consumed and the entry disappears.

When counts tie, Python compares the second list element and uses the character as a deterministic tie-breaker. The problem permits any longest happy string, so choosing `'a'` before `'b'` in a tie affects only which valid answer is returned, not its maximum length.

**The normal greedy iteration**

At the start of each loop, `cur = heappop(h)` removes the character with the greatest remaining count. The suffix check asks whether the answer already ends in two copies of that character:

```python
len(ans) >= 2 and ans[-1] == cur[1] and ans[-2] == cur[1]
```

If the condition is false, appending `cur[1]` is legal. The code adds exactly one character, consumes one unit of its count, and returns its entry to the heap only when more copies remain.

Why append only one copy per iteration instead of trying to append a pair? Reconsidering the heap after every character keeps the implementation simple and automatically accounts for changing priorities. It may still produce two equal characters consecutively when that letter remains most frequent, but the suffix check prevents a third.

**What happens when the most frequent letter is blocked**

Suppose `cur` would make an illegal triple. The algorithm must not discard it, because a different letter may separate the existing pair from future copies of `cur`. It looks for that separator in the remaining heap.

If the heap is empty, every available character is the blocked kind. No legal next character exists, so `break` is correct. Leaving copies unused is allowed because each input count is an upper bound, not a requirement.

If another entry exists, `nxt = heappop(h)` obtains the most frequent legal alternative. It cannot equal `cur` because there is only one heap entry per letter. The code appends `nxt[1]`, decreases its remaining count in the same negative-count manner, pushes it back if necessary, and finally pushes `cur` back unchanged. On the next iteration, the just-added separator makes `cur` legal again.

It is important that `cur` is not decremented in this branch. The blocked character was inspected but not used. Only `nxt` contributes a character to `ans`.

**Why choosing the largest legal supply is optimal**

Validity is immediate from the suffix check. In the normal branch, the chosen letter is appended only if the preceding two positions are not both that letter. In the blocked branch, a different letter is appended, which also cannot form a triple of the blocked kind. The same check applies on every later iteration.

For maximum length, consider what can make characters unusable. A letter can be stranded only when the current answer ends with two copies of it and no other letter remains to act as a separator. While several letters are legal, taking one from the largest supply never makes the remaining multiset more imbalanced than taking a scarcer one would. It spends from the resource most at risk of eventually being stranded.

When the largest letter is blocked, every valid continuation must choose a different letter next. Among those forced separators, choosing the one with the largest remaining count again leaves the most balanced possible supplies after the step. The blocked entry is preserved for later. Thus the greedy step does not sacrifice a continuation that could use more characters.

There is also a useful capacity view. If one letter has $m$ copies and all other letters together have $r$ copies, the $r$ other letters create $r + 1$ gaps. At most two copies of the dominant letter fit in each gap, so no happy string can use more than $2(r + 1)$ of that dominant letter. If $m$ is below that capacity, the greedy balancing can consume every character. If $m$ exceeds it, some dominant copies are mathematically impossible to place. The algorithm stops precisely after all separators and all two-copy gap capacities have been used, so the unused suffix cannot be rescued by a different arrangement.

**Following the example with seven `c` characters**

For `a = 1`, `b = 1`, and `c = 7`, `c` repeatedly has the highest priority. It can be appended twice, but the third attempt is blocked. The heap then supplies `a` or `b` as a separator. After another pair of `c` characters, the other separator is used. Finally, at most two more `c` characters can be appended. A possible result has length eight, such as `"ccaccbcc"`. One `c` remains unused because two separator letters create only three gaps, each with capacity two.

The list `ans` is used instead of repeatedly concatenating immutable strings. At the end, `''.join(ans)` performs one linear construction of the returned string.

## Complexity detail

Let $N = a + b + c$, the total number of available characters. Each successful loop iteration appends exactly one character, so there can be at most $N$ successful iterations. There can be one final unsuccessful iteration when the top character is blocked and no separator exists. Each iteration performs only a constant number of heap pushes and pops.

The heap contains at most three entries. A heap operation therefore costs $O(\log 3)$, which is constant, and the overall time is $O(N)$. Joining `ans` also costs $O(L)$ for returned length $L \le N$, so it does not change the bound.

The heap holds no more than three pairs, so its auxiliary storage is $O(1)$. Apart from the returned answer, the algorithm uses only constant additional state. The `ans` list itself contains $L$ characters and therefore occupies $O(L)$ construction space in Python. As is customary for the manifest's $O(1)$ space bound, output storage is excluded; if output construction is counted, total space is $O(L)$.

## Alternatives and edge cases

- **Three explicit counters:** Because the alphabet is fixed, nested conditions can select the largest legal count without a heap. This retains $O(N)$ time and $O(1)$ auxiliary space but tends to duplicate comparison and streak logic, making tie and forced-separator cases easier to implement incorrectly.
- **Pair-at-a-time greedy construction:** A solution can place up to two dominant characters followed by one separator. It can be efficient, but it needs careful reordering after each group because the identity of the dominant character may change.
- **Backtracking over all strings:** Trying every legal next character can prove optimality by exhaustive search, but the number of possible prefixes grows exponentially and is unnecessary for counts up to 100.
- **Fixed round-robin order:** Cycling through `a`, `b`, and `c` preserves validity in many cases but can stop too early when counts are unbalanced. It does not prioritize the supply most likely to become unusable.
- **Only one nonzero count:** The answer contains at most two copies of that letter. After those two, the heap has no alternative separator, and the correct behavior is to stop.
- **A zero count:** Letters with zero availability are never inserted, so they cannot be selected accidentally and require no special loop branch.
- **Equal counts:** Heap tie-breaking may select a particular alphabetical order, but any tie choice among largest legal letters can lead to a maximum-length answer.
- **Exactly two matching trailing characters:** The next copy of that letter is forbidden, even if it has overwhelmingly the largest count. The code temporarily chooses `nxt` and preserves `cur` unchanged.
- **One matching trailing character:** Appending a second copy is legal. The suffix condition deliberately requires at least two existing result characters.
- **Unused characters are valid:** The contract says at most `a`, `b`, and `c` occurrences. When one count exceeds all available separator capacity, stopping with some copies unused is necessary rather than a failure.
