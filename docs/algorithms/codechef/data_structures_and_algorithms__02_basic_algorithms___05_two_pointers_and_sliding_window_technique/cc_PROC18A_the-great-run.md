# The Great Run

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PROC18A |
| Difficulty Rating | 1097 |
| Difficulty Band | Two Pointers and Sliding Window Technique |
| Path | Data Structures and Algorithms |
| Lesson | Sliding Window |
| Official Link | [PROC18A](https://www.codechef.com/practice/course/two-pointers/SLIDINGWINDO/problems/PROC18A) |

---

## Problem Statement

Vishal loves running. He often visits his favourite Nehru Park and runs for very long distances. On one such visit he found that the number of girls in the park was unusually high. Now he wants to use this as an opportunity to impress a large number of girls with his awesome speed.

The track on which he runs is an $\text{N}$ kilometres long straight path. There are $\mathbf{a_i}$ girls standing within the $\text{ith}$ kilometre of this path. A girl will be impressed only if Vishal is running at his maximum speed when he passes by her. But he can run at his best speed only for a single continuous stretch of $\text{K}$ kilometres. Now Vishal wants to know what is the maximum number of girls that he can impress.

### Input
First line of the input contains the number of testcases $\text{T}$.

For each test case,

First line contains two space-separated integers $\text{N}$ and $\text{K}$, the length of the track and the maximum distance he can run at his best speed.

Second line contains N space-separated integers, the number of girls within each kilometre of the track.

### Output
For each test case print one line containing an integer, denoting the maximum number of girls Vishal can impress.

### Constraints
$1 \leq \text{T} \leq 10$

$1 \leq \text{K} \leq \text{N} \leq 100$

$1 \leq \mathbf{a_i} \leq 100$

---

## Examples

**Example 1**

**Input**

```text
1
7 2
2 4 8 1 2 1 8
```

**Output**

```text
12
```

**Explanation**

He can impress 4+8=12 girls if he runs at his best speed between the 2nd and the 3rd kilometre, inclusive.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### [](#explanation-1)Explanation

To solve this problem, we can use a sliding window approach. Vishal can impress the maximum number of girls by running his best speed through the segment of the track that has the highest number of girls.

Here’s how you can approach the problem:

- Iterate through the track using a window of size `K` to see how many girls Vishal can impress in that window.

- Keep track of the maximum number of girls impressed in any window so far.

- Output the maximum number after checking all possible windows.

Let’s define the algorithm in steps:

- Initialize a variable `maxImpressed` to 0, which will hold the maximum number of girls that can be impressed.

- For each test case, read `N` and `K`, and then read the array of numbers of girls per kilometre into an array `girls`.

- Initialize a variable `currentImpressed` to sum of the first `K` elements of the `girls` array.

- Set `maxImpressed` to `currentImpressed`.

- Now, slide the window by one kilometre at a time from the beginning to the end :

- Subtract the number of girls at the left end of the window from `currentImpressed` and add the number of girls at the new right end of the window.

- If `currentImpressed` is greater than `maxImpressed`, update `maxImpressed` with the value of `currentImpressed`.

- Once we have checked all windows, `maxImpressed` contains the highest number of girls Vishal can impress.

### [](#c-2)C++
``#include <iostream>
#include <vector>
using namespace std;

int main() {
    int T, N, K;
    cin >> T;
    while (T--) {
        cin >> N >> K;
        vector<int> girls(N);
        int currentImpressed = 0, maxImpressed = 0;
        for (int i = 0; i < N; i++) {
            cin >> girls[i];
            if (i < K) currentImpressed += girls[i];
        }
        maxImpressed = currentImpressed;
        for (int i = K; i < N; i++) {
            currentImpressed = currentImpressed - girls[i - K] + girls[i];
            maxImpressed = max(maxImpressed, currentImpressed);
        }
        cout << maxImpressed << endl;
    }
    return 0;
}
``

### [](#java-solution-3)Java Solution
``import java.util.Scanner;

class main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int T = Integer.parseInt(scanner.nextLine());
        for (int t = 0; t < T; t++) {
            String[] firstLine = scanner.nextLine().split(" ");
            int N = Integer.parseInt(firstLine[0]);
            int K = Integer.parseInt(firstLine[1]);

            String[] girlsInput = scanner.nextLine().split(" ");
            int[] girls = new int[girlsInput.length];
            for (int i = 0; i < girlsInput.length; i++) {
                girls[i] = Integer.parseInt(girlsInput[i]);
            }

            int currentImpressed = 0;
            for (int i = 0; i < K; i++) {
                currentImpressed += girls[i];
            }
            int maxImpressed = currentImpressed;

            for (int i = K; i < N; i++) {
                currentImpressed = currentImpressed - girls[i - K] + girls[i];
                maxImpressed = Math.max(maxImpressed, currentImpressed);
            }
            System.out.println(maxImpressed);
        }
        scanner.close();
    }
}
``

### [](#python-solution-4)Python Solution
``T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    girls = list(map(int, input().split()))
    currentImpressed = sum(girls[:K])
    maxImpressed = currentImpressed
    for i in range(K, N):
        currentImpressed = currentImpressed - girls[i - K] + girls[i]
        maxImpressed = max(maxImpressed, currentImpressed)
    print(maxImpressed)
``

</details>
