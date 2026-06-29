# Deputy Chef

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | DEPCHEF |
| Difficulty Rating | 1397 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1200 to 1400 difficulty problems |
| Official Link | [DEPCHEF](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1400/problems/DEPCHEF) |

---

## Problem Statement

A battle is going to begin in the kingdom of Airland. There are $N$ soldiers in the kingdom, numbered $1$ through $N$ and standing in a circle in such a way that for each valid $i$, the soldier directly to the right of the $i$-th soldier is soldier $i+1$, and the soldier directly to the right of the $N$-th soldier is soldier $1$.

Each soldier holds a sword and a shield. The sword is used to attack other soldiers and the shield is used to defend from attacks. Let's denote the *attack value* of the $i$-th soldier's sword by $a_i$ and the *defense value* of the $i$-th soldier's shield by $d_i$.

In the battle, each soldier picks one of the soldiers standing to his left and right, and attacks that soldier. The choices of the soldiers are completely independent, so each soldier can be attacked by the soldier to his left, by the soldier to his right (the power of such an attack is the attack value of the attacking soldier's sword), by both of them (then, the power of the resulting attack is the sum of the attack values of these soldiers' swords) or by nobody. A soldier remains alive if the defense value of his shield is strictly greater than the power with which he is attacked. Everyone attacks simultaneously and there is only one round of attacks. Each soldier that remains alive at the end is awarded a laurel.

The king of Airland likes these fights, so the host of the battle promised the king that he can pick one soldier and if the soldier he picks survives the battle, the king receives the shield of that soldier.

Chef is the deputy of the king and you want to help him pick a soldier for the king in such a way that the king receives the best shield (with the greatest defense value). However, if Chef picks a soldier and that soldier does not survive, Chef will be thrown in a snake pit. Therefore, it should be guaranteed that the chosen soldier will survive regardless of the decisions of the other soldiers.

Can you help Chef make the best choice and tell him the defense value of the shield which the king gets, or decide that he can be thrown in the snake pit no matter which soldier he picks?

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains a single integer $N$.
- The second line contains $N$ space-separated integers $a_1, a_2, \ldots, a_N$.
- The third line contains $N$ space-separated integers $d_1, d_2, \ldots, d_N$.

### Output
For each test case, print a single line containing one integer ― the best defense value of the shield the king gets, or $-1$ if Chef can be thrown in the snake pit.

### Constraints
- $1 \le T \le 100$
- $3 \le N \le 100$
- $1 \le a_i, d_i \le 10^4$ for each valid $i$

### Subtasks
**Subtask #1 (100 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
2
4
1 1 4 1
3 4 2 1
7
5 4 5 4 5 4 5
3 2 4 7 2 5 9
```

**Output**

```text
3
-1
```

**Explanation**

**Example case 1:** Soldier $1$ can be attacked by soldier $2$ and/or soldier $4$. If only soldier $2$ attacks him, the power of the attack is $1$. If only soldier $4$ attacks him, the power of the attack is $1$ again. If they attack together, the power of the attack is $2$. In each of these cases, soldier $1$ will live.

Soldier $2$ can be attacked by soldier $3$, with attack power $4$. His shield has defense value $4$, which is not enough, so in this case, soldier $2$ would die. The best safe choice is soldier $1$, with defense value $3$.

**Example case 2:** No soldier is guaranteed to survive the battle, so the answer is $-1$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4
1 1 4 1
3 4 2 1
```

**Output for this case**

```text
3
```



#### Test case 2

**Input for this case**

```text
7
5 4 5 4 5 4 5
3 2 4 7 2 5 9
```

**Output for this case**

```text
-1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](https://www.codechef.com/problems/ARTBALAN)

[Contest: Division 1](https://www.codechef.com/FEB19A/problems/ARTBALAN)

[Contest: Division 2](https://www.codechef.com/FEB19B/problems/ARTBALAN)

**Setter:** [Stylianos Kasouridis](https://www.codechef.com/users/stelkasouridis)

**Tester:** [Alexey Zayakin](https://www.codechef.com/users/alex_2oo8) and [Yash Chandnani](https://www.codechef.com/users/yash_chandnani)

**Editorialist:** [Taranpreet Singh](https://www.codechef.com/users/taran_1407)

### DIFFICULTY:

Simple

### PREREQUISITES:

Arrays would do.

### PROBLEM:

Given Attacking power and shield power of N soldiers standing in a circle in order, labeled from 1 to N such that soldier N is to the left to soldier 1. When the king commands, each soldier may attack one of the soldiers standing adjacent to it at once. King asks to find out the most powerful shield of the soldier which is guaranteed to survive irrespective of the soldiers being attacked. A soldier survives if its defense shield power is strictly greater than the attack applied on him. Print -1, if no soldier is guaranteed to survive.

### QUICK EXPLANATION

- In the worst case for each soldier, both of the adjacent soldiers might choose to attack him, in which case, the attack applied on him is the sum of attacking power of both soldiers attacking the current soldier.

- So, a soldier survives in the worst case only if the power of his defence shield is greater than the sum of attacking power of two adjacent soldiers. Out of all surviving soldiers, the power of most powerful shield is the required shield power here.

### EXPLANATION

First of all, understand the worst case for any soldier. If considering soldier x, both soldiers labeled x-1 and x+1 may choose to attack him. In this case, Attack applied on him shall be sum of attacking powers of soldiers x-1 and x+1.

Now, Since we need to guarantee that the soldier survives, we shall only choose the shield of a soldier whose defense shield is powerful than the sum of attacking power of adjacent soldiers. Since we want to find the most powerful shield, we may offer to the king, the shield with maximum power out of all these shields.

For implementation, we can just make two arrays A and D and check D[i] > A[i-1]+A[i+1] and take maximum value of D[i] here. Don’t forget to consider that solder N and soldier 1 are adjacent too.

**Extended problem**

In this problem, there are N soldiers and given M pairs of soldiers which may attack each other, find out the best shield to be offered to king. The condition is same. If the chosen soldier doesn’t survive, you, the deputy of Chef die a painful death.

### Time Complexity

Time complexity is O(N) per test case.

### AUTHOR’S AND TESTER’S SOLUTIONS:

[Setter’s solution](https://www.codechef.com/download/Solutions/FEB19/setter/ARTBALAN.cpp)

[Tester’s solution](https://www.codechef.com/download/Solutions/FEB19/tester/ARTBALAN.cpp)

[Editorialist’s solution](https://www.codechef.com/download/Solutions/FEB19/editorialist/ARTBALAN.java)

Feel free to Share your approach, If it differs. Suggestions are always welcomed.

</details>
