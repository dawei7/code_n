# Gasoline Introduction

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | BEGGASOL |
| Difficulty Rating | 1263 |
| Difficulty Band | Level up from 1* to 2* |
| Path | Become 5 star |
| Lesson | Arrays |
| Official Link | [BEGGASOL](https://www.codechef.com/practice/course/1to2stars/LP1TO202/problems/BEGGASOL) |

---

## Problem Statement

There are $N$ cars (numbered $1$ through $N$) on a circular track with length $N$. For each $i$ ($2 \le i \le N$), the $i$-th of them is at a distance $i-1$ clockwise from car $1$, i.e. car $1$ needs to travel a distance $i-1$ clockwise to reach car $i$. Also, for each valid $i$, the $i$-th car has $f_i$ litres of gasoline in it initially.

You are driving car $1$ in the clockwise direction. To move one unit of distance in this direction, you need to spend $1$ litre of gasoline. When you pass another car (even if you'd run out of gasoline exactly at that point), you steal all its gasoline. Once you do not have any gasoline left, you stop.

What is the total clockwise distance travelled by your car?

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains a single integer $N$.
- The second line contains $N$ space-separated integers $f_1, f_2, \ldots, f_N$.

### Output
For each test case, print a single line containing one integer ― the total clockwise distance travelled.

### Constraints
- $1 \le T \le 100$
- $1 \le N \le 100$
- $0 \le f_i \le 100$ for each valid $i$

### Subtasks
**Subtask #1 (100 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
3
5
3 0 0 0 0
5
1 1 1 1 1
5
5 4 3 2 1
```

**Output**

```text
3
5
15
```

**Explanation**

**Test case $1$:** The car starts with $3$ liters of gasoline. Using this, the car can travel $3$ units. On its journey, there is no other car having gasoline. Thus, the car stops after $3$ units.

**Test case $2$:** The car starts with $1$ liter of gasoline.
- After traveling $1$ unit, it passes another car with $1$ liter gasoline. Thus, the amount of gasoline left after traveling $1$ unit is $1$ liter.
- After traveling $2$ units, it passes another car with $1$ liter gasoline. Thus, the amount of gasoline left after traveling $2$ units is $1$ liter.
- After traveling $3$ units, it passes another car with $1$ liter gasoline. Thus, the amount of gasoline left after traveling $3$ units is $1$ liter.
- After traveling $4$ units, it passes another car with $1$ liter gasoline. Thus, the amount of gasoline left after traveling $4$ units is $1$ liter.
- After traveling $5$ units, there is no car with gasoline. Thus, the car stops after $5$ units.

**Test case $3$:** The car starts with $5$ liters of gasoline.
- After traveling $1$ unit, it passes another car with $4$ liters gasoline. Thus, the amount of gasoline left after traveling $1$ unit is $5-1+4 = 8$ liters.
- After traveling $2$ units, it passes another car with $3$ liters gasoline. Thus, the amount of gasoline left after traveling $2$ units is $8-1+3 = 10$ liters.
- After traveling $3$ units, it passes another car with $2$ liters gasoline. Thus, the amount of gasoline left after traveling $3$ units is $10-1+2 = 11$ liters.
- After traveling $4$ units, it passes another car with $1$ liter gasoline. Thus, the amount of gasoline left after traveling $4$ units is $11-1+1 = 11$ liters.
- After traveling $5$ units, there is no car with gasoline. Thus, after $5$ units, $10$ liters of gasoline is left.

The car can move $10$ more units using the leftover gasoline. The total distance travelled is $15$ units.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5
3 0 0 0 0
```

**Output for this case**

```text
3
```



#### Test case 2

**Input for this case**

```text
5
1 1 1 1 1
```

**Output for this case**

```text
5
```



#### Test case 3

**Input for this case**

```text
5
5 4 3 2 1
```

**Output for this case**

```text
15
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Practice](https://www.codechef.com/problems/PROBLEMCODE)

[Div-2 Contest](https://www.codechef.com/LTM90B/problems/PROBLEMCODE)

[Div-1 Contest](https://www.codechef.com/LTM90A/problems/PROBLEMCODE)

*Author:* [Ildar Gainullin](https://www.codechef.com/users/gainullinildar)

*Tester:* [Nikolay Budin](https://www.codechef.com/users/budalnik)

*Editorialist:* [Alei Reyes](https://www.codechef.com/users/alei)

# DIFFICULTY:

CAKEWALK

# PREREQUISITES:

None

# PROBLEM:

There are N cars in a circle, the i-th car has f_i units of gasoline. The distance between each pair of adjacent cars is one unit.

You are in the first car and keep driving clockwise, it takes you one unit of gasoline to move one unit of distance. Whenever you reach a new car, you steal all of its gasoline.

Find the maximum distance you can travel until your car gets out of gasoline.

# QUICK EXPLANATION:

Simulate the process.

# EXPLANATION:

Let G be the current amount of gasoline in our car, D the total distance we have traveled, and i the index of our current position in the circle.

Initially G=0, D=0 and i=1. The process goes as follows:

- Steal the gasoline from the i-th car, i.e G increases by f_i.

- If we are left whithout gasoline, the process finishes.

- Otherwise, move to the next car clockwise: i increases by one, G decreases by one (we have to consume gasoline) and D increases by one (we travel an additional unit of distance).

We have to repeat the previous process at most N times (one full circle), after that each car will be visited at most once and no more gasoline can be stealed. To keep moving we have to consume all the remaining G units of gasoline and travel an additional G units of distance.

# SOLUTIONS:

Setter's Solution
``int main() {
  int t;
  cin >> t;
  while (t--) {
    int n;
    cin >> n;
    vector <int> f(n);
    for (int i = 0; i < n; i++) {
      cin >> f[i];
    }
    int cur = 0;
    int ans = 0;
    int i = 0;
    while (true) {
      cur += f[i];
      f[i] = 0;
      if (cur >= 1) {
        ans++;
        cur--;
        i++;
        if (i >= n) i -= n;
      } else {
        break;
      }
    }
    cout << ans << '\n';
  }
}
``

Tester's Solution
``void solve() {
  int n;
  cin >> n;
  vector<int> arr;
  for (int i = 0; i < n; ++i) {
    int num;
    cin >> num;
    arr.push_back(num);
  }

  int ans = 0;
  int left = 0;
  for (int i = 0; i < n; ++i) {
    left += arr[i];
    if (left == 0) {
      cout << ans << "\n";
      return;
    }
    left--;
    ans++;
  }
  ans += left;
  cout << ans << "\n";
}

int main() {
  int test_count = 1;
  cin >> test_count;
  for (int test = 1; test <= test_count; ++test) {
    solve();
  }
}
``

# VIDEO EDITORIAL (Hindi):

# VIDEO EDITORIAL (English):

</details>
