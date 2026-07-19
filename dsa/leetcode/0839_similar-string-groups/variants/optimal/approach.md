## General
**Reduce one-swap similarity to mismatch counting**

Compare each unordered pair of strings character by character. Stop once more than two differing positions have been found. Identical strings have zero mismatches and are similar. Because the contract guarantees the strings are anagrams, exactly two mismatches must contain the same two letters in opposite order, so swapping those positions makes the strings equal. A pair with more than two mismatches is not directly similar.

**Merge links rather than materializing paths**

Create one disjoint-set component per list position. Whenever a pair is similar, union their representatives. Path compression and union by size keep later operations nearly constant. Direct similarity need not be transitive, but union-find deliberately computes its transitive closure: every chain of pairwise links receives one representative.

After all pairs have been considered, two indices have the same representative exactly when a similarity path connects their strings. Counting distinct representatives therefore gives precisely the number of required groups.

## Complexity detail
There are $g(g-1)/2$ unordered pairs, and a similarity check examines at most $\ell$ characters. Disjoint-set operations contribute only an inverse-Ackermann factor, so the stated bound is $O(g^2\ell)$ time. Parent and component-size arrays use $O(g)$ space.

## Alternatives and edge cases
- **Build an explicit graph and traverse it:** Pairwise checks followed by DFS or BFS have the same $O(g^2\ell)$ time but can require $O(g^2)$ space for all similarity edges.
- **Generate every one-swap neighbor:** Hashing list strings and trying position pairs can be attractive when $\ell$ is much smaller than $g$, but constructing and looking up all swapped candidates requires careful handling of duplicates and string-copy cost.
- **Repeated transitive-closure scans:** Rechecking reachability through every intermediate string is correct but can add a cubic factor in $g$.
- **Identical strings:** Zero mismatches qualifies as similar, so duplicate entries must be merged.
- **Two mismatches:** The anagram guarantee is what ensures the two differing characters cross-match after a swap.
- **Indirect membership:** Two strings with more than two mismatches may still share a group through intermediate strings.
- **Single string:** One isolated entry forms exactly one group.
