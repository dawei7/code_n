# N Buttons 1 Bulb

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | ON_OFF |
| Difficulty Rating | 977 |
| Difficulty Band | Practice Strings |
| Path | Data Structures and Algorithms |
| Lesson | Strings |
| Official Link | [ON_OFF](https://www.codechef.com/practice/course/strings/STRINGSPRO/problems/ON_OFF) |

---

## Problem Statement

Kulyash stays in room that has a single bulb and $N$ buttons. The bulb is initially **on**.

The initial states of the buttons are stored in a binary string $S$ of length $N$ — if $S_i$ is $0$, the $i$-th button is off, and if $S_i$ is $1$, the $i$-th button is on. If Kulyash toggles any single button then the state of the bulb reverses i.e. the bulb lights up if it was off and vice versa.

Kulyash has toggled some buttons and the final states of the buttons are stored in another binary string $R$ of length $N$. He asks you to determine the final state of the bulb.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of three lines of input.
    - The first line of each test case contains an integer $N$ — the number of buttons.
    - The second line of each test case contains a binary string $S$ — the initial states of the buttons.
    - The third line of each test case contains a binary string $R$ — the final states of the buttons.

---

## Output Format

For each test case, output on a new line the final state of the bulb ($0$ for off and $1$ for on).

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N \leq 100$
- $S$ and $R$ are binary strings, i.e, contain only the characters $0$ and $1$.

---

## Examples

**Example 1**

**Input**

```text
2
3
000
001
2
00
11
```

**Output**

```text
0
1
```

**Explanation**

**Test case $1$:** All the buttons are initially off and finally the state of only one button has changed so the state of the bulb reverses once i.e. it turns off.

**Test case $2$:** All the buttons are initially off and finally the states of two buttons have changed so the state of the bulb reverses twice i.e. it remains on.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3
000
001
```

**Output for this case**

```text
0
```



#### Test case 2

**Input for this case**

```text
2
00
11
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

[Contest](https://www.codechef.com/START49/)

[Practice](https://www.codechef.com/problems/ON_OFF)

**Setter:** [kulyash](https://www.codechef.com/users/kulyash)

**Testers:** [iceknight1093 ](https://www.codechef.com/users/iceknight1093), [jeevanjyot](https://www.codechef.com/users/jeevanjyot)

**Editorialist:** [kiran8268](https://www.codechef.com/users/kiran8268)

#
[](#difficulty-2)DIFFICULTY:

977

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Kulyash stays in room that has a **single bulb** and  N buttons. The bulb is initially **on**. The initial states of the buttons are stored in a binary string S of length N, where S_i is the i the button. If Kulyash toggles any single button then the state of the bulb reverses i.e. the bulb lights up if it was off and vice versa. Kulyash has toggled some buttons and the final states of the buttons are stored in another binary string R of length N . We need to find the final stage of the bulb.

#
[](#explanation-5)EXPLANATION:

The important things note before we beigin are:

- The initial state of the bulb is On.

- Even If a button is toggled the state of bulb reverses. Also, the state of bulb reverses for every single toggle.

- Initial state of buttons are defined in string S.

- Final state  of buttons are defined in string R.

-If a single button is toggled the final state of the bulb will be 0, as the initial state is 1.

-If  two buttons are toggled then the state of bulb reverses twice and stays as 1.

-Thus we can conclude that if number of buttons toggled is an even number then the state of bulb stays as 1 else if its an odd number, its state stays as 0.

#
[](#time-complexity-6)TIME COMPLEXITY:

Time complexity is O(n).

#
[](#solution-7)SOLUTION:

Editorialist's Solution
``int t;
	cin>>t;
	while(t--)
	{
	    int n,c=0;
	    string s,r;
	    cin>>n;
	    cin>>s>>r;

	    for(int j=0;j<n;j++)
	    {
	        if(s[j]!=r[j])
	        c++;
	    }

	   if(c%2==0)
	    cout<<"1"<<"\n";
	    else
	    cout<<"0"<<"\n";

``

</details>
