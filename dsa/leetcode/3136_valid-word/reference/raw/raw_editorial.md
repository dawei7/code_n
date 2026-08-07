### Approach: One-Time Traversal

#### Intuition

First, we check whether the length of the given word is at least 3. Then, using a single traversal, we determine whether the word contains at least one vowel letter, at least one consonant letter, and only valid characters, i.e., letters and digits. Any other characters are not allowed.

#### Implementation


```python
class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False

        has_vowel = False
        has_consonant = False

        for c in word:
            if c.isalpha():
                if c.lower() in "aeiou":
                    has_vowel = True
                else:
                    has_consonant = True
            elif not c.isdigit():
                return False

        return has_vowel and has_consonant
```


#### Complexity analysis

Let $n$ be the length of $\textit{word}$.

- Time complexity: $O(n)$.
  
  We iterate through the word only once to check each character, so the time complexity is linear in the length of the word.

- Space complexity: $O(1)$.