[TOC]

## Solution

---

### Approach 1: Counting 

**Intuition and Algorithm**

Every uncommon word occurs exactly once in total.  We can count the number of occurrences of every word, then return ones that occur exactly once.


```python
class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        from collections import defaultdict

        count = defaultdict(int)

        # Count occurrences of words in sentence A
        for word in A.split():
            count[word] += 1

        # Count occurrences of words in sentence B
        for word in B.split():
            count[word] += 1

        # Collect words that appear exactly once
        return [word for word in count if count[word] == 1]
```


**Complexity Analysis**

* Time Complexity:  $$O(M + N)$$, where $$M, N$$ are the lengths of `A` and `B` respectively.

* Space Complexity:  $$O(M + N)$$, the space used by `count`.
<br />
<br />