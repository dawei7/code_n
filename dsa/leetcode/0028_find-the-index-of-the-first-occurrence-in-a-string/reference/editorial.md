## Solution

---

### Overview

The problem is a standard [String Matching](https://en.wikipedia.org/wiki/Category:String_matching_algorithms) Problem. It can be stated as

> Find one or more occurrences of a pattern $x_0 x_1 \ldots x_{m-1}$ in a text $y_0 y_1 \ldots y_{n-1}$. Elements of $x$ and $y$ are characters taken from the set $\Sigma$.

In this problem, we have to find the first occurrence of `needle` in a `haystack`. The characters are taken from the set of lowercase English Characters `{a, b, c, ... , y, z}`.

There are multiple applications of String Matching, and that's why a lot of research has been done in this field. Multiple [algorithms](http://www-igm.univ-mlv.fr/~lecroq/string/index.html) have been devised to solve this problem. Some of the application includes:

- Spell Checker
- Plagiarism Detection
- Text Editors
- Spam Filters
- Digital Forensics
- Matching DNA Sequences
- Intrusion Detection
- Search Engines
- Bioinformatics and Cheminformatics
- Information Retrieval System
- Language Syntax Checker

Throughout the article, we will use

- $m$ (or `m` in code) to denote the length of the `needle` and

- $n$ (or `n` in code) to denote the length of the `haystack`.

---

### Approach 1: Sliding Window

#### Intuition

The most naïve approach is to traverse each possible substring of length $m$ in the `haystack` and check if it is equal to the `needle`.

- First substring of length $m$ will start at index `0` in the `haystack` and will end at index $(m - 1) + 0$.
- The second substring of length $m$ will start at index `1` in the `haystack` and will end at index $(m - 1) + 1$, i.e. `m`.
- The third substring of length $m$ will start at index `2` in the `haystack` and will end at index $(m - 1) + 2$ i.e. $m + 1$.

Thus, if a substring ends at index $(m - 1) + k$, then it starts at index `k`. We know that the last substring ends at index $(n - 1)$. Thus, to find starting index `k` of the last substring, we can equate $(n - 1)$ with $(m - 1) + k$, to get $k = (n-1) - (m-1)$, or $k = n - m$.

- Thus, the last substring of length $m$ will start at index $n - m$ in the `haystack` and will end at index $n - 1$.

We will create a `window` of size $m$ and slide it across the `haystack`. We will keep track of the starting index of the `window` in a variable $\text{window}_{start}$. For every $\text{window}_{start}$, we will iterate till $\text{window}_{start} + m$.  During each iteration,

- if the $i^{th}$ character in the `window` is equal to the $i^{th}$ character in the `needle`, then we will increment $i$ by 1.
- If the $i^{th}$ character in the `window` is not equal to the $i^{th}$ character in the `needle`, then we conclude that the substring of length $m$ starting from index $\text{window}_{start}$ cannot be equal to the `needle`, and we will reset $\text{window}_{start}$ to $\text{window}_{start} + 1$.

If all the $i^{th}$ characters in the `window` are equal to the $i^{th}$ characters of `needle`, then we will return the $\text{window}_{start}$.

#### Algorithm

1. Declare `m` and `n` as variables, and initialize them with the length of `needle` and `haystack` respectively.

2. Declare the $\text{window}_{start}$ variable, and initialize it with `0`. Now, iterate $\text{window}_{start}$ till starting index of the last substring of length $m$, i.e till $n - m$.

3. For each $\text{window}_{start}$, iterate variable `i` from `0` to $m - 1$. Check if the $i^{th}$ character in the `window` i.e index $\text{window}_{start} + i$ is equal to the $i^{th}$ character in the `needle`, if yes, then increment `i` by 1. If not, reset $\text{window}_{start}$ to $\text{window}_{start} + 1$.

4. If all the $i^{th}$ characters in the `window` are equal to the $i^{th}$ characters of `needle`, then return the $\text{window}_{start}$.

5. If we are done iterating over all values of $\text{window}_{start}$ and none of them return a match, then return -1.

> **Example:** Let `haystack` be "mississippi" and `needle` be “issipi”. The sliding window algorithm would get executed like this.
>
> !?!../Documents/28/28_Sliding_Window.json:1280,720!?!
>
> <br/>

#### Implementation

```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(needle)
        n = len(haystack)

        for window_start in range(n - m + 1):
            for i in range(m):
                if needle[i] != haystack[window_start + i]:
                    break
                if i == m - 1:
                    return window_start

        return -1
```

#### Complexity Analysis

* Time complexity: $O(nm)$. For every $\text{window}_{start}$, we may have to iterate at most $m$ times. There are $n-m+1$ such $\text{window}_{start}$'s. Thus, it is $O((n-m+1) \cdot m)$, which is $O(nm)$.

    One example where the worst case occurs is when `needle` is "aaaaab", while `haystack` is all `a`'s (Let's say, "aaaaaaaaaa"). In this, we always have to take the last character of `needle` into comparison to conclude that the current `m-substring` is not equal to `needle`. Thus, we will have to iterate $m$ times for every $\text{window}_{start}$.

* Space complexity: $O(1)$.

    There are a handful of variables in the code (`m`, `n`, `i`, $\text{window}_{start}$), and all of them use constant space, hence, the space complexity is constant.

---

### Approach 2: Rabin-Karp Algorithm (Single Hash)

#### Intuition

This algorithm is based on the concept of hashing. We can hash any string to a numeric value. For this purpose, we can use different hashing algorithms.

**Example:** Let's define our hash function as _sum of mapped values of all the characters in the string_. The `mapped value` of `a` is `1`, the `mapped value` of `b` is `2`, and so on.
Using this `abb` will be mapped to $1 + 2 + 2 = 5$. If two strings are equal, then their hash values will be equal. However, using **this** hashing approach, the reverse will not necessarily be True. If two hash values are equal, we can't say that the strings are also equal. `aca` will also map to `5`, however, `aca` and `abb` are not equal. Thus, we can have lots of collisions (also called spurious hits).

> **Spurious Hits:** If the hash value of `needle` matches with the hash-value of the m-Substring of `haystack` but the m-Substring is not equal to `needle`, then we have a spurious hit.

Hence, *"If two strings are equal, then their hash values will be equal"*. The same can be rephrased as _"If two hash values are NOT equal, then strings will NOT be equal"_. This fact can be used to NOT check character-by-character for every m-substring. What we can do is check character-by-character only if the hash value of the m-substring of `haystack` is equal to the Hash Value of `needle`.

> Let `haystack` be "ccaccaacdba" and `needle` be "dba". Using above discussed hash function, hash("dba") will be $4+2+1=7$
>
> !?!../Documents/28/28_Rabin_Karp_Single_Hash_Simple.json:1280,720!?!
>
> <br/>

As illustrated in the above example, we have checked character-by-character only 5 times. Out of which 4 times, we had a spurious hit. This is better than checking character-by-character for every m-substring (which are 9 in this example). Still, spurious hits are one of the limitations.

Another commonly encountered limitation is that if we calculate the hash value of every m-substring of `haystack`, then it is equivalent to iterating each character of the m-substring, producing the same time complexity as the brute force approach.

We can overcome both the limitations (Spurious Hits and Computing Hash Value again) by using the concept of **rolling hash**.

1. To overcome spurious hits, we can assign position weight to each index of the string. For example, the last character of the string is assigned a weight of $1$, the second last character of the string is assigned a weight of $10$, the third last character of the string is assigned a weight of $10^2$, and so on.

    In this way `aca` will be mapped to $1\cdot $10^{2}$ + 3\cdot $10^{1}$ + 1\cdot $10^{0}$ = 100+30+1 = 131$, while `abb` will be mapped to $1\cdot $10^{2}$ + 2\cdot $10^{1}$ + 2\cdot $10^{0}$ = 100+20+2 = 122$.
    Thus, both strings, which were being mapped to $5$ using traditional hash, are now being mapped to different values, thereby reducing the number of spurious hits.

    However, the approach is still not fool-proof. `aal` will also be mapped to $1\cdot $10^{2}$ + 1\cdot $10^{1}$ + 12\cdot $10^{0}$ = 100+10+12 = 122$. Thus, we still can have spurious hits. The reason being our chosen position weight $10$ is not enough to overcome spurious hits.

    Mathematically, it turns out that to have a unique hash value for every m-substring, positional weight should be greater than or equal to the number of characters in the set, which is $26$ in our case. Any number (preferably, a prime number) no less than $26$ is a workable base. To have a lower hash value, we can map `a` to $0$, `b` to $1$, `c` to $2$, and so on.

    Thus, let the string be $S[0\ldots(m-1)]$. we can calculate hash value $h(S[0\ldots(m-1)])$ as
 $h(S[0])\cdot 26^{(m-1)} + h(S[1])\cdot 26^{(m-2) }+ \ldots + h(S[m-1])\cdot 26^0$
    where $h(S[i])$ is the mapped value of character $S[i]$ and $m$ is the length of the string.

    The formula works fine, but the hash value may easily overflow. To prevent overflow, we can use modular arithmetic. There may be spurious hits after `MOD`, but this can be minimized by using a sufficiently large prime number.

2. It turns out that we never explicitly need to compute the hash value of every m-substring. We only need to compute the hash value of the first m-substring of `haystack` and `needle`. For the remaining m-substrings of `haystack`, we can:

- Multiply the hash value of the previous m-substring by radix $26$.
- Subtract the value of the first character of the previous m-substring, since we are moving the window by one character, and that character is now out of the window.
- Add the value of the last character of the current m-substring, since we are moving the window by one character.

    This can be understood using the following example.

    !?!../Documents/28/28_Rabin_Karp_Single_Hash_Rolling.json:1280,720!?!

    <br/>

    Mathematically,
    $H[i] = S[i]b^{m-1} + S[i+1]b^{m-2} + \ldots + S[i+m-1]b^0$
    where $b$ is the base, $m$ is the length of the string, and $H[i]$ is the hash value of the m-substring of `haystack` starting from index $i$.

    Now,
    $H[i+1] = S[i+1]b^{m-1} + S[i+2]b^{m-2} + \ldots + S[i+m]b^0$

    This can be simplified as
    $H[i+1] = H[i]b - S[i]b^{m} + S[i+m]$

    The three terms can be interpreted as:
- $H[i]b$ is left shifting one radix
- $S[i]b^{m}$ is the leftmost character with modified weightage which is now out of the window, hence subtracted.
- $S[i+m]$ is the rightmost character with weight 1, which is now in the window, hence added.

    Thus, from the previous hash value, we can compute the next hash value in $O(1)$ time. Moreover, we can apply modular arithmetic to the previous hash to compute the next hash value.

    $H[i+1] = ((H[i]b \mod \red{\text{MOD}}) - (S[i]b^{m} \mod \red{\text{MOD}})  + (S[i+m] \mod \red{\text{MOD}})) \mod \red{\text{MOD}}$
    where $\red{\text{MOD}}$ is a large prime number.

Thus, the basic intuition of Rabin Karp is that we will compute the hash of each substring, and if the hash matches the hash of `needle`, we will compare the substring character by character. We can produce a unique hash but that can result in an overflow. To prevent overflow, we will take $\text{MOD}$, but that will result in spurious hits. To minimize spurious hits, we will use a very large prime number for taking $\text{MOD}$.
Finally, to reduce the re-computing of hash values again and again, we will use the concept of rolling hash. This rolling hash formula is distributive over $\text{MOD}$, and the amortized time to compute the hash value of every m-substring is constant.

#### Algorithm

1. Store the length of `needle` in `m` and the length of `haystack` in `n`.

2. If `n` is less than `m`, it means that `needle` cannot be there in `haystack`. Return -1.

3. Define constants as follows:
- `RADIX` is the base of the number system. In our case, it is $26$.
- `MOD` is a large prime number to prevent overflow.
- $\text{MAX}_{WEIGHT}$ is the largest value of the `weight` of any character. In our case, it is $26^m$. This value is used in the $O(1)$ formula. Hence, it's better to store it.

4. Define the $\text{hash}_{value}()$ function which takes a string as input and returns the hash value of the string. The hash value is calculated by
- Iterating string from right to left.
- Multiplying the mapping value of each character with its weight `factor` and adding it to hash value `ans`.
- The `factor` gets multiplied by `RADIX` in each iteration.
- The `ans` and `factor` are moduloed by `MOD` at each iteration.

5. Using the $\text{hash}_{value}()$ function, compute the hash value of `needle`.

6. Iterate over `haystack` from index `0` to $n - m$ using $\text{window}_{start}$.
- Compute the hash value of the current window, if it's the first window, then compute using the $\text{hash}_{value}()$ function, otherwise use the $O(1)$ formula. Make sure to use the property of modular arithmetic to prevent overflow.
- If the hash value of the current window matches with the hash value of `needle`, then compare characters in the current window with `needle`.
- If any character doesn't match, then it's a spurious hit. Move on to the next window.
- If all characters match, then return the index of the current $\text{window}_{start}$.

7. If we reach the end of the `haystack` and didn't find the `needle`, return -1.

> **Example:** Let `haystack` be "ccaccaacdba" and `needle` be "dba".
> Let `m` be the length of `needle` and `n` be the length of `haystack`. Thus, $m = 3$ and $n = 11$. Let `RADIX` be $26$ and `MOD` be $10^9 + 7$. Therefore, $\text{MAX}_{WEIGHT}$  will be $26^3 = 17576$.
>
> Let's compute the hash value of `needle` "dba". Please note that 'a' is mapped to $0$, 'b' to $1$ and 'c' to $2$, and so on.
> $\text{dba} = $26^{2}$ \cdot 3 + $26^{1}$ \cdot 1 + $26^{0}$ \cdot 0 = 2054$.
> We are interested in finding a substring in `haystack` which has the same hash value as `needle`, i.e. $2054$.
>
> The slides illustrates the process of computing the hash value of every m-substring of `haystack` and comparing it with the hash value of `needle`.
>
> !?!../Documents/28/28_Rabin_Karp_Single_Hash_Rolling_Algorithm.json:1280,720!?!
>
> <br/>

#### Implementation

```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(needle)
        n = len(haystack)
        if n < m:
            return -1

        # CONSTANTS
        RADIX = 26
        MOD = 1_000_000_033
        MAX_WEIGHT = 1

        for _ in range(m):
            MAX_WEIGHT = (MAX_WEIGHT * RADIX) % MOD

        # Function to compute the hash of m-String
        def hash_value(string):
            ans = 0
            factor = 1

            for i in range(m - 1, -1, -1):
                ans += ((ord(string[i]) - 97) * (factor)) % MOD
                factor = (factor * RADIX) % MOD

            return ans % MOD

        # Compute the hash of needle
        hash_needle = hash_value(needle)

        # Check for each m-substring of haystack, starting at window_start
        for window_start in range(n - m + 1):
            if window_start == 0:
                # Compute hash of the First Substring
                hash_hay = hash_value(haystack)
            else:
                # Update Hash using Previous Hash Value in O(1)
                hash_hay = (
                    (hash_hay * RADIX) % MOD
- ((ord(haystack[window_start - 1]) - 97) * MAX_WEIGHT)
                    % MOD
                    + (ord(haystack[window_start + m - 1]) - 97)
                    + MOD
                ) % MOD

            # If hash matches, Check Character by Character.
            # Because of Mod, spurious hits can be there.
            if hash_needle == hash_hay:
                for i in range(m):
                    if needle[i] != haystack[i + window_start]:
                        break
                if i == m - 1:
                    return window_start

        return -1
```

**Implementation Notes**

- In Python3, we have used `ord` to convert a character to its ASCII value. Now, the ASCII Value of `a` is `97`, and we want to scale it down to `0`, hence, we have used $ord(\text{string}[i]) - 97$ in the code.

- Since Python3 can handle large integers, we need not use `MOD`. In that case, the hash value will be unique, and we can simply return $\text{window}_{start}$ if the hash value matches. But operations (addition, multiplication, and subtraction) on large integers are slow.

- Since $\text{MAX}_{WEIGHT}$ is `MOD` $26^m$, therefore, we have calculated it iteratively, instead of using the `pow()` function, for a few reasons:
- `pow()` function can overflow, and we don't want that. In Iteration, we are `MOD`ing the value at each step, so we are safe.
- In Java, the `Math.pow()` function returns a `double`, and it has a precision error. Thus, iterating is a better option.
- `MOD`ing at each step of iteration is better than first computing the entire large $26^m$ and then `MOD`ing it.

- In Java, we have added `MOD` in the $O(1)$ formula to avoid downflowing to a negative value. When we subtract two `MOD`ed integers, we need to add MOD. In We can write $(a - b)\%MOD = (a\%MOD - b\%MOD)\%MOD$. In actual case `a > b` but after `MOD`ing, `a%MOD` can be smaller than `b%MOD`. In that case, we need to add `MOD`. Thus $(a - b)\%MOD = (a\%MOD - b\%MOD + MOD)\%MOD$.

#### Complexity Analysis

* Time complexity: $O(nm)$.

    In the worst case, `hashNeedle` might match with the hash value of all `haystack` substrings. Hence, we then have to iterate character by character in each window. There are $n-m+1$ such windows of length $m$. Hence, the time complexity is $O(nm)$.

    But in the best case, if no hash value of the `haystack` substring matches with `hashNeedle`, then we don't have to iterate character by character in each window. In that case, it will be $O(n+m).$ Computing the hash value of `haystack` and `needle` will be $O(m)$ and for traversing all windows, we will have $O(n-m)$ time complexity. And during traversal, we are doing constant number of operations, hence, in that case, it will be $O(n-m+2m)=O(n+m)$.

* Space complexity: $O(1)$. We are not using any extra space.

    There are a handful of variables in the code, namely, `hashNeedle`, `hashHay`, `windowStart`, `windowEnd`, `m`, `n`, $\text{MAX}_{WEIGHT}$, `RADIX`, `MOD`. All of them use constant space, and hence, the space complexity is $O(1)$.

---

### Approach 3: Rabin-Karp algorithm (Double Hash)

#### Intuition

The major drawback of [previous approach](#approach-2-rabin-karp-algorithm-single-hash) was that even in case of a match, we had to iterate character by character in each window. We can't return true immediately, because of the CHANCE of spurious hits.

What if we can minimize the CHANCE of spurious hits? Before proceeding, let's analyze some spurious hits using the previous approach.

>
> **A.**
Let `MOD` be $2^{31}$, and the approach used for mapping is `a` to `1`, `b` to `2`, `c` to `3`, etc.
    Then, both `gytisyz` and `aaaaaab` will have a hash value of $321272408$. If we avoid comparing character-by-character, and return $\text{window}_{start}$ immediately on matching hash value, then we will have a wrong answer.
>
> **B.**
Let `MOD` be $10^9 + 33$, and the approach used for mapping is `a` to `0`, `b` to `1`, `c` to `2`, etc.
    Then, both `cadbbca` and `fghivbt` will have the hash value of $1619220817$. If we avoid comparing character-by-character, and return $\text{window}_{start}$ immediately on matching hash value, then we will have a wrong answer.

But if we use case **A.** for `cadbbca` and `fghivbt`, then `cadbbca` will map to $1940493224$ while `fghivbt` will map to $940493191$. And no spurious hits will be there.

Similarly, if we use case **B.** for `gytisyz` and `aaaaaab`, then `gytisyz` will map to $147483583$ while `aaaaaab` will map to $1$. And no spurious hits will be there.

**What do these cases suggest?**
Using a different approach for computing hash value, we may avoid spurious hits. But which approach to use? It turns out that instead of a single hash value, if we compute two (or more) hash values, we can significantly reduce the CHANCE of spurious hits. We need to compare these  _hash value pair of `needle`_ with _hash value pair of windows of `haystack`_.

We can produce different hash values by changing

- MOD value

- RADIX value

- MAPPING value

- `a` to `0`, `b` to `1`, `c` to `2`, and so on.
- `a` to `1`, `b` to `2`, `c` to `3`, and so on.
- `a` to `25`, `b` to `24`, `c` to `23`, and so on.

- WEIGHTAGE associated with characters of the string. There can be two or more versions
- Rightmost character has weightage 1, then the second rightmost character has weightage RADIX, and so on. The leftmost character will have weightage RADIX $^{(m-1)}$.
- Leftmost character will have weightage 1, then the second leftmost character will have weightage RADIX, and so on. The rightmost character will have weightage RADIX $^{(m-1)}$.

We can make one or more changes (Change MOD, RADIX as well as MAPPING) for producing a second value for Pair. We can even use three techniques for hash value, generating triplet for string.

Mathematically, we can prove that by using different MOD and RADIX, we can reduce the CHANCE (i. e. probability) of spurious hits to $10^{-10}$

#### Algorithm

1. Store the length of `needle` in `m` and the length of `haystack` in `n`.

2. If `n` is less than `m`, it means that `needle` cannot be there in `haystack`. Return -1.

3. Define constants as follows:
- $\text{RADIX}_{1}$ as the radix of the first hashing mechanism. It should be at least $26$.
- $\text{RADIX}_{2}$ as the radix of the second hashing mechanism. It should be at least $26$, and different from $\text{RADIX}_{1}$.
- $\text{MOD}_{1}$ as the modulus for the first hashing mechanism. It should be a large prime number.
- $\text{MOD}_{2}$ as the modulus for the second hashing mechanism. It should be a large prime number, and different from $\text{MOD}_{1}$.
- `MAX_WEIGHT_1` as the maximum weightage for the first hashing mechanism. It will be RADIX_1 $^{m}$. This value is used in the $O(1)$ formula. Hence, it's better to store it.
- `MAX_WEIGHT_2` as the maximum weightage for the second hashing mechanism. It will be RADIX_2 $^{m}$. This value is used in the $O(1)$ formula. Hence, it's better to store it.

4. Define the $\text{hash}_{pair}()$ function which takes a string as input and returns the hash value pair of the string.
- Compute the hash value of the first hashing mechanism using $\text{RADIX}_{1}$, and $\text{MOD}_{1}$.
- Compute the hash value of the second hashing mechanism using $\text{RADIX}_{2}$ and $\text{MOD}_{2}$.

5. Using the $\text{hash}_{pair}()$ function, compute the hash value of `needle`.

6. Iterate over `haystack` from index `0` to `n-m` using $\text{window}_{start}$.
- Compute the hash value pair of the current window, if it's the first window, then compute using the $\text{hash}_{pair}()$ function, otherwise use the $O(1)$ formula. Make sure to use the property of modular arithmetic to prevent overflow.
- If the hash value pair of the current window matches with the hash value pair of `needle`, then return $\text{window}_{start}$. The probability of a spurious hit tends to zero.

7. If we reach the end of the `haystack` and didn't find the `needle`, return -1.

#### Implementation

```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(needle)
        n = len(haystack)

        if n < m:
            return -1

        # CONSTANTS
        RADIX_1 = 26
        MOD_1 = 10**9 + 33
        MAX_WEIGHT_1 = 1
        RADIX_2 = 27
        MOD_2 = 2**31 - 1
        MAX_WEIGHT_2 = 1

        for _ in range(m):
            MAX_WEIGHT_1 = (MAX_WEIGHT_1 * RADIX_1) % MOD_1
            MAX_WEIGHT_2 = (MAX_WEIGHT_2 * RADIX_2) % MOD_2

        # Function to compute hash_pair of m-String
        def hash_pair(string):
            hash_1 = hash_2 = 0
            factor_1 = factor_2 = 1
            for i in range(m - 1, -1, -1):
                hash_1 += ((ord(string[i]) - 97) * (factor_1)) % MOD_1
                factor_1 = (factor_1 * RADIX_1) % MOD_1
                hash_2 += ((ord(string[i]) - 97) * (factor_2)) % MOD_2
                factor_2 = (factor_2 * RADIX_2) % MOD_2

            return [hash_1 % MOD_1, hash_2 % MOD_2]

        # Compute hash pairs of needle
        hash_needle = hash_pair(needle)

        # Check for each m-substring of haystack, starting at window_start
        for window_start in range(n - m + 1):
            if window_start == 0:
                # Compute hash pairs of the First Substring
                hash_hay = hash_pair(haystack)
            else:
                # Update Hash pairs using Previous using O(1) Value
                hash_hay[0] = (
                    (hash_hay[0] * RADIX_1) % MOD_1
- ((ord(haystack[window_start - 1]) - 97) * (MAX_WEIGHT_1))
                    % MOD_1
                    + (ord(haystack[window_start + m - 1]) - 97)
                ) % MOD_1
                hash_hay[1] = (
                    (hash_hay[1] * RADIX_2) % MOD_2
- ((ord(haystack[window_start - 1]) - 97) * (MAX_WEIGHT_2))
                    % MOD_2
                    + (ord(haystack[window_start + m - 1]) - 97)
                ) % MOD_2

            # If the hash matches, return immediately.
            # Probability of Spurious Hit tends to zero
            if hash_needle == hash_hay:
                return window_start
        return -1
```

**Implementation Notes**

- In Python3, we have used `ord` to convert a character to its ASCII value. Now, the ASCII Value of `a` is `97`, and we want to scale it down to `0`, hence, we have used $ord(\text{string}[i]) - 97$ in the code.

- Since $\text{MAX}_{WEIGHT}$ is `MOD`ed $26^m$, therefore, we have calculated it iteratively, instead of using the `pow()` function, for a few reasons:
- `pow()` function can overflow, and we don't want that. In Iteration, we are `MOD`ing the value at each step, so we are safe.
- In Java, the `Math.pow()` function returns a `double`, and it has a precision error. Thus, iterating is a better option.
- `MOD`ing at each step of iteration is better than first computing the entire large $26^m$ and then `MOD`ing it.

- In Java, we have added `MOD` in the $O(1)$ formula to avoid downflowing to a negative value. When we subtract two `MOD`ed integers, we need to add MOD. In We can write $(a - b)\%MOD = (a\%MOD - b\%MOD)\%MOD$. In actual case `a > b` but after `MOD`ing, `a%MOD` can be smaller than `b%MOD`. In that case, we need to add `MOD`. Thus $(a - b)\%MOD = (a\%MOD - b\%MOD + MOD)\%MOD$.

#### Complexity Analysis

* Time complexity: $O(n)$.

- For computing hash pairs of `needle`, we have to do $O(m)$ work.

- For checking for a match, we have to iterate over $n-m+1$ times. Out of these $n-m+1$ operations, we have to do $O(1)$ work for $n-m$ times, and $O(m)$ work for $1$ time.
- Hence, total time complexity is $O(m + (n-m)\cdot 1 + (1)\cdot m)$, which is $O(n+m)$
- Moreover, we are proceeding only when $n\geq m$, thus final time complexity is $O(n)$ only. In this case, $O(m+n)$ has an upper bound of $O(2\cdot n)$, that's why we can ignore the $m$ term. When $n < m$ we are simply returning -1. Thus, only $n$ is dominating in Time Complexity, and not $m$.

* Space complexity: $O(1)$. We are not using any extra space.

    There are a handful of variables in the code, and all of them use constant space, hence, the space complexity is $O(1)$.

---

### Approach 4: Knuth–Morris–Pratt Algorithm

#### Intuition

The drawback of [Brute Force](#approach-1-sliding-window) is that after mismatch, we need to set $\text{window}_{start}$ to $\text{window}_{start}+1$, and thus, there are a lot of repeated comparisons.

**Note:** A common pitfall is when we think of setting $\text{window}_{start}$ to one step ahead of the index where mismatching occurs. It works fine here.

> Let `haystack` be "trailtrain", and `needle` be "train". Thus, `n` is 10, and `m` is 5.
>
> !?!../Documents/28/28_Sliding_Window_train.json:1280,720!?!
>
> <br/>

However, it is not the case. We should not entirely ignore the previously matched characters. See the following example.

> Let `haystack` be "mememesmes", and `needle` be "memes". Thus, `n` is 10, and `m` is 5.
>
> !?!../Documents/28/28_Sliding_Window_memes.json:1280,720!?!
>
> <br/>

Thus, in certain cases, we can ignore the previously matched characters, while in some cases we can save time if we don't. KMP is built on this concept. After the mismatch, the string `needle` itself allows us to determine where to begin the next substring to bypass the re-examination of previously matched characters. For this, we need to preprocess the `needle` string.

KMP studies the `needle` string, while brute force doesn't. Let us first define a few terms.

> **Prefix:** Substring of a string that starts from the beginning of the string. Empty string (`""`) is a prefix of every string.
> - `"", "a", "ab", "aba", "abac", "abaca", "abacab"` are prefix of `"abacab"`
> - `"", "a", "ab", "aba", "abab", "ababa", "ababab", "abababa"` are prefix of `"abababa"`
>
> **Suffix:** Substring of a string that ends at the end of the string. Empty string (`""`) is a suffix of every string.
> - `"abacab", "bacab", "acab", "cab", "ab", "b", ""` are suffix of `"abacab"`
> - `"abababa", "bababa", "ababa", "baba", "aba", "ba", "a", ""` are suffix of `"abababa"`
>
> **Proper Prefix:** Prefix that is not equal to the string itself.
> - `"", "a", "ab", "aba", "abac", "abaca"` are proper prefix of `"abacab"`
> - `"", "a", "ab", "aba", "abab", "ababa", "ababab"` are proper prefix of `"abababa"`
>
> **Proper Suffix:** Suffix that is not equal to the string itself.
> - `"bacab", "acab", "cab", "ab", "b", ""` are proper suffix of `"abacab"`
> - `"bababa", "ababa", "baba", "aba", "ba", "a", ""` are proper suffix of `"abababa"`
>
> **Border:** Substring of a string that is both proper prefix and proper suffix. The length of the border is often called the _Width of the Border_. Although, the term _Width_ is rarely used.
> - `"", "ab"` are borders of `"abacab"`
> - `"", "aba", "ababa"` are borders of `"abababa"`
> _See `"ababa"` border. It suggests that proper prefix and proper suffix can overlap._ Readers can practice [1392. Longest Happy Prefix](https://leetcode.com/problems/longest-happy-prefix/) problem, which is similar to this concept.
>
> **Technical Note:** The empty string (`""`) is always a border of any non-empty string. However, the empty string (`""`) itself has no border

Now, for `needle`, we generate a $\text{longest}_{border}$ array. (Often called `lps` _(Longest Proper Prefix that is also a Suffix)_, `π-table`, or `Prefix Table`)

> **longest_border:** Array that stores the length of _**L**ongest Proper **P**refix that is also a **S**uffix_ of every prefix of `string`. More precisely, $\text{longest}_{border}[i]$ is the length of the longest border of the `string[0...i]` (both inclusive).
>
> $\text{longest}_{border}[0] = 0$ because for a single character, the only border is `""`, whose length is 0. Remember, we are only considering proper prefixes and proper suffixes.
>
> Mathematically, we can say that
> $\text{longest\\\text{_border}[i]} = \max_{k = 0 \dots i} \{ k \text{ such that } s[0 \dots k-1] = s[i-(k-1) \dots i]  \}$

>
> Let's construct `LPS` for `"abcdabeeabf"`
>
>  !?!../Documents/28/28_LPS_Building.json:1280,720!?!
>
> <br/>

We will be using $\text{longest}_{border}$ and `lps` interchangeably. Both are the same.

> **Interview Tip:** The Longest Border Array (LPS, π-table, or Prefix Table) is used in multiple algorithms. The naïve approach to built it is of $O(m^3)$ by adhering to the mathematical formula and searching for the longest proper prefix that is also a suffix, for every index.
>```
>for i = 1 to m-1
>   for k = 0 to i
>      if needle[0..k-1] == needle[i-(k-1)..i]
>        longest_border[i] = k
>````
>
> However, we can follow the greedy approach (discussed below), and can build it in linear time. The longest Border Array is used in
>- KMP
>- Counting the number of occurrences of each prefix.
>- Counting the number of different substrings of a string.
>- Compression of a string.

Now, we will examine the `haystack `characters using $\text{haystack}_{pointer}$ and `needle` characters using $\text{needle}_{pointer}$.

- if characters corresponding to $\text{haystack}_{pointer}$ and $\text{needle}_{pointer}$ match, we increment both pointers, to check the new character.

- if the very first character of `needle` (which means $\text{needle}_{pointer} = 0$) doesn't match, we increment $\text{haystack}_{pointer}$ by 1 to check the new character. In this case, $\text{needle}_{pointer}$ remains 0.
- if there is some partial matching, we can say that $\text{needle}_{pointer} > 0$.
- Now, lets say the first $\text{needle}_{pointer} - 1$ characters match and $\text{needle}_{pointer}$$^{th}$ character doesn't match. Then we need to check the length of the longest border corresponding to $\text{needle}_{pointer} - 1$.

- This length tells that the last $\text{longest}_{border}[\text{needle}_{pointer}-1]$ characters of $\text{needle}_{substring}$ are the same as the first $\text{longest}_{border}[\text{needle}_{pointer}-1]$ characters of $\text{needle}_{substring}$

       _(We are using $\text{needle}_{substring}$ to denote partially matched substring of `needle`)_.
- If the last $\text{longest}_{border}[\text{needle}_{pointer}-1]$ characters of $\text{needle}_{substring}$ match with the same number of the last character of $\text{haystack}_{window}$, then we can say that the first $\text{longest}_{border}[\text{needle}_{pointer}-1]$ characters of $\text{needle}_{substring}$ match with the same character of $\text{haystack}_{window}$.

       _[Note that all of $\text{needle}_{substring}$ match with the same number of last characters of $\text{haystack}_{window}$, but $\text{longest}_{border}[\text{needle}_{pointer}-1]$ characters are special because we can say that first $\text{longest}_{border}[\text{needle}_{pointer}-1]$ (along with last) also matches with the last $\text{longest}_{border}[\text{needle}_{pointer}-1]$ characters of $\text{haystack}_{window}$]_
- Now, a mismatch occurs at the $\text{needle}_{pointer}$$^{th}$ character. Since first $\text{longest}_{border}[\text{needle}_{pointer}-1]$ characters of $\text{needle}_{substring}$ matches with last $\text{longest}_{border}[\text{needle}_{pointer}-1]$ characters of $\text{haystack}_{window}$, we can compare this mismatched-character of $\text{haystack}_{window}$ with $\text{longest}_{border}[\text{needle}_{pointer}-1]$$^{th}$ character of $\text{needle}_{substring}$.

        _[If the first 2 characters match, we have to check $3^{rd}$ character of $\text{needle}_{substring}$, which is at index 2]_
- Thus, in partial matching
- don't change $\text{haystack}_{pointer}$. We want to examine the mismatched character of $\text{haystack}_{window}$
- set $\text{needle}_{pointer}$ to $\text{longest}_{border}[\text{needle}_{pointer}-1]$ _(which is the length of the longest border of the $\text{needle}_{substring}$, or index of the first character of `needle` after partial matching)_

Thus, we can avoid rematching partial matches in the "Sliding Window" by using the $\text{longest}_{border}$ array, hence avoiding the redundant comparisons on partial matches. The purpose of $\text{longest}_{border}$ is not to match any character of `haystack` more than once.
Thus using this approach, $\text{haystack}_{pointer}$ will never decrease. It will only increase. $\text{needle}_{pointer}$ will be made to move leftwards optimally in case of a mismatch after a partial match.

Moreover, we can build the $\text{longest}_{border}$ array greedily in linear time. We need to iterate over `needle` using `i`. We use another variable `prev` to store the length of the longest border of the previous prefix. Initially, it is `0` and, $\text{longest}_{border}[0] = 0$. Now, we need to iterate `i` from `1` to $len(needle) - 1$.

1. If the character at index `prev` is the same as index `i`, it means we have found another border with one more length, then we should increment `prev`. Moreover, $\text{longest}_{border}[i]$ will be incremented `prev`. We then increment `i`.

2. Else if the character at index `prev` is different from index `i`.

- If `prev` is equal to `0`, then $\text{longest}_{border}[i]$ will be set to `0`. Since we don't have any non-empty border for the previous prefix, we can't have non-empty for this too, courtesy to mismatching of $\text{needle}[0]$ and $\text{needle}[i]$. After setting, we will move to the next `i`

- Else if `prev` is not equal to `0`, we have to set $prev = \text{longest}_{border}[prev-1]$. In this case, `i` will not be incremented. We are still interested in finding $\text{longest}_{border}[i]$ with less length. That less length by definition will be $\text{longest}_{border}[prev-1]$.

> The slide illustrates the linear algorithm to compute LPS for "abcdabeeabf"
>
> !?!../Documents/28/28_LPS_Linear.json:1280,720!?!

<br/>

> It turns out that Linear Algorithm for PREPROCESSING is more or less the same as SEARCHING. In PREPROCESSING we compare `needle` with itself, trying to find the prefix in the latter part (often called "pre-searching" the needle). In SEARCHING, we compare `needle` with `haystack`, trying to find `needle` in `haystack`.

#### Algorithm

1. Let `n` be the length of `haystack` and `m` be the length of `needle`. If `n < m`, return `-1`, as `needle` cannot be found in `haystack`.

2. PREPROCESS `needle` to generate the $\text{longest}_{border}$ array.
- Let `prev` be `0` and $\text{longest}_{border}$ be an array of size `m`.
- Set $\text{longest}_{border}[0] = 0$.
- Iterate `i` from `1` to `m-1`.
- If $\text{needle}[prev] = \text{needle}[i]$, increment `prev` and set $\text{longest}_{border}[i] = prev$. Increment `i`.
- Else if $\text{needle}[prev] \neq \text{needle}[i]$.
           - If $prev = 0$, set $\text{longest}_{border}[i] = 0$. Increment `i`
           - Else if $prev \neq 0$, set $prev = \text{longest}_{border}[prev-1]$.

4. SEARCH in `haystack` for `needle`.
- Let $\text{haystack}_{pointer}$ be `0`.
- Let $\text{needle}_{pointer}$ be `0`. It also represents the number of matches in the current window.
- Do this until $\text{haystack}_{pointer} < n$
- If characters at $haystack[\text{haystack}_{pointer}]$ matches with character at $needle[\text{needle}_{pointer}]$, increment $\text{needle}_{pointer}$ and $\text{haystack}_{pointer}$, and check for next characters.
            If $\text{needle}_{pointer} = m$, return $\text{haystack}_{pointer}-m$ (as `needle` is found in `haystack` starting at index $\text{haystack}_{pointer}-m$).
- If characters don't match,
- If $\text{needle}_{pointer} = 0$, it means zero matching. In this case, increment $\text{haystack}_{pointer}$ and check for the next m-substring.
- Else if $\text{needle}_{pointer} \neq 0$, it means Partial Matching. Set $\text{needle}_{pointer} = \text{longest}_{border}[\text{needle}_{pointer}-1]$. Don't increment $\text{haystack}_{pointer}$. We want to examine the mismatched character of `haystack` with the first character after matched characters of `needle`.

5. If we have reached here, return `-1`, as `needle` is not found in `haystack`.

> **Example:** Let `haystack` be "onionionskys" and `needle` be "onions". The length of `haystack` is $n = 12$ and length of the `needle` is $m = 6$.
>
> !?!../Documents/28/28_KMP.json:1280,720!?!

<br/>

#### Implementation

```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(needle)
        n = len(haystack)

        if n < m:
            return -1

        # PREPROCESSING
        # longest border array
        longest_border = [0] * m
        # Length of Longest Border for prefix before it.
        prev = 0
        # Iterating from index-1. longest_border[0] will always be 0
        i = 1

        while i < m:
            if needle[i] == needle[prev]:
                # Length of Longest Border Increased
                prev += 1
                longest_border[i] = prev
                i += 1
            else:
                # Only empty border exist
                if prev == 0:
                    longest_border[i] = 0
                    i += 1
                # Try finding longest border for this i with reduced prev
                else:
                    prev = longest_border[prev - 1]

        # SEARCHING
        # Pointer for haystack
        haystack_pointer = 0
        # Pointer for needle.
        # Also indicates number of characters matched in current window.
        needle_pointer = 0

        while haystack_pointer < n:
            if haystack[haystack_pointer] == needle[needle_pointer]:
                # Matched Increment Both
                needle_pointer += 1
                haystack_pointer += 1
                # All characters matched
                if needle_pointer == m:
                    # m characters behind last matching will be window start
                    return haystack_pointer - m
            else:
                if needle_pointer == 0:
                    # Zero Matched
                    haystack_pointer += 1
                else:
                    # Optimally shift left needle_pointer.
                    # Don't change haystack_pointer
                    needle_pointer = longest_border[needle_pointer - 1]

        return -1
```

#### Complexity Analysis

* Time complexity: $O(n)$.

- If $n<m$, then we immediately return -1. Hence, it is $O(1)$ in this case.
- Otherwise,

- Pre-processing takes $O(m)$ time.
- In the case of "Matching", or "Mismatch (Empty Previous Border)", we simply increment `i`, which is $O(1)$.
- In the case of "Mismatch (Non-Empty Previous Border)", we reduce `prev` to $\text{longest}_{border}[prev-1]$. In other words, we try to reduce at most as many times as the `while` loop has executed. There will be at most $m-1$ such reductions.
- Thus, it will be $O(m)$.
- Searching takes $O(n)$ time.
- We never backtrack/reset the $\text{haystack}_{pointer}$. We increment it by 1 in Matching or Zero-Matching.
- In Partial-Matching, we don't immediately increment and try to reduce to a condition of Matching, or Zero-Matching. For this, we set $\text{needle}_{pointer}$ to $\text{longest}_{border}[\text{needle}_{pointer}-1]$, which always reduces to 0 or matches. The maximum number of rollbacks of $\text{needle}_{pointer}$ is bounded by $\text{needle}_{pointer}$. **For any mismatch, we can only roll back as much as we have advanced up to the mismatch.**.
- Thus, for searching it is $O(2n)$, which is $O(n)$.
- Hence, it is $O(m+n)$ and since $n \geq m$, we can ignore $m$ term. The final upper bound is $O(2 \cdot n)$, which is $O(n)$.
- Therefore, overall it is $O(n) + O(1)$, which is $O(n)$.
- No worst-case or accidental inputs exist here.

* Space complexity: $O(m)$. To store the $\text{longest}_{border}$ array, we need $O(m)$ extra space.

> **Note:** Although KMP is fast, still built-in functions of many programming languages use Brute Force. KMP is based on assumption that there would be many duplicate similar substrings. In real-world strings, this is not the case. So, KMP is not used in real-world applications. Moreover, it requires linear space.
>
> However, it has its application in DNA sequencing. DNA is a long string of characters (A, C, G, T). There are many similar substrings in DNA. So, KMP is used in DNA sequencing.

---