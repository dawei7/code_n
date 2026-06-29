# Bidding

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | AUCTION |
| Difficulty Rating | 330 |
| Difficulty Band | 500 difficulty rating |
| Path | Become 5 star |
| Lesson | Less than 500 difficulty rating |
| Official Link | [AUCTION](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/AUCTION) |

---

## Problem Statement

Alice, Bob and Charlie are bidding for an artifact at an auction.
Alice bids $A$ rupees, Bob bids $B$ rupees, and Charlie bids $C$ rupees (where $A$, $B$, and $C$ are **distinct**).

According to the rules of the auction, the person who bids the **highest** amount will win the auction.
Determine who will win the auction.

---

## Input Format

- The first line contains a single integer $T$ — the number of test cases. Then the test cases follow.
- The first and only line of each test case contains three integers $A$, $B$, and $C$, — the amount bid by Alice, Bob, and Charlie respectively.

---

## Output Format

For each test case, output who (out of `Alice`, `Bob`, and `Charlie`) will win the auction.

You may print each character of `Alice`, `Bob`, and `Charlie` in uppercase or lowercase (for example, `ALICE`, `aliCe`, `aLIcE` will be considered identical).

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq A, B, C \leq 1000$
- $A$, $B$, and $C$ are **distinct**.

---

## Examples

**Example 1**

**Input**

```text
4
200 100 400
155 1000 566
736 234 470
124 67 2
```

**Output**

```text
Charlie
Bob
Alice
Alice
```

**Explanation**

**Test Case $1$:** Charlie wins the auction since he bid the highest amount.

**Test Case $2$:** Bob wins the auction since he bid the highest amount.

**Test Case $3$:** Alice wins the auction since she bid the highest amount.

**Test Case $4$:** Alice wins the auction since she bid the highest amount.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
200 100 400
```

**Output for this case**

```text
Charlie
```



#### Test case 2

**Input for this case**

```text
155 1000 566
```

**Output for this case**

```text
Bob
```



#### Test case 3

**Input for this case**

```text
736 234 470
```

**Output for this case**

```text
Alice
```



#### Test case 4

**Input for this case**

```text
124 67 2
```

**Output for this case**

```text
Alice
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest](https://www.codechef.com/JULY221/)

[Practice](https://www.codechef.com/problems/AUCTION)

Setter: [Jeevan Jyot Singh](https://www.codechef.com/users/jeevanjyot)

Tester: [ Satyam](https://www.codechef.com/users/satyam_343), [ Jatin Garg](https://www.codechef.com/users/rivalq)

Editorialist: [Kiran](https://www.codechef.com/users/kiran8268)

#
[](#difficulty-2)DIFFICULTY:

330

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Alice, Bob, and Charlie are bidding for an artifact at an auction. Alice, Bob and Charlie bids for A rupees, B rupees and C rupees respectively. According to the rules of the auction, the person who bids the highest amount will win the auction. The objective is to find the winner.

#
[](#explanation-5)EXPLANATION:

-

The objective of this problem is to input three distinct values, compare its values

and return the highest value.

-

We input three distinct values to three variables A, B & C (representing Alice, Bob, and Charlie). Let’s compare the three variables using a max function and return the highest value.

-

Solution:

-

If A has the max value, Alice is the winner.

-

If B has the max value, Bob is the winner.

-

If C has the max value, Charlie is the winner.

#
[](#time-complexity-6)TIME COMPLEXITY:

O(1)

#
[](#solution-7)SOLUTION:

Editorialist's Solution
``int t;
    cin>>t;
    for(int i=0;i<t;i++)
    {
        int a,b,c,d;
        cin>>a>>b>>c;
        d=max(a,max(b,c));
        if(d==a)
        cout<<"Alice"<<"\n";
        else if(d==b)
        cout<<"Bob"<<"\n";
        else
        cout<<"Charlie"<<"\n";

    }
``

</details>
