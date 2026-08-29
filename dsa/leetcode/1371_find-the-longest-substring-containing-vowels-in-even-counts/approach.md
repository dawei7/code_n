## General

**Track parity, not exact counts**

The condition asks whether each vowel count is even. The exact number of occurrences is unnecessary: only its parity, even or odd, matters. One bit can store that information for one vowel. Reading another copy of the vowel flips its parity, which is exactly what XOR with that bit does.

The variable `mask` represents vowel parities in the prefix ending at the current index. A zero bit means the corresponding vowel has appeared an even number of times in that prefix; a one bit means it has appeared an odd number of times.

The exact code chooses bit position `ord(c) - ord("a")`. Thus `a` uses position zero, `e` position four, `i` position eight, `o` position fourteen, and `u` position twenty. These bits are not adjacent, but they are distinct, which is all correctness requires. Only five bits can ever vary, so there are still only $2^5=32$ reachable masks despite the largest bit position being twenty.

When `c` is a vowel, `mask ^= 1 << (...)` flips its unique bit. When `c` is a consonant, the condition is false and `mask` remains unchanged because consonants do not affect the requirement.

**Why equal prefix masks identify a valid substring**

Suppose the parity mask after index $j$ equals the mask after index $i$, where $j<i$. For each vowel, the parity accumulated through $j$ and through $i$ is the same. Removing the earlier prefix means XORing those parities; equal bits cancel to zero. Therefore every vowel occurs an even number of times in substring `s[j + 1:i + 1]`.

The converse is also true. If every vowel count in that substring is even, moving from the prefix at $j$ to the prefix at $i$ flips every vowel bit an even number of times, leaving the mask unchanged. Hence valid substrings correspond exactly to pairs of equal prefix masks.

This converts a substring search into a repeated-state search: at each right endpoint $i$, find an earlier endpoint with the same mask and measure the distance.

**Why only the first occurrence of a mask is stored**

The dictionary `d` maps each seen mask to its earliest prefix-ending index. If the current mask has been seen at index $j$, the valid substring length is `i - j`. For a fixed current $i$, the smallest possible $j$ produces the longest substring. Therefore replacing the stored index with a later occurrence could only make future candidates shorter.

The `else` branch stores `d[mask] = i` only when the mask is new. Once recorded, its earliest index remains unchanged for the entire scan.

**Why mask zero starts at index negative one**

Before reading any characters, every vowel has count zero, so the parity mask is zero. This empty prefix is conceptually located just before the string, at index $-1$. Initializing `d = {0: -1}` allows a valid substring beginning at index zero to use the same formula.

For example, if the mask after index five is zero, then `i - j` becomes `5 - (-1) = 6`, correctly measuring `s[0:6]`. Without the virtual entry, whole-prefix answers would require a separate special case and might be missed.

**Step-by-step behavior**

`ans` and `mask` both begin at zero. For each character at index `i`, the code first updates the mask if necessary. If that resulting state already exists in `d`, the substring after its earliest occurrence through `i` has all-even vowel counts, and `ans` is updated with its length. Otherwise, the current index becomes the first occurrence of the new state.

Consonant runs demonstrate why unchanged masks are useful. In `"bcbcbc"`, the mask remains zero at every index. Its earliest stored position stays $-1$, so candidate lengths grow from one through six and the entire string is returned.

**Why the algorithm is correct**

Every candidate used to update `ans` lies between two equal prefix masks, so all five vowel parities in that substring are even. Thus the algorithm never records an invalid length. Conversely, take any valid substring ending at $i$ and let $j$ be the preceding prefix endpoint. Its endpoint masks are equal. The dictionary stores an occurrence of that same mask no later than $j$, so the candidate examined at $i$ is at least as long as this valid substring. Consequently, the maximum recorded length is at least the optimum and cannot exceed it because all recorded candidates are valid. The returned `ans` is exactly the longest valid length.

## Complexity detail

Let $n$ be the length of `s`. The loop reads every character once. Membership testing, bit operations, dictionary lookup, and arithmetic are expected $O(1)$ operations, so total time is $O(n)$.

Although `d` is a dictionary, it can contain at most 32 reachable parity states because only five vowel bits vary. Its size is therefore bounded independently of $n$, giving $O(1)$ auxiliary space. The integers may use sparse bit positions through twenty, but their width is still a fixed constant. These bounds match the manifest.

## Alternatives and edge cases

- **Five-bit contiguous mapping:** Map `a, e, i, o, u` to bit positions zero through four. It is more compact visually and has the same 32 states; the exact code derives distinct positions directly from character codes.
- **Array of 32 first positions:** With contiguous bits, a fixed array can replace the dictionary. The current sparse masks are not indices from zero through 31, so a dictionary is convenient.
- **Five parity booleans:** A tuple of booleans can serve as the prefix state. It is correct but more verbose to update and hash than one integer mask.
- **Brute-force substrings:** Count vowels for every possible substring. Even with prefix counts, examining $O(n^2)$ endpoint pairs is too slow for strings up to $5\cdot10^5$ characters.
- **No vowels:** The mask stays zero, and the virtual index $-1$ makes the entire string the answer.
- **All vowels already even:** The final mask matches an earlier state, often zero, allowing the complete qualifying span to be measured.
- **Odd total counts:** The full string may fail, but equal masks inside it can still identify a long valid interior substring.
- **Repeated state:** The earliest index must not be overwritten; later copies can never produce a longer future span.
- **Substring starting at zero:** `d[0] = -1` handles it without branching.
- **Consonants:** They leave `mask` unchanged but extend the distance from the stored state, which can increase the answer.
- **Empty string outside the contract:** The loop would not run and zero would be returned, consistent with an empty valid substring.
- **Lowercase guarantee:** The membership test explicitly recognizes lowercase `aeiou`, matching the stated input alphabet.
