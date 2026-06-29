# Auto-Complete

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | TRIE11 |
| Difficulty Band | Tries |
| Path | Data Structures and Algorithms |
| Lesson | Learn Tries |
| Official Link | [TRIE11](https://www.codechef.com/learn/course/tries/LTRIE02/problems/TRIE11) |

---

## Problem Statement

Complete the function autocomplete to print all the words in the trie that start with a string $S$. The string $S$ is passed as an argument in the function

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case contains two space-separated integers $N$ and $M$ — the number of vertices and edges of the graph, respectively.
    - The next $M$ lines describe the edges. The $i$-th of these $M$ lines contains two space-separated integers $u_i$ and $v_i$, denoting an edge between $u_i$ and $v_i$.

---

## Output Format

For each test case, output on a new line the number of good subgraphs of $G$, modulo $10^9 + 7$.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N \leq 100$
- $1 \leq M \leq N\cdot(N-1)/2$
- $1 \leq u_i, v_i \leq N$
- $u_i \neq v_i$ for each $1 \leq i \leq M$.
- The sum of $N$ over all test cases won't exceed $100$.

---

## Examples

**Example 1**

**Input**

```text
10 sa
hello 
world
code
chef
so
safari
safe
safer
save
saved
```

**Output**

```text
safari
safe
safer
save
saved
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Auto-Complete](https://www.codechef.com/learn/course/tries/LTRIE02/problems/TRIE11)

### [](#problem-statement-1)Problem Statement:

Complete the function autocomplete to print print all the words in the trie that start with a string `S`. The string `S` is passed as an argument in the function

### [](#approach-2)Approach:

The key idea of this solution is to use a **Trie** (pronounced as “try”), which is a specialized tree-like data structure used for storing a dynamic set of strings. Each node in the Trie represents a character of a word, and it allows for efficient insertion and search operations.

-

**TrieNode Structure**:

-

Each `TrieNode` has an array of pointers (`children`) to its child nodes, representing the next characters in the words.

-

A boolean flag (`isEndOfWord`) indicates if the node marks the end of a valid word.

-

**Trie Class**: `insert(const string& word)`

-

This function inserts a word into the Trie by iterating through each character of the word.

-

For each character, it checks if the corresponding child node exists; if not, it creates a new node.

-

Once all characters of the word are processed, it marks the last node as the end of a word.

-

**search(const string& word)**:

-

This function searches for a word in the Trie by checking if the characters exist in sequence.

-

It returns true if the word exists in the Trie and is marked as an end of a word.

-

**Main Function**:

-

First, it reads a number of words to be inserted into the Trie.

-

It then reads words to be searched and prints “correct” if found and “incorrect” otherwise.

This logic makes the Trie a powerful tool for prefix-based search problems and ensures efficient lookup times.

### [](#time-complexity-3)Time Complexity:

-

**Insertion**: **O(m)** where `m` is the length of the word being inserted.

-

**Search**: **O(m)** where `m` is the length of the word being searched.

### [](#space-complexity-4)Space Complexity:

- **O(n * m)** where `n` is the number of words and `m` is the average length of the words, as each word can create up to m nodes in the Trie.

</details>
