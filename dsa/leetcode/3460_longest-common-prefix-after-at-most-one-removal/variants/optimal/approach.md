## General

**Use two indices because only \(s\) may lose a character.** `i` points into `s` and `j` points into `t`. `j` is also the number of target-prefix characters successfully matched so far. `rem` records whether the one allowed deletion from `s` has already been used.

When `s[i] == t[j]`, the characters extend the common prefix. Both strings advance: the source increments `j` inside the equality branch and increments `i` at the end of the loop.

When they differ and no removal has been used, the only way to continue matching this same `t[j]` is to delete `s[i]`. The source marks `rem = True`, leaves `j` unchanged, and advances only `i`.

At a mismatch after removal has been used, no operation remains that can fix the alignment. The common prefix ends and the loop breaks.

The unconditional increment of `i` at the bottom of the loop is what makes both cases work. After equality, `j` has already advanced, so both pointers move. After the first mismatch, `j` has deliberately not advanced, so only the unwanted source character is consumed. Reading the code this way avoids a common misconception that the mismatch branch somehow accepts `t[j]`; it does not. That target character still has to equal the next available character of `s` on a later iteration.

**Why deleting at the first mismatch is optimal.** Before the first mismatch, `s[0..i-1]` and `t[0..j-1]` already match. Deleting any earlier matched character would shift subsequent characters and lose that established prefix. Deleting a later character leaves the current mismatch unchanged. If an optimal solution extends beyond this mismatch, it must delete the current `s[i]`. Therefore, the greedy choice is forced.

It is also legal not to remove anything. If all compared characters match until one string ends, `rem` may remain false and `j` is the ordinary common-prefix length.

For `s = "madxa"` and `t = "madam"`, the first three letters match. At `x` versus `a`, the source skips `x`. The following `a` matches, making `j=4` before `s` ends.

For `s = "leetcode"` and `t = "eetcode"`, the very first mismatch deletes `l`, after which all seven target characters match.

For `s = "a"` and `t = "b"`, deleting `a` leaves no character to match `b`, so `j` stays zero.

Consider also `s = "abxcde"` and `t = "abcdef"`. The scan matches `a` and `b`, skips `x`, and then matches `c`, `d`, and `e`. It stops when `s` ends with `j = 5`; deleting one character cannot manufacture the missing target `f`. By contrast, with `s = "abxcdef"`, the same forced skip lets `j` reach the complete target length $6$. These examples show that the deletion repairs alignment but does not change the number of remaining source characters.

**Why the returned value is \(j\).** Only equality increments `j`, so it counts exactly how many consecutive characters from the beginning of `t` have been matched after the optional skip in `s`. The loop never skips a character of `t`, which would be illegal. When it stops, no longer common prefix can be formed under the forced-first-mismatch argument.

If `t` ends first, all of `t` is a common prefix and `j == len(t)`. Extra characters in `s` do not matter. If `s` ends first, no further target prefix character can be supplied, even if the deletion was unused.

There is no need to use the deletion after `t` has been fully matched. The phrase “at most one” means an unused operation is allowed, and deleting a trailing source character cannot increase a prefix beyond the entire length of `t` anyway. Similarly, when both strings already share a long ordinary prefix, greedily preserving every equality is always safe: removing a character that already matches would make the very next target position unmatched and cannot create a longer prefix.
At the top of every iteration, the first `j` characters of `t` equal the sequence consumed from the first `i` characters of `s` after deleting at most the one marked character. Equality extends this invariant; the first mismatch consumes the only forced deletion. A second mismatch or an exhausted string proves extension impossible. Thus the final `j` is optimal.

The stopping argument deserves emphasis. At a second mismatch, the current source and target characters are unequal, and the only permitted deletion has already been spent. Advancing both would falsely count unequal characters; advancing only `t` would delete from the wrong string; advancing only `s` would require a second deletion. Since every legal continuation is ruled out, breaking is not a heuristic choice—it proves that no longer prefix can be obtained.

The source stores no reconstructed string. It obtains the length directly from the aligned scan.

## Complexity detail

Each loop iteration advances `i`, and `j` never decreases. At most `len(s)` iterations occur, stopping no later than target exhaustion. Time is $O(\min(n,m+1))$, conventionally stated as $O(\min(n,m))$ up to the one possible skipped character.

Only two indices and one Boolean are stored, so auxiliary space is $O(1)$, matching the manifest.

The scan performs no slicing or concatenation. If it created `s[:i] + s[i+1:]` to test a deletion, that new string would require linear space and repeated comparisons. Keeping the deletion as a Boolean alignment state is what preserves constant auxiliary memory.

## Alternatives and edge cases

- **Try deleting every position:** Recomputing a prefix for each choice can take $O(n^2)$ time.
- **Dynamic programming:** A two-state matched-prefix DP works but is unnecessary because the first useful deletion is forced.
- **Delete from \(t\):** The operation permits removal only from `s`; `j` must never skip.
- **No mismatch:** No removal is needed, and the shorter-string length is returned.
- **Mismatch at index zero:** The source correctly tries deleting the first character of `s`.
- **Second mismatch:** With the budget spent, matching stops immediately.
- **\(s\) one character longer:** One deletion may allow all of `t` to match.
- **\(t\) longer than \(s\):** At most the available post-deletion characters can contribute.
- **At most one removal:** Leaving `rem` false is a valid outcome.
- **Input preservation:** Indices scan immutable strings without constructing modified copies.
