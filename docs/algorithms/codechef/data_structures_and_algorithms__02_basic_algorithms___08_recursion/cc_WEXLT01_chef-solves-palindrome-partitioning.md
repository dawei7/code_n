# Chef Solves Palindrome Partitioning

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | WEXLT01 |
| Difficulty Band | Recursion |
| Path | Data Structures and Algorithms |
| Lesson | Fundamentals of Recursion |
| Official Link | [WEXLT01](https://www.codechef.com/learn/course/recursion/LRECUR03/problems/WEXLT01) |

---

## Problem Statement

Chef has discovered a magical string and wants to explore all the ways to split it such that every piece of the split is a palindrome. \
Given a string $inputString$ consisting of lowercase English letters, Chef wants to find all possible palindrome partitions of this string. \
Help Chef by generating all combinations where each substring is a palindrome.

Chef is excited to see all the ways the string can be partitioned into palindromic substrings and needs your help to list them all.

## Function Declaration

### Function Name
$partitionString$ - This function generates all possible palindrome partitionings of the given string.

### Parameters
- $inputString$ : The input string to be partitioned.
  The string consists of lowercase English letters with length constraints up to 16 characters.

### Return Value
- Returns a array of array of strings, representing all palindrome partitions.
- Each inner array contains a list of substrings forming a palindrome partition.
- The output includes all possible palindrome partition combinations of $inputString$.

## Constraints
- 1 ≤ $T$ ≤ 10
- $1 \leq |$inputString$| \leq 16$
- $inputString$ contains only lowercase English letters.

---

## Input Format

* The first line contains a single integer $T$ — the number of test cases.
* Each of the next $T$ lines contains a single string $inputString$ — the string Chef wants to partition.

---

## Output Format

* For each test case, print all palindrome partitions of the given string.
* Each palindrome partition should be printed as a list of substrings separated by spaces.
* Print each partition on a new line.
* The order of partitions does not matter, but all valid partitions must be printed.

---

## Examples

**Example 1**

**Input**

```text
1
madam
```

**Output**

```text
[m a d a m]
[m ada m]
[madam]
```

**Explanation**

- For "madam", every substring that is a palindrome is considered for partitioning.
- [m a d a m]: all single letters, each a palindrome.
- [m ada m]: "ada" is a palindrome substring in the middle.
- [madam]: the whole string is a palindrome itself.

**Example 2**

**Input**

```text
2
abc
bbb
```

**Output**

```text
[a b c]
[b b b]
[b bb]
[bb b]
[bbb]
```

**Explanation**

- For "abc": Each character is different, so the only palindrome partitions are single letters: [a b c].
- For "bbb": All substrings are palindromes, so partitions include all single letters, pairs like b, bb, and the whole string bbb.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# Approach 1: Naive – Generate All Possible Partitions

## Idea
The string of length n has (n − 1) possible cut positions.
Each cut can either be taken or skipped → 2^(n−1) total partitions.

For each partition:
1. Check all substrings
2. Validate if each substring is a palindrome

## Complexity
- **Time:** O(2ⁿ × n²)
- **Space:** O(2ⁿ × n)

## Drawbacks
- Too many partitions to examine
- Repeated palindrome checks
- No pruning of invalid paths

---

# Approach 2: Improved – Backtracking with On-The-Fly Palindrome Checking

## Idea
Instead of generating all partitions first, build partitions step-by-step:

At index `start`:
- Try every `end` from `start` to `n−1`
- Extract substring S[start..end]
- Check if it is palindrome
  - If yes → extend the current partition
  - If no → stop exploring that extension

This avoids exploring invalid partitions.

## Complexity
- **Time:** O(n × 2ⁿ)
- **Space:** O(n × 2ⁿ)

## Drawbacks
- Still repeats palindrome checks for same substrings
- Palindrome checking costs O(n) each time

---

# Approach 3 (Final Used Approach): DFS + Backtracking with Two-Pointer Palindrome Check

This is the final method used.

## Core Idea
Use depth-first search (DFS) to explore all valid partitions, but prune aggressively:

1. At each position, try all possible substrings starting there.
2. A substring is only accepted if it is a palindrome (checked using two pointers).
3. Once a substring is valid, recursively process the remaining part of the string.
4. When the end of the string is reached, the current partition is complete.

This method ensures:
- Only valid paths are explored
- No extra data structures (like DP tables) are required
- Code remains simple and efficient

---

# Steps of the Final Algorithm

### Step 1: Palindrome Check
To check if substring S[l..r] is a palindrome:
- Use two pointers at l and r
- Move inward while characters match
- If mismatch occurs → not a palindrome
- If pointers cross → palindrome

### Step 2: Depth-First Search (DFS)
At position `start`:
- If `start` = length of string:
  - Current partition is complete → add to result
- Otherwise:
  - Loop `end` from `start` to string length − 1
  - If S[start..end] is palindrome:
    - Add substring to current path
    - Recursively explore from `end + 1`
    - Remove substring (backtracking)

### Step 3: Return All Collected Partitions

---

# Example Walkthrough (Input: "aab")

Start = 0:
- "a" → palindrome → continue
  Start = 1:
  - "a" → palindrome → continue
    Start = 2:
    - "b" → palindrome → continue
      Start = 3 → end reached → output ["a","a","b"]
  - "ab" → not palindrome → skip
- "aa" → palindrome → continue
  Start = 2:
  - "b" → palindrome → output ["aa","b"]
- "aab" → not palindrome → skip

Final Output:
[a a b]
[aa b]

---

# Complexity Analysis

## Time Complexity: O(n × 2ⁿ)
- There are at most 2ⁿ partitions.
- Each palindrome check uses two pointers (worst O(n)).
- Pruning reduces actual cost significantly.

## Space Complexity: O(n)
- Recursion depth at most n.
- Temporary path storage.

(Plus output size: up to O(n × 2ⁿ))

---

# Key Insights
1. Backtracking generates partitions incrementally.
2. Palindrome checks prune invalid branches early.
3. Two-pointer palindrome check keeps cost minimal.
4. For n ≤ 16, this method is fast and memory-efficient.
5. This approach is widely used in competitive programming and interviews.

---

</details>
