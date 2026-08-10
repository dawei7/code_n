## General

**Convert minimum length into maximum saved overlap**

If word `b` follows word `a`, part of `b` may already be a suffix of `a`. Joining `"abcd"` to `"cdef"` needs only `"ef"` because `"cd"` overlaps.

No input word is a substring of another. Therefore, each word must contribute something, and an ordering's final length equals the sum of all word lengths minus the overlaps saved between consecutive words. Since the sum of word lengths is fixed, minimizing length is equivalent to maximizing total saved overlap.

**Precompute directed overlaps**

The matrix `g[i][j]` is the largest `k` for which the final `k` characters of `words[i]` equal the first `k` characters of `words[j]`.

For every ordered pair of different words, candidate lengths are tested from largest to smallest. The first match is maximum. Direction matters: the overlap for `i` followed by `j` can differ from the overlap for `j` followed by `i`.

Once `g` is known, placing `j` after `i` requires appending only `words[j][g[i][j]:]`.

**Subset dynamic programming**

A bitmask records which words have been used. Bit `j` is one exactly when word `j` belongs to that subset.

State `dp[mask][j]` is the maximum total overlap of an ordering that uses exactly the words in `mask` and ends at word `j`. Table `p[mask][j]` records the preceding word for reconstruction.

To calculate a state ending at `j`, the code removes `j`:

`previous = mask ^ (1 << j)`.

Every word `k` present in `previous` can be the predecessor. That choice gives:

`dp[previous][k] + g[k][j]`.

The largest candidate becomes `dp[mask][j]`, and `p[mask][j]` stores its `k`. Singleton states need no edge, so their overlap is zero and parent remains minus one.

This state is sufficient because future choices care only about which words have already been used and which word is currently last. The detailed earlier order matters only through its best accumulated overlap.

**Choose an endpoint and reconstruct**

For the full mask, the code chooses an ending word with maximum DP value. It starts with that word and repeatedly follows its parent. Before moving to the parent, it removes the current word's bit, reaching the exact smaller state from which that parent transition was selected.

These indices are collected backward, so `arr[::-1]` restores forward order.

Updates use strict `v > dp[i][j]`. When every relevant transition adds zero, a state can retain parent minus one despite containing several words. The implementation accounts for this: it makes a set of reconstructed indices and appends all missing word indices. Those missing words did not contribute a recorded positive improvement, and including them ensures every input appears.

The answer begins with the first word in full. For each adjacent pair `i, j`, it appends the suffix of word `j` after the already-covered prefix. Joining these pieces produces one string containing each ordered word as a substring.

**Why maximizing overlap is correct**

Consider an optimal ordering for state `(mask, j)`. Its predecessor is some `k` in `previous`. Removing final word `j` leaves an ordering for state `(previous, k)`. If that prefix did not have maximum overlap for its state, replacing it with a better prefix would improve the full ordering, contradicting optimality.

Therefore, trying every possible predecessor and taking the maximum gives the correct state. Induction on the number of set bits proves the entire DP table.

At the full mask, maximum overlap gives minimum length because individual word lengths are constant. The reconstruction follows transitions that achieve that score. During concatenation, every omitted prefix is already the suffix of the preceding result, while the remainder is appended, so every word is contained. Appended zero-overlap words are also included whole when necessary.

**A useful way to see the constraints**

The number of words is at most twelve, which makes a table over all `2^n` subsets practical. Word lengths are small enough to precompute pairwise overlaps directly. A factorial search over all permutations would grow much faster, while polynomial-only state would not remember enough about which words have been used.

## Complexity detail

Let `N` be the number of words and `W` their maximum length.

The subset DP has `2^N * N` states and checks up to `N` predecessors per state, so it costs `O(2^N N^2)` time. Overlap preprocessing considers `O(N^2)` ordered pairs and up to `W` candidate lengths. In Python, slicing and comparing a candidate can inspect `O(W)` characters, giving a conservative `O(N^2 W^2)` preprocessing bound.

The DP and parent tables use `O(2^N N)` space, and the overlap matrix uses `O(N^2)`. These are the bounds of the exact checked-in code. The current manifest's `O(T)` time and `O(S)` space do not describe this subset DP.

## Alternatives and edge cases

- **Try every permutation:** This evaluates `N!` orders. Subset DP merges permutations sharing the same used set and ending word.
- **Greedily merge the largest overlap:** A locally largest overlap can prevent two later overlaps whose combined saving is greater, so it has no optimality guarantee.
- **Store full superstrings in each state:** It simplifies reconstruction but repeatedly copies strings and consumes much more memory than scores plus parent pointers.
- **One word:** The only full state has overlap zero, and reconstruction returns that word unchanged.
- **No positive overlaps:** Every ordering has the same total length. The missing-index extension produces a valid concatenation.
- **Several shortest answers:** Strict comparison selects one representative among ties, and the problem accepts any shortest result.
- **Directed edges:** Always use `g[i][j]` when `i` precedes `j`. Reversing indices can remove a prefix that is not actually present.
- **Contained words:** The contract excludes them. Without that guarantee, contained words should be removed before applying the length-minus-overlap reasoning.
- **Zero-overlap parent ties:** The explicit missing-word append is important because strict DP updates may leave a reconstructed chain shorter than the full mask.
