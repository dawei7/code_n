# Stone Pile

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | STONE_PILE |
| Difficulty Rating | 1200 |
| Difficulty Band | Stacks and Queues |
| Path | Data Structures and Algorithms |
| Lesson | Queues |
| Official Link | [STONE_PILE](https://www.codechef.com/learn/course/stacks-and-queues/LQUEUES02/problems/STONE_PILE) |

---

## Problem Statement

Aman and Akshat are trying to solve a task given to them by their teacher. They are given a pile of stones containing $N$ stones with an integer written on each of them. There are two different kinds of moves that can be performed on the pile :

1) Player will remove a stone from the $top$ of the pile and put it back on the $bottom$ of the pile

2) Player will remove a stone from the $top$ of the pile and $throw$ it away.

Aman in his turn will perform move $1$ once and then move $2$ once. Akshat in his turn will perform move $1$ twice and then move $2$ once.

They will stop making moves when there is only $1$ stone left in the pile.

Both of them gets turn alternatively with Aman going first. Find the person performing the last move and the number written on the last stone left in the pile.

The stones at index $i'th$ is located higher than the stones at index $j'th$ , such that $(i \lt j)$

---

## Input Format

- The first line contains an integer $T$, representing $T$ Testcases.

- The first line of each test case contains an integer $N$, representing the size of Array $A$.

- The second line of each test case contains $N$ integer, representing array $A$

---

## Output Format

- For each test case, Print $2$ space-separated integer representing the person making the last move ($1$ for Aman and $0$ for Akshat) and the number written on the stone remaining.

---

## Constraints

- $1 \le T \le 100$

- $2 \le N \le 100000$

- $-10^9 \le A_i \le 10^9$

- Sum of $N$ over all test cases does not exceed $10^6$

---

## Examples

**Example 1**

**Input**

```text
3
3
-5 0 5
4 
-1 -3 2 4
6
-100000 0 0 100000 -1000000 1000000
```

**Output**

```text
0 -5
1 2
1 0
```

**Explanation**

In the first test case,

Aman removes the stone $-5$ and put it at the bottom making the pile $\{0,5,-5\}$.

Aman then removes the stone $0$ and throw it away making the pile $\{5,-5\}$.

Akshat then removes $5$ from the top and put it at the bottom of the pile making the pile $\{-5,5\}$.

Akshat then removes $-5$ from the top and put it at the bottom of the pile making the pile $\{5,-5\}$.

Akshat then removes the stone $5$ and throw it away making the pile $\{-5\}$.

The last stone remaining has $-5$ written on it.

In the second test case, Aman removes the second last stone, and the last stone remaining has $2$ written on it.

In the third test case, Aman removes the second last stone, and the last stone remaining has $0$ written on it.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3
-5 0 5
```

**Output for this case**

```text
0 -5
```



#### Test case 2

**Input for this case**

```text
4
-1 -3 2 4
```

**Output for this case**

```text
1 2
```



#### Test case 3

**Input for this case**

```text
6
-100000 0 0 100000 -1000000 1000000
```

**Output for this case**

```text
1 0
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# Editorial

In this lesson, we analyze a game‐simulation problem where two players – Aman and Akshat – manipulate a pile of stones by rotating (moving from the top to the bottom) and discarding stones. The moves are defined as follows:

- **Aman’s Turn:**
  1. Remove the stone from the **top** and put it at the **bottom**.
  2. Remove the next stone (now at the top) and **throw** it away.

- **Akshat’s Turn:**
  1. Remove the stone from the **top** and put it at the **bottom**.
  2. Do the same again (i.e. remove the new top stone and put it at the **bottom**).
  3. Remove the stone now at the **top** and **throw** it away.

The game terminates when only one stone remains. Besides determining the number written on the last stone, we must also decide which player makes the last move. We represent Aman by `1` and Akshat by `0`.

We now discuss two key approaches to solve the problem.

---

## Approach 1: Simulation Using a Deque

### Idea

Since the operations are similar to a queue (removing from the front and appending at the back), a **deque** (double-ended queue) is the ideal data structure for an exact simulation. We simply process the moves until one stone remains:
- On Aman’s turn, we:
  1. Rotate the top stone to the bottom.
  2. Check if only one stone remains (and break if so).
  3. Discard the new top stone.
- On Akshat’s turn, we:
  1. Rotate once.
  2. Check the number of stones.
  3. Rotate a second time.
  4. Check again.
  5. Discard the top stone.

Since every turn discards exactly one stone, the total number of removal moves equals $N-1$. By alternately simulating Aman’s and Akshat’s moves, we not only determine the last remaining stone but also record which player performed the final discard. Notably, if we number the moves beginning with Aman, the final move is performed by:
- **Aman** when $(N-1)$ is odd.
- **Akshat** when $(N-1)$ is even.

### Complexity

Each move (rotation or removal) takes $O(1)$ time. Since there are $N-1$ removals, the overall time complexity per test case is $O(N)$, which is efficient given the problem constraints.

### Code Implementation

Below are the code implementations in both C++ and Python for the simulation approach.

#### C++ Code (Approach 1)
```cpp
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
        deque dq;
        for(int i = 0; i < N; i++){
            long long num;
            cin >> num;
            dq.push_back(num);
        }

        // Aman is represented by 1, Akshat by 0.
        int turn = 1;
        int lastPlayer = -1;
        while(dq.size() > 1){
            if(turn == 1){
                // Aman: rotate once then discard.
                long long top = dq.front();
                dq.pop_front();
                dq.push_back(top);

                if(dq.size() == 1){
                    lastPlayer = 1;
                    break;
                }
                dq.pop_front(); // Discard.
                lastPlayer = 1;
            } else {
                // Akshat: rotate twice then discard.
                long long top = dq.front();
                dq.pop_front();
                dq.push_back(top);

                if(dq.size() == 1){
                    lastPlayer = 0;
                    break;
                }
                top = dq.front();
                dq.pop_front();
                dq.push_back(top);

                if(dq.size() == 1){
                    lastPlayer = 0;
                    break;
                }
                dq.pop_front(); // Discard.
                lastPlayer = 0;
            }
            turn = 1 - turn; // Alternate turns.
        }

        cout << lastPlayer << " " << dq.front() << "\n";
    }
    return 0;
}
```

#### Python Code (Approach 1)
```python
from collections import deque

T = int(input())
for _ in range(T):
    N = int(input())
    dq = deque(map(int, input().split()))
    turn = 1  # Aman: 1, Akshat: 0.
    lastPlayer = -1
    while len(dq) > 1:
        if turn == 1:
            # Aman’s turn: rotate then discard.
            top = dq.popleft()
            dq.append(top)
            if len(dq) == 1:
                lastPlayer = 1
                break
            dq.popleft()  # Discard.
            lastPlayer = 1
        else:
            # Akshat’s turn: rotate twice then discard.
            top = dq.popleft()
            dq.append(top)
            if len(dq) == 1:
                lastPlayer = 0
                break
            top = dq.popleft()
            dq.append(top)
            if len(dq) == 1:
                lastPlayer = 0
                break
            dq.popleft()  # Discard.
            lastPlayer = 0
        turn = 1 - turn  # Alternate turns.

    print(lastPlayer, dq[0])
```

---

## Approach 2: Mathematical Recurrence (Josephus-style Analysis)

### Idea

An important observation is that **each complete turn discards one stone**, so there are exactly $N-1$ removal operations. Instead of simulating every rotation, we can derive a recurrence relation to determine which stone (by its index) survives.

Notice that:
- On **Aman’s turn** (player `1`), the process is:
  - Rotate one stone (shift the start pointer by $1$),
  - Then discard the stone now at the top.

  Thus, if the starting pointer is at index $s$, the discarded stone is at $(s+1) \mod n$, and after removal, the pointer shifts to $(s+2) \mod n$. The recurrence for Aman becomes:
  $$ f(n, 1) = (f(n-1, 0) + 2) \mod n $$

- On **Akshat’s turn** (player `0`), the process involves:
  - Two rotations (shifting the pointer by $2$),
  - Then discarding the stone at the top.

  Hence, the recurrence for Akshat is:
  $$ f(n, 0) = (f(n-1, 1) + 3) \mod n $$

Here, $f(n, p)$ represents the safe (remaining) stone’s index when there are $n$ stones, and the current turn is assigned to player $p$ (with Aman as $1$ and Akshat as $0$). The base case is:
$$ f(1, p) = 0 $$
for any player $p$, because with one stone the index is $0$.

Since the game always begins with Aman’s turn, the safe index is $f(N, 1)$, and the corresponding stone number is the element at that index in the original array.

### Last Player Determination

Because one stone is removed per turn:
- If $(N-1)$ is **odd**, then Aman (player `1`) makes the final move.
- If $(N-1)$ is **even**, then Akshat (player `0`) makes the final move.

### Complexity

This approach computes the safe position using an iterative recurrence in $O(N)$ time and requires only constant extra space. Although it may seem more complex than the simulation, it provides an elegant mathematical interpretation.

### Code Implementation

Below are the implementations for the recurrence approach in both C++ and Python.

#### C++ Code (Approach 2)
```cpp
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
        vector A(N);
        for (int i = 0; i < N; i++){
            cin >> A[i];
        }

        // f(n, 1) represents Aman’s turn and f(n, 0) represents Akshat’s turn.
        // Base case: for n = 1, both f(1, 1) and f(1, 0) equal 0.
        int aman = 0;   // f(n, 1)
        int akshat = 0; // f(n, 0)

        for (int n = 2; n <= N; n++){
            int new_aman = (akshat + 2) % n;    // Aman’s recurrence.
            int new_akshat = (aman + 3) % n;      // Akshat’s recurrence.
            aman = new_aman;
            akshat = new_akshat;
        }

        // The safe position when starting with Aman’s turn:
        int safePos = aman;
        long long lastStone = A[safePos];

        // Determine the last player: starting with Aman, the moves alternate.
        int lastPlayer = ((N - 1) % 2 == 1) ? 1 : 0;

        cout << lastPlayer << " " << lastStone << "\n";
    }
    return 0;
}
```

#### Python Code (Approach 2)
```python
T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))

    # Initialize recurrence values for Aman (1) and Akshat (0).
    aman = 0     # f(n, 1)
    akshat = 0   # f(n, 0)

    for n in range(2, N + 1):
        new_aman = (akshat + 2) % n   # Aman’s recurrence.
        new_akshat = (aman + 3) % n   # Akshat’s recurrence.
        aman, akshat = new_aman, new_akshat

    safePos = aman   # Safe index for initial Aman’s turn.
    lastStone = A[safePos]

    # Determine last player based on the parity of (N-1).
    lastPlayer = 1 if ((N - 1) % 2 == 1) else 0
    print(lastPlayer, lastStone)
```

---

## Summary

Both approaches yield an $O(N)$ solution:

- **Approach 1 (Simulation):** Directly simulates the game using a deque. It is easy to implement and understand.
- **Approach 2 (Mathematical Recurrence):** Uses a recurrence relation inspired by the Josephus problem to determine the safe index without simulating each rotation explicitly.

Select the approach that best suits your comfort level. The simulation method is more intuitive, while the recurrence method offers mathematical insights into the underlying process.

Happy Coding!

</details>
