# Guided Example: Reverse Words in a String II

We trace an in-place word-order reversal on a fifteen-character array, tracking every swap, and then prove why reversing the whole buffer and then reversing each word inside it is the same as moving words without touching their spelling.

- **Representative input:** the character array spelling `"the sky is blue"`, namely `["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]`.
- **Required outcome:** the same array, mutated in place, spelling `"blue is sky the"`, namely `["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]`.
- **Contrasting instances used later:** the single-element array `["a"]`, which must come back unchanged, and a single-word array such as `["c","o","d","e"]`, which also must come back unchanged.

## 1. Instance and Required Outcome

The input is a mutable array `s` of single characters of length $N$, here $N = 15$. Words are maximal runs of non-space characters, and the words in `s` are guaranteed to be separated by a single space, with no leading or trailing space and at least one word present. The function returns nothing; its entire effect is the mutation of `s`. The array is indexed $0 \dots N-1$:

| Index | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `s[i]` | `t` | `h` | `e` | ␣ | `s` | `k` | `y` | ␣ | `i` | `s` | ␣ | `b` | `l` | `u` | `e` |
| Role | word 1 | · | · | separator | word 2 | · | · | separator | word 3 | · | separator | word 4 | · | · | · |

The requested output keeps the four words, keeps the three separators at positions $3, 7, 10$, and replaces the words in place:

| Index | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `s[i]` | `b` | `l` | `u` | `e` | ␣ | `i` | `s` | ␣ | `s` | `k` | `y` | ␣ | `t` | `h` | `e` |

A tempting reading of "without allocating extra space" is that the answer should be built somewhere else and copied back. That is not the requirement: the mutation must be achieved by rearranging the existing characters, so the auxiliary state must not grow with $N$.

## 2. The Double-Reversal Identity

Write the array as a sequence of words and separators,

$$
s = W_1 \;\text{␣}\; W_2 \;\text{␣}\; \dots \;\text{␣}\; W_k ,
$$

with $k = 4$ in this instance and word lengths $\lvert W_1 \rvert = 3$, $\lvert W_2 \rvert = 3$, $\lvert W_3 \rvert = 2$, $\lvert W_4 \rvert = 4$. Let $\mathrm{rev}(L, R)$ denote the operation that swaps the characters at positions $L$ and $R$, then $L+1$ and $R-1$, and so on until the two indices meet or cross. Applied to a substring $W$, it produces the character-wise reverse $W^{R}$.

Two facts drive the whole method.

1. **Reversal is an involution.** Applying $\mathrm{rev}$ twice to the same range restores the original order, because every swap is undone by itself: $(W^{R})^{R} = W$.
2. **A global reversal reverses the word sequence too.** The separators are single characters and hence their own reverses, and their positions are symmetric about the centre of the array, so

$$
\mathrm{rev}(0, N-1)\bigl(W_1 \;\text{␣}\; \dots \;\text{␣}\; W_k\bigr) = W_k^{R} \;\text{␣}\; \dots \;\text{␣}\; W_1^{R}.
$$

Composing the two operations reverses each word block again, and by fact 1 every spelling is restored:

$$
\bigl(\text{global reversal}\bigr) \;\text{then}\; \bigl(\text{reversal of each word block}\bigr) \;=\; W_k \;\text{␣}\; \dots \;\text{␣}\; W_1 .
$$

That is the requested outcome: the word *sequence* is inverted while every word's *internal* order is preserved.

> **Invariant.** After pass one the words occupy their final positions but are mirrored internally. After pass two every word block is un-mirrored, so the final state is the word-reversed sentence with all characters in their original spelling.

## 3. Pass One: Reversing the Whole Array

Pass one applies $\mathrm{rev}(0, 14)$. The two indices approach the centre, so exactly $\lfloor N/2 \rfloor = 7$ swaps occur and index $7$ is never touched.

| Swap | Left index $L$ | Right index $R$ | Exchanged characters | Array after the swap (spaces shown as ␣) |
|:---:|:---:|:---:|:---|:---|
| 1 | 0 | 14 | `t` ↔ `e` | `e h e ␣ s k y ␣ i s ␣ b l u t` |
| 2 | 1 | 13 | `h` ↔ `u` | `e u e ␣ s k y ␣ i s ␣ b l h t` |
| 3 | 2 | 12 | `e` ↔ `l` | `e u l ␣ s k y ␣ i s ␣ b e h t` |
| 4 | 3 | 11 | ␣ ↔ `b` | `e u l b s k y ␣ i s ␣ ␣ e h t` |
| 5 | 4 | 10 | `s` ↔ ␣ | `e u l b ␣ k y ␣ i s s ␣ e h t` |
| 6 | 5 | 9 | `k` ↔ `s` | `e u l b ␣ s y ␣ i k s ␣ e h t` |
| 7 | 6 | 8 | `y` ↔ `i` | `e u l b ␣ s i ␣ y k s ␣ e h t` |
| — | 7 | 7 | none (indices meet) | `e u l b ␣ s i ␣ y k s ␣ e h t` |

After pass one the array is `eulb si yks eht`. The words are already in the right order — `blue`, `is`, `sky`, `the` — but each reads backwards. The separators have moved too, yet they land exactly where they belong, because reversing a sentence reverses the gaps between words along with the words themselves.

## 4. Pass Two: Restoring Each Word's Spelling

Pass two scans the buffer from left to right, finds each maximal non-space block, and reverses that block. Because the separator positions are now fixed, the blocks are contiguous and disjoint.

| Block | Detected range | Content before | Reversal applied | Content after | Array state (spaces shown as ␣) |
|:---:|:---:|:---:|:---:|:---:|:---|
| 1 | $[0, 3]$ | `eulb` | $\mathrm{rev}(0,3)$: `e`↔`b`, `u`↔`l` | `blue` | `blue ␣ si ␣ yks ␣ eht` |
| 2 | $[5, 6]$ | `si` | $\mathrm{rev}(5,6)$: `s`↔`i` | `is` | `blue ␣ is ␣ yks ␣ eht` |
| 3 | $[8, 10]$ | `yks` | $\mathrm{rev}(8,10)$: `y`↔`s`, `k` unmoved | `sky` | `blue ␣ is ␣ sky ␣ eht` |
| 4 | $[12, 14]$ | `eht` | $\mathrm{rev}(12,14)$: `e`↔`t`, `h` unmoved | `the` | `blue ␣ is ␣ sky ␣ the` |

Each block costs $\lfloor \lvert W_j \rvert / 2 \rfloor$ swaps: 1, 1, 1 and 1 respectively here. Odd-length blocks leave their middle character untouched, which is why `k` and `h` never move during pass two.

## 5. Finding the Word Boundaries With Constant Extra State

Pass two needs no delimiter list and no token copies. It keeps a single integer, the start index of the current block, and advances an end index one position at a time. A block ends in one of two ways, and both must be handled:

- a separator character is met at position `end`, in which case the block is $[\text{start}, \text{end}-1]$ and the next block begins at `end + 1`; or
- the end of the array is reached, in which case the block is $[\text{start}, N-1]$ and the scan stops.

The second case is the one that is easy to omit, and omitting it leaves only the last word of every sentence reversed. It fires here for the block `eht` at $[12, 14]$, the only block not terminated by a space. Because the statement guarantees single-space separation with no leading or trailing space, no empty block can be produced.

| Boundary condition | Guarantee used | Consequence if the code assumed otherwise |
|:---|:---|:---|
| Last word not followed by a space | none needed — the end of the array terminates it | The final word stays mirrored |
| No leading or trailing spaces | stated explicitly | An empty first or last block would be reversed pointlessly |
| Exactly one space between words | stated explicitly | Runs of spaces would create empty blocks and could break the skip |
| At least one word present | stated explicitly | An all-space buffer would produce no blocks at all |

## 6. Correctness of the Composition

**Soundness.** Let the input be $W_1 \dots W_k$ with single-space separators. Pass one produces $\mathrm{rev}(0, N-1)(s) = W_k^{R} \dots W_1^{R}$ by the identity of section 2. Pass two reverses each maximal non-space block, which is exactly the range occupied by some $W_j^{R}$, turning it into $(W_j^{R})^{R} = W_j$. The final array is therefore $W_k \dots W_1$, the word order the task asks for.

**Completeness.** Every non-space character lies in exactly one maximal block, and every block is visited because the scan runs to the end of the array and the two termination cases cover both ways a block can end. No word is left mirrored.

**Purity and degenerate lengths.** Both passes only swap characters inside the buffer, so the result is a permutation of the input multiset: separators stay separators and word lengths are unchanged. A word of length one is its own reverse, so single-character words are unaffected; a single-word array is reversed twice overall and returns to its original spelling.

## 7. Boundary and Trap Analysis

| Instance | Input | Expected result | Why it matters |
|:---|:---|:---|:---|
| Single character | `["a"]` | `["a"]` | Pass one has $\lfloor 1/2 \rfloor = 0$ swaps and pass two one trivial block |
| Single word | `["c","o","d","e"]` | `["c","o","d","e"]` | Global reversal followed by a local reversal is an exact cancellation |
| Every word one character | `["a"," ","b"," ","c"]` | `["c"," ","b"," ","a"]` | Blocks of length one cost no swaps; only the word order changes |
| Two words of unequal length | `["h","i"," ","w","o","r","l","d"]` | `["w","o","r","l","d"," ","h","i"]` | The global pass moves characters across the whole buffer, not word by word |
| Digits and capitals | `["A","1"," ","b","2"]` | `["b","2"," ","A","1"]` | The method is purely positional and never inspects character classes |
| Trailing word of the buffer | any sentence | last word correctly spelled | The block terminated by the array end must be reversed too |
| Token-based rewrite | any sentence | correct string, wrong cost | Splitting into tokens and rejoining allocates $O(N)$ extra space and violates the in-place requirement |

The last row is the one to internalize: a token-splitting rewrite is easy to write and produces the right answer, but its auxiliary space grows linearly with the input, so it fails the stated constraint regardless of its output.

## 8. Complexity Derivation

Let $N = \lvert s \rvert$ and let the word lengths be $\ell_1, \dots, \ell_k$, with $\sum_j \ell_j = N - (k-1)$ because $k-1$ positions are separators.

**Time.** Pass one performs exactly $\lfloor N/2 \rfloor$ swaps, and pass two performs $\sum_{j=1}^{k} \lfloor \ell_j / 2 \rfloor$ swaps. The boundary scan visits each index once. Hence

$$
T(N) = \left\lfloor \frac{N}{2} \right\rfloor + \sum_{j=1}^{k} \left\lfloor \frac{\ell_j}{2} \right\rfloor + O(N) = O(N),
$$

and more sharply the total number of character writes is at most $N$: each character is touched a constant number of times, and no ordering comparison is ever performed.

**Auxiliary space.** The only state beyond the buffer itself is the pair of indices used by the reversal plus the block start and end indices — a constant number of integers:

$$
S(N) = O(1).
$$

This is why the method satisfies the in-place requirement. The token-splitting rewrite instead stores a list of $k$ tokens plus a fresh output buffer, giving $S(N) = O(N)$ and failing the constraint even though its time bound is the same.
