
---
### Approach #1: Store Prefixes [Accepted]

**Intuition**

First, let's remove the duplicate strings since it is not optimal to include two or more of the same string in the final answer. We can do this with a set.

Next, let's handle the suffix relationship.

In this article, a "proper suffix" will refer to a suffix that is not an empty string and not equal to the string itself.

An observation is that if the word `X` is a proper suffix of `Y`, then it does not need to be considered, as the encoding of `Y` in the reference string will also encode `X`.  For example, if `"me"` and `"time"` are in `words`, we can discard `"me"` without changing the answer.

If a word `Y` does not have any other word `X` (in the list of `words`) that is a proper suffix of `Y`, then `Y` must be part of the reference string.

Thus, the goal is to remove words from the list such that no word is a proper suffix of another.  The final answer would be $sum(\text{word.length} + 1 for word in words)$.

**Algorithm**

Since a word has at most 6 proper suffixes (as $\text{words}[i].length \le 7$), let's iterate over all of them.  For each proper suffix, we'll try to remove it from our `words` list.  For efficiency, we'll make `words` a set.

**Implementation**

```python
class Solution(object):
    def minimumLengthEncoding(self, words):
        good = set(words)
        for word in words:
            for k in range(1, len(word)):
                good.discard(word[k:])

        return sum(len(word) + 1 for word in good)
```

**Complexity Analysis**

* Time Complexity:  $O(\sum w_i^2)$, where $w_i$ is the length of $\text{words}[i]$.

* Space Complexity: $O(\sum w_i)$, the space used in storing suffixes.

---
### Approach #2: Trie [Accepted]

**Intuition**

As in *Approach #1*, the goal is to remove words that are proper suffixes of another word in the list.

**Algorithm**

To find whether different words have the same suffix, let's put them backwards into a trie (prefix tree).  For example, if we have `"time"` and `"me"`, we will put `"emit"` and `"em"` into our trie.

After, the leaves of this trie (nodes with no children) represent words that have no proper suffix, and we will count $sum(\text{word.length} + 1 for word in words)$.

**Implementation**

```python
class Solution(object):
    def minimumLengthEncoding(self, words):
        words = list(set(words)) #remove duplicates
        #Trie is a nested dictionary with nodes created
        # when fetched entries are missing
        Trie = lambda: collections.defaultdict(Trie)
        trie = Trie()

        #reduce(..., S, trie) is trie[S[0]][S[1]][S[2]][...][S[S.length - 1]]
        nodes = [reduce(dict.__getitem__, word[::-1], trie)
                 for word in words]

        #Add word to the answer if it's node has no neighbors
        return sum(len(word) + 1
                   for i, word in enumerate(words)
                   if len(nodes[i]) == 0)
```

**Complexity Analysis**

* Time Complexity:  $O(\sum w_i)$, where $w_i$ is the length of $\text{words}[i]$.

* Space Complexity: $O(\sum w_i)$, the space used by the trie.