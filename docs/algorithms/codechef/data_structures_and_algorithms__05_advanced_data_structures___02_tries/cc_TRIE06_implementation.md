# Implementation

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | TRIE06 |
| Difficulty Band | Tries |
| Path | Data Structures and Algorithms |
| Lesson | Learn Tries |
| Official Link | [TRIE06](https://www.codechef.com/learn/course/tries/LTRIE01/problems/TRIE06) |

---

## Problem Statement

Implement the trie data structure as taught in the previous sections.

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
8
insert cat
insert cats
insert dog
insert hello
words
search hello
delete hello
search hello
```

**Output**

```text
cat
cats
dog
hello
present
not present
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Statement - [https://www.codechef.com/learn/course/tries/LTRIE01/problems/TRIE06](https://www.codechef.com/learn/course/tries/LTRIE01/problems/TRIE06)

### [](#problem-statement-1)Problem Statement:

Implement the trie data structure as taught in the previous sections.

### [](#approach-2)Approach:

The key idea of this solution is to utilize a **Trie** data structure to manage and store words efficiently. A Trie is especially useful for prefix-related queries. Here’s how the approach works:

-

**Trie Structure**:

- Each `TrieNode` contains:

- An array of children nodes (one for each letter of the alphabet).

- A boolean flag `isEndOfWord` to indicate if a node marks the end of a valid word.

-

**Insert Function**:

- The `insert` function adds a new word to the Trie.

- It starts from the root and traverses through each character of the word, creating new nodes as needed. At the end of the word, it marks the last node as an end-of-word.

-

**Search Function**:

- The `search` function checks if a word exists in the Trie.

- It traverses through the Trie using the characters of the word. If it reaches the end and finds the end-of-word flag set to true, the word exists.

-

**Delete Function**:

- The `deleteWord` function allows for removing a word from the Trie.

- It recursively navigates through the Trie and removes nodes if they are not needed (i.e., if they don’t form a prefix of any other word).

-

**Print All Words**:

- The `printAllWords` function prints all the words stored in the Trie.

- It uses a recursive helper function to traverse the Trie and builds words character by character.

-

**Main Function**:

- The main function handles user input to execute commands: inserting words, searching for words, deleting words, and printing all stored words.

### [](#time-complexity-3)Time Complexity:

-

**Insertion**: O(L)

-

**Search**: O(L)

-

**Deletion**: O(L)

-

**Print All Words**: O(N * L) where N is the number of words and L is the average length of the words.

### [](#space-complexity-4)Space Complexity:

- **O(N * L)** for storing N words of average length L, since each character can create a node in the Trie.

</details>
