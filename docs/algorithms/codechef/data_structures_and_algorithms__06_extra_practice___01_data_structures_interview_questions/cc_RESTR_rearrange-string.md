# Rearrange String

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | RESTR |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Strings |
| Official Link | [RESTR](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_05/problems/RESTR) |

---

## Problem Statement

Chef gave you a string $S$ of length $N$, then he asked you whether it is possible to rearrange the characters such that no character appears thrice consecutively.

If it is possible then print **YES** otherwise print **No**.

---

## Input Format

- First-line will contain $T$ - the number of test cases. Then the test cases follow.
- Each test case contains two lines of input.
- The first line of every test case contains an integer $N$ - the size of the string.
- The second line of every test case contains a string $S$ of size $N$.

---

## Output Format

For each testcase, output whether it is possible to rearrange the characters such that no character appears thrice consecutively.

---

## Constraints

- $1 \leq T \leq 5000$
- $1 \leq N \leq 10^5, \sum N \leq 5\cdot10^5$
- The string contains only lowercase english letters

---

## Examples

**Example 1**

**Input**

```text
3
4
wsww
3
www
7
xwakwms
```

**Output**

```text
YES
NO
YES
```

**Explanation**

- **Test Case $1$**: The given arrangement already satisfies the given condition.

- **Test Case $2$**: Since only 'w' is present three times, therefore, it is not possible to satisfy the condition here.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4
wsww
```

**Output for this case**

```text
YES
```



#### Test case 2

**Input for this case**

```text
3
www
```

**Output for this case**

```text
NO
```



#### Test case 3

**Input for this case**

```text
7
xwakwms
```

**Output for this case**

```text
YES
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

In this lesson, we will discuss how to solve the problem of rearranging a string so that no character appears three consecutive times. We will explore three different approaches. Understanding multiple techniques not only helps you decide which method is best for a given situation but also deepens your understanding of problem solving and algorithm design.

---

### **Approach 1: Frequency Analysis**

In the first approach, we analyze the frequency of each character in the string. The key observation is that if a character appears too frequently, it may be impossible to separate its occurrences so that there are never three consecutive copies.

Let the maximum frequency of any character in the string be $f_{max}$ and let the total number of characters be $N$. If we wish to arrange the $f_{max}$ copies such that no three consecutive occurrences happen, we can consider grouping them in blocks of at most two. The number of groups needed is given by:

$$
\text{groups} = \left\lceil \frac{f_{max}}{2} \right\rceil
$$

Between these groups, we require at least $\text{groups} - 1$ other characters to act as separators. Therefore, the condition for a valid rearrangement is:

$$
N - f_{max} \geq \left\lceil \frac{f_{max}}{2} \right\rceil - 1
$$

If this condition holds, the answer is **YES**; otherwise, it is **NO**.

Below are the code implementations in both C++ and Python for this approach.

#### **C++ Code (Approach 1)**
```cpp
#include
#include
#include
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    while(T--){
        int N;
        cin >> N;
        string S;
        cin >> S;

        vector freq(26, 0);
        for(char c : S)
            freq[c - 'a']++;

        int fmax = *max_element(freq.begin(), freq.end());
        int groups = (fmax + 1) / 2; // Equivalent to ceil(fmax/2)
        int others = N - fmax;

        if(others >= groups - 1)
            cout << "YES\n";
        else
            cout << "NO\n";
    }

    return 0;
}
```

#### **Python Code (Approach 1)**
```python
import sys

inputData = sys.stdin.read().strip().split()
t = int(inputData[0])
index = 1
for _ in range(t):
    n = int(inputData[index])
    index += 1
    s = inputData[index]
    index += 1

    freq = [0] * 26
    for c in s:
        freq[ord(c) - ord('a')] += 1
    fmax = max(freq)
    groups = (fmax + 1) // 2  # Equivalent to ceil(fmax/2)
    others = n - fmax
    if others >= groups - 1:
        print("YES")
    else:
        print("NO")
```

---

### **Approach 2: Greedy Simulation Using Sorted Iteration**

In this approach, we simulate the process of rearranging the string character by character. We maintain a frequency table of characters, and at each step, we choose the character with the highest remaining frequency that does not cause three consecutive occurrences.

**Key Idea:**
- At each position, check each character (from 'a' to 'z') that still has remaining occurrences.
- If the last two characters in our constructed answer are the same as the candidate, skip that candidate.
- Among the valid candidates, choose the one with the highest remaining frequency.
- If no character can be chosen, then it is impossible to create a valid rearrangement.

This simulation runs in $O(N \cdot 26)$ per test case, which is efficient given that there are only 26 letters.

#### **C++ Code (Approach 2)**
```cpp
#include
#include
#include
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    while(T--){
        int N;
        cin >> N;
        string s;
        cin >> s;

        vector freq(26, 0);
        for(char c: s)
            freq[c - 'a']++;

        string ans = "";
        bool possible = true;

        for (int i = 0; i < N; i++){
            int candidate = -1;
            for (int c = 0; c < 26; c++){
                if (freq[c] <= 0) continue;
                int len = ans.size();
                if(len >= 2 && ans[len-1] == 'a' + c && ans[len-2] == 'a' + c)
                    continue;
                if(candidate == -1 || freq[c] > freq[candidate])
                    candidate = c;
            }
            if(candidate == -1){
                possible = false;
                break;
            }
            ans.push_back('a' + candidate);
            freq[candidate]--;
        }

        if(possible)
            cout << "YES\n";
        else
            cout << "NO\n";
    }
    return 0;
}
```

#### **Python Code (Approach 2)**
```python
import sys

data = sys.stdin.read().strip().split()
t = int(data[0])
index = 1

for _ in range(t):
    n = int(data[index])
    index += 1
    s = data[index]
    index += 1

    freq = [0] * 26
    for c in s:
        freq[ord(c) - ord('a')] += 1

    ans = []
    possible = True

    for i in range(n):
        candidate = -1
        for c in range(26):
            if freq[c] <= 0:
                continue
            if len(ans) >= 2 and ans[-1] == chr(c + ord('a')) and ans[-2] == chr(c + ord('a')):
                continue
            if candidate == -1 or freq[c] > freq[candidate]:
                candidate = c
        if candidate == -1:
            possible = False
            break
        ans.append(chr(candidate + ord('a')))
        freq[candidate] -= 1
    if possible:
        sys.stdout.write("YES\n")
    else:
        sys.stdout.write("NO\n")
```

---

### **Approach 3: Greedy Rearrangement Using a Priority Queue**

This approach also constructs an answer greedily but uses a max-heap (priority queue) to always extract the character with the highest remaining frequency. The modified steps are as follows:

1. **Initialization:**
   - Count the frequency of each character.
   - Push each character along with its frequency into a max-heap.

2. **Rearrangement Process:**
   - At each step, extract the character with the highest frequency.
   - Check if placing this character would cause three consecutive occurrences. If it does, temporarily set it aside and check the next character.
   - Once a valid character is found, append it to the answer, decrease its frequency, and push it back into the heap if it still has remaining occurrences.
   - If no valid character is found at any step, then it is impossible to form a valid arrangement.

3. **Final Check:**
   - After processing all characters, if the constructed answer’s length equals $N$, the rearrangement is successful.

This approach efficiently manages the candidates using the heap data structure.

#### **C++ Code (Approach 3)**
```cpp
#include
#include
#include
#include
using namespace std;

struct Node {
    int freq;
    char ch;
};

struct cmp {
    bool operator()(const Node &a, const Node &b) {
        return a.freq < b.freq;
    }
};

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    while(T--){
        int N;
        cin >> N;
        string s;
        cin >> s;

        vector freq(26, 0);
        for(char c: s)
            freq[c - 'a']++;

        priority_queue, cmp> pq;
        for (int i = 0; i < 26; i++) {
            if(freq[i] > 0)
                pq.push({freq[i], char('a' + i)});
        }

        string ans = "";
        bool possible = true;

        while(!pq.empty()){
            bool placed = false;
            vector temp;
            while(!pq.empty()){
                Node cur = pq.top();
                pq.pop();
                int len = ans.size();
                if(len >= 2 && ans[len-1] == cur.ch && ans[len-2] == cur.ch){
                    temp.push_back(cur);
                }
                else {
                    ans.push_back(cur.ch);
                    cur.freq -= 1;
                    if(cur.freq > 0)
                        pq.push(cur);
                    placed = true;
                    break;
                }
            }
            for(auto &node: temp)
                pq.push(node);
            if(!placed){
                possible = false;
                break;
            }
        }

        if(ans.size() == N && possible)
            cout << "YES\n";
        else
            cout << "NO\n";
    }

    return 0;
}
```

#### **Python Code (Approach 3)**
```python
import sys, heapq
input_data = sys.stdin.read().strip().split()
t = int(input_data[0])
index = 1
for _ in range(t):
    n = int(input_data[index])
    index += 1
    s = input_data[index]
    index += 1

    freq = [0] * 26
    for c in s:
        freq[ord(c) - ord('a')] += 1

    heap = []
    for i in range(26):
        if freq[i] > 0:
            heapq.heappush(heap, (-freq[i], chr(i + ord('a'))))

    ans = []
    possible = True
    while heap:
        placed = False
        temp = []
        while heap:
            f, ch = heapq.heappop(heap)
            if len(ans) >= 2 and ans[-1] == ch and ans[-2] == ch:
                temp.append((f, ch))
            else:
                ans.append(ch)
                f += 1  # since f is negative, add 1 to decrease count
                if f < 0:
                    heapq.heappush(heap, (f, ch))
                placed = True
                break
        for item in temp:
            heapq.heappush(heap, item)
        if not placed:
            possible = False
            break
    if possible and len(ans) == n:
        sys.stdout.write("YES\n")
    else:
        sys.stdout.write("NO\n")
```

---

### **Summary and Intuition**

- **Approach 1** leverages a mathematical observation about the distribution of characters. The formula
  $$ N - f_{max} \geq \left\lceil \frac{f_{max}}{2} \right\rceil - 1 $$
  ensures that there are enough other characters to separate the most frequent letters. This method is very efficient with $O(N)$ time.

- **Approach 2** directly simulates the rearrangement by iterating over positions and choosing the most frequent valid candidate. It is intuitive and easy to implement when the number of distinct characters is small (only 26 lowercase letters).

- **Approach 3** uses a priority queue to always pick the most promising candidate. This is a classic greedy method for rearrangement problems and is highly adaptable to similar problem constraints.

Understanding these methods provides a robust toolkit when facing rearrangement and scheduling problems in data structures and algorithms interviews.

Happy coding and good luck with your interviews!

</details>
