[TOC]

### Approach #1: Trie + Set Intersection [Time Limit Exceeded]

**Intuition and Algorithm**

We use two tries to separately find all words that match the prefix, plus all words that match the suffix. Then, we try to find the highest-weight element in the intersection of these sets.

Of course, these sets could still be large, so we might TLE if we aren't careful.


```python
Trie = lambda: collections.defaultdict(Trie)
WEIGHT = False

class WordFilter:
    def __init__(self, words: List[str]):
        self.trie1 = Trie() #prefix
        self.trie2 = Trie() #suffix
        for weight, word in enumerate(words):
            cur = self.trie1
            self.addw(cur, weight)
            for letter in word:
                cur = cur[letter]
                self.addw(cur, weight)

            cur = self.trie2
            self.addw(cur, weight)
            for letter in word[::-1]:
                cur = cur[letter]
                self.addw(cur, weight)

    def addw(self, node, w):
        if WEIGHT not in node:
            node[WEIGHT] = {w}
        else:
            node[WEIGHT].add(w)

    def f(self, pref: str, suff: str) -> int:
        cur1 = self.trie1
        for letter in pref:
            if letter not in cur1:
                return -1
            cur1 = cur1[letter]

        cur2 = self.trie2
        for letter in suff[::-1]:
            if letter not in cur2: r
                eturn -1
            cur2 = cur2[letter]

        return max(cur1[WEIGHT] & cur2[WEIGHT], default=-1)
```


**Complexity Analysis**

* Time Complexity: $$O(NK + Q(N+K))$$ where $$N$$ is the number of words, $$K$$ is the maximum length of a word, and $$Q$$ is the number of queries. If we use memoization in our solution, we could produce tighter bounds for this complexity, as the complex queries are somewhat disjoint.

* Space Complexity: $$O(NK)$$, the size of the tries.

---
### Approach #2: Paired Trie [Accepted]

**Intuition and Algorithm**

Say we are inserting the word `apple`.  We could insert `('a', 'e'), ('p', 'l'), ('p', 'p'), ('l', 'p'), ('e', 'a')` into our trie. Then, if we had equal length queries like `prefix = "ap", suffix = "le"`, we could find the node `trie['a', 'e']['p', 'l']` in our trie.  This seems promising.

What about queries that aren't equal?  We should just insert them like normal. For example, to capture a case like `prefix = "app", suffix = "e"`, we could create nodes `trie['a', 'e']['p', None]['p', None]`.

After inserting these pairs into our trie, our searches are straightforward.


```python
Trie = lambda: collections.defaultdict(Trie)
WEIGHT = False

class WordFilter:
    def __init__(self, words: List[str]):
        self.trie = Trie()

        for weight, word in enumerate(words):
            cur = self.trie
            cur[WEIGHT] = weight
            for i, x in enumerate(word):
                #Put all prefixes and suffixes
                tmp = cur
                for letter in word[i:]:
                    tmp = tmp[letter, None]
                    tmp[WEIGHT] = weight

                tmp = cur
                for letter in word[:-i or None][::-1]:
                    tmp = tmp[None, letter]
                    tmp[WEIGHT] = weight

                #Advance letters
                cur = cur[x, word[~i]]
                cur[WEIGHT] = weight

    def f(self, pref: str, suff: str) -> int:
        cur = self.trie
        for a, b in zip_longest(pref, suff[::-1]):
            if (a, b) not in cur:
                return -1
            cur = cur[a, b]
        return cur[WEIGHT]
```


**Complexity Analysis**

* Time Complexity: $$O(NK^2 + QK)$$ where $$N$$ is the number of words, $$K$$ is the maximum length of a word, and $$Q$$ is the number of queries.

* Space Complexity: $$O(NK^2)$$, the size of the trie.

---
### Approach #3: Trie of Suffix Wrapped Words [Accepted]

**Intuition and Algorithm**

Consider the word `'apple'`. For each suffix of the word, we could insert that suffix, followed by `'#'`, followed by the word, all into the trie.

For example, we will insert `'#apple', 'e#apple', 'le#apple', 'ple#apple', 'pple#apple', 'apple#apple'` into the trie.  Then for a query like `prefix = "ap", suffix = "le"`, we can find it by querying our trie for `le#ap`.


```python
Trie = lambda: collections.defaultdict(Trie)
WEIGHT = False

class WordFilter:
    def __init__(self, words: List[str]):
        self.trie = Trie()

        for weight, word in enumerate(words):
            word += '#'
            for i in range(len(word)):
                cur = self.trie
                cur[WEIGHT] = weight
                for j in range(i, 2 * len(word) - 1):
                    cur = cur[word[j % len(word)]]
                    cur[WEIGHT] = weight

    def f(self, pref: str, suff: str) -> int:
        cur = self.trie
        for letter in suff + '#' + pref:
            if letter not in cur:
                return -1
            cur = cur[letter]
        return cur[WEIGHT]
```


**Complexity Analysis**

* Time Complexity: $$O(NK^2 + QK)$$ where $$N$$ is the number of words, $$K$$ is the maximum length of a word, and $$Q$$ is the number of queries.

* Space Complexity: $$O(NK^2)$$, the size of the trie.