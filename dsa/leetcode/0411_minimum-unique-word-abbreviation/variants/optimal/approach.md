## General

**Represent an abbreviation by the letters it keeps**

An abbreviation of `target` makes one decision at every position: keep that character literally, or hide it inside a numeric run. The solution represents these decisions with an integer bitmask. Bit `index` is `1` when `target[index]` remains as a letter and `0` when that position is abbreviated.

For example, with a five-letter target, a mask that keeps only positions `0` and `4` represents a form like `a3e`: the two kept positions appear literally and the three consecutive zero bits between them become one number. Consecutive zero bits must be combined into one count. This automatically prevents adjacent numeric abbreviations such as `1` followed immediately by `2`; they would instead be the single run `3`.

The mask is an especially useful representation because the question “does this abbreviation distinguish the target from a dictionary word?” becomes a bitwise test.

**Discard dictionary lengths that cannot conflict**

Expanding any valid abbreviation of `target` always accounts for exactly `len(target)` character positions. A dictionary word with a different length therefore cannot match that abbreviation. The first loop ignores all such words.

For each same-length word, the code builds a `difference` mask. Bit `index` is set exactly when `target[index] != word[index]`. Thus a `1` identifies a position whose literal target character could distinguish this word, while a `0` identifies a position where keeping the character would not help because the word contains the same character there.

Suppose the target is `apple` and a same-length word is `ample`. They differ only at position `1`, so that word's difference mask has only bit `1` set. Any unique abbreviation must keep the target's `p` at that position. If the position is hidden by a number, the same abbreviation also describes `ample`.

If no dictionary word has the target's length, `differences` is empty. Then the shortest possible abbreviation is the one numeric run covering the whole target, returned as `str(length)`. Its abbreviation length is one token, regardless of whether the decimal text has one digit or several.

**The exact uniqueness condition**

Let `mask` describe the target abbreviation and `difference` describe one competing word. The expression

`mask & difference`

contains the positions that are both kept literally and different between the two words. If this intersection is nonzero, at least one visible target letter disagrees with the competitor, so the abbreviation cannot abbreviate that word.

If the intersection is zero, every literal position selected by `mask` contains the same character in both words. All other positions are skipped in identical run lengths because the words have equal total length. The abbreviation therefore matches the competitor as well and is not unique.

The required mask must consequently satisfy `mask & difference != 0` for every stored difference mask. In set language, it must choose at least one position from every set of differing positions. This is a minimum-cost hitting-set problem, where cost is abbreviation token length rather than simply the number of selected positions.

The constraint that `dictionary` does not contain `target` guarantees that each relevant difference mask has at least one set bit. An identical word would have `difference == 0`, and no abbreviation of the target could distinguish it.

**Measure the problem's definition of length correctly**

The helper `abbreviation_length(mask)` scans the target positions from left to right. Each kept letter contributes one token. Each maximal consecutive run of abbreviated positions also contributes one token, even if its written decimal count has multiple digits.

The helper increments `tokens` once at the beginning of each next item. If the current bit is `1`, it advances by one position. If the bit is `0`, the nested loop skips the entire zero run before another token is counted. This exactly implements the stated length definition: unchanged letters plus replaced substrings.

For a length-12 target, the all-zero mask has cost `1` because it renders as `12`, one replaced substring. A mask keeping the first and final letters has cost `3`: one letter, one numeric run, and one letter. Counting characters in the rendered string would incorrectly give a different result whenever a run length uses multiple digits.

**Search only branches that can solve a current conflict**

The search begins with `mask = 0`, meaning every target position is abbreviated. For the current mask, it collects `uncovered`: all dictionary difference masks for which `mask & difference == 0`. These are precisely the words that the current abbreviation still matches.

If `uncovered` is empty, the mask is unique. Its measured length is compared with `best_length`, and it replaces `best_mask` only when strictly shorter. The problem permits any answer among ties, so there is no need to replace an equally short result.

If conflicts remain, the algorithm selects one of them with

`min(uncovered, key=int.bit_count)`.

This chooses a difference mask containing the fewest possible distinguishing positions. Any completion of the current mask must keep at least one bit from this particular mask; otherwise that word remains indistinguishable. The loop extracts each available bit with `bit = remaining & -remaining`, recursively explores `mask | bit`, and removes that choice from `remaining`.

This branching is complete: every valid final mask extending the current one must occur in at least one branch, because it must select one of the chosen conflict's bits. Choosing the smallest conflict first is a search heuristic that tends to reduce branching. It affects speed, not correctness.

The `seen` set prevents the same mask from being evaluated repeatedly when different orders of choices reach it.

**Why the length pruning is safe**

Before branching, the algorithm computes `candidate_length`. If it is already at least `best_length`, the branch stops. Adding kept bits can never reduce abbreviation token length. Turning a zero bit into a kept letter either replaces a one-position numeric run with one letter, leaving the token count unchanged, or breaks/shortens a larger numeric run while adding a literal, increasing the token count. It cannot merge tokens or make the representation shorter.

Therefore every descendant of a mask has length at least that mask's length. Once the current cost cannot beat the best known result, no descendant can beat it either.

The initial best mask keeps every target letter: `(1 << length) - 1`. This is always unique because the dictionary does not contain `target`, and its length is `length`. It provides a valid upper bound before the first recursive call.

**Reconstruct the abbreviation**

After the best mask is known, the final loop walks through `target`. A zero bit increments `abbreviated`, the length of the current hidden run. On a one bit, any pending count is appended first, then the literal target character is appended. A final pending count is appended after the loop. Joining `parts` produces a syntactically valid abbreviation with no adjacent numbers.

Every selected literal belongs to the target, every number covers exactly its zero-bit run, and the mask has already been proven to hit every relevant difference. The returned string is therefore an abbreviation of `target`, abbreviates no dictionary word, and has minimum possible token length among all such abbreviations.

## Complexity detail

Let $m$ be the target length, let $d$ be the number of dictionary words having length $m$, and let $p$ be the number of target positions that appear as a difference in at least one relevant word. Only those $p$ positions can help distinguish a word, so at most $2^p$ useful masks need to be considered.

Building all difference masks takes $O(dm)$ time. For each visited search mask, forming `uncovered` checks up to $d$ masks and `abbreviation_length` scans up to $m$ positions. In the worst case the search visits $2^p$ masks, giving

$$
O\bigl(dm + (d+m)2^p\bigr)
$$

time, conventionally summarized by the manifest as $O((d+m)2^p)$. Reconstructing the chosen abbreviation costs another $O(m)$ time.

The `differences` list uses $O(d)$ machine integers, and `seen` can hold $O(2^p)$ masks. The recursive call stack is at most $O(p)$ deep, while the temporary `uncovered` list can hold $O(d)$ references. The dominant bound is $O(d + 2^p)$ auxiliary space. Python integers can represent all needed bits, and the contract limits $m$ to 21, making each mask compact.

The relation $\log_2(n)+m \le 21$ when the dictionary is nonempty is designed to keep this exponential search practical: larger dictionaries are paired with smaller target lengths.

## Alternatives and edge cases

- **Enumerate every one of the `2^m` masks:** Test each abbreviation against every relevant word and keep the shortest. This is conceptually simpler and has the same broad exponential ceiling, but it ignores conflict-directed branching and length pruning, so it performs much more unnecessary work in typical inputs.
- **Breadth-first search by number of kept letters:** The objective is not the number of one bits. Keeping one letter can split a numeric run into several tokens, so masks with the same popcount can have different abbreviation lengths. A correct search must use the problem's token-cost definition.
- **Generate abbreviation strings directly:** String recursion makes conflict testing and deduplication cumbersome. Bitmasks give constant-time intersection tests and a canonical state representation.
- **Different-length dictionary words:** They are deliberately ignored because an abbreviation's expanded length is fixed. Comparing their characters would waste work and could produce false restrictions.
- **Empty dictionary or no same-length words:** The all-number abbreviation `str(len(target))` is immediately valid and has the absolute minimum length of one token.
- **Dictionary word differing at one position:** That sole difference bit is mandatory. The selected minimum-bit-count conflict exposes this forced choice immediately.
- **Several shortest answers:** The strict `<` update retains the first one found. This is valid because the contract accepts any minimum-length abbreviation.
- **Multi-digit skip counts:** A count such as `12` is one abbreviation token, not two. Both the length helper and reconstruction preserve that distinction.
- **No adjacent replaced substrings:** Consecutive zero bits are emitted as one accumulated count, so the result never contains adjacent numeric components.
- **Identical dictionary entry:** Such an entry would have a zero difference mask and make uniqueness impossible. The contract explicitly guarantees that `target` is absent from `dictionary`.
- **Letter case and alphabet:** Inputs contain lowercase English letters, and direct character comparison correctly identifies all differing positions without normalization.
