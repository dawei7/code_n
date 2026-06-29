# Asteroid Hit

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | ASTHIT |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Basic programming - 1 |
| Official Link | [ASTHIT](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_01/problems/ASTHIT) |

---

## Problem Statement

Dr. Strange asks for your help and we don't have time for a background chit-chat!

$N$ asteroids of different sizes are moving on a line, with the $i$-th asteroid being in the $i$-th coordinate. For each asteroid you know its direction (left or right), and its size. In this universe, all asteroids are moving with the same speed.

When two asteroids hit, there are two possible scenarios:

1. If they are the same size - they are both destroyed.
2. Otherwise, the smaller one is destroyed and the bigger one gains bonus size. The size of the bigger asteroid increases by the size of the smaller asteroid.

Help Dr. Strange determine which of the asteroids will survive (or if all of them will be destroyed).

---

## Input Format

- First line will contain $T$, the number of test cases. Then the test cases follow - each test case has $N+1$ lines.
- The first line of input of each test case contains a single integer $N$.
- Next $N$ lines contain two space-separated integers: $dir_i$ and $a_i$ - representing the direction ($0$ if left, $1$ if right) and the size of the asteroid.

---

## Output Format

For each test case, first output in a single line the number of survived asteroids - $x$.
In the next line, output $x$ integers representing the indices of the survived asteroids $\textbf{sorted by increasing order}$.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N \leq 10^5$
- Sum of $N$ over all test cases does not exceed $2\cdot 10^5$
- $dir_i \in \{0, 1\}$
- $1 \leq a_i \leq 10^9$

---

## Examples

**Example 1**

**Input**

```text
2
4
1 1
0 1
1 4
0 4
4
1 5
1 1
0 2
1 1
```

**Output**

```text
0
2
1 4
```

**Explanation**

In the first test case, the first two asteroids destroy each other, as they are the same size. Same thing happens to third and fourth asteroids - so all of them are destroyed and we are left with $0$ asteroids.

In the second test case, the second and third asteroid collide and the bigger is third, so it now becomes larger and its size is $1+2=3$. Next, the first asteroid collides with the asteroid of size $3$ and wins. We are left with the first asteroid, whose size is $5+3=8$ now, and the fourth asteroid with size $1$.

**Example 2**

**Input**

```text
1
4
1 9
1 2
1 3
0 5
```

**Output**

```text
1
4
```

**Explanation**

The third asteroid hits the fourth and loses, so the fourth now has the size $5+3=8$. Then, it hits the second asteroid and wins. So its size now is $8+2 = 10$. Finally, the first asteroid is being destroyed by the fourth (whose size now is $10+9 = 19$) and the fourth asteroid remains the only one.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

## Asteroid Collision Problem Editorial

In this lesson, we analyze a problem where $N$ asteroids move along a line (each placed at coordinates $1$ through $N$). Each asteroid has a direction ($0$ for left, $1$ for right) and a size. When two asteroids collide, they interact as follows:
- If they are of equal size, both are destroyed.
- If they are of different sizes, the smaller one gets destroyed and the larger one “gains” the smaller asteroid’s size.

The goal is to identify the surviving asteroids and output their indices in increasing order.

Below, we discuss two effective approaches to solve this problem.

---

### Approach 1: Stack Simulation

#### Concept

In this approach, we simulate the collisions by processing asteroids one by one while maintaining a **stack** (or list) for potential survivors. The main idea is:

- **Right-moving asteroids**: Since they can later collide with left-moving asteroids, we push them onto our stack.
- **Left-moving asteroids**: They are potential candidates for collision with the right-moving asteroids present in our stack. For each left-moving asteroid, we simulate collisions with the top of the stack until either:
  - The left-moving asteroid is destroyed.
  - It survives after destroying one or more right-moving asteroids (gaining bonus size as required).
  - No more right-moving asteroids are available in the stack.

The collision rules are carefully applied:
- If the top right-moving asteroid has the same size as the left-moving asteroid, both are destroyed (pop from the stack and do not push the current asteroid).
- If the right-moving asteroid is smaller, the left-moving asteroid absorbs its size and continues colliding with the next candidate in the stack.
- If the right-moving asteroid is larger, it absorbs the left-moving asteroid’s size, and the left-moving asteroid is destroyed.

After processing all asteroids, the remaining ones in our stack are the survivors. We then extract their original indices, sort them in increasing order, and output the result.

#### Code Implementation

Below are the implementations for this approach in both C++ and Python.

**C++ Code:**
```cpp
#include
#include
#include
using namespace std;

struct Asteroid {
    int dir;
    long long size;
    int idx;
};

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    while(T--){
        int N;
        cin >> N;
        vector asteroids(N);
        for(int i = 0; i < N; i++){
            cin >> asteroids[i].dir >> asteroids[i].size;
            asteroids[i].idx = i + 1;
        }

        vector stack;
        for(int i = 0; i < N; i++){
            Asteroid curr = asteroids[i];
            if(curr.dir == 1){
                stack.push_back(curr);
            } else {
                bool destroyed = false;
                while(!stack.empty() && stack.back().dir == 1){
                    if(stack.back().size == curr.size){
                        stack.pop_back();
                        destroyed = true;
                        break;
                    } else if(stack.back().size < curr.size){
                        curr.size += stack.back().size;
                        stack.pop_back();
                    } else{
                        stack.back().size += curr.size;
                        destroyed = true;
                        break;
                    }
                }
                if(!destroyed){
                    stack.push_back(curr);
                }
            }
        }

        vector survivors;
        for(const auto &ast : stack){
            survivors.push_back(ast.idx);
        }
        sort(survivors.begin(), survivors.end());

        cout << survivors.size() << "\n";
        for(int i = 0; i < survivors.size(); i++){
            cout << survivors[i] << (i == survivors.size()-1 ? "\n" : " ");
        }
    }
    return 0;
}
```

**Python Code:**
```python
def process_test_case():
    import sys
    input_data = sys.stdin.read().strip().split()
    it = iter(input_data)
    t = int(next(it))
    results = []

    for _ in range(t):
        n = int(next(it))
        asteroids = []
        for i in range(n):
            d = int(next(it))
            size = int(next(it))
            asteroids.append((d, size, i + 1))

        stack = []
        for d, size, idx in asteroids:
            if d == 1:
                stack.append([d, size, idx])
            else:
                destroyed = False
                while stack and stack[-1][0] == 1:
                    if stack[-1][1] == size:
                        stack.pop()
                        destroyed = True
                        break
                    elif stack[-1][1] < size:
                        size += stack[-1][1]
                        stack.pop()
                    else:
                        stack[-1][1] += size
                        destroyed = True
                        break
                if not destroyed:
                    stack.append([d, size, idx])

        survivors = sorted(ast[2] for ast in stack)
        results.append(str(len(survivors)))
        if survivors:
            results.append(" ".join(map(str, survivors)))

    sys.stdout.write("\n".join(results))

if __name__ == "__main__":
    process_test_case()
```

---

### Approach 2: In-Place Result Simulation

#### Concept

This approach uses the same fundamental collision logic as the stack simulation. However, instead of naming our container a "stack", we refer to it as an in-place **result list**. The steps are nearly identical:

1. **Right-moving asteroids:** Directly add them to the result list.
2. **Left-moving asteroids:** Check the last asteroid in the result list (if it is moving right) and simulate the collision:
   - When sizes are equal, remove the right-moving asteroid and mark the current one as destroyed.
   - If the right-moving asteroid is smaller, remove it and increase the size of the left-moving asteroid before continuing.
   - If the right-moving asteroid is larger, update its size and mark the left-moving asteroid as destroyed.
3. If the left-moving asteroid survives (i.e. it collides with no right-moving asteroid or wins all collisions), append it to the result list.

The survivors are obtained from the result list, and their indices are sorted in increasing order before output.

#### Code Implementation

Below are the implementations in both C++ and Python for Approach 2.

**C++ Code:**
```cpp
#include
#include
#include
using namespace std;

struct Asteroid {
    int dir;
    long long size;
    int idx;
};

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    while(T--){
        int N;
        cin >> N;
        vector asteroids(N);
        for (int i = 0; i < N; i++){
            cin >> asteroids[i].dir >> asteroids[i].size;
            asteroids[i].idx = i + 1;
        }

        // Use a result list to maintain survivors.
        vector result;
        for (int i = 0; i < N; i++){
            Asteroid curr = asteroids[i];
            if(curr.dir == 1){
                result.push_back(curr);
            } else {
                bool collided = false;
                while(!result.empty() && result.back().dir == 1){
                    if(result.back().size == curr.size){
                        result.pop_back();
                        collided = true;
                        break;
                    } else if(result.back().size < curr.size){
                        curr.size += result.back().size;
                        result.pop_back();
                    } else {
                        result.back().size += curr.size;
                        collided = true;
                        break;
                    }
                }
                if(!collided){
                    result.push_back(curr);
                }
            }
        }

        vector survivors;
        for(auto ast : result){
            survivors.push_back(ast.idx);
        }
        sort(survivors.begin(), survivors.end());

        cout << survivors.size() << "\n";
        for (int i = 0; i < survivors.size(); i++){
            cout << survivors[i] << (i == survivors.size()-1 ? "\n" : " ");
        }
    }
    return 0;
}
```

**Python Code:**
```python
def solve():
    import sys
    data = sys.stdin.read().strip().split()
    it = iter(data)
    t = int(next(it))
    output = []

    for _ in range(t):
        n = int(next(it))
        asteroids = []
        for idx in range(n):
            d = int(next(it))
            size = int(next(it))
            asteroids.append((d, size, idx + 1))

        result = []
        for d, size, idx in asteroids:
            if d == 1:
                result.append([d, size, idx])
            else:
                collided = False
                while result and result[-1][0] == 1:
                    if result[-1][1] == size:
                        result.pop()
                        collided = True
                        break
                    elif result[-1][1] < size:
                        size += result[-1][1]
                        result.pop()
                    else:
                        result[-1][1] += size
                        collided = True
                        break
                if not collided:
                    result.append([d, size, idx])

        survivors = sorted(asteroid[2] for asteroid in result)
        output.append(str(len(survivors)))
        if survivors:
            output.append(" ".join(map(str, survivors)))

    sys.stdout.write("\n".join(output))

if __name__ == "__main__":
    solve()
```

---

### Summary

Both approaches simulate the asteroid collisions in a single pass, achieving an overall time complexity of $O(N)$ per test case. The key insight is to handle the collision rules correctly by maintaining a list (or stack) that represents the currently surviving asteroids. Once processed, sorting the original indices of survivors gives the required answer.

Happy coding and best of luck with your DSA interviews!

</details>
