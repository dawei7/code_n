## General

**Count occurrences inside runs**

A special string contains copies of only one character. Therefore, every occurrence lies completely inside one maximal run of equal characters in `s`. If a run has length $L$, then a special substring of the same character and length $x$ has

$$
\max(0,L-x+1)
$$

starting positions in that run.

The $+1$ is the usual inclusive-window count. In a run of four `'a'` characters, length-two `"aa"` starts at positions zero, one, and two, giving $4-2+1=3$ occurrences. Overlap is allowed because the problem counts substrings by positions; those three occurrences do not need to be disjoint.

Function `check(x)` asks whether any special string of length `x` occurs at least three times. It scans maximal runs with pointers `i` and `j`. For the run `s[i:j]`, it adds `max(0, j - i - x + 1)` to `cnt[s[i]]`.

Counts from separate runs of the same character are added together because they represent occurrences of the same special string. A length-two run of `'a'` in one place and another length-two run elsewhere each contribute one occurrence of `"aa"`.

**Why checking the maximum character count is sufficient**

For a fixed length $x$, there are only 26 possible special strings: $x$ copies of `'a'`, $x$ copies of `'b'`, and so on. The dictionary stores exactly their occurrence totals. If its maximum value is at least three, some special string qualifies; otherwise none does.

The input is nonempty, so the run scan always inserts at least one dictionary key and `max(cnt.values())` is defined.

**Use monotonicity to binary-search the length**

If a special substring of length $x$ occurs at least three times, then its first $x-1$ characters form a special substring of length $x-1$ at each of those same starting positions. Thus every smaller positive length is also feasible. Feasibility has the form:

`true, true, ..., true, false, false, ...`.

The code binary-searches lengths from zero through $N$. `l` is the greatest length currently known feasible, with zero used as a sentinel. `r` is the greatest remaining candidate. The upper midpoint `(l + r + 1) >> 1` prevents an infinite loop when the interval has two values.

If `check(mid)` succeeds, the answer is at least `mid`, so `l = mid`. Otherwise `mid` and every greater length are impossible, so `r = mid - 1`. When both boundaries meet, `l` is the greatest feasible length.

Length zero is not a valid nonempty substring. It exists only as a search sentinel. If the final `l` is zero, the method returns `-1`; otherwise it returns `l`.

**A trace for one long run**

For `s = "aaaa"`, checking $x=2$ examines one run of length four and contributes three, so length two is feasible. Checking $x=3$ contributes two, so it is not. Binary search settles on two, matching the three overlapping occurrences beginning at positions zero, one, and two.

For `s = "abcaba"`, each `'a'` run has length one, and the three runs contribute one each when $x=1$. Length one is feasible even though no run contains three adjacent `'a'` characters. This illustrates why counts must be combined by character across runs.

**Why the result is exact**

`check(x)` partitions the string into all maximal runs. Every length-$x$ special occurrence belongs to exactly one such run, and the formula counts every possible start in that run exactly once. Summing by character gives the exact occurrence count of each possible special string.

The binary search uses this exact predicate and its proven monotonicity, so it returns the largest length with at least three occurrences. Translating the zero sentinel to `-1` handles the absence of any legal answer.

**The executable algorithm differs from the manifest summary**

The manifest describes a one-pass method that keeps the three longest run-derived lengths per letter and claims $O(N)$ time. The protected source instead reruns a full run scan for every binary-search probe. Its actual running time is $O(N\log N)$.

This still easily handles the smaller $N\le50$ constraint of version I, but an explanation of the exact code must not claim the different linear implementation.

## Complexity detail

Let $N$ be the string length. One `check` call advances through every character once, so it costs $O(N)$. Binary search performs $O(\log N)$ checks, giving $O(N\log N)$ time.

The dictionary has at most 26 keys, so its auxiliary space is $O(26)=O(1)$ for the fixed lowercase alphabet. Loop pointers and search boundaries also use constant space. The source string is never modified.

## Alternatives and edge cases

- **Track three best run contributions:** A true one-pass $O(N)$ solution exists and matches the manifest summary, but it is not the exact implementation documented here.
- **Enumerate every substring:** The small version permits slower methods, but testing all substrings repeats work and obscures the run formula.
- **Count only maximal runs:** Three occurrences can overlap inside one run, so merely counting how many runs have length at least $x$ is wrong.
- **Require disjoint occurrences:** The problem allows overlaps; `"aaaa"` contains three occurrences of `"aa"`.
- **Occurrences across runs:** Separate runs of the same letter contribute to the same special string and must be summed.
- **No letter appears three times:** Binary search ends at zero and the method returns `-1`.
- **All characters equal:** A run of length $N$ supports three occurrences up to length $N-2$.
- **Manifest mismatch:** Use $O(N\log N)$ for this binary-search source, not the listed $O(N)$ top-three-run method.
- **Input preservation:** All operations scan `s` without constructing or changing substrings.
