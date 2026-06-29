# Graphs - Word Ladder

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PREP36 |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Graphs |
| Official Link | [PREP36](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_12/problems/PREP36) |

---

## Problem Statement

Given two words $A$, $B$ and a set $W$ consisting of $M$ distinct words $W_1, W_2, \dots, W_M$. Every word has same length and consists of lowercase english characters.

A **transformation sequence** from word $A$ to word $B$ using a set of words $W$ is a sequence of words $A \rightarrow S_1 \rightarrow S_2 \rightarrow \dots \rightarrow S_l \rightarrow B$ such that,
- Every adjacent pair of words differs by a single letter.
- Every $S_i$ for $1 \leq i \leq l$ should be in $W$. Note that $A$, $B$ does not need to be in $W$.

Find the number of words in the **shortest transformation sequence** from $A$ to $B$, or $-1$ if no such sequence present.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- The first line of each test case contains two space-separated words $A$, $B$.
- Then next line each test case contains integer $M$ — number of distinct words in $W$.
- The next line contain $M$ space-separated words $W_i$ — the $i^{th}$ word.

---

## Output Format

For each test case, output on a new line the number of words in the **shortest transformation sequence** from $A$ to $B$, or $-1$ if no such sequence present.

---

## Constraints

- $1 \leq T \leq 10$
- $1 \leq M \leq 45000$
- $ 1 \leq |A|, |B|, |W_i| \leq 10$
- $|A| = |B| = |W_i|$

---

## Examples

**Example 1**

**Input**

```text
3
chef chef
2
chef chaf
abc acb
5
abd acd acj aab cbb
a j
2
c q
```

**Output**

```text
1
4
2
```

**Explanation**

**Test case $1$**: As $A$, $B$ both same words so the **shortest transformation sequence** will have one word `chef` only.

**Test case $2$**: The **shortest transformation sequence** will be `abc` $\rightarrow$ `abd` $\rightarrow$ `acd` $\rightarrow$ `acb`. So there will be $4$ words in the sequence.

**Test case $3$**: The **shortest transformation sequence** will be `a` $\rightarrow$ `j`.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
chef chef
2
chef chaf
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
abc acb
5
abd acd acj aab cbb
```

**Output for this case**

```text
4
```



#### Test case 3

**Input for this case**

```text
a j
2
c q
```

**Output for this case**

```text
2
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# Editorial: Shortest Transformation Sequence

In this lesson, we will solve the problem of finding the shortest transformation sequence from a given word $A$ to a word $B$ by changing one letter at a time. Each intermediate word must belong to a given set $W$, and every adjacent word in the sequence should differ by exactly one letter.

The problem can be visualized as an unweighted graph where each word is a node, and an edge exists between two nodes if the corresponding words differ by a single letter. Our goal is to find the shortest path from $A$ to $B$ in this graph.

Below are three important approaches used to solve this problem.

---

## Approach 1: Single-Directional Breadth-First Search (BFS)

The **BFS approach** is a straightforward and effective method to determine the shortest transformation sequence. The idea is as follows:

1. **Graph Representation:** Treat every word as a node and consider an edge between two words if they differ by one letter.
2. **BFS Initialization:** Start with word $A$ with an initial distance of $1$. Use a queue to explore all possible one-letter variations.
3. **Transformation:** For each word, for every position in the word, try replacing the character with every letter from `'a'` to `'z'`. If the new word exists in $W$ (or equals $B$) and hasn't been visited, add it to the queue with an updated distance.
4. **Termination:** Stop when you reach word $B$ and return its distance; if the queue is exhausted without finding $B$, return $-1$.

This approach has a time complexity of roughly $$\mathcal{O}(M \times L \times 26)$$ where $M$ is the number of words and $L$ is their length. Given the constraints, this is efficient enough.

### Code Implementation

#### C++ Code

```cpp
#include
#include
#include
#include
#include
#include
using namespace std;

int shortestTransformationSequence(string A, string B, vector& W) {
    if (A == B) return 1;

    unordered_set wordSet(W.begin(), W.end());
    if (wordSet.find(B) == wordSet.end()) wordSet.insert(B);

    queue q;
    unordered_map distance;
    q.push(A);
    distance[A] = 1;

    while (!q.empty()) {
        string current = q.front();
        q.pop();

        if (current == B) return distance[current];

        for (int i = 0; i < current.length(); i++) {
            string temp = current;
            for (char ch = 'a'; ch <= 'z'; ch++) {
                temp[i] = ch;
                if (wordSet.find(temp) != wordSet.end() && distance.find(temp) == distance.end()) {
                    distance[temp] = distance[current] + 1;
                    q.push(temp);
                }
            }
        }
    }

    return -1;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int T;
    cin >> T;

    while (T--) {
        string A, B;
        cin >> A >> B;

        int M;
        cin >> M;

        vector W(M);
        for (int i = 0; i < M; i++) {
            cin >> W[i];
        }

        cout << shortestTransformationSequence(A, B, W) << "\n";
    }

    return 0;
}
```

#### Python Code

```python
def shortest_transformation_sequence(A, B, words):
    if A == B:
        return 1
    wordSet = set(words)
    wordSet.add(B)
    from collections import deque
    distance = {A: 1}
    q = deque([A])

    while q:
        current = q.popleft()
        if current == B:
            return distance[current]
        for i in range(len(current)):
            for ch in 'abcdefghijklmnopqrstuvwxyz':
                temp = current[:i] + ch + current[i+1:]
                if temp in wordSet and temp not in distance:
                    distance[temp] = distance[current] + 1
                    q.append(temp)
    return -1

if __name__ == '__main__':
    import sys
    input_data = sys.stdin.read().strip().split()
    t = int(input_data[0])
    index = 1
    outputs = []
    for _ in range(t):
        A = input_data[index]
        B = input_data[index+1]
        index += 2
        m = int(input_data[index])
        index += 1
        words = input_data[index:index+m]
        index += m
        outputs.append(str(shortest_transformation_sequence(A, B, words)))
    sys.stdout.write("\n".join(outputs))
```

---

## Approach 2: Bidirectional Breadth-First Search

The **Bidirectional BFS** approach reduces the search space by simultaneously exploring from both ends ($A$ and $B$). The main steps include:

1. **Initialization:** Maintain two sets for the frontiers starting from $A$ and $B$ respectively.
2. **Alternate Expansion:** Expand the smaller frontier at each level to keep the search tree balanced.
3. **Intersection Check:** If the frontiers intersect, a connection is found and the number of levels we have expanded gives the shortest transformation sequence length.
4. **Edge Cases:** If no transformation is found, return $-1$.

This approach can often be faster than single-direction BFS especially when the difference between $A$ and $B$ is significant.

### Code Implementation

#### C++ Code

```cpp
#include
#include
#include
#include
#include
#include
using namespace std;

int bidirectionalBFS(string start, string end, unordered_set& wordSet) {
    if (start == end) return 1;

    unordered_set beginSet, endSet, visited;
    beginSet.insert(start);
    endSet.insert(end);
    int level = 1;

    while (!beginSet.empty() && !endSet.empty()) {
        if (beginSet.size() > endSet.size())
            swap(beginSet, endSet);

        unordered_set tempSet;
        for (auto word : beginSet) {
            string current = word;
            for (int i = 0; i < current.size(); i++) {
                char original = current[i];
                for (char ch = 'a'; ch <= 'z'; ch++) {
                    current[i] = ch;
                    if (endSet.find(current) != endSet.end()) {
                        return level + 1;
                    }
                    if (wordSet.find(current) != wordSet.end() && visited.find(current) == visited.end()) {
                        tempSet.insert(current);
                        visited.insert(current);
                    }
                }
                current[i] = original;
            }
        }
        beginSet = tempSet;
        level++;
    }
    return -1;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;

    while (T--) {
        string A, B;
        cin >> A >> B;

        int M;
        cin >> M;

        unordered_set wordSet;
        for (int i = 0; i < M; i++) {
            string word;
            cin >> word;
            wordSet.insert(word);
        }
        if (wordSet.find(B) == wordSet.end()) wordSet.insert(B);

        cout << bidirectionalBFS(A, B, wordSet) << "\n";
    }

    return 0;
}
```

#### Python Code

```python
def bidirectional_bfs(begin, end, wordSet):
    if begin == end:
        return 1
    begin_set = {begin}
    end_set = {end}
    visited = set()
    level = 1

    while begin_set and end_set:
        if len(begin_set) > len(end_set):
            begin_set, end_set = end_set, begin_set
        temp_set = set()
        for word in begin_set:
            for i in range(len(word)):
                for ch in 'abcdefghijklmnopqrstuvwxyz':
                    new_word = word[:i] + ch + word[i+1:]
                    if new_word in end_set:
                        return level + 1
                    if new_word in wordSet and new_word not in visited:
                        temp_set.add(new_word)
                        visited.add(new_word)
        begin_set = temp_set
        level += 1
    return -1

if __name__ == "__main__":
    import sys
    data = sys.stdin.read().split()
    t = int(data[0])
    idx = 1
    results = []
    for _ in range(t):
        A = data[idx]
        B = data[idx+1]
        idx += 2
        m = int(data[idx])
        idx += 1
        words = set(data[idx:idx+m])
        idx += m
        words.add(B)
        results.append(str(bidirectional_bfs(A, B, words)))
    sys.stdout.write("\n".join(results))
```

---

## Approach 3: BFS with Precomputed Generic States

Another variation involves precomputing **generic states** (or intermediate representations) of words to speed up the neighbor-finding process.

1. **Generic State Construction:** For each word, form all generic states by replacing each character one position at a time with a special character (e.g., `*`). For a word of length $L$, you generate $L$ generic states.

   $$ \text{Generic state for word } w \text{ at position } i: \quad w[0:i] + "*"+ w[i+1:] $$

2. **Dictionary Mapping:** Build a map from these generic states to all words that can be created with that pattern.
3. **BFS Traversal:** Use BFS starting from $A$. For every intermediate state of the current word, quickly retrieve all potential neighboring words. If you reach $B$, return the level.
4. **Advantages:** This precomputation makes the lookup of adjacent nodes efficient, especially when the list of words is huge.

### Code Implementation

#### C++ Code

```cpp
#include
#include
#include
#include
#include
#include
using namespace std;

int ladderLength(string beginWord, string endWord, vector& wordList) {
    if (beginWord == endWord) return 1;
    int L = beginWord.length();
    unordered_map> allComboDict;

    for (auto &word : wordList) {
        for (int i = 0; i < L; i++) {
            string newWord = word;
            newWord[i] = '*';
            allComboDict[newWord].push_back(word);
        }
    }

    queue> q;
    q.push({beginWord, 1});
    unordered_set visited;
    visited.insert(beginWord);

    while (!q.empty()) {
        auto curr = q.front();
        q.pop();
        string word = curr.first;
        int level = curr.second;

        for (int i = 0; i < L; i++) {
            string intermediate = word;
            intermediate[i] = '*';
            if (allComboDict.find(intermediate) != allComboDict.end()) {
                for (auto adjacent : allComboDict[intermediate]) {
                    if (adjacent == endWord)
                        return level + 1;
                    if (visited.find(adjacent) == visited.end()) {
                        visited.insert(adjacent);
                        q.push({adjacent, level + 1});
                    }
                }
            }
        }
    }
    return -1;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;

    while (T--) {
        string A, B;
        cin >> A >> B;

        int M;
        cin >> M;

        vector wordList(M);
        for (int i = 0; i < M; i++) {
            cin >> wordList[i];
        }

        // Ensure end word is in wordList.
        bool found = false;
        for (auto s : wordList) {
            if (s == B) {
                found = true;
                break;
            }
        }
        if (!found)
            wordList.push_back(B);

        cout << ladderLength(A, B, wordList) << "\n";
    }

    return 0;
}
```

#### Python Code

```python
from collections import defaultdict, deque

def ladder_length(beginWord, endWord, wordList):
    if beginWord == endWord:
        return 1
    L = len(beginWord)
    all_combo_dict = defaultdict(list)
    for word in wordList:
        for i in range(L):
            generic_state = word[:i] + "*" + word[i+1:]
            all_combo_dict[generic_state].append(word)

    q = deque([(beginWord, 1)])
    visited = {beginWord}

    while q:
        word, level = q.popleft()
        for i in range(L):
            generic_state = word[:i] + "*" + word[i+1:]
            for adjacent in all_combo_dict.get(generic_state, []):
                if adjacent == endWord:
                    return level + 1
                if adjacent not in visited:
                    visited.add(adjacent)
                    q.append((adjacent, level + 1))
    return -1

if __name__ == "__main__":
    import sys
    data = sys.stdin.read().split()
    t = int(data[0])
    idx = 1
    results = []
    for _ in range(t):
        beginWord = data[idx]
        endWord = data[idx+1]
        idx += 2
        m = int(data[idx])
        idx += 1
        wordList = data[idx: idx+m]
        idx += m
        if endWord not in wordList:
            wordList.append(endWord)
        results.append(str(ladder_length(beginWord, endWord, wordList)))
    sys.stdout.write("\n".join(results))
```

---

In summary, all three approaches leverage the BFS strategy to explore neighbor words. The **Single-Directional BFS** is simple and intuitive. The **Bidirectional BFS** reduces the search space significantly by working from both $A$ and $B$. The **BFS with Precomputed Generic States** precomputes possible neighbors to make the search faster. Choosing an approach depends on the input size and performance requirements.

Happy coding and best of luck with your DSA preparations!

</details>
