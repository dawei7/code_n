## General

**Process words from left to right**

A legal pair requires $i<j$. When current word `w=words[j]` is processed, every word recorded in `cnt` comes from an earlier index and automatically satisfies the index order.

The partner needed for `w` is its reversal `w[::-1]`. The code adds how many such earlier words have been seen:

`ans += cnt[w[::-1]]`.

Only afterward does it record the current word with `cnt[w] += 1`.

**Why update order matters**

Recording `w` before checking would let a palindromic word such as `"aa"` match itself at the same index. That is illegal because a pair needs two distinct indices with the earlier one strictly smaller.

Checking first ensures the current occurrence can pair only with previous occurrences.

Under the problem's distinct-word guarantee, there is at most one previous occurrence of any reversal, so the added count is zero or one.

**Why every reverse pair can be counted independently**

Every word has exactly one reversal. If `"ab"` pairs with `"ba"`, neither word can be the reversal partner of a third distinct string: the reversal of `"ab"` is uniquely `"ba"` and vice versa.

Thus discovered pairs cannot compete for the same word. There is no need to remove matched words from the Counter or solve a general matching problem.

The distinctness guarantee is central to this exact simplicity. With duplicate words, counts and one-use constraints would require consuming available occurrences carefully.

**Palindromic two-letter words**

A word such as `"zz"` equals its own reversal. Because words are distinct, there cannot be another `"zz"`. Checking before insertion yields zero, so it forms no pair.

This matches the rule that one string can belong to at most one pair and cannot pair with itself.

**Trace the first example**

Process `"cd"`: its reversal `"dc"` has count zero, then record `"cd"`.

Process `"ac"`: `"ca"` has not appeared, then record `"ac"`.

Process `"dc"`: its reversal `"cd"` has count one, so answer becomes one.

Process `"ca"`: `"ac"` has count one, so answer becomes two.

Process `"zz"`: it has not previously appeared, so no self-pair is counted. Final answer is two.

**Why ans is the maximum, not just a greedy count**

Each unordered reversal class is either:

- two distinct strings `w` and `reverse(w)`, permitting exactly one pair if both occur;
- one palindromic string, permitting no pair because it occurs once;
- a single nonpalindromic word whose reversal is absent, permitting no pair.

Classes are disjoint. The scan counts one for every complete two-string class. Since those pairs share no words, all can be chosen simultaneously. No solution can take more than one pair from a class, so the count is globally maximal.

**Counter versus set**

Because input words are distinct, a set would be sufficient. The exact code uses `Counter`, and lookup of a missing reversal conveniently returns zero rather than requiring a membership branch.

The arithmetic formulation also generalizes partway to duplicates, although without decrementing counts it would then count pair combinations rather than enforce one-use matching.

**String reversal cost**

Each word has length exactly two. `w[::-1]` therefore creates a constant-size string. The stated linear time relies on this fixed length. For general length $L$, reversal would cost $O(L)$ per word.


When current index `j` is processed, `cnt` contains exactly the earlier words. The algorithm increments `ans` exactly when the unique reversed partner is among them. Every valid reverse pair is detected when its later endpoint arrives, and no pair is detected twice. Distinct words make reversal classes disjoint, so every detected pair can coexist and every possible pair is detected. Hence `ans` is the maximum number of disjoint pairs.

## Complexity detail

Let $n$ be the number of words. Every word undergoes one constant-length reversal, one expected $O(1)$ Counter lookup, and one expected $O(1)$ update. Total expected time is $O(n)$.

The Counter stores up to $n$ distinct two-character strings, so auxiliary space is $O(n)$. Since only $26^2=676$ possible legal words exist, the space is technically bounded by a fixed universe, but $O(n)$ is the natural input-relative and manifest bound.

The answer itself uses constant scalar space.

## Alternatives and edge cases

- **Hash set:** Sufficient under distinctness; check the reversal and then insert the current word.
- **Nested pair scan:** Direct but costs $O(n^2)$ time.
- **Remove a matched reversal:** Unnecessary for distinct words because no third word can need the same unique partner.
- **Palindromic word:** Cannot pair with itself and cannot have a duplicate under the constraints.
- **Reversal absent:** The word contributes no pair.
- **All words in reversal classes:** The answer is half the number of nonpalindromic words.
- **Check before insert:** Prevents illegal self-pairing.
- **Fixed length two:** Makes reversal constant time.
- **Distinctness removed:** The exact Counter accumulation would overcount combinations relative to one-use pairing.
- **Input order:** Only determines which endpoint discovers a pair; the final maximum is order-independent.
