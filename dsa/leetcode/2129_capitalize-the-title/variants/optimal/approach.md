## General

**Normalize one word at a time**

Split the title at its guaranteed single-space separators. For each word,
first inspect its length. If the length is at most two, lowercase every
letter. Otherwise, uppercase the first letter and lowercase the rest. Join the
normalized words with one space.

The input guarantees make this direct transformation exact: splitting cannot
create an empty word, and joining with single spaces reconstructs the original
separator structure. Each word is classified into exactly one of the two
length groups, and its chosen transformation sets every letter to precisely
the required case. Applying the rule independently to all words therefore
produces the required title.

## Complexity detail

Let $n$ be the length of `title`. Splitting, case conversion, and joining
process $O(n)$ characters in total, so the time complexity is $O(n)$. The
normalized words and returned string occupy $O(n)$ space.

## Alternatives and edge cases

- **Character-state scan:** Track word boundaries and rewrite characters
  directly. This also takes $O(n)$ time but needs extra boundary bookkeeping
  before the word length is known.
- **Repeatedly rebuild each word:** Recomputing a word-wide transformation for
  every character is correct but can take $O(n^2)$ time.
- A word of length exactly two follows the all-lowercase rule.
- A word of length exactly three follows the capitalized-first-letter rule.
- A single-letter uppercase title must become lowercase.
- Already normalized titles remain unchanged.
