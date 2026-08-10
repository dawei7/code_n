## General

Each word contains lowercase English letters with no repeated letter. Because the conversion may rearrange the result arbitrarily, letter order does not matter. A word is fully characterized by the set of letters it contains.

The conversion adds exactly one letter that was absent before. Therefore a target word is obtainable exactly when deleting one of its letters leaves the letter set of some start word.

**Encode a letter set as a 26-bit integer**

Assign bit $0$ to `'a'`, bit $1$ to `'b'`, and so on through bit $25$ for `'z'`. For a character `c`, the expression `1 << (ord(c) - 97)` creates an integer with only that character’s bit set. The code builds a word’s mask with `sum(1 << (ord(c) - 97) for c in w)`.

Usually bit masks are combined with bitwise OR. Summation is equally correct here because the constraints guarantee no letter repeats within a word. Every added power of two occupies a different bit, so no carries occur. For example, `"act"` maps to the bits for `a`, `c`, and `t` regardless of the letters’ order.

Two words containing exactly the same letters produce the same mask. That is desirable because arbitrary rearrangement makes them interchangeable for this problem.

**Store all possible predecessor masks**

The set comprehension converts every string in `startWords` and stores its mask in `s`. A set provides expected $O(1)$ membership testing. If multiple start words have the same letter set in different orders, they collapse to one mask, but multiplicity is irrelevant: a target only asks whether any qualifying start word exists, and start words are not consumed or changed.

**Reverse the mandatory addition**

For each target word `w`, the solution first computes its complete mask `x`. It then tries every character `c` in that target and evaluates `x ^ (1 << (ord(c) - 97))`.

The target contains `c` exactly once, so its bit is currently set in `x`. XOR with the same one-bit mask turns that bit off and leaves every other bit unchanged. The result is exactly the letter set obtained by deleting `c` from the target.

If that reduced mask occurs in `s`, there is a start word containing all the target’s other letters and not containing `c`. Appending `c` is legal because it was absent from the start word. The resulting letter set equals the target’s, and arbitrary rearrangement can place those letters in the target’s order. The target is therefore obtainable.

The solution increments `ans` and immediately executes `break`. A target must be counted once even if several different deletions match start words. Breaking prevents multiple successful predecessor choices from counting the same target repeatedly.

If none of the target’s deletions produces a stored start mask, no conversion can form it. Any legal conversion adds one of the target’s letters; reversing that addition would have appeared among the tested deletions. The target contributes nothing.

**Why exact length differences are handled automatically**

Deleting one set bit reduces the number of letters by exactly one. A stored start mask can match only if its word has exactly one fewer distinct letter than the target. The algorithm does not need a separate length comparison.

This also explains why an identical start word does not by itself qualify. If `"act"` is both a start and target, the conversion must still append a new letter, producing four distinct letters. Every one-letter deletion of target `"act"` has only two letters, so the unchanged three-letter start mask is never matched.

For the target `"tack"`, deleting `k` leaves the mask for `"tac"`, which is the same set as start word `"act"`. The membership test succeeds even though their orders differ. Appending `k` and rearranging yields `"tack"`.

**Why the reverse test is complete**

Suppose the algorithm accepts a target. Its matched reduced mask corresponds to a start word, and the removed target letter is absent from that mask. Adding that letter and rearranging gives the target, so every accepted target is truly obtainable.

Conversely, suppose some start word can produce the target. The operation adds exactly one previously absent letter. Delete that added letter from the target’s set; the remaining set is exactly the chosen start word’s mask. The loop tests that target character, finds the mask in `s`, and accepts. Thus no obtainable target is missed.

## Complexity detail

Define $L$ as the sum of the lengths of every word in `startWords` and `targetWords`. Building all start masks processes each start character once. For a target of length $\ell$, building `x` costs $O(\ell)$ and trying every possible deleted character costs another $O(\ell)$ expected time because each set lookup is expected $O(1)$. Summed across all words, total expected time is $O(L)$.

Let $s$ be the number of distinct masks produced by `startWords`. The stored set uses $O(s)$ space, matching the manifest. Each mask is one integer, and the per-target variables use constant extra space. Since masks have only 26 bits, there are at most $2^{26}$ theoretical letter sets, but $O(s)$ is the useful input-sensitive bound.

The character generators used while summing masks are consumed lazily and do not construct per-word character lists.

## Alternatives and edge cases

- **Sort every word:** Sorting converts each word to an order-independent canonical string, after which every one-letter deletion can be tested. This is simpler conceptually but costs $O(\ell\log\ell)$ per word instead of linear mask construction.
- **Store sorted start words by length:** This can narrow candidates but still requires building deletion strings or sorting target variants. Bit removal is constant time after the target mask is built.
- **Try adding letters to every start word:** Each start has up to 26 possible additions, and generated results could be stored. This can work, but reversing the operation from each target tests only its own at most 26 letters and directly enforces the one-letter difference.
- **Bitwise OR instead of sum:** OR is the conventional mask construction and would produce the same result. Summation is safe only because no word contains a repeated letter.
- **Repeated letter outside the contract:** With duplicates, summing the same bit twice could carry into another bit and XOR deletion would no longer represent removing one occurrence. The uniqueness guarantee is essential to the exact encoding.
- **One-letter target:** Removing its only letter yields mask zero. It can match only an empty start word, but start words have minimum length one, so such a target is never obtainable.
- **Target length 26:** Every lowercase letter is already present. It can be formed from a 25-letter start word by adding its unique missing letter, and the deletion loop checks all 26 possibilities.
- **Same word in both arrays:** Equality alone does not qualify because one new letter must be appended. The deletion-based test correctly demands a predecessor with one fewer letter.
- **Anagram start words:** They map to the same mask. Collapsing them in `s` loses no useful information because only existence matters.
- **Duplicate target words:** Each array entry is checked independently. If a target value appears multiple times and is obtainable, each occurrence increments `ans` once.
- **Several matching predecessors:** The `break` ensures one target contributes exactly one to the count even if deleting different letters finds different start masks.
- **Missing predecessor:** Exhausting all target letters proves failure because every legal conversion has exactly one added letter that could be reversed.
- **Start words remain reusable:** The algorithm never removes masks from `s`. This matches the note that checking one target does not consume or modify a start word.
- **Letter order:** Masks deliberately erase order because the conversion permits arbitrary rearrangement after appending.
