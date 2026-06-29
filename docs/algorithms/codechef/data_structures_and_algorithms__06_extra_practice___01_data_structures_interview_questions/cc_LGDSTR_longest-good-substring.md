# Longest Good Substring

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | LGDSTR |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Two pointers |
| Official Link | [LGDSTR](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_11/problems/LGDSTR) |

---

## Problem Statement

Given a string $s$ and an integer $k$, Alice calls a string good if it follows the following condition
- All the characters present in the string are of frequency $k$

Find the longest good substring of the string $s$ to make Alice happy.

String $a$ is a substring of string $b$ if it is possible to choose several consecutive letters in $b$ in such a way that they form $a$.

Output the First such string that occurs.

---

## Input Format

- The first line will contain $2$ numbers |$S$| ,$k$
- The second line contains the string $S$

---

## Output Format

Output the length of the longest good substring and on next line output the substring as well. If there is no such substring, print “IMPOSSIBLE” without the quotes.

---

## Constraints

- $1 \leq |S|,k \leq 10^5$

---

## Examples

**Example 1**

**Input**

```text
8 2
aabcbcde
```

**Output**

```text
6
aabcbc
```

**Explanation**

Substrings {aa,aabcbc,bcbc} follow the good substring condition out of which aabcbc is the longest. and its length is 6.

**Example 2**

**Input**

```text
8 3
abcdefgh
```

**Output**

```text
IMPOSSIBLE
```

**Explanation**

Its not possible to find such a string such that it has all characters with 3 exact occurences.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# Editorial: Longest Good Substring Problem

In this problem, we are given a string $s$ and an integer $k$. A substring is defined as *good* if every character present in it appears exactly $k$ times. Our goal is to find the longest contiguous substring of $s$ that is good. If multiple valid substrings of maximum length exist, we output the first one (i.e. the one that appears earliest in the string). If no such substring exists, we output **IMPOSSIBLE**.

Understanding this problem involves a careful analysis of the frequency distribution of characters in substrings and leveraging efficient methods to search through $s$. In this editorial, we discuss two approaches to solving this problem.

---

## Approaches to the Problem

### Approach 1: Sliding Window with Fixed Window Size

**Concept:**
If a substring is good and contains $d$ distinct characters, then its length is exactly $d \times k$. The key observation is that $d$ can range from $1$ to $\min(26, \lfloor n/k \rfloor)$. For each possible $d$, we set the window size to $d \times k$ and slide it across the string. In each window, we maintain a frequency count of characters and check whether every character present appears exactly $k$ times.

**Methodology:**
1. Compute the maximum possible distinct character count using $\min(26, n/k)$.
2. For each possible distinct count $d$, calculate the required window length $L = d \times k$.
3. Slide a window of size $L$ across the string, updating the frequency counts.
4. For each window, if every character that appears has frequency exactly $k$, output that substring immediately (since we scan from the largest possible window size downward).

**Time Complexity:**
This approach runs efficiently because for each candidate window length, we perform a check in $O(26)$ time per window, which is constant.

Below are the implementations in both **C++** and **Python**.

#### C++ Code (Approach 1)
```cpp
#include
#include
#include
#include
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    cin >> n >> k;
    string s;
    cin >> s;

    // Maximum possible distinct letters in a valid substring
    int maxDistinct = min(26, n / k);
    for (int d = maxDistinct; d >= 1; d--){
        int winSize = d * k;
        if (winSize > n) continue;
        vector freq(26, 0);
        // Initialize first window
        for (int i = 0; i < winSize; i++){
            freq[s[i]-'a']++;
        }

        for (int start = 0; start <= n - winSize; start++){
            if (start > 0){
                freq[s[start-1]-'a']--;
                freq[s[start+winSize-1]-'a']++;
            }
            int distinctCount = 0;
            bool valid = true;
            for (int j = 0; j < 26; j++){
                if (freq[j] > 0){
                    distinctCount++;
                    if (freq[j] != k){
                        valid = false;
                        break;
                    }
                }
            }
            if (valid && distinctCount == d){
                cout << winSize << "\n" << s.substr(start, winSize);
                return 0;
            }
        }
    }
    cout << "IMPOSSIBLE";
    return 0;
}
```

#### Python Code (Approach 1)
```python
def main():
    import sys
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    n = int(input_data[0])
    k = int(input_data[1])
    s = input_data[2]

    maxDistinct = min(26, n // k)
    for d in range(maxDistinct, 0, -1):
        winSize = d * k
        if winSize > n:
            continue
        freq = [0] * 26
        for i in range(winSize):
            freq[ord(s[i]) - ord('a')] += 1
        for start in range(0, n - winSize + 1):
            if start > 0:
                freq[ord(s[start-1]) - ord('a')] -= 1
                freq[ord(s[start+winSize-1]) - ord('a')] += 1
            valid = True
            distinctCount = 0
            for count in freq:
                if count > 0:
                    distinctCount += 1
                    if count != k:
                        valid = False
                        break
            if valid and distinctCount == d:
                sys.stdout.write(str(winSize) + "\n" + s[start:start+winSize])
                return
    sys.stdout.write("IMPOSSIBLE")

if __name__ == "__main__":
    main()
```

---

### Approach 3: Binary Search on Substring Length

**Concept:**
A valid substring must have a length equal to $d \times k$ (i.e. a multiple of $k$). We can perform a binary search over the possible substring lengths that are multiples of $k$. For a candidate length, we use a sliding window to check if a valid substring exists. If one exists, we record its position and try for a larger length; if not, we try a smaller length.

**Methodology:**
1. The candidate lengths are $k$, $2k$, $3k$, \(\dots,\) up to $\lfloor \frac{n}{k} \rfloor \times k$.
2. Use binary search over these candidate lengths:
   - For each candidate length $L$, slide a window over $s$ while updating character frequencies.
   - Check if each character that appears occurs exactly $k$ times.
3. Maintain the first occurrence of the valid substring for the maximum $L$ found.
4. If no candidate length works, output **IMPOSSIBLE**.

**Time Complexity:**
The binary search narrows down the candidate lengths efficiently, and each window validation occurs in $O(n)$ time with a constant $O(26)$ check per window. This method is efficient for large input sizes.

Below are the implementations in both **C++** and **Python**.

#### C++ Code (Approach 3)
```cpp
#include
#include
#include
using namespace std;

bool isValid(const string &s, int L, int k, int &startIndex) {
    int n = s.size();
    vector freq(26, 0);
    for (int i = 0; i < L; i++){
        freq[s[i]-'a']++;
    }
    auto check = [&]() -> bool {
        for (int c = 0; c < 26; c++){
            if(freq[c] > 0 && freq[c] != k)
                return false;
        }
        return true;
    };
    if (check()){
        startIndex = 0;
        return true;
    }
    for (int i = 1; i <= n - L; i++){
        freq[s[i-1]-'a']--;
        freq[s[i+L-1]-'a']++;
        if (check()){
            startIndex = i;
            return true;
        }
    }
    return false;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    cin >> n >> k;
    string s;
    cin >> s;

    int maxCandidate = (n / k) * k;
    int ansLen = -1, ansStart = -1;

    // Binary search only for lengths that are multiples of k
    int low = k, high = maxCandidate;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        // Adjust 'mid' to be a multiple of k
        mid = (mid / k) * k;
        if(mid < k) mid = k;
        if(mid > high) mid = high;
        int startIndex = -1;
        if (isValid(s, mid, k, startIndex)) {
            if (mid > ansLen) {
                ansLen = mid;
                ansStart = startIndex;
            }
            low = mid + k;
        } else {
            high = mid - k;
        }
    }

    if (ansLen == -1)
        cout << "IMPOSSIBLE";
    else {
        cout << ansLen << "\n" << s.substr(ansStart, ansLen);
    }
    return 0;
}
```

#### Python Code (Approach 3)
```python
def is_valid(s, L, k):
    n = len(s)
    freq = [0] * 26
    for i in range(L):
        freq[ord(s[i]) - ord('a')] += 1
    def check():
        for count in freq:
            if count > 0 and count != k:
                return False
        return True
    if check():
        return 0  # Valid starting at index 0
    for i in range(1, n - L + 1):
        freq[ord(s[i-1]) - ord('a')] -= 1
        freq[ord(s[i+L-1]) - ord('a')] += 1
        if check():
            return i
    return -1

def main():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    k = int(data[1])
    s = data[2]

    maxCandidate = (n // k) * k
    ansLen = -1
    ansStart = -1
    low = k
    high = maxCandidate
    while low <= high:
        mid = low + (high - low) // 2
        mid = (mid // k) * k  # Adjust 'mid' to be a multiple of k
        if mid < k:
            mid = k
        if mid > high:
            mid = high
        startIndex = is_valid(s, mid, k)
        if startIndex != -1:
            if mid > ansLen:
                ansLen = mid
                ansStart = startIndex
            low = mid + k
        else:
            high = mid - k
    if ansLen == -1:
        sys.stdout.write("IMPOSSIBLE")
    else:
        sys.stdout.write(str(ansLen) + "\n" + s[ansStart:ansStart+ansLen])

if __name__ == "__main__":
    main()
```

---

## Summary

- **Approach 1** efficiently utilizes the observation that a good substring’s length is fixed once the number of distinct characters is chosen, using a sliding window method.
- **Approach 3** leverages binary search to optimize the search over substring lengths, combining it with a sliding window check for validity.

Each approach has been implemented in both C++ and Python. For practical usage given the constraints, **Approach 1** or **Approach 3** is recommended.

</details>
