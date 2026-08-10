## General

Long pressing can increase the number of consecutive copies of a character, but it cannot change the order of distinct character runs, remove a required occurrence, or introduce a new run character. The exact solution compares `name` and `typed` one run at a time.

A run is a maximal consecutive block of the same character. For example, `alex` has runs `a`, `l`, `e`, `x`, while `aaleex` has `aa`, `l`, `ee`, `x`.

Pointers `i` and `j` mark the beginnings of the next unprocessed runs in `name` and `typed`.

**Run characters must match.** At the top of the loop, if `name[i] != typed[j]`, return false. Long pressing repeats the intended key; it cannot turn one character into another. Since earlier runs have already been consumed, a mismatch also cannot be repaired by skipping characters.

**Find both run ends.** Pointer `x` starts at `i + 1` and advances while `name[x]` equals the current name character. Thus `x - i` is the required run length.

Pointer `y` similarly finds the typed run length `y - j`.

**Typed run must be at least as long.** One original press produces at least one typed copy, and long pressing may produce additional copies. Therefore

$$
\text{typed run length}
\ge
\text{name run length}.
$$

If `x - i > y - j`, typed omitted at least one required occurrence, so return false.

When the lengths are compatible, set `i = x` and `j = y` to compare the next runs.

**Why comparing runs is sufficient.** Suppose corresponding run characters match and every typed run is at least as long as its name run. For each run, interpret the first required number of typed copies as the intended key presses and every extra copy as long-press output. Concatenating these interpretations recreates the complete `typed` string from `name`.

Conversely, any valid long-press typing preserves the distinct-run sequence and can only increase each run's length. It must pass these exact tests.

**Both strings must end together.** The loop stops when either pointer reaches its string end. The final expression `i == m and j == n` requires both to be exhausted.

If name ends first but typed has another run, typed introduced an impossible extra character. If typed ends first, at least one name run is missing. Either case returns false.

For `name = "alex"` and `typed = "aaleex"`, run sequences match and lengths $(1,1,1,1)$ are dominated by $(2,1,2,1)$, so the answer is true.

For `name = "saeed"` and `typed = "ssaaedd"`, the name's `e` run has length two while typed's corresponding `e` run has length one. Long pressing cannot shorten it, so the answer is false.

An extra copy is legal only inside the matching current run. For example, `name = "alex"` and `typed = "aaleexa"` fail even though the extra final `a` appeared earlier in the name. Once the `x` run has been completed, long pressing cannot return to the old `a` key without changing run order. The final joint-exhaustion check catches that new trailing run.

Likewise, `name = "leelee"` and `typed = "lleeelee"` must be compared run by run rather than by total character counts. Matching totals cannot compensate for a short run in one location with extra copies in another location, because those occurrences belong to different key-press events separated by other characters.

**Why adjacent equal intended characters form one run.** If `name` contains `ee`, the two required presses and any long-press repetitions are indistinguishable in output. Only the total typed `e` count matters, and it must be at least two. Run-length comparison captures that exactly.
Before each loop iteration, prefixes `name[:i]` and `typed[:j]` have been matched as compatible complete runs. The current character and length tests accept exactly when the next run can arise through long pressing. Advancing to both run ends preserves the invariant. Joint exhaustion therefore proves validity.

## Complexity detail

Let $m=\lvert\texttt{name}\rvert$ and $t=\lvert\texttt{typed}\rvert$. Each pointer and its run-end helper moves only forward; every character is examined a constant number of times.

- **Time complexity:** $O(m+t)$.
- **Space complexity:** $O(1)$ auxiliary space.

No run arrays or substrings are created. The original strings are not modified.

## Alternatives and edge cases

- **Character-by-character greedy pointer:** Match name characters directly and allow typed repeats of the previous matched character. This also works but needs careful handling of leading and trailing extras.
- **Materialize run-length arrays:** Compare character/count pairs after grouping. It is conceptually clear but uses $O(m+t)$ extra space.
- **Only compare character sets:** Sets lose order and multiplicity and are insufficient.
- **Typed shorter than name:** It cannot contain enough required presses and eventually fails a run length or exhaustion test.
- **No long presses:** Identical strings pass with equal run lengths.
- **Every run extended:** All typed counts may be larger and still pass.
- **Extra final run:** Joint exhaustion rejects it.
- **Missing final run:** Joint exhaustion rejects it.
- **Same total length but different run structure:** A character mismatch rejects it even if counts coincidentally sum equally.
- **Single-character name:** Typed must contain only that character and at least one copy.
- **Repeated intended character:** The typed run must be at least the full required multiplicity.
- **Lowercase contract:** Direct character equality has no case or locale complication.
- **Run order:** Long pressing cannot reorder runs; advancing both pointers together enforces identical order.
