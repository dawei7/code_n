# Spell Check

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | TRIE09 |
| Difficulty Band | Tries |
| Path | Data Structures and Algorithms |
| Lesson | Learn Tries |
| Official Link | [TRIE09](https://www.codechef.com/learn/course/tries/LTRIE02/problems/TRIE09) |

---

## Problem Statement

You are given a list of words contained in the dictionary and you have to check if a certain word is correct i.e. it is present in this dictionary or not.
Output "correct" if it is present in the dictionary, Otherwise print "incorrect"

---

## Input Format

- The first line of input will contain a single integer $N$, denoting the number of words in the dictionary.
- Following $N$ lines contain $N$ words in the dictionary.
- Next line contains a single integer $M$, denoting the number words to check.
- Following $M$ lines contain $M$ words to check.

---

## Output Format

For each word to check, print "correct" if it exists in the dictionary, otherwise print "incorrect".

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
5
cat
call
bat
god
apple
4
apple
wolf
god
puppy
```

**Output**

```text
correct
incorrect
correct
incorrect
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link: [Spell Check](https://www.codechef.com/learn/course/tries/LTRIE02/problems/TRIE09)

### [](#problem-statement-1)Problem Statement:

You are given a list of words contained in the dictionary and you have to check if a certain word is correct i.e. it is present in this dictionary or not.

Output `correct` if it is present in the dictionary, Otherwise print `incorrect`.

### [](#approach-2)Approach:

The key idea of this solution is to use a **Trie** (pronounced as “try”), which is a specialized tree-like data structure used for storing a dynamic set of strings. Each node in the Trie represents a character of a word, and it allows for efficient insertion and search operations.

-

**TrieNode Structure**:

-

Each `TrieNode` has an array of pointers (`children`) to its child nodes, representing the next characters in the words.

-

A boolean flag (`isEndOfWord`) indicates if the node marks the end of a valid word.

-

**Trie Class**: insert(const string& word):

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

### [](#time-complexity-3)Time Complexity:

-

**Insertion**: **O(m)** where `m` is the length of the word being inserted.

-

**Search**: **O(m)** where `m` is the length of the word being searched.

### [](#space-complexity-4)Space Complexity:

- **O(n * m)** where `n` is the number of words and `m` is the average length of the words, as each word can create up to m nodes in the Trie.

</details>
