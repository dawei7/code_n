## General

**Compress consecutive equal vowels into runs.** In a beautiful substring, every `a` comes before every `e`, every `e` before every `i`, then `o`, then `u`. Because the input contains only vowels, such a substring consists of exactly five nonempty consecutive character runs with labels

`a, e, i, o, u`.

The solution first turns `word` into a run-length encoding `arr`. Each entry is a pair containing a vowel and the length of its maximal consecutive run.

Pointer `i` starts a run. Pointer `j` advances while `word[j] == word[i]`. When that equality stops or the string ends, `j - i` is the run length, so the code appends `(word[i], j - i)` and starts the next run at `i = j`.

For example, `"aaaaeiiiiouuu"` becomes

`[("a", 4), ("e", 1), ("i", 4), ("o", 1), ("u", 3)]`.

The compression preserves exactly the information needed: run order, vowel labels, and how much length each run contributes.

**Why a beautiful candidate corresponds to five consecutive runs.** Every required vowel must occur at least once, so there must be an `a` run, then an `e` run, then `i`, `o`, and `u`. No other vowel run can occur between them without breaking alphabetical order. Equal adjacent vowels would already belong to the same maximal run, so there cannot be two consecutive run entries with the same label. Therefore the complete candidate is represented by five adjacent entries whose labels concatenate to `"aeiou"`.

Conversely, any five consecutive runs with those labels form a beautiful substring when concatenated. Each vowel appears at least once because runs are nonempty, and the labels are in the required order.

**Scan every five-run window.** The second loop uses indices from zero through `len(arr) - 5`. The slice `arr[i : i + 5]` gives entries `a`, `b`, `c`, `d`, and `e`. These variable names denote run tuples, not the vowel characters themselves.

The condition

`a[0] + b[0] + c[0] + d[0] + e[0] == "aeiou"`

concatenates the five run labels. It succeeds exactly for the required sequence. When it succeeds, the candidate length is the sum `a[1] + b[1] + c[1] + d[1] + e[1]`. `ans` keeps the largest such sum.

If the run array contains fewer than five entries, `range(len(arr) - 4)` is empty and `ans` remains zero. If it contains exactly five, the range contains index zero and tests that one possible group.

**Why taking whole boundary runs is optimal.** A valid substring could technically start partway through an `a` run or end partway through a `u` run. However, once the five-run labels are correct, extending left within the same `a` run preserves validity and only increases length. Extending right within the same `u` run does the same. Therefore the longest candidate associated with those runs always includes both complete boundary runs, as well as every complete middle run. Summing all five run lengths does not miss a better partial choice.

**Trace the main candidate.** The segment `"aaaaeiiiiouuu"` compresses to labels `"aeiou"` with lengths four, one, four, one, and three. Their sum is 13, so `ans` becomes 13. Other regions of the word either contain fewer than all five vowels or have a descent such as `u` followed by `a`. A descent creates a run boundary whose five-label window cannot equal `"aeiou"`, separating candidates naturally.

For `"aeeeiiiioooauuuaeiou"`, the first long ordered portion fails before reaching `u` because an `a` appears after `o`. Compression makes that descent visible as an unexpected run label. The final five singleton runs spell `"aeiou"`, producing answer five.
Every beautiful substring maps to a consecutive five-run sequence labeled `a` through `u`. Extending to the full first and last runs cannot hurt, so a longest beautiful substring is exactly the full concatenation of some sequence that the loop tests. When the loop accepts a sequence, its concatenation satisfies both beauty conditions. Taking the maximum accepted run-length sum therefore returns the longest beautiful substring, and leaving zero when none is accepted is correct.

**Why the algorithm does not need to examine characters again.** After compression, all characters in a run are identical. Beauty depends only on transitions between runs and total lengths. The run array is thus a sufficient summary of the original string for the second phase.

## Complexity detail

Let `n = word.length` and `R` be the number of maximal runs. The two pointers in the compression phase advance monotonically and inspect each character a constant number of times, giving `O(n)` time. The second phase scans `R - 4` windows, each involving exactly five entries, so it takes `O(R)` time. Since `R <= n`, total time is `O(n)`.

The exact implementation stores all `R` run tuples in `arr`. In the worst case the vowel changes at every character, making `R = n`, so auxiliary space is `O(n)`. Each five-entry slice is constant-sized temporary storage. Thus the manifest’s `O(1)` space claim does not describe this exact run-array implementation; a streaming state machine could achieve constant space, but it is not the checked-in code.

## Alternatives and edge cases

- **Streaming vowel-stage scan:** Track the current ordered segment, distinct vowel stages reached, and best length while reading characters once. It can achieve `O(n)` time and `O(1)` space but requires more careful reset logic.
- **Dynamic programming by ending vowel:** Maintain best valid lengths ending in each of the five vowel stages. This is constant-space but less direct than run recognition.
- **Enumerate substrings:** Checking every interval is at least quadratic and ignores the strong ordered-run structure.
- **Fewer than five runs:** All five distinct vowels cannot appear in order, so the answer remains zero.
- **Exactly `"aeiou"`:** Five singleton runs pass and yield length five.
- **Repeated vowels within a stage:** They enlarge one run and are all included in the candidate length.
- **Missing vowel:** No five-run label sequence can equal `"aeiou"`.
- **Descending transition:** A transition such as `o` to `a` prevents any five-run window crossing it from matching the required labels.
- **Several beautiful regions:** Every five-run window is tested, and `ans` retains the longest.
- **Partial first or last run:** Extending to the complete same-vowel run preserves beauty, so a maximum never needs a partial run.
- **One-character word:** Compression creates one run, the scan is empty, and zero is returned.
- **Exact space accounting:** `arr` can contain one tuple per input character in an alternating-vowel word, so this source is `O(n)` space rather than `O(1)`.
