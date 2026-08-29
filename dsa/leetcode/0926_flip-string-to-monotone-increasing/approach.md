## General

Every monotone increasing binary string has a split point:

- positions before the split are all `0`;
- positions at or after the split are all `1`.

The split may be before the first character, producing all ones, or after the last character, producing all zeros. The solution evaluates the flip cost of every split in linear time.

Let `tot` be the total number of zeros in the string. During the scan:

- `i` is the prefix length, because enumeration starts at one;
- `cur` is the number of zeros in the first `i` characters.

For a split after that prefix, two kinds of mistakes must be flipped.

**Ones in the prefix must become zeros.** The prefix has length $i$ and contains `cur` zeros, so its number of ones is

$$
i-\text{cur}.
$$

Every one there violates the required all-zero prefix.

**Zeros in the suffix must become ones.** The entire string has `tot` zeros, of which `cur` are in the prefix. The suffix therefore contains

$$
\text{tot}-\text{cur}
$$

zeros to flip.

The exact cost is

$$
(i-\text{cur})+(\text{tot}-\text{cur}),
$$

which is the expression `i - cur + tot - cur`.

**Include the split before the string.** Before scanning, `ans = tot`. If the split is at position zero, the whole result must be ones, so every original zero is flipped and the cost is exactly `tot`.

The loop then evaluates splits after positions 1 through $n$, including the split after the entire string. At the final split, `cur = tot` and the cost becomes the total number of ones, corresponding to flipping the whole string to zeros.

**Why evaluating splits is exhaustive.** Any monotone increasing result has some first position containing 1; choose that as its split, with a split after the end if no 1 exists. For a fixed split, every wrong-side bit must be flipped, and flipping exactly those bits is sufficient. Thus the formula is the minimum for that split, and taking the minimum across all splits gives the global optimum.

For `s = "00110"`, total zeros are three. The split after the fourth character has one prefix one too many? More directly, the prefix `0011` contains two ones that already belong on the one side if the split is after the leading zeros, while the final suffix zero is wrong. Evaluating the split after the first two characters gives prefix-one cost zero and suffix-zero cost one, so answer one.

For `"010110"`, different splits yield different tradeoffs: moving the split right reduces suffix zeros but increases prefix ones. The minimum cost two appears at a boundary corresponding to results such as `000111` or `011111`.

The split scan can be visualized as a small cost table. Moving the boundary one position right changes only the character crossed. Crossing a zero removes one zero from the suffix cost and adds no prefix-one cost, so the total decreases by one. Crossing a one adds one prefix-one flip and removes no suffix zero, so the total increases by one. The running formula updates these effects implicitly through `i` and `cur`.

This view also explains why the minimum may occur at several boundaries. A sequence of alternating zero and one crossings can make the cost fall and rise repeatedly, so a greedy rule based only on the first inversion is insufficient. Recording the minimum across all boundaries is necessary.

**Why only zero counts are stored.** Prefix ones are derived from prefix length minus prefix zeros. Suffix zeros are total zeros minus prefix zeros. These identities avoid maintaining separate prefix and suffix arrays.
After reading `i` characters, `cur` is their exact zero count and `ans` is the minimum cost among all split positions from zero through $i$. The current formula evaluates the newly available split after `i` and the minimum update preserves the invariant. After all characters, every split has been considered.

The code uses `int(c == "0")` to add one for a zero and zero for a one.

## Complexity detail

Let $n$ be the string length. `s.count("0")` is one linear pass and the loop is another linear pass.

- **Time complexity:** $O(n)$.
- **Space complexity:** $O(1)$ auxiliary space.

Two passes differ only by a constant factor. No transformed string or prefix array is constructed.

## Alternatives and edge cases

- **One-pass dynamic programming:** Track ones seen and minimum flips so far; on a zero, either flip it or flip all previous ones. This also gives $O(n)$ time and $O(1)$ space.
- **Prefix/suffix arrays:** Precompute prefix ones and suffix zeros, then minimize their sum. It is clear but uses $O(n)$ space.
- **Try every split by rescanning:** Correct but costs $O(n^2)$.
- **Already all zeros:** The final split has cost zero.
- **Already all ones:** The initial split has cost zero.
- **Already monotone mixed string:** Its existing zero/one boundary yields zero.
- **Single character:** Either boundary choice gives zero without a required flip.
- **Alternating bits:** The scan balances accumulated prefix ones against remaining suffix zeros.
- **Split before first:** Represents an all-one result and is covered by initial `ans`.
- **Split after last:** Represents an all-zero result and is covered by the final loop iteration.
- **Equality of optimal splits:** Several different monotone results may use the same minimum number of flips; only the number is returned.
- **Nonempty result:** Flips change bits but never remove characters, so every split interpretation preserves length.
- **Binary-only contract:** Counting zeros automatically classifies every other character as one.
