# Saving a gift of love

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | ASHIGIFT |
| Difficulty Rating | 2265 |
| Difficulty Band | 2000 to 2500 difficulty problems |
| Path | Become 5 star |
| Lesson | 2000 to 2500 difficulty problems |
| Official Link | [ASHIGIFT](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/ASHIGIFT) |

---

## Problem Statement

Suraj, the Chief Prankster is back in action now and this time he has stolen the valentine's day gift given by Ashi (the love of Chef) to the Chef and ran away with it to Byteland.

Byteland is a not a regular place like Chef's town. The safest way from Chef's town to Byteland is through *the path of tasty dishes*. The path is named so because there are magical tasty dishes which appear to the traveler that no one can resist eating. Also, Suraj has added a strong sleep potion to each of the dish on this path to stop anyone from following him.

Knowing the devilish nature of Suraj, Ashi is concerned about the Chef and has asked all of Chef's town people to help. The distance from Chef's town to Byteland through the *the path of tasty dishes* is **X** units. They have the location where the magic dishes are and how many people are required to eat it completely. Anyone who eats a dish would go to a long sleep and won't be able to continue. They have the information about the tribal clans that live along the *the path of tasty dishes* who can be of real help in this journey.

The journey Chef and his friends can be described as follows: There is a total of **B** dishes on *the path of tasty dishes*. Each dish is located at some distance from Chef's town denoted by **xi** for the ith dish ( **xi-1** <  **xi**). To minimize the number of friends Chef has to leave behind, all of them have decided that exactly **yi** of them will eat the ith dish, which is the required number of people needed to finish it completely. Also, there are a total of **C** tribal chef clans, each with their own population and location on the path that Chef and his friends will meet on their way to Byteland. They know that for some clan (say *i*), they are located at a distance of **pi** ( **pi-1** <  **pi**) from Chef's town with a population of **ri**. And if a group of **at least qi** men approaches them, they would be able to convince them to join their forces against Suraj.

Given the information about all this, help the Chef to find out the minimum size of the group (including him and his friends) he should start with to reach Byteland and get back Ashi's gift from Suraj.

### Input

The first line of the input contains an integer **T** denoting the number of test cases. Each test case contains three lines which are as follows:

First line of each test case contains **X**, the distance of Byteland from Chef's town.

Next line contains an integer **B**, the number of dishes on *the path of tasty dishes*. Then follows **B** pairs of space separated integers of the form **xi yi**, where **xi yi** are as defined above for the ith dish.
Next line contains an integer **C**, followed **C** space separated triplets of integers **pi qi ri** as defined above.

### Output

For each test case, print the minimum size of the group  (including Chef) that is needed to reach Byteland.

### Constraints

- **1** ≤ **T** ≤ **10**

- **1** ≤ **X** ≤ **109**

- **1** ≤ **B** ≤ **10000**

-  Constraints on **C**

- Subproblem 1 (25 points): ** C = 0**

- Subproblem 2 (75 points): **1** ≤ **C** ≤ **10000**

- **1** ≤ **xi** < **X**, **xi** < **xi+1**

- **1** ≤ **pi** < **X**, **pi** < **pi+1**

- **1** ≤ **yi** ≤ **1014**

- **1** ≤ **qi** ≤ **1014**

- **1** ≤ **ri** ≤ **1014**

- All the positions, of the tasty dishes and tribal clans are distinct.

---

## Examples

**Example 1**

**Input**

```text
3
10
2 1 3 8 1
0
10
2 1 3 8 5
0
10
2 2 3 8 5
3 1 2 1 4 3 2 9 1 1
```

**Output**

```text
5
9
6
```

**Explanation**

**Example case 1.** In the first case, there are no tribal clans, and two dishes, one which needs to be eaten by 3 chefs on their way and one to be eaten by 1 chef. Hence, we have to start with atleast 5 people in total to pass *the path of tasty dishes*.

**Example case 2.** Similar as Example Case 1.

**Example case 3.** In this case, if we start with 5 Chefs. At point 1, we have more than or equal to 2 chefs, hence the tribal clan of size 1 adds to the Chef's party and now they have size of 6. At position 2, three of them would be left behind eating a dish, leaving 3 of them to go ahead. At position 4, since the size is exactly 3, the tribal clan joins the chef's party making it of size 5. At position 8, all 5 of them will stop to eat the dish and none would go ahead. Similarly, if we start with 6, one of them would be able to pass position 8 and reach position 9, where it will also add one of the tribal clans to its party and reach Byteland.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
10
2 1 3 8 1
0
```

**Output for this case**

```text
5
```



#### Test case 2

**Input for this case**

```text
10
2 1 3 8 5
0
```

**Output for this case**

```text
9
```



#### Test case 3

**Input for this case**

```text
10
2 2 3 8 5
3 1 2 1 4 3 2 9 1 1
```

**Output for this case**

```text
6
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

**PROBLEM LINK:**

[Practice](http://www.codechef.com/problems/ASHIGIFT)

[Contest](http://www.codechef.com/LTIME22/problems/ASHIGIFT)

**Author:** [Pankaj Jindal](http://www.codechef.com/users/pankaj%20jindal), [Piyush Kumar](http://www.codechef.com/users/piyushkumar)

**Tester: **[Sergey Kulik](http://www.codechef.com/users/xcwgf666)

**Editorialist:** [Aman jain](http://www.codechef.com/users/amanjain110893)

### DIFFICULTY:

Simple

### PREREQUISITES:

Binary search

### PROBLEM:

Poor Chef now wants to go to Byteland. On the way to Byteland he found B tasty dishes, each dish requires B_i people to complete, after eating the dish one can’t move forward. He can ask support from C tribal clans, found on the way, but on one condition by each clan that is, "they will join only if he approaches them with a group of size atleast q_i". Now chef wants to know with what minimum number of people including him he should start his journey to Byteland.

### QUICK EXPLANATION:

Binary search over the range of group size Chef can start with and check whether it is possible to reach Byteland with the group size.

### EXPLANATION:

Its easy to observe that if there are no tribal clans in the path, then Chef has to start with x = 1+\sum{B_i} people to reach Byteland, first sub-task can be solved using this. But how can he minimize number of people on start when help from tribal clans is available?

Basic idea that might struck to your mind would be to try all possible values in range and check what should be minimum size to reach Byteland, one can easily see that the ans would be in range [1,x], since in the worst case no clan members joins you. Complexity of this solution would be O(x*(B+C)), where B is number of dishes and C is number of tribal clans, that’s about 10^{13} computations which do not fit in our time limit.

If Chef start with x people (including him) and can reach Byteland, then if he starts with more than x people, then also he can reach Byteland.

Let f(n): checks whether its possible to reach Byteland with n people or not. You can do binary search over range [1,x] to find out minimum n such that f(n) is true, as answer would lie in range [1,x] only. For binary searching in a range, the idea is to check value of function in mid point of current range and decide to go to one half depending on its value. This will ensure that in log(x) steps we will reach the optimal value.

**Pseudocode:**

``
low = 1, high = x, ans = x
while(low <= high){
  m = (low+high)/2
  if(possible(m)){
    ans = min(ans,m);
    high = m-1;
  }
  else low = m+1;
}
possible(v){
  // store dishes and clans in a vector, in increasing order of their distance from Chef's town
  // pi,qi,ri are same convention described in problem
  for each item in vector:
    if item is a dish:
      v-=pi
    else if v >= qi: v+= ri
  return (v>0)
}

</pre>
``

### COMPLEXITY:

Binary search takes O(log(x))

Possible function takes O(B+C)

Total complexity should be O(log(x)*(B+C))

**AUTHOR’S, TESTER’S and Editorialist’s SOLUTIONS:**

[author](https://s3.amazonaws.com/codechef_shared/download/Solutions/LTIME22/Setter/ASHIGIFT.cpp)

[tester](https://s3.amazonaws.com/codechef_shared/download/Solutions/LTIME22/Tester/ASHIGIFT.cpp)

[editorialist](https://s3.amazonaws.com/codechef_shared/download/Solutions/LTIME22/Editorialist/ASHIGIFT.cpp)

</details>
