[TOC]

---
### Approach 1: Hash Set

**Intuition and Algorithm**

We can transform each `word` into it's Morse Code representation.

After, we put all transformations into a set `seen`, and return the size of the set.

```python
class Solution(object):
    def uniqueMorseRepresentations(self, words):
        MORSE = [".-","-...","-.-.","-..",".","..-.","--.",
                 "....","..",".---","-.-",".-..","--","-.",
                 "---",".--.","--.-",".-.","...","-","..-",
                 "...-",".--","-..-","-.--","--.."]

        seen = {"".join(MORSE[ord(c) - ord('a')] for c in word)
                for word in words}

        return len(seen)
```

**Complexity Analysis**

* Time Complexity:  $O(S)$, where $S$ is the sum of the lengths of words in `words`.  We iterate through each character of each word in `words`.

* Space Complexity: $O(S)$.