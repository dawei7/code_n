# Cutting Recipes

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CUTRECIPE |
| Difficulty Rating | 1047 |
| Difficulty Band | Number theory |
| Path | Data Structures and Algorithms |
| Lesson | GCD and LCM |
| Official Link | [CUTRECIPE](https://www.codechef.com/learn/course/number-theory/LINTDSA04/problems/CUTRECIPE) |

---

## Problem Statement

The chef has a recipe he wishes to use for his guests,
but the recipe will make far more food than he can serve to the guests.
The chef therefore would like to make a reduced version of the recipe which has the same ratios of ingredients, but makes less food.
The chef, however, does not like fractions.
The original recipe contains only whole numbers of ingredients,
and the chef wants the reduced recipe to only contain whole numbers of ingredients as well.
Help the chef determine how much of each ingredient to use in order to make as little food as possible.

### Input

Input will begin with an integer T, the number of test cases.
Each test case consists of a single line.
The line begins with a positive integer N, the number of ingredients.
N integers follow, each indicating the quantity of a particular ingredient that is used.

### Output

For each test case, output exactly N space-separated integers on a line,
giving the quantity of each ingredient that the chef should use in order to make as little food as possible.

### Constraints

T ≤ 100

2 ≤ N ≤ 50

All ingredient quantities are between 1 and 1000, inclusive.

---

## Examples

**Example 1**

**Input**

```text
3
2 4 4
3 2 3 4
4 3 15 9 6
```

**Output**

```text
1 1
2 3 4
1 5 3 2
```

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2 4 4
```

**Output for this case**

```text
1 1
```



#### Test case 2

**Input for this case**

```text
3 2 3 4
```

**Output for this case**

```text
2 3 4
```



#### Test case 3

**Input for this case**

```text
4 3 15 9 6
```

**Output for this case**

```text
1 5 3 2
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Cutting Recipes in Number theory](https://www.codechef.com/learn/course/number-theory/LINTDSA04/problems/CUTRECIPE)

### [](#problem-statement-1)Problem Statement:

The chef wants to reduce a recipe while maintaining the same ratios of ingredients, but without fractions, meaning all ingredient amounts must remain whole numbers. Given the quantities of ingredients, you need to find the smallest possible version of the recipe.

### [](#approach-2)Approach:

- To maintain the same ratio between ingredients but reduce their overall quantities, the greatest common divisor of all the ingredient quantities needs to be calculated.

- By dividing each ingredient by the **GCD**, you ensure that the ratio of the ingredients remains intact while minimizing the total quantity.

- The **GCD** of all quantities is calculated, and each quantity is divided by this GCD to get the reduced ingredient values.

- **See how to find gcd here**:- [Euclid Algorithm in Number theory](https://www.codechef.com/learn/course/number-theory/LINTDSA04/problems/PRIMFACT08)

### [](#complexity-3)Complexity:

- **Time Complexity:** To compute the gcd of two numbers - `O(log(min(a,b)))`, We are computing the gcd of each element in the array by iterating over the array once - `O(N log⁡(max⁡(A)))`

- **Space Complexity:** `O(1)` No extra space needed.

</details>
