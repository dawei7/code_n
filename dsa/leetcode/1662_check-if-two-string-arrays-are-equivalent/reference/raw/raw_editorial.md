[TOC]

## Solution

---

#### Overview

It's a fairly basic problem and we have many different ways to solve it.

Below, we will discuss five approaches: *Connecting*, *Splitting*, *No Pretreatment*, *Splitting One*, and *Connecting One*.

Generally, we recommend *Connecting* and *Splitting* since they are easy to implement. We also provide other solutions for exploring possibilities. The ideas of those solutions are similar, but their implementations are different.

---

#### Approach 1: Connecting

**Intuition**

Since many programming languages have built-in methods to compare two strings, it is natural to concatenate `word1` and `word2` into whole strings, and then compare them.

![Figure 1.1](images/5605_1_1.drawio.svg)

**Algorithm**

*Step 1:* Build concatenated strings for `word1` and `word2`.

*Step 2:* Check if the strings are the same.

> Challenge: Can you implement the code yourself without seeing our implementations?

**Implementation**


```python
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return ''.join(word1) == ''.join(word2)
```


**Complexity Analysis**

Let $$N$$ be the maximum of the number of all characters in `word1` and the number of all characters in `word2`.

* Time Complexity: $$\mathcal{O}(N)$$, since we need to iterate over all characters in `word1` and `word2` to build the new strings.

* Space Complexity: $$\mathcal{O}(N)$$, since we need extra $$\mathcal{O}(N)$$ space to store the new built strings.

---

#### Approach 2: Splitting

**Intuition**

If you do not like concatenating, we can split them into single characters, and then use for-loop to compare them.

![Figure 2.1](images/5605_2_1.drawio.svg)

**Algorithm**

*Step 1:* Build lists of split characters for `word1` and `word2`.

*Step 2:* Check if the lists are the same.

> Challenge: Can you implement the code yourself without seeing our implementations?

**Implementation**


```python
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        list1 = []
        list2 = []
        for s in word1:
            for c in s:
                list1.append(c)
        for s in word2:
            for c in s:
                list2.append(c)
        if len(list1) != len(list2):
            return False
        for i in range(len(list1)):
            if list1[i] != list2[i]:
                return False
        return True
```


**Complexity Analysis**

Let $$N$$ be the maximum of the number of all characters in `word1` and the number of all characters in `word2`.

* Time Complexity: $$\mathcal{O}(N)$$, since we need to iterate over all characters in `word1` and `word2` to split them in the list.

* Space Complexity: $$\mathcal{O}(N)$$, since we need extra $$\mathcal{O}(N)$$ space to store the lists.

---

#### Approach 3: No Pretreatment

**Intuition**

Both approaches above require some preprocessing on `word1` or `word2`. Can we compare them directly?

Of course. We can iterate over each character in one string array and compare the corresponding character in the other string array.

To achieve this, we need some index to track the character in the other string array.

Here we use two indexes: `stringIndex ` and `characterIndex `. `stringIndex` points to the index of the string in the string array, and `characterIndex` represents the index of the character in the string.

For example:

![Figure 3.1](images/5605_3_1.drawio.svg)

**Algorithm**

*Step 1:* Iterate over `word1` and check if the corresponding character in `word2` is the same.

> Note: You can switch the position of `word1` and `word2`.

> Challenge: Can you implement the code yourself without seeing our implementations?

**Implementation**


```python
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        string_index = 0
        character_index = 0
        word2_len = len(word2)
        words2_len_list = [len(s) for s in word2]
        
        for s in word1:
            for c in s:
                if string_index >= word2_len or c != word2[string_index][character_index]:
                    return False
                character_index += 1
                if character_index == words2_len_list[string_index]:
                    string_index += 1
                    character_index = 0
        
        return string_index == word2_len
```


> Note: We precalculate the lengths of strings in `word2` to prevent re-calculate it during the iteration. However, some built-in data structures automatically maintain the lengths as integers (such as list in Python). In this case, you can skip this precalculation. We here explicitly write the precalculation to emphasize it.
> 

**Complexity Analysis**

Let $$N$$ be the number of all characters in `word1`, and $$M$$ be the length of `word2`.

* Time Complexity: $$\mathcal{O}(N)$$, since we need to iterate over `word1` to check if characters match.

* Space Complexity: $$\mathcal{O}(M)$$, since we need extra $$\mathcal{O}(M)$$ space to store the lengths of strings in `word2`. You can save this space if the data structure automatically stores the lengths.

---

#### Approach 4: Splitting One

**Intuition**

The tracking method in *Approach 3* seems to be a little complicated: we need two indexes! Can we simplify it? 

Yes! If we split the string array into a character array, then only one index is needed.

![Figure 4.1](images/5605_4_1.drawio.svg)

**Algorithm**

*Step 1:* Build lists of split characters for `word2`.

*Step 2:* Iterate over `word1` and check if the corresponding character in `word2` is the same.

> Note: You can switch the position of `word1` and `word2`.

> Challenge: Can you implement the code yourself without seeing our implementations?

**Implementation**


```python
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        list2 = []
        for s in word2:
            list2.extend(s)
        index = 0
        for s in word1:
            for c in s:
                if index >= len(list2) or c != list2[index]:
                    return False
                index += 1

        return index == len(list2)
```


**Complexity Analysis**

Let $$N$$ be the maximum of the number of all characters in `word1` and the number of all characters in `word2`.

* Time Complexity: $$\mathcal{O}(N)$$, since we need to iterate over `word1` to check if characters match.

* Space Complexity: $$\mathcal{O}(N)$$, since we need extra $$\mathcal{O}(N)$$ space to store the list in the worst case.

---

#### Approach 5: Connecting One

**Intuition**

Of course, instead of splitting in *Approach 4*, we can connect them into a whole array. In this case also, we only need one index.

![Figure 5.1](images/5605_5_1.drawio.svg)

**Algorithm**

*Step 1:* Build concatenated strings for `word2`.

*Step 2:* Iterate over `word1` and check if the corresponding character in `word2` is the same.

> Note: You can switch the position of `word1` and `word2`.

> Challenge: Can you implement the code yourself without seeing our implementations?

**Implementation**


```python
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        string2 = ''.join(word2)
        index = 0
        for s in word1:
            for c in s:
                if index >= len(string2) or c != string2[index]:
                    return False
                index += 1
        return index == len(string2)
```


**Complexity Analysis**

Let $$N$$ be the maximum of the number of all characters in `word1` and the number of all characters in `word2`.

* Time Complexity: $$\mathcal{O}(N)$$, since we need to iterate over `word1` to check if characters match.

* Space Complexity: $$\mathcal{O}(N)$$, since we need extra $$\mathcal{O}(N)$$ space to store the new string in the worst case.