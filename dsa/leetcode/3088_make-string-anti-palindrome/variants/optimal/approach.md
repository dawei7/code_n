## General

**Translate the requirement into mirrored pairs.** A string of even length $n$ is an anti-palindrome when every position in the first half differs from its mirror in the second half:

$$
s[p]\ne s[n-1-p]
\quad\text{for every }0\le p<n/2.
$$

The characters may be rearranged, and among all valid rearrangements the lexicographically smallest one is required. Lexicographic order is decided at the first position where two candidate strings differ, so small characters should remain as far left as feasibility allows.

**Begin with the absolute lexicographic minimum.** `cs = sorted(s)` arranges every character in nondecreasing order. Among all permutations of the same multiset, this is the lexicographically smallest. If it is already an anti-palindrome, no other answer can be better, and the code immediately joins and returns it.

Why can the source test only the two middle characters before deciding that the sorted string is already valid? In a sorted array, all occurrences of a character are contiguous. A mirrored equality can happen only when one contiguous equal-character block reaches from the first half into the second half. Any block that crosses the half boundary necessarily makes `cs[m - 1] == cs[m]`, where `m = n // 2`. Conversely, if those two characters differ, every character in the first half is at most `cs[m - 1]` and every character in the second half is at least `cs[m]`, so no mirrored pair can be equal.

**Locate the problematic block.** When `cs[m] == cs[m - 1]`, one character occurs on both sides of the midpoint. The pointer `i` starts at `m` and advances while `cs[i] == cs[i - 1]`. Because the array is sorted, this moves to the first index strictly after that repeated block. Characters from `i` onward are therefore larger than the problematic character and can serve as replacements in the second half.

The pointer `j` also starts at `m`, but it has a different role. It visits second-half positions in increasing order. At a position `j`, the mirror is `n - j - 1`. The loop continues while:

`cs[j] == cs[n - j - 1]`.

That condition identifies a still-invalid mirrored pair. The code swaps `cs[j]` with `cs[i]`, then advances both pointers. The left half is left untouched; only the earliest bad positions of the second half receive replacement characters.

**Why these swaps repair the anti-palindrome.** Before `i`, the relevant second-half value belongs to the midpoint-crossing block. At and after `i`, the sorted order guarantees a different, larger value. Swapping that value into the bad second-half position makes it differ from its mirrored first-half character. Each subsequent bad pair receives the next available replacement.

Already valid pairs do not need to be disturbed. The loop's condition stops when `j` reaches a second-half position whose character differs from its mirror. Because only one sorted block can straddle the midpoint, the invalid pairs form the relevant prefix of the second half; repairing them removes the only source of mirror equalities.

**Why the result is lexicographically smallest.** Sorting initially gives the smallest possible first half. The algorithm never changes that first half. Once a repair is unavoidable, it changes positions in the second half from left to right, exactly the order in which they affect lexicographic comparison. For each such position, it takes the earliest available character after the bad block. That is the smallest replacement capable of breaking the equality. A later replacement would be equal or larger and could not produce a lexicographically smaller result.

Although the swap moves the problematic character to a later position, later positions are less important lexicographically. This is the standard greedy exchange: spend the smallest viable larger character at the earliest place that must change, and push the displaced smaller character as far right as the one-to-one swaps allow.

**Detecting impossibility.** If `i >= n` while a bad mirrored pair remains, no character outside the midpoint-crossing block is available as a replacement. Equivalently, the dominant character occurs more than $n/2$ times. Every anti-palindrome has only one slot from each mirrored pair available for any single character, so no character can appear more than $n/2$ times. The source returns `"-1"` exactly when its repair process proves that this necessary capacity is unavailable.

For a small trace, take sorted characters `a a a b b c` with $n=6$. The midpoint lies between indices 2 and 3, and the middle values differ, so it is already anti-palindromic: the mirrors are `(a,c)`, `(a,b)`, and `(a,b)`. By contrast, with `a a b b c c`, the middle boundary is `b,b`. The repair pointer skips beyond the `b` block to `c`, and the earliest bad second-half `b` is exchanged with that `c`.

## Complexity detail

Let $n$ be the string length. Python's `sorted(s)` takes $O(n\log n)$ time and creates a list of $n$ characters. The scans performed by `i` and `j` are monotone: neither pointer moves backward, so all repair work is $O(n)$. Joining the final list also takes $O(n)$ time.

The exact total is therefore $O(n\log n)$ time and $O(n)$ auxiliary space. This differs from the local Optimal manifest, which claims $O(n)$ time. A counting construction over a fixed lowercase alphabet could attain linear time, but the checked-in `solution.py` explicitly uses comparison sorting and must be documented as such.

The swaps themselves are constant-time list operations. No recursion or additional structure proportional to the alphabet is used beyond the sorted character list.

## Alternatives and edge cases

- **Frequency-count construction:** With only lowercase English letters, counts can avoid sorting and achieve $O(n)$ time, but careful lexicographic placement is still required.
- **Try arbitrary swaps:** It may find a valid permutation, but choosing a larger replacement too early can lose lexicographic minimality.
- **Maximum-frequency test first:** Checking whether any count exceeds $n/2$ can reject impossible inputs early; the exact source discovers the same shortage through `i >= n`.
- **Already sorted anti-palindrome:** If the two middle characters differ, the sorted permutation is valid and is globally lexicographically smallest.
- **Exactly half one character:** This is feasible in principle because that character can occupy one side of every mirrored pair.
- **More than half one character:** It is impossible because at least one mirrored pair must contain that character twice.
- **Repeated block crossing the midpoint:** This is the only block capable of causing mirror equality in sorted order.
- **Even length:** The problem contract supplies even length. With odd length, the center would mirror itself and anti-palindromicity under this definition would be impossible.
- **Earliest second-half repair:** Changing `j` before a later bad position is required for lexicographic optimality.
- **Earliest replacement:** `i` points to the smallest character outside the bad block, so using it minimizes the forced increase at `j`.
- **Pointer exhaustion:** Returning `"-1"` is not a loop failure; it is the constructive proof that too many copies of the dominant character exist.
- **Duplicate replacement characters:** They can be used for consecutive repairs because each is still different from the dominant mirrored character.
- **No mutation of the input string:** Strings are immutable; the algorithm works on the new list `cs`.
- **Source/manifest mismatch:** The implementation is sorting-based $O(n\log n)$, even though the manifest summarizes the fixed-alphabet linear possibility.
