### 1. Description

You are given a string `s` of length `n` and an integer array `cost` of the same length, where $\text{cost}[i]$ is the cost to **delete** the $$i^{\text{th}}$$ character of `s`.

You may delete any number of characters from `s` (possibly none), such that the resulting string is **non-empty** and consists of **equal** characters.

Return an integer denoting the **minimum** total deletion cost required.

### 2. Function Contract

**Inputs**

- `s`: A nonempty string of lowercase English letters.
- `cost`: A positive deletion cost for each corresponding character of `s`.

Let $N=\lvert s\rvert=\lvert\texttt{cost}\rvert$. A deletion removes a character from the result but does not change the cost associated with any other original position. At least one character must remain.

**Return value**

Return the minimum total cost of deletions that leaves a nonempty string containing only one distinct character.

### 3. Examples

#### Example 1

- **Input:** s = "aabaac", cost = [1,2,3,4,1,10]

- **Output:** 11

- **Explanation:** Deleting the characters at indices 0, 1, 2, 3, 4 results in the string `"c"`, which consists of equal characters, and the total cost is $\text{cost}[0] + \text{cost}[1] + \text{cost}[2] + \text{cost}[3] + \text{cost}[4] = 1 + 2 + 3 + 4 + 1 = 11$.

#### Example 2

- **Input:** s = "abc", cost = [10,5,8]

- **Output:** 13

- **Explanation:** Deleting the characters at indices 1 and 2 results in the string `"a"`, which consists of equal characters, and the total cost is $\text{cost}[1] + \text{cost}[2] = 5 + 8 = 13$.

#### Example 3

- **Input:** s = "zzzzz", cost = [67,67,67,67,67]

- **Output:** 0

- **Explanation:** All characters in `s` are equal, so the deletion cost is 0.

### 4. Constraints

- $n = \text{s.length} = \text{cost.length}$

- $1 \le n \le 10^{5}$

- $1 \le \text{cost}[i] \le 10^{9}$

- `s` consists of lowercase English letters.
