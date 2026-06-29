# Download file

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | DWNLD |
| Difficulty Rating | 1147 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1000 to 1200 difficulty problems |
| Official Link | [DWNLD](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1200/problems/DWNLD) |

---

## Problem Statement

Chef has recently got a broadband internet connection. His history of internet data usage is provided as below.

During the first **T1** minutes, the internet data used was **D1** MBs per minute, and during the next **T2** minutes, it was **D2** MBs per minute, and so on till during last **TN** minutes it was **DN** MBs per minute.

The internet provider charges the Chef **1** dollar for every **1** MB data used, except for the first **K** minutes, when the internet data is free as part of the plan provided to Chef.

Please find out the total amount that Chef has to pay the internet provider (in dollars).

### Input

First line of the input contains a single integer **TC** the number of test cases. Description of **TC** test cases follow.

First line of each test case contains two space separated integers **N** and **K**.

Next **N** lines of each test case contains information about the internet data usage. Specifically, in the **i**-th line, there will be two space separated integers: **Ti** and **Di**.

### Output

For each test case output a single integer in separate line, the amount that Chef has to pay in dollars.

### Constraints

- **1** ≤ **TC** ≤ **1,000**

- **1** ≤ **N** ≤ **10**

- **0** ≤ **K** ≤ **T1 + T2 + ... + TN **

- **1** ≤ **Ti**, **Di** ≤ **10**

---

## Examples

**Example 1**

**Input**

```text
3
2 2
2 1
2 3
2 2
1 2
2 3
3 0
1 2
2 4
10 10
```

**Output**

```text
6
3
110
```

**Explanation**

**Example case 1.** For the first two minutes, internet data of usage of Chef is free. He has to pay for last 2 minutes only, for which he will be charged at 3 dollars per minute, i.e. total 6 dollars.

**Example case 2.** For the first two minutes, internet data of usage of Chef is free. He has to pay for last 1 minute only, for which he is being charged at 3 dollars per minute. So, in total he has to pay 3 dollars.

**Example case 3.** This time, Chef is not provided any free data usage. He has to pay
for entire data usage, which comes out to be 1 * 2 + 2 * 4 + 10 * 10 = 110 dollars.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# Problem Link:

[Contest](http://www.codechef.com/COOK79/problems/DWNLD)

[Practice](http://www.codechef.com/problems/DWNLD)

**Author:** [Hasan Jaddouh](http://www.codechef.com/users/kingofnumbers)

**Testers:**   [Kamil Debowski](http://www.codechef.com/users/errichto)

**Editorialist:** [Hasan Jaddouh](http://www.codechef.com/users/kingofnumbers)

# Difficulty:

cakewalk

# Pre-requisites:

none

# Problem Statement:

Given a list internet speed during different times, the internet service provider charges 1 dollar per 1 MB downloaded, except for the first **K** minutes it was free, calculate the total cost that should be paid.

### Explanation

We will describe the logic of the solution and the implementation details will be in C++

One input file contains multiple test-cases, we should process each test-case alone, so first thing we need a variable to read the number of test-cases then we make a loop to iterator over test-cases, inside it we will solve the problem for a single test-case, it’s fine to output the result of one test-case before reading the rest of test-cases.

so far our code should look like this:

``#include <iostream>
using namespace std;

int Tc;

int main(){
	cin>>Tc;
	for(int j=0;j<Tc;j++){
		// process a single test-case here

	}
}
``

for single test-case, we should read **N** and **K**, so we need two variables for them we also need a variable to store the answer (Let’s name it sol) initially it has value 0. after that we should a make a loop to iterate over lists of durations and speeds, in every step in this loop we should read the duration and speed so we also need variables for them, thus so far our code is like this:

``#include <iostream>
using namespace std;

int Tc;

int main(){
	cin>>Tc;
	for(int j=0;j<Tc;j++){
		// process a single test-case here
		int N,K,sol=0;
		cin>>N>>K;
		for(int j=0;j<N;j++){
			int T,D;
			cin>>T>>D;

		}
	}
}
``

Now, let’s use the variable K as how much time remaining for free period so if T is less than K then the whole T duration will be free but K should decrease by T, otherwise if T is greater or equal to K then only first K minutes will be free so we will pay for the rest (T-K) minutes and the amount to pay will be (T-K)*D so we increase sol by it, after that we should decrease K to 0 because free period is ended

by the end of the loop we just output sol, so the full solution is:

``#include <iostream>
using namespace std;

int Tc;

int main(){
	cin>>Tc;
	for(int j=0;j<Tc;j++){
		// process a single test-case here
		int N,K,sol=0;
		cin>>N>>K;
		for(int j=0;j<N;j++){
			int T,D;
			cin>>T>>D;
			if(T<K){
				K= K - T;
			} else {
				sol += (T-K)*D;
				K=0;
			}
		}
		cout<<sol<<endl;
	}
}
``

# Author’s and Tester’s Solutions

[Setter](http://www.codechef.com/download/Solutions/COOK79/Setter/DWNLD.cpp)

[Tester](http://www.codechef.com/download/Solutions/COOK79/Tester/DWNLD.cpp)

</details>
