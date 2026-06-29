# Dessert Wizard

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | DELISH |
| Difficulty Rating | 1804 |
| Difficulty Band | Rise from 3* to 4* |
| Path | Become 5 star |
| Lesson | Dynamic Programming |
| Official Link | [DELISH](https://www.codechef.com/practice/course/3to4stars/LP3TO406/problems/DELISH) |

---

## Problem Statement

It's finally summer in Chefland! So our chef is looking forward to prepare some of the best "beat-the-heat" dishes to attract more customers. He summons the Wizard of Dessert to help him with one such dish.

 The wizard provides the chef with a sequence of **N** ingredients where the **ith** ingredient has a delish value of **D[i]**. The preparation of the dish takes place in two phases.

**Phase 1 :** The chef chooses two indices **i** and **j** and adds the ingredients **i, i+1, ..., j** to his dish. He also finds the sum of the delish value in this range i.e **D[i] + D[i+1] + ... + D[j]**.

**Phase 2 :** The chef chooses two more indices **k** and **l** and adds the ingredients **k, k+1, ..., l** to his dish. He also finds the sum of the delish value in this range i.e **D[k] + D[k+1] + ... + D[l]**.

Note that **1**  ≤ **i**  ≤ **j** < **k**  ≤ **l** ≤ **N**.

The total delish value of the dish is determined by the absolute difference between the values obtained in the two phases. Obviously, the chef wants to maximize the total delish value for his dish. So, he hires you to help him.

### Input
First line of input contains an integer **T** denoting the number of test cases. For each test case, the first line contains an integer **N** denoting the number of ingredients. The next line contains **N** space separated integers where the **ith** integer represents the delish value **D[i]** of the **ith** ingredient.

### Output

Print the maximum delish value of the dish that the chef can get.

### Constraints

-  **1** ≤ **T** ≤ **50**

-  **2** ≤ **N** ≤ **10000**

-  **-1000000000 (−109)** ≤ **D[i]** ≤ **1000000000 (109)**

---

## Examples

**Example 1**

**Input**

```text
2
5
1 2 3 4 5
4
1 1 -1 -1
```

**Output**

```text
13
4
```

**Explanation**

**Example case 1.**

Chef can choose **i = j = 1, k = 2, l = 5**.

The delish value hence obtained  is ** | (2+3+4+5) ? (1) | = 13 **.

**Example case 2.**

 Chef can choose **i = 1, j = 2, k = 3, l = 4**.

The delish value hence obtained  is ** | ( ( ?1 ) + ( ?1 ) ) ? ( 1 + 1 ) | = 4 **.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5
1 2 3 4 5
```

**Output for this case**

```text
13
```



#### Test case 2

**Input for this case**

```text
4
1 1 -1 -1
```

**Output for this case**

```text
4
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# Problem Link:

[Practice](http://www.codechef.com/problems/DELISH)

[Contest](http://www.codechef.com/JUNE13/problems/DELISH)

# Difficulty:

Simple

# Pre-requisites:

Dynamic Programming

# Problem:

Given an array D[1…N], find max(abs((D[i] + … + D[j]) - (D[k] + … D[l])) : 1<= i <= j < k <= l <= N).

# Explanation:

Let us look at the final solution, and work backwards. Let the final solution be due to some i0, j0, k0, l0. We now have two cases:

Case 1: D[k0] + … + D[l0] <= D[i0] + … + D[j0].

In this case, we get that among all possible choices of l, D[k0] + … + D[l] is MINIMUM for l = l0. Else, we could choose such l, and this would give us a larger absolute difference. We also get, that among all 1 <= i <= j <= k0-1, D[i] + … + D[j] is MAXIMUM.

Case 2: D[k0] + … + D[l0] > D[i0 + … + D[j0].

In this case, among all possible choices of l, we choose l0 to give the MAXIMUM value of the sum, and we choose i0, j0 to give the MINIMUM possible sum.

Hence, it would be useful precomputing values that answer “what is the [minimum|maximum] value I can get if I [start|end] at position i?”

### Solution 1

The above setting motivates the following few definitions:

HardLeftMin(i) = Minimum value of the sum of a contiguous subarray whose rightmost point = i.

HardLeftMax(i) = Maximum value of the sum of a contiguous subarray whose rightmost point = i.

SoftLeftMin(i) = Minimum value of the sum of a contiguous subarray whose rightmost point <= i.

SoftLeftMax(i) = Maximum value of the sum of a contiguous subarray whose rightmost point <= i.

HardRightMin(i) = Minimum value of the sum of a contiguous subarray whose leftmost point = i.

HardRightMax(i) = Maximum value of the sum of a contiguous subarray whose rightmost point = i.

Recurrences for the above are easy to find:

HardLeftMin(i) = min(D[i], D[i] + HardLeftMin(i-1)) : either you select position i-1 as well in your subarray and take the best from there, or you don’t even take position i-1.

HardLeftMax(i) = max(D[i], D[i] + HardLeftMax(i-1)) : similarly.

HardRightMin(i) = min(D[i], D[i] + HardRightMin(i+1)) : similarly.

HardRightMax(i) = max(D[i], D[i] + HardRightMax(i+1)) : similarly.

SoftLeftMin(i) = min(HardLeftMin(i), SoftLeftMin(i-1)) : either your minimum ends at points i, or it ends at some point <= i-1.

SoftLeftMax(i) = max(HardLeftMax(i), SoftLeftMax(i-1)) : similarly.

Note that, using the above recurrences, we can calculate all the arrays in O(N) time using dynamic programming.

Finally, our case (1) will be covered by SoftLeftMax(j0) - HardRightMin(j0+1), and case (2) will be covered by HardRightMax(j0+1) - SoftLeftMin(j0).

Iterate over all values of j0, and take the maximum, as your answer. This again takes O(N) time to run.

### Solution 2

This solution cleverly disposes of SoftLeftMin, SoftLeftMax() functions and works relying on the following claim.

Claim: Without loss of generality, k0 - j0 = 1. That is, we can consider our optimal phases as being consecutive.

Let us say that OPT returned i, j, k, l, with k-j > 1. Now, consider sum S = D[j+1] + D[j+2] + … + D[k-1]. If S >= 0, then it can be added to the larger of the two segments [i…j], [k…l]. If S <= 0, then the segment can be added to the smaller of the two segments [i…j], [k…l]. In both cases, it gives us a Delish value atleast as good as the Optimal. Hence, wlog, the two segments we choose are consecutive.

Thus, finally, we iterate over j, and consider abs(LeftMax(j) - RightMin(j+1)) and abs(RightMax(j+1) - LeftMin(j)) as candidates. This approach was used by the Setter.

# Setter’s Solution:

Can be found [here](http://www.codechef.com/download/Solutions/2013/June/Setter/DELISH.cpp)

# Tester’s Solution:

Can be found [here](http://www.codechef.com/download/Solutions/2013/June/Tester/DELISH.cpp)

</details>
