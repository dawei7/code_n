#  Am I Lucky!

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SPCP4 |
| Difficulty Rating | 941 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 800 to 1000 difficulty rating problems |
| Official Link | [SPCP4](https://www.codechef.com/practice/course/logical-problems/DIFF1000/problems/SPCP4) |

---

## Problem Statement

A school has organized a field trip for a class of $N$ students, of which $X$ students are boys, and the remaining students are girls.
Everyone is excited to go trekking, and must form groups of size exactly $K$ to do so. However, boys will only form groups among themselves, and girls will only form groups among themselves.
Both boys and girls will form *as many* groups as possible.

The remaining students can either dance around a bonfire, or just read books.
Dancing around the bonfire requires a pair of one girl and one boy, while reading is done alone.

Reading is much more boring than dancing, so students will try to avoid it.
What's the minimum number of students who will be engaged in reading?

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- The only line of each test case contains three space-separated integers $N$, $X$ and $K$ — the total number of students, the number of boys and the number of students in each trekking group.

---

## Output Format

* For each test case, output on a new line the  the minimum number of students engaged in reading.

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq N, K \leq 10^9$
- $1 \leq X \leq N$

---

## Examples

**Example 1**

**Input**

```text
3
12 4 3
15 10 5
8 8 3
```

**Output**

```text
1
0
2
```

**Explanation**

**Test case $1$:** There are $4$ boys and $8$ girls. The boys will form $1$ group of $3$ members and the girls will form $2$ groups of $3$ members each.
Of the remaining $1$ boy and $2$ girls, one boy and one girl will pair up to dance around the bonfire, while the remaining girl will read books.

**Test case $2$:** There are $10$ boys and $5$ girls. The boys will form $2$ groups of $5$ members each, and the girls will form one group containing $5$ members. So, there is no one left for reading in this case.

**Test case $3$:** There are $8$ boys and $0$ girls. The boys will form $2$ groups of $3$ members each; now, the remaining $2$ boys will have to read books as there is no partner to pair up for dancing.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
12 4 3
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
15 10 5
```

**Output for this case**

```text
0
```



#### Test case 3

**Input for this case**

```text
8 8 3
```

**Output for this case**

```text
2
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# [](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/SPCP4)

[Contest: Division 1](https://www.codechef.com/START110A/problems/SPCP4)

[Contest: Division 2](https://www.codechef.com/START110B/problems/SPCP4)

[Contest: Division 3](https://www.codechef.com/START110C/problems/SPCP4)

[Contest: Division 4](https://www.codechef.com/START110D/problems/SPCP4)

***Author:*** [kg_26](https://www.codechef.com/users/kg_26), [shanmukh29](https://www.codechef.com/users/shanmukh29)

***Tester:*** [raysh07](https://www.codechef.com/users/raysh07)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

# [](#difficulty-2)DIFFICULTY:

TBD

# [](#prerequisites-3)PREREQUISITES:

None

# [](#problem-4)PROBLEM:

N students go on a trip. X of them are boys, and the remaining are girls.

Boys and girls will form groups of K among themselves for trekking.

Among the remaining people, one boy will pair up with one girl for a bonfire dance.

How many people will do neither activity?

# [](#explanation-5)EXPLANATION:

This is a fairly straightforward math task, only requiring you to parse the statement step-by-step.

Let’s go over all the details.

- There are N students, and X of them are boys. This means N-X of them are girls.

Let Y = N-X for convenience.

- The boys will make groups of K till them can’t anymore — which can only happen when there are less than K boys remaining.

So, we need to keep subtracting K from X till we reach something \lt K.

The value we reach is exactly X\ \%\ K, the remainder when X is divided by K.

- Similarly, there will be Y\ \% \ K girls remaining.

- Now, one boy must pair up with one girl.

It’s easy to see that the number of pairs created this way will be exactly \min(X\ \%\ K, Y\ \%\ K).

- The answer is just the number of students remaining - which from above we know is just

(X\ \%\ K) + (Y\ \%\ K) - 2\cdot \min(X\ \%\ K, Y\ \%\ K)

Alternate formulas include |(X\ \%\ K) - (Y\ \%\ K)| and

\max(X\ \%\ K, Y\ \%\ K) - \min(X\ \%\ K, Y\ \%\ K), they all describe the same quantity.

# [](#time-complexity-6)TIME COMPLEXITY:

\mathcal{O}(1) per testcase.

# [](#code-7)CODE:

Author's code (C++)
``#include<iostream>
using namespace std;
int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int n,boys,k;
        cin>>n>>boys>>k;
        int girls=n-boys;
        boys%=k;
        girls%=k;
        cout<<max(boys,girls)-min(boys,girls)<<"\n";
    }
}
``

Editorialist's code (Python)
``for _ in range(int(input())):
    n, x, k = map(int, input().split())
    remb, remg = x%k, (n-x)%k
    dif = abs(remb - remg)
    print(dif)
``

</details>
