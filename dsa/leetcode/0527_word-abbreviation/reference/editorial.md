[TOC]

### Approach #1: Greedy [Accepted]

**Intuition**

Let's choose the shortest abbreviation for each word. Then, while we have duplicates, we'll increase the length of all duplicates.

**Algorithm**

For example, let's say we have `"aabaaa", "aacaaa", "aacdaa"`, then we start with `"a4a", "a4a", "a4a"`. Since these are duplicated, we lengthen them to `"aa3a", "aa3a", "aa3a"`.  They are still duplicated, so we lengthen them to `"aab2a", "aac2a", "aac2a"`. The last two are still duplicated, so we lengthen them to `"aacaaa", "aacdaa"`.

Throughout this process, we were tracking an index $\text{prefix}[i]$ which told us up to what index to take the prefix to. For example, $\text{prefix}[i] = 2$ means to take a prefix of $\text{word}[0], \text{word}[1], \text{word}[2]$.

```python
class Solution(object):
    def wordsAbbreviation(self, words):
        def abbrev(word, i = 0):
            if (len(word) - i <= 3): return word
            return word[:i+1] + str(len(word) - i - 2) + word[-1]

        N = len(words)
        ans = map(abbrev, words)
        prefix = [0] * N

        for i in xrange(N):
            while True:
                dupes = set()
                for j in xrange(i+1, N):
                    if ans[i] == ans[j]:
                        dupes.add(j)

                if not dupes: break
                dupes.add(i)
                for k in dupes:
                    prefix[k] += 1
                    ans[k] = abbrev(words[k], prefix[k])

        return ans
```

**Complexity Analysis**

* Time Complexity: $O(C^2)$ where $C$ is the number of characters across all words in the given array.

* Space Complexity: $O(C)$.

---
### Approach #2: Group + Least Common Prefix [Accepted]

**Intuition and Algorithm**

Two words are only eligible to have the same abbreviation if they have the same first letter, last letter, and length. Let's group each word based on these properties, and then sort out the conflicts.

In each group `G`, if a word `W` has the longest common prefix `P` with any other word `X` in `G`, then our abbreviation must contain a prefix of more than `|P|` characters. The longest common prefixes must occur with words adjacent to `W` (in lexicographical order), so we can just sort `G` and look at the adjacent words.

```python
class Solution(object):
    def wordsAbbreviation(self, words):
        def longest_common_prefix(a, b):
            i = 0
            while i < len(a) and i < len(b) and a[i] == b[i]:
                i += 1
            return i

        ans = [None for _ in words]

        groups = collections.defaultdict(list)
        for index, word in enumerate(words):
            groups[len(word), word[0], word[-1]].append((word, index))

        for (size, first, last), enum_words in groups.iteritems():
            enum_words.sort()
            lcp = [0] * len(enum_words)
            for i, (word, _) in enumerate(enum_words):
                if i:
                    word2 = enum_words[i-1][0]
                    lcp[i] = longest_common_prefix(word, word2)
                    lcp[i-1] = max(lcp[i-1], lcp[i])

            for (word, index), p in zip(enum_words, lcp):
                delta = size - 2 - p
                if delta <= 1:
                    ans[index] = word
                else:
                    ans[index] = word[:p+1] + str(delta) + last

        return ans
```

**Complexity Analysis**

* Time Complexity: $O(C \log C)$ where $C$ is the number of characters across all words in the given array. The complexity is dominated by the sorting step.

* Space Complexity: $O(C)$.

---
### Approach #3: Group + Trie [Accepted]

**Intuition and Algorithm**

As in *Approach #1*, let's group words based on length, first letter, and last letter, and discuss when words in a group do not share the longest common prefix.

Put the words of a group into a trie (prefix tree), and count at each node (representing some prefix `P`) the number of words with the prefix `P`. If the count is 1, we know the prefix is unique.

```python
class Solution(object):
    def wordsAbbreviation(self, words):
        groups = collections.defaultdict(list)
        for index, word in enumerate(words):
            groups[len(word), word[0], word[-1]].append((word, index))

        ans = [None] * len(words)
        Trie = lambda: collections.defaultdict(Trie)
        COUNT = False
        for group in groups.itervalues():
            trie = Trie()
            for word, _ in group:
                cur = trie
                for letter in word[1:]:
                    cur[COUNT] = cur.get(COUNT, 0) + 1
                    cur = cur[letter]

            for word, index in group:
                cur = trie
                for i, letter in enumerate(word[1:], 1):
                    if cur[COUNT] == 1: break
                    cur = cur[letter]
                if len(word) - i - 1 > 1:
                    ans[index] = word[:i] + str(len(word) - i - 1) + word[-1]
                else:
                    ans[index] = word
        return ans
```

**Complexity Analysis**

* Time Complexity: $O(C)$ where $C$ is the number of characters across all words in the given array.

* Space Complexity: $O(C)$.