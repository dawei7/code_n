# Chef and his Apps

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CHEFAPPS |
| Difficulty Rating | 702 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 500 to 800 difficulty rating problems |
| Official Link | [CHEFAPPS](https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/CHEFAPPS) |

---

## Problem Statement

Chef's phone has a total storage of $S$ MB. Also, Chef has $2$ apps already installed on his phone which occupy $X$ MB and $Y$ MB respectively.

He wants to install another app on his phone whose memory requirement is $Z$ MB. For this, he might have to delete the apps already installed on his phone. Determine the minimum number of apps he has to delete from his phone so that he has enough memory to install the third app.

---

## Input Format

- The first line contains a single integer $T$ — the number of test cases. Then the test cases follow.
- The first and only line of each test case contains four integers $S, X, Y$ and $Z$ — the total memory of Chef's phone, the memory occupied by the two already installed apps and the memory required by the third app.

---

## Output Format

For each test case, output the minimum number of apps Chef has to delete from his phone so that he can install the third app.

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq S \leq 500$
- $1 \le X \le Y \le S$
- $X + Y \le S$
- $Z \le S$

---

## Examples

**Example 1**

**Input**

```text
4
10 1 2 3
9 4 5 1
15 5 10 15
100 20 30 75
```

**Output**

```text
0
1
2
1
```

**Explanation**

**Test Case 1:** The unused memory in the phone is $7$ MB. Therefore Chef can install the $3$ MB app without deleting any app.

**Test Case 2:** There is no unused memory in the phone. Chef has to first delete one of the apps from the phone and then only he can install the $1$ MB app.

**Test Case 3:** There is no unused memory in the phone. Chef has to first delete both the apps from the phone and then only he can install the $15$ MB app.

**Test Case 4:** The unused memory in the phone is $50$ MB. Chef has to first delete the $30$ MB app from the phone and then only he can install the $75$ MB app.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
10 1 2 3
```

**Output for this case**

```text
0
```



#### Test case 2

**Input for this case**

```text
9 4 5 1
```

**Output for this case**

```text
1
```



#### Test case 3

**Input for this case**

```text
15 5 10 15
```

**Output for this case**

```text
2
```



#### Test case 4

**Input for this case**

```text
100 20 30 75
```

**Output for this case**

```text
1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/START45A/problems/CHEFAPPS)

[Contest Division 2](https://www.codechef.com/START45B/problems/CHEFAPPS)

[Contest Division 3](https://www.codechef.com/START45C/problems/CHEFAPPS)

[Contest Division 4](https://www.codechef.com/START45D/problems/CHEFAPPS)

**Setter:** [jeevanjyot](https://www.codechef.com/users/jeevanjyot)

**Testers:** [iceknight1093](https://www.codechef.com/users/iceknight1093), [tabr](https://www.codechef.com/users/tabr)

**Editorialist:** [kiran8268](https://www.codechef.com/users/kiran8268)

#
[](#difficulty-2)DIFFICULTY:

702

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Chef’s phone has a total storage of S MB, of which X MB and Y MB of spaces are acquired by 2 apps which are already installed. Chef wants to add a new app with a memory requirement of Z MB. The objective is to find the minimum number apps should be removed so that the new app can be installed

#
[](#explanation-5)EXPLANATION:

-

What is the available free memory when there are 2 apps already installed?

Free memory=S-(X+Y)

-

Lets compare the free memory with the additional required memory Z.

a. Additional memory required, say A = Z- {S-(X+Y)}

-

Solutions

a. If A is less than or equal to Z, output 0

b. If A is less than or equal to max of X and Y, output 1

c. If both a and b are not true then output 2

#
[](#time-complexity-6)TIME COMPLEXITY:

Time complexity is O(1).

#
[](#solution-7)SOLUTION:

Editorialist's Solution
``int t;
cin>>t;
for(int k=0; k<t;k++)
 {
   int s,x,y,z,a;
   cin>>s>>x>>y>>z;
   a=z-(s-(x+y));

   if(a<=0)
   cout<<"0"<<"\n";

   else if(a<=max(x,y))
   cout<<"1"<<"\n";

   else
   cout<<"2"<<"\n";
}

	return 0;
}

``

</details>
