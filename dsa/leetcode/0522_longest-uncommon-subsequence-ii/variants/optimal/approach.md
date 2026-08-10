## General

With many input strings, a candidate is uncommon only if it is a subsequence of one string and is **not** a subsequence of every other string. The key simplification is that it is enough to test each entire input string as a candidate.

Suppose some deletion-produced subsequence `u` of `strs[i]` is uncommon. If the whole `strs[i]` is not a subsequence of any other input, then that whole string is also uncommon and is at least as long as `u`. If the whole string is a subsequence of another input, `u` may or may not occur there, but an optimal uncommon answer can always be represented by some full input string: choose the source string of a longest uncommon subsequence; if its whole string appeared as a subsequence elsewhere, every subsequence of it—including the candidate—would also appear there, a contradiction.

The algorithm therefore evaluates each `strs[i]` as a full candidate `s` and asks whether any other string `t` contains it as a subsequence.

**Test one subsequence with two pointers.** The helper `check(s, t)` returns whether candidate `s` is a subsequence of container `t`.

Pointer `i` identifies the next character of `s` that still needs to be matched. Pointer `j` scans `t` from left to right. Both begin at zero.

While neither string has been exhausted:

- if `s[i] == t[j]`, the current container character matches the next needed candidate character, so `i` advances;
- `j` advances on every iteration because each character of `t` can be considered only once.

When characters differ, advancing only `j` effectively deletes that character from `t`. When they match, advancing both accepts the match and preserves order. Greedily taking the earliest possible matching position is safe: it leaves at least as much suffix of `t` available for later characters as any later matching choice would.

At loop end, `i == len(s)` exactly means every character of `s` was matched in order. If `t` ended first while `i` still points inside `s`, the candidate is not a subsequence.

**Compare a candidate with every other input.** The outer loop selects index `i` and string `s`. The inner loop visits index `j` and string `t`. The condition `i != j` is crucial because every string is a subsequence of itself; comparing a candidate to its own occurrence would reject every candidate.

If some distinct input passes `check(s, t)`, the candidate is not uncommon, so `break` stops its inner loop. This includes an equal duplicate at another index. Equal strings are subsequences of each other, so no occurrence of a duplicated value can be uncommon.

Python's `for ... else` has precise behavior here: the `else` block runs only if the inner loop finishes without executing `break`. Thus reaching the `else` means no other input contains `s` as a subsequence. The whole `s` is then a valid uncommon subsequence.

The update:

`ans = max(ans, len(s))`

keeps the greatest length among all valid full-string candidates. `ans` starts at `-1`, the required result when every candidate is rejected.

For `["aba", "cdc", "eae"]`, none of the three length-three strings is a subsequence of either other string. Each reaches the loop's `else`, and the maximum remains three.

For `["aaa", "aaa", "aa"]`, each `"aaa"` occurrence is a subsequence of the other duplicate. The candidate `"aa"` is a subsequence of either `"aaa"`. Every inner loop breaks, `ans` stays `-1`, and no uncommon subsequence exists.

**Why testing only full strings is complete.** Consider an optimal uncommon subsequence `u` and let `s` be the input string from which it comes. If `s` were a subsequence of some other `t`, then transitivity would make `u` a subsequence of `t` as well: first delete from `t` to get `s`, then delete from `s` to get `u`. That contradicts `u` being uncommon. Therefore `s` itself passes the algorithm's all-other-strings test, and `len(s) >= len(u)`. Since `u` was optimal, the full candidate gives an equally good or better answer.

This transitivity argument is the reason an exponential enumeration of deletion patterns is unnecessary.

The order of `strs` does not affect correctness. The solution evaluates all indices and keeps only the maximum length, so it needs neither sorting nor lexicographic tie-breaking.

## Complexity detail

Let $k$ be the number of strings and $L$ their maximum length. There are $k^2$ index pairs in the nested loops up to constant exclusions. One `check(s, t)` scans at most $L$ characters of `t` and advances the candidate pointer at most $L$ times, so it costs $O(L)$. Worst-case time is $O(k^2L)$, matching the manifest.

The exact code uses only loop variables, two integer pointers, and `ans`, so its auxiliary space is $O(1)$ beyond the input. The manifest states $O(k)$ space, which is a valid loose upper bound but is not tight for this implementation. No set, sorted copy, or candidate list is allocated.

Early `break` and early exhaustion can reduce actual work, but the worst case occurs when many pair checks scan their complete container strings.

## Alternatives and edge cases

- **Sort by decreasing length:** The first full candidate not contained in another string gives the answer, but sorting adds $O(k\log k)$ organization and does not eliminate the pairwise containment checks.
- **Count exact duplicates first:** Duplicate values can be ruled out quickly, yet unique candidates must still be tested as subsequences of longer strings.
- **Enumerate all subsequences:** Each short string has exponentially many deletion patterns; the full-candidate transitivity proof makes this unnecessary.
- **Identical strings at different indices:** `i != j` still compares them, and each duplicate correctly disqualifies the other.
- **Candidate longer than container:** The helper cannot advance `i` enough before `j` ends, so it returns false naturally.
- **Candidate equal to container value:** At a different index, every character matches and the candidate is rejected.
- **Shorter string embedded in a longer one:** It is not uncommon even if it appears only once as an exact array value.
- **Same-length different strings:** One can be a subsequence of the other only if they are equal, so different values do not disqualify each other.
- **No valid candidate:** `ans` is never updated and remains `-1`.
- **Several valid candidates with equal maximum length:** Only the length is requested, so `max` needs no tie-breaking.
- **Greedy earliest match:** Choosing the earliest usable character in `t` cannot block a solution that a later choice would enable.
