# Sudhanva and Books

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SUDBOOKS |
| Difficulty Band | Jump from 2* to 3* |
| Path | Become 5 star |
| Lesson | Standard Template Library |
| Official Link | [SUDBOOKS](https://www.codechef.com/practice/course/2to3stars/LP2TO304/problems/SUDBOOKS) |

---

## Problem Statement

As we all know, Sudhanva is fond of reading books and taking photographs. His dad (after gifting him an iPad last birthday) gifted him a custom-made bookshelf this birthday. This shelf is made in such a way that books can be inserted and removed only from the top. Books are placed one over the other in that shelf. Now to remember each book, Sudhanva develops an algorithm. He first writes a number in his iPad, then takes a photo of that number in his DSLR and then pastes that photograph on the cover of each book. Initially the bookshelf is empty.

You have given $Q$ queries of either of the two types

•	Type 1. $(1, N)$ In this type of query Sudhanva places a book with photo of number N on the top. You don't have to print anything in this query

•	Type 2.  $(-1)$ In this Query Sudhanva takes out the topmost book, you have to print the number on the book he just took out. If the shelf is empty and Sudhanva is trying to take out a book, print "kuchbhi?" Without quotes

### Input:

- First line will contain $Q$, number of queries
- Following $Q$ lines will contain queries of one of the types mentioned
- Type 1:    $1$ $N$
	This query specifies that Sudhanva places a book with number $N$ on it, at the top of the shelf.
- Type 2:    $-1$
	This query specifies that Sudhanva takes out the topmost books from the shelf.

### Output:
For each query of Type 2, print the number $N$ on the book he just took out, if the shelf was empty and it was not possible to take out a book, then print "kuchbhi?" (without quotes)  Each output should be printed on a new line.

### Constraints
- $1 \leq Q \leq 10^6$
- $1 \leq N \leq 10^9$

### Subtasks
- 100 points : Original Constraints

---

## Examples

**Example 1**

**Input**

```text
5
1 2
1 45
-1
-1
-1
```

**Output**

```text
45
2
kuchbhi?
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

[Practice](https://www.codechef.com/problems/SUDBOOKS)

[CAC2.0 Contest](https://www.codechef.com/CAC22020/problems/SUDBOOKS)

***Author:***  [Uttkarsh Bawakar](https://www.codechef.com/users/utkd52)

***Tester:*** [Priyanshu Damodhare](https://www.codechef.com/users/priyanshud)  [Mayuresh Patle](https://www.codechef.com/users/mayureshpatle)

***Editorialist:***  [Uttkarsh Bawankar](https://www.codechef.com/users/utkd52)

# DIFFICULTY:

CAKEWALK

# PREREQUISITES:

Stack, Basic I/O operations

# PROBLEM:

Given a stack, you have to perform two types of queries on it. Push and Pop. Whenever the pop operation is performed you have to print the element which is being removed. If the stack is empty and no element can be removed then you have to print “kuchbhi?”

# QUICK EXPLANATION:

This is a straight forward stack implementation with no twist in it. You just have to create a stack and while taking  the input check if you have to push or pop. If pop then print the last element in the stack and remove it and if the stack is already empty empty print “kuchbhi?”

# EXPLANATION:

There are many approaches to this problem in different languages. Lets discuss the simplest one in  C++ using vector from STL.

First take input T and enter a loop of T iterations

For each test case:

First define a vector of int.

Then take interger input Q

For each Q take input input operation

if operation is 1 then take another input number and push_back in the vector

else if operation is -1 then first check if the stack is empty

if the stack is empty, print “kuchbhi?”

else if the stack is not empty print last element of the stack and then pop the last element.

# SOLUTIONS:

Setter's Solution
``#include<bits/stdc++.h>
using namespace std;
int main()
{
int testCases;
int operation, number;
vector<int> stck;
cin>>testCases;
while(testCases--)
{

	cin>>operation;
	if(operation==-1)
	{
		if(stck.size() ==0)cout<<"kuchbhi?\n";
		else
		{
			cout<<stck.back()<<"\n";
			stck.pop_back();
		}
	}
	else
	{
		cin>>number;
		stck.push_back(number);
	}
}
}
``

Tester's Solution
``q = int(input())
l = []
for _ in range(q):

  n = list(map(int,input().split()))
  if n[0]==1:
    l.append(n[1])
  else:
    if(len(l)!=0):
      print(l[-1])
      del l[-1]
    else:
      print("kuchbhi?")
``

</details>
