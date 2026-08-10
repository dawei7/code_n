
---
### Approach #1: Recursion [Accepted]

**Intuition**

Maintain the correct answer as we increase the size of the prefix of `S` we are considering.

For example, when $S = "abc"$, maintain $ans = [""]$, and update it to $ans = ["a", "A"]$, $ans = ["ab", "Ab", "aB", "AB"]$, $ans = ["abc", "Abc", "aBc", "ABc", "abC", "AbC", "aBC", "ABC"]$ as we consider the letters `"a", "b", "c"`.

**Algorithm**

If the next character `c` is a letter, then we will duplicate all words in our current answer, and add `lowercase(c)` to every word in the first half, and `uppercase(c)` to every word in the second half.

If instead `c` is a digit, we'll add it to every word.

```python
class Solution(object):
    def letterCasePermutation(self, S):
        ans = [[]]

        for char in S:
            n = len(ans)
            if char.isalpha():
                for i in xrange(n):
                    ans.append(ans[i][:])
                    ans[i].append(char.lower())
                    ans[n+i].append(char.upper())
            else:
                for i in xrange(n):
                    ans[i].append(char)

        return map("".join, ans)
```

**Complexity Analysis**

* Time Complexity:  $O(2^{N} * N)$, where $N$ is the length of `S`.  This reflects the cost of writing the answer.

* Space Complexity:  $O(2^N * N)$.

---
### Approach #2: Binary Mask [Accepted]

**Intuition**

Say there are $B$ letters in the string `S`.  There will be $2^B$ strings in the answer, which we can represent uniquely by the bitmask `bits`.

For example, we could represent `a7b` by `00`, `a7B` by `01`, `A7b` by `10`, and `A7B` by `11`.  Note that numbers are not part of the bitmask.

**Algorithm**

For every possible bitmask, construct the correct result to put in the final answer.  If the next letter in the word is a letter, write a lowercase or uppercase letter depending on the bitmask.  Otherwise, write the digit as given.

```python
class Solution(object):
    def letterCasePermutation(self, S):
        B = sum(letter.isalpha() for letter in S)
        ans = []

        for bits in xrange(1 << B):
            b = 0
            word = []
            for letter in S:
                if letter.isalpha():
                    if (bits >> b) & 1:
                        word.append(letter.lower())
                    else:
                        word.append(letter.upper())

                    b += 1
                else:
                    word.append(letter)

            ans.append("".join(word))
        return ans
```

**Complexity Analysis**

* Time and Space Complexity:  $O(2^{N} * N)$.  The analysis is the same as in *Approach #1*.

---
### Approach #3: Built-In Library Function [Accepted]

**Intuition and Algorithm**

A *cartesian product* of sets is every possible combination of one choice from those sets.  For example, ${1, 2} x {a, b, c} = {1a, 1b, 1c, 2a, 2b, 2c}$.

For languages that have a built-in function to calculate a cartesian product, we can use this function to minimize our work.

```python
class Solution(object):
    def letterCasePermutation(self, S):
        f = lambda x: (x.lower(), x.upper()) if x.isalpha() else x
        return map("".join, itertools.product(*map(f, S)))
```

**Complexity Analysis**

* Time and Space Complexity:  $O(2^{N} * N)$.  The analysis is the same as in *Approach #1*.