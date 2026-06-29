# Devu and friendship testing

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CFRTEST |
| Difficulty Rating | 1061 |
| Difficulty Band | Level up from 1* to 2* |
| Path | Become 5 star |
| Lesson | Time Complexity |
| Official Link | [CFRTEST](https://www.codechef.com/practice/course/1to2stars/LP1TO205/problems/CFRTEST) |

---

## Problem Statement

Devu has **n** weird friends. Its his birthday today, so they thought that this is the best occasion for testing their friendship with him. They put up conditions before Devu that they will break the friendship unless he gives them a grand party on their chosen day. Formally, **i**th friend will break his friendship if he does not receive a grand party on **di**th day.

Devu despite being as rich as Gatsby, is quite frugal and can give at most one grand party daily. Also, he wants to invite only one person in a party. So he just wonders what is the maximum number of friendships he can save. Please help Devu in this tough task !!

### Input

- The first line of the input contains an integer **T** denoting the number of test cases. The description of **T** test cases follows.

- First line will contain a single integer denoting **n**.

- Second line will contain **n** space separated integers where **i**th integer corresponds to the day **di**th as given in the problem.

### Output

Print a single line corresponding to the answer of the problem.

### Constraints

- **1** ≤ **T** ≤ **104**

- **1** ≤ **n** ** ≤ 50**

- **1** ≤ **di** **≤ 100**

---

## Examples

**Example 1**

**Input**

```text
2
2
3 2
2
1 1
```

**Output**

```text
2
1
```

**Explanation**

**Example case 1.** Devu can give party to second friend on day 2 and first friend on day 3, so he can save both his friendships.

**Example case 2.** Both the friends want a party on day 1, and as the Devu can not afford more than one party a day, so he can save only one of the friendships, so answer is 1.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2
3 2
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
2
1 1
```

**Output for this case**

```text
1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](http://www.codechef.com/COOK58/problems/CFRTEST)

[Contest](http://www.codechef.com/problems/CFRTEST)

**Author:** [Praveen Dhinwa](http://www.codechef.com/users/dpraveen)

**Tester:** [Utkarsh Lath](http://www.codechef.com/users/utkarsh_lath)

**Editorialist:** [Balajiganapathi Senthilnathan](http://www.codechef.com/users/balajiganapath)

**Russian Translator:** [Sergey Kulik](http://www.codechef.com/users/xcwgf666)

**Mandarian Translator:** [Gedi Zheng](http://www.codechef.com/users/stzgd)

### DIFFICULTY:

Cakewalk

### PREREQUISITES:

None

### PROBLEM:

There are **n** people and the i_{th} of them wants a party on the d_i^{th} day. Devu can give at most one party in a day. What is the maximum number of people who can take parties from Devu?

### SHORT EXPLANATION

- Answer will be the number of distinct days.

### EXPLANATION:

Since Devu can give only one party each day. So if more than one people want a party on a day, then he can give party to only one of them. Also, if nobody wants a party on a particular day, then Devu won’t give a party on that day. So it means that number of parties given by Devu will be number of days on which people are asking parties. In other words, it is equal to number of distinct elements in the array d.

**Finding number of distinct elements in an array**

There are a lot of ways of finding number of distinct elements in an array. The most basic idea is to maintain number of occurrences of of each element in the array and then our answer will be number of elements having non zero number of occurrences.

For maintaining count of elements in the array, we can make an look up array whose i-th element denotes number of occurrences of element i.

**Pseudo Code**

`
int cnt[101]; // (since 1 <= d_i <= 100)
// fill the cnt array.
for (int i = 1; i <= n; i++) {
	cnt[d[i]]++;
}
// Now check number of elements having non zero count.
int ans = 0;
for (int i = 1; i <= 100; i++) {
	if (cnt[i] > 0) {
		ans++;
	}
}
`

Time complexity of the above algorithm is \mathcal{O}(100 + n) which is \mathcal{O}(n).

**Another way of finding number of distinct elements in the array**

First let us sort the array d. Now, we can notice that all equal elements will appear continuously in the array. So, we will go from left to right in the sorted order and will count only first occurrence of each element.

Time complexity of this method will be \mathcal{O} (n log n)

**Yet another way of finding number of distinct elements in the array**

You can use STL (standard template library) data structure set which maintains only unique elements in the sorted order. So all we need to do is add all the numbers in the set and finally find the size of the set.

**Pseudo Code**

`
set st;
// insert all the array elements into the set
for (int i = 1; i <= n; i++) {
	st.insert(d[i]);
}
// Size of set can be found using .size() function
int ans = st.size();
`

Time complexity of each insertion in set is \mathcal{O}(log n). As we are inserting n elements in the array, so overall time will be \mathcal{O}(n log n)

### AUTHOR’S AND TESTER’S SOLUTIONS:

[Author’s solution](http://www.codechef.com/download/Solutions/COOK58/setter/CFRTEST.cpp)

[Tester’s solution](http://www.codechef.com/download/Solutions/COOK58/tester/CFRTEST.cpp)

</details>
