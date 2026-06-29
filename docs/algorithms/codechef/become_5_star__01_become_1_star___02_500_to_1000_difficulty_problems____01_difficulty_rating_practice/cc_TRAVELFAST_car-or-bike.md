# Car or Bike

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | TRAVELFAST |
| Difficulty Rating | 571 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 500 to 800 difficulty rating problems |
| Official Link | [TRAVELFAST](https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/TRAVELFAST) |

---

## Problem Statement

Chef wants to reach home as soon as possible. He has two options:

- Travel with his `BIKE` which takes $X$ minutes.
- Travel with his `CAR` which takes $Y$ minutes.

Which of the two options is faster or do they both take same time?

---

## Input Format

- First line will contain $T$, number of test cases. Then the test cases follow.
- Each test case contains a single line of input, two integers $X, Y$ representing the time taken to travel with `BIKE` and `CAR` respectively.

---

## Output Format

For each test case, print `CAR` if travelling with Car is faster, `BIKE` if travelling with Bike is faster, `SAME` if they both take the same time.

You may print each character of `CAR`, `BIKE` and `SAME` in uppercase or lowercase (for example, `CAR`, `Car`, `cAr` will be considered identical).

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq X,Y \leq 10$

---

## Examples

**Example 1**

**Input**

```text
3
1 5
4 2
6 6
```

**Output**

```text
BIKE
CAR
SAME
```

**Explanation**

**Test case-1:** Travelling with `BIKE` takes $1$ minute while travelling with `CAR` takes $5$ minutes. So travelling with `BIKE` is faster.

**Test case-2:** Travelling with `BIKE` takes $4$ minutes while travelling with `CAR` takes $2$ minutes. So travelling with `CAR` is faster.

**Test case-3:** Travelling with both `BIKE` and `CAR` takes the `SAME` time i.e. $6$ minutes.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1 5
```

**Output for this case**

```text
BIKE
```



#### Test case 2

**Input for this case**

```text
4 2
```

**Output for this case**

```text
CAR
```



#### Test case 3

**Input for this case**

```text
6 6
```

**Output for this case**

```text
SAME
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/START26A/problems/TRAVELFAST)

[Contest Division 2](https://www.codechef.com/START26B/problems/TRAVELFAST)

[Contest Division 3](https://www.codechef.com/START26C/problems/TRAVELFAST)

[Contest Division 4](https://www.codechef.com/START26D/problems/TRAVELFAST)

**Setter:** [Utkarsh Gupta](https://www.codechef.com/users/utkarsh_adm)

**Tester:** [Abhinav Sharma](https://www.codechef.com/users/inov_360)

**Editorialist:** [Kanhaiya Mohan](https://www.codechef.com/users/notsoloud)

#
[](#difficulty-2)DIFFICULTY:

Cakewalk

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Chef wants to reach home as soon as possible. He has two options:

- Travel with his bike which takes X minutes.

- Travel with his car which takes Y minutes.

Which of the two options is faster or they both take the same time?

#
[](#explanation-5)EXPLANATION:

We are given that travel by bike takes X minutes and travel by car takes Y minutes. Following cases are possible:

-
X<Y: This means that travel by bike is faster. Thus, we print `BIKE`.

-
X>Y: This means that travel by car is faster. Thus, we print `CAR`.

-
X=Y: Both vehicles take the same amount of time. Thus, we print `SAME`.

Examples

-
X = 9, Y = 7: Here X>Y. Thus, car is faster and we print `CAR`.

-
X = 3, Y = 5: Here X<Y. Thus, bike is faster and we print `BIKE`.

-
X = 4, Y = 4: Here X=Y. Thus, both take same time and we print `SAME`.

#
[](#time-complexity-6)TIME COMPLEXITY:

We just need to compare the values X and Y. Thus, the time complexity is O(1) per test case.

#
[](#solution-7)SOLUTION:

Editorialist's Solution
``#include <iostream>
using namespace std;

int main() {
	int t;
	cin>>t;
	while(t--){
	    int x, y;
	    cin>>x>>y;
	    if(x<y){
	        cout<<"BIKE";
	    }
	    else if(x>y){
	        cout<<"CAR";
	    }
	    else{
	        cout<<"SAME";
	    }
	    cout<<endl;
	}
	return 0;
}
``

</details>
