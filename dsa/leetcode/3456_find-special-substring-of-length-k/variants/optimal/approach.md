## General

**The boundary conditions mean the substring must be a whole run.** A maximal run is a largest consecutive block containing one repeated character. By maximality, the character immediately before and after the run, when present, is different.

Any substring satisfying the problem's neighbor conditions cannot be a strict interior portion of a longer equal-character run. If it started after the run's beginning, its preceding character would be equal; if it ended before the run's end, its following character would be equal. Therefore, a valid substring exists exactly when some maximal run has length $k$.

The source scans these runs directly.

**Locate one maximal run at a time.** `l` is the first index of the current run. `r` starts at `l` and advances while it stays inside the string and `s[r] == s[l]`. When the inner loop ends, the run is half-open interval `[l,r)` and has length `r - l`.

The left boundary is valid automatically: either `l == 0` or the preceding run ended because its character differed. The right boundary is also valid: either `r == n` or the inner loop stopped at a different character.

If `r - l == k`, the complete run is the requested special substring and the method returns `True` immediately. Otherwise, `l = r` starts the next run. Every index belongs to exactly one processed run.

For `"aaabaaa"` and $k=3$, the runs are `"aaa"`, `"b"`, and `"aaa"`. The first run already has length three and would cause an immediate true result; the example's trailing run is another valid choice.

For `"aaaa"` and $k=3$, there are many three-character all-`a` slices, but neither boundary condition can hold for a strict length-three slice. The single maximal run has length four, so the source correctly returns false.

**Why checking exact equality is necessary.** A run longer than $k$ does contain an equal-character substring of length $k$, but that slice touches an equal character on at least one side. A run shorter than $k$ cannot supply enough characters. Only exact run length works.
When the source returns true, it found a maximal run of length $k$. All its characters match, and maximality guarantees different immediate neighbors where they exist, so it is valid.

Conversely, take any valid special substring. Its neighbor conditions show it cannot extend to another equal character on either side, making it a maximal run. The outer scan eventually processes exactly that run, measures length $k$, and returns true. If the scan finishes, no valid run exists.

The scan compares characters directly and does not need frequency counts because the property is local to consecutive positions.

**Edge positions need no special branch.** A missing neighbor imposes no restriction. The run scanner naturally accepts a run beginning at zero or ending at $n$ because those are maximal boundaries.

The source is also input-preserving. It stores only indices and never slices or modifies the string.

**Run decomposition is unique.** Every string has one unambiguous partition into maximal equal-character runs. For example, `"aabbba"` decomposes into lengths $2$, $3$, and $1$. Testing those lengths is therefore not a heuristic reduction; it is a complete re-expression of the original conditions. The inner loop identifies the right endpoint of exactly one part, and assigning `l = r` prevents overlap or omission.

The character immediately before a non-first run is the final character of the prior run, which differs by the definition of where the prior run ended. Similarly, if `r < n`, the inner loop stopped only because `s[r] != s[l]`. These facts prove both neighbor requirements without explicit character comparisons after the run is measured.

**Why a sliding count is unnecessary.** A fixed-size window could track whether all $k$ characters match, then separately inspect neighbors. But overlapping windows inside a long run would repeatedly discover candidates that must be rejected. Jumping by entire runs performs one decision per maximal block and mirrors the statement more directly.

If several runs have length $k$, returning after the first is sufficient because the output is Boolean. No lexicographic or positional choice is requested.

## Complexity detail

Let $n=\lvert s\rvert$. Although there are nested loops, `r` advances across each character once, and `l` jumps directly to the next unprocessed position. Total time is $O(n)$.

Only `l`, `r`, `n`, and character references are stored. Auxiliary space is $O(1)$, matching the manifest.

## Alternatives and edge cases

- **Check every length-\(k\) window:** This works in $O(nk)$ naively or with extra state, but maximal-run scanning is simpler and linear.
- **Use global character counts:** A character may have several separated runs; global frequency does not determine local validity.
- **Run longer than \(k\):** It must be rejected because any length-$k$ slice has an equal neighbor.
- **Run shorter than \(k\):** It cannot contain a qualifying substring.
- **Run exactly \(k\):** Its maximal boundaries satisfy both neighbor rules automatically.
- **Whole string one run:** It is valid exactly when `len(s) == k`.
- **\(k=1\):** Any maximal run of one isolated character qualifies.
- **First run:** No preceding character is required.
- **Last run:** No following character is required.
- **Early return:** Only existence is requested, so scanning later runs after a match is unnecessary.
