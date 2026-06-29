# ATM Machine

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | ATM2 |
| Difficulty Rating | 1001 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1000 to 1200 difficulty problems |
| Official Link | [ATM2](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1200/problems/ATM2) |

---

## Problem Statement

There is an ATM machine. Initially, it contains a total of $K$ units of money. $N$ people (numbered $1$ through $N$) want to withdraw money; for each valid $i$, the $i$-th person wants to withdraw $A_i$ units of money.

The people come in and try to withdraw money one by one, in the increasing order of their indices. Whenever someone tries to withdraw money, if the machine has at least the required amount of money, it will give out the required amount. Otherwise, it will throw an error and not give out anything; in that case, this person will return home directly without trying to do anything else.

For each person, determine whether they will get the required amount of money or not.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains two space-separated integers $N$ and $K$.
- The second line contains $N$ space-separated integers $A_1, A_2, \dots, A_N$.

### Output
For each test case, print a single line containing a string with length $N$. For each valid $i$, the $i$-th character of this string should be '1' if the $i$-th person will successfully withdraw their money or '0' otherwise.

### Constraints
- $1 \le T \le 100$
- $1 \le N \le 100$
- $1 \le A_i \le 1,000,000$ for each valid $i$
- $1 \le K \le 1,000,000$

---

## Examples

**Example 1**

**Input**

```text
2
5 10
3 5 3 2 1
4 6
10 8 6 4
```

**Output**

```text
11010
0010
```

**Explanation**

**Example case 1:** The ATM machine initially contains $10$ units of money. The first person comes and withdraws $3$ units, so the amount remaining in the machine is $7$. Then the second person withdraws $5$ units and the remaining amount is $2$. The third person wants to withdraw $3$ units, but since there are only $2$ units of money in the machine, it throws an error and the third person must leave without getting anything. Then the fourth person withdraws $2$ units, which leaves nothing in the machine, so the last person does not get anything.

**Example case 2:** The ATM machine initially contains $6$ units of money, so it cannot give anything to the first and second person. When the third person comes, it gives them all the money it has, so the last person does not get anything either.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5 10
3 5 3 2 1
```

**Output for this case**

```text
11010
```



#### Test case 2

**Input for this case**

```text
4 6
10 8 6 4
```

**Output for this case**

```text
0010
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](http://www.codechef.com/problems/ATM2/)

[Contest: Division 1](https://www.codechef.com/COOK98A/problems/ATM2)

[Contest: Division 2](https://www.codechef.com/COOK98B/problems/ATM2)

**Setter:** [Jafar Badour](https://www.codechef.com/users/jafarbadour)

**Tester:** [Hussain](https://www.codechef.com/users/deadwing97)

**Editorialist:** [Taranpreet Singh](http://www.codechef.com/users/taran_1407)

### DIFFICULTY:

Cakewalk

### PREREQUISITES:

None at all (what did you expect?? :D)

### PROBLEM:

A bank have a total of K cash. N customers visit bank one day, and request to withdraw A[i] money. We have to tell which customers get money, and which ones doesn’t.

### SUPER QUICK EXPLANATION

-
``  Check customers from front to end, if bank can give cash to customer, Bank gives and reduces its cash balance. That's all.
``

### EXPLANATION

The only thing we need to do is to simulate the customers from front to end, and see if we can satisfy their cash requirement.

Formally, If K \geq A[i] for ith customer, we set K = K-a[i] and append 1 to answer string. Otherwise we append 0 to answer string and move to next customer.

What we are doing here is, that if we can lend cash to ith customer (this occurs when K \geq A[i]), we lend it and reduce bank’s cash balance by A[i], Otherwise we refuse that customer and bank’s cash balance remains unaffected.

This is it. You may feel free to refer Solutions if you wish to.

### Time Complexity

Since we iterate over all customers only once, Time complexity is O(N).

### AUTHOR’S AND TESTER’S SOLUTIONS:

[Setter’s solution](http://www.codechef.com/download/Solutions/COOK98/setter/ATM2.cpp)

[Tester’s solution](http://www.codechef.com/download/Solutions/COOK98/tester/ATM2.cpp)

[Editorialist’s solution](http://www.codechef.com/download/Solutions/COOK98/editorialist/ATM2.java)

Feel free to Share your approach, If it differs. Suggestions are always welcomed.

</details>
