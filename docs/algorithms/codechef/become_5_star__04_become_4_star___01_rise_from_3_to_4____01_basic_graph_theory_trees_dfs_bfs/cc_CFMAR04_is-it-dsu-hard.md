# IS IT DSU HARD!!

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CFMAR04 |
| Difficulty Band | Rise from 3* to 4* |
| Path | Become 5 star |
| Lesson | Basic Graph Theory - Trees, DFS, BFS |
| Official Link | [CFMAR04](https://www.codechef.com/practice/course/3to4stars/LP3TO401/problems/CFMAR04) |

---

## Problem Statement

You might hear about  Disjoint Set Union,[click here](https://en.wikipedia.org/wiki/Disjoint-set_data_structure) for more info. Question is, You are given a list of $N$ words (strings containing only lower case English alphabet). Let's say two words are equivalent if one word can be obtained by rearranging the letters of another word. Your task is, form sets equivalent words and print the size of the $largest$ set.

### Input:

- First-line will contain $N$, the number of words.
- The next $N$ line contains a string.

### Output:
Output the size of the $largest$ subset of equivalent words.

### Constraints
- $1 \leq N \leq 10^5$
- $1 \leq |S| \leq 10^5$
- $$
\begin{equation}
\sum_{i=1}^{N}|S|
\leq 10^6 \end{equation}
$$

---

## Examples

**Example 1**

**Input**

```text
4
aaa
aba
aab
aca
```

**Output**

```text
2
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [IS IT DSU HARD!!](https://www.codechef.com/practice/course/3to4stars/LP3TO401/problems/CFMAR04?tab=statement)

### [](#problem-statement-1)Problem Statement

You might hear about  Disjoint Set Union,[click here](https://en.wikipedia.org/wiki/Disjoint-set_data_structure) for more info. Question is, You are given a list of N words (strings containing only lower case English alphabet). Let’s say two words are equivalent if one word can be obtained by rearranging the letters of another word. Your task is, form sets equivalent words and print the size of the largest set.

### [](#approach-2)Approach

To solve this problem, the idea is to group words that are equivalent by using a common representation for all anagrams. For each word, we sort its letters; this sorted version will be the same for any anagrams, allowing us to use it as a **“key”** in an unordered map. Each unique sorted form in the map represents a distinct group of equivalent words, and the map’s values track the size of each group.

-

Initialize an unordered map `mp` where each key is the sorted form of a word and each value is the count of words that share this form.

-

For each word, sort it to find its **“canonical”** form, then add or update this form in the map.

-

After processing all words, find the largest value in the map, representing the largest group size of equivalent words.

### [](#time-complexity-3)Time Complexity

O(n \times m \log m), where n is the number of words and m is the maximum length of a word.

### [](#space-complexity-4)Space Complexity

O(n \times m), for storing each word’s sorted version in the hash map.

</details>
