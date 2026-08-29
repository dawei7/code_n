## General

**Turning many prefix questions into one shared structure**

For every word, the required answer is the sum of the scores of all its non-empty prefixes. The score of a prefix is the number of input words that begin with that prefix. A direct solution could generate every prefix as a separate string, count it in a dictionary, and later look those strings up again. That can work, but repeatedly creating slices such as `word[:i]` copies characters. The solution instead uses a trie, also called a prefix tree, so common prefixes are represented only once and can be followed one character at a time.

Let

$$
S = \sum_{w \in \texttt{words}} \lvert w \rvert
$$

be the total number of characters across all input words. The trie contains a root that represents the empty prefix. Moving from a node through the child for a letter extends the represented prefix by that letter. For example, after following the children for `a` and then `b`, the current node represents the prefix `"ab"`. Words that start the same way share these nodes, which is precisely the sharing this problem needs.

**What each trie node stores**

The `Trie` class has two fields. Its `children` field is a list of 26 positions, one for each lowercase English letter. Character `c` is converted to a zero-based position by `ord(c) - ord("a")`. A missing child is `None`; a present child points to another `Trie` object. This fixed array makes choosing the next edge a constant-time operation.

The `cnt` field records how many inserted words pass through that node. Importantly, the root's count is never used because the empty prefix must not contribute to an answer. Every non-root node corresponds to one non-empty prefix, and its count becomes exactly that prefix's score.

**First pass: insert every word and build the counts**

The method creates one root named `trie` and calls `insert` for every word. Inserting begins at the root. For each character, it finds the appropriate child position, creates a node if that path has not appeared before, moves to the child, and increments that child's `cnt`.

The order of the last two actions matters conceptually: the count belongs to the node for the prefix including the current character. Suppose `"abc"` is inserted. The nodes representing `"a"`, `"ab"`, and `"abc"` each receive one increment. If `"ab"` is inserted afterward, the first two nodes receive another increment while the third does not. Their final counts are therefore 2, 2, and 1, exactly the three prefix scores needed for `"abc"`.

Duplicate words are also handled naturally. Inserting the same path again increments every node on it again, because each occurrence is another string in `words`. No terminal marker is needed: the problem asks how many words pass through each prefix, not how many distinct words end at a node.

After all insertions, consider any trie node representing a prefix `p`. A word increments that node if and only if insertion follows every character of `p`. That happens if and only if `p` is a prefix of the word. Consequently, `node.cnt` equals the number of input words having `p` as a prefix. This establishes the central fact on which the second pass relies.

**Second pass: sum the counts along each word's path**

The list comprehension calls `trie.search(w)` once per input word and preserves the original word order. Despite its name, `search` is not checking whether the full word exists. It walks the word's path and accumulates `node.cnt` after every character.

After the first character, the visited node represents the length-one prefix; after the second, it represents the length-two prefix; and so on. Thus each iteration adds the score of exactly one non-empty prefix, with no prefix skipped and no prefix counted twice. When the walk ends, `ans` is the sum requested for that word.

The defensive `None` check would return the sum accumulated so far if a path were absent. In this program, every searched word was inserted during the first pass, so that branch cannot be reached for a valid call. It nevertheless makes `search` safe if reused independently.

For `words = ["abc", "ab", "bc", "b"]`, the `a` and `ab` nodes have count 2 while `abc` has count 1. Walking `"abc"` adds `2 + 2 + 1` and returns 5. On the other root branch, `b` has count 2 and `bc` has count 1, so `"bc"` receives `2 + 1 = 3`. The trie has converted the global question about all words into simple additions along each word's own path.

**Why the returned array is correct**

For a word of length $m$, its non-empty prefixes correspond one-to-one with the $m$ non-root nodes visited while following its characters from the root. The insertion pass makes the count at each such node equal to that prefix's score. The search pass adds all and only those $m$ counts. Therefore each returned value is exactly the sum of the scores of every non-empty prefix of the corresponding input word. Applying the same argument independently to every list position proves the complete result.

## Complexity detail

Using $S$ for the total number of input characters, insertion examines every character once, for $O(S)$ time. Searching examines every character once again, also $O(S)$. Character-to-index conversion, child access, count increments, and additions are constant-time operations, so the combined time is $O(S)$; the factor of two is discarded in asymptotic notation.

At most one trie node is created for each distinct non-empty prefix. There cannot be more distinct prefix nodes than the $S$ character positions processed during insertion, so the trie uses $O(S)$ nodes. Each node allocates a 26-entry child list. Because 26 is a fixed alphabet size, this is still $O(S)$ auxiliary space, although the constant memory cost is significant in Python. The returned answer list uses $O(n)$ space and the temporary traversal variables use $O(1)$ space. Since every word is non-empty, $n \le S$, so including the output does not change the overall $O(S)$ bound.

The loops are iterative, so trie depth does not consume recursion-stack space. In the best case, when many words share prefixes, the number of nodes can be far smaller than $S$; the stated bound describes the worst case.

## Alternatives and edge cases

- **Dictionary of materialized prefix strings:** Count every slice such as `word[:i]` and then sum the stored counts. It is easy to describe, but constructing and hashing each growing prefix can copy or inspect $O(i)$ characters, making the total work potentially quadratic in word lengths rather than linear in $S$.
- **Dictionary keyed by incremental immutable strings:** Building a prefix one character at a time still creates new Python strings because strings are immutable. A trie avoids those repeated full-prefix objects and compares only the next character.
- **Sparse child dictionaries:** Replacing every 26-slot child array with a dictionary stores only edges that exist. It can use less memory when nodes have few children, at the cost of hashing and larger per-edge overhead. The fixed lowercase alphabet makes the array representation straightforward and predictable.
- **Sorting adjacent words:** Lexicographic sorting can expose shared prefixes between neighbors, but converting those relationships into the score of every prefix requires extra bookkeeping. The trie expresses the needed prefix groups directly.
- **One word:** Every prefix is shared by exactly that one word, so a word of length $m$ receives score $m$. The insert and search passes produce this without a special case.
- **Duplicate words:** Each occurrence must count separately. Repeated insertion increments the same path once per occurrence, so duplicates correctly raise every shared-prefix score.
- **A word that is a prefix of another:** Its complete path is shared with the longer word. No terminal-node logic should stop traversal or prevent the longer word from increasing those counts.
- **Completely different first letters:** Such words immediately occupy different root children and share no non-empty prefix, which is exactly why the root's count is excluded.
- **Maximum lengths:** The total-character bound, rather than only the number of words or maximum individual length, is the right measure because every character is processed twice and can create at most one node.
