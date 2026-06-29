# Ada and Dishes

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | ADADISH |
| Difficulty Rating | 1237 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1200 to 1400 difficulty problems |
| Official Link | [ADADISH](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1400/problems/ADADISH) |

---

## Problem Statement

Chef Ada is preparing $N$ dishes (numbered $1$ through $N$). For each valid $i$, it takes $C_i$ minutes to prepare the $i$-th dish. The dishes can be prepared in any order.

Ada has a kitchen with two identical burners. For each valid $i$, to prepare the $i$-th dish, she puts it on one of the burners and after $C_i$ minutes, removes it from this burner; the dish may not be removed from the burner before those $C_i$ minutes pass, because otherwise it cools down and gets spoiled. Any two dishes may be prepared simultaneously, however, no two dishes may be on the same burner at the same time. Ada may remove a dish from a burner and put another dish on the same burner at the same time.

What is the minimum time needed to prepare all dishes, i.e. reach the state where all dishes are prepared?

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains a single integer $N$.
- The second line contains $N$ space-separated integers $C_1, C_2, \ldots, C_N$.

### Output
For each test case, print a single line containing one integer ― the minimum number of minutes needed to prepare all dishes.

### Constraints
- $1 \le T \le 1,000$
- $1 \le N \le 4$
- $1 \le C_i \le 5$ for each valid $i$

### Subtasks
**Subtask #1 (1 points):** $C_1 = C_2 = \ldots = C_N$

**Subtask #2 (99 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
3
3
2 2 2
3
1 2 3
4
2 3 4 5
```

**Output**

```text
4
3
7
```

**Explanation**

**Example case 1:** Place the first two dishes on the burners, wait for two minutes, remove both dishes and prepare the last one on one burner.

**Example case 2:** Place the first and third dish on the burners. When the first dish is prepared, remove it and put the second dish on the same burner.

**Example case 3:** Place the third and fourth dish on the burners. When the third dish is prepared, remove it and put the second dish on the same burner. Similarly, replace the fourth dish (when it is prepared) by the first dish on the other burner.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3
2 2 2
```

**Output for this case**

```text
4
```



#### Test case 2

**Input for this case**

```text
3
1 2 3
```

**Output for this case**

```text
3
```



#### Test case 3

**Input for this case**

```text
4
2 3 4 5
```

**Output for this case**

```text
7
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Practice](https://www.codechef.com/problems/ADADISH)

[Div-2 Contest](https://www.codechef.com/NOV20B/problems/ADADISH)

[Div-1 Contest](https://www.codechef.com/NOV20A/problems/ADADISH)

Author & Editorialist: [Alei Reyes](https://www.codechef.com/users/alei)

Tester: [Istvan Nagy](https://www.codechef.com/users/istva_adm)

# DIFFICULTY:

CAKEWALK

# PREREQUISITES:

None

# PROBLEM:

Chef Ada is preparing N dishes (numbered 1 through N), the i-the dish requires a cooking time of C_i seconds.

Ada has a kitchen with two identical burners. To cook the i-th dish, she puts it in one of the burners, waits for C_i seconds, and then removes it from the burner. The dishes can be prepared in any order. Two dishes can be cooked simultaneously, however no two dishes can be in the same burner at the same time. When a dish is in a burner, it can’t be removed before it is completely cooked.

What is the minimum time to prepare all dishes?

# QUICK EXPLANATION:

Brute force all possible ways of assigning each dish to a burner.

# EXPLANATION:

The dishes will be splitted between the two burners. Let L be the sum of cooking times of all the dishes cooked in the first burner, similarly let R be the sum of cooking times of the second burner. The total time required to cook all dishes is T=min(L,R). If we denote by S the sum of cooking times of all dishes, then L+R=S and therefore T=min(L,S-L)

There are three possible ways of splitting the dishes, we can try all possibilities:

- all dishes are cooked in only one burner, this optimal when there is only one dish!

- one dish is cooked in the first burner (let’s say dish i), and the rest in the second burner. The cooking time is min(C_i,S-C_i).

- each burner cooks two dishes, let’s say dishes i and j are cooked in the first burner. The cooking time is min(C_i+C_j, S-(C_i+C_j))

# SOLUTIONS:

Setter's Solution, first subtask
``for _ in range(input()):
    n = input()
    c = map(int, raw_input().split())
    s = sum(c)
    print ((n+1)/2)*c[0]
``

Setter's Solution, full score
``for _ in range(input()):
    n = input()
    c = map(int, raw_input().split(" "))
    s = sum(c)
    ans = s
    for x in c:
        ans = min(ans, max(x, s-x))
    for i in range(n):
        for j in range(i+1,n):
            x = c[i] + c[j]
            ans = min(ans, max(x, s-x))
    print ans
``

Tester's Solution (C++)
``int main(int argc, char** argv)
{
  int T;
  cin >> T;
  forn(i, T)
  {
    int N, csum = 0, best = 1000;
    cin >> N;
    vector<int> C(N);
    for (auto& ci : C)
    {
      cin >> ci;
      csum += ci;
    }

    for (int j = 0; j < (1 << N); ++j)
    {
      int su = 0;
      for (int k = 0; k < N; ++k)
      {
        if ((1 << k) & j)
          su += C[k];
      }
      best = min(best, max(su, csum - su));
    }
    cout << best << endl;
  }
  return 0;
}
``

# VIDEO EDITORIAL (Hindi):

# VIDEO EDITORIAL (English):

</details>
