# A Big Sale

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | BIGSALE |
| Difficulty Rating | 1260 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1200 to 1400 difficulty problems |
| Official Link | [BIGSALE](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1400/problems/BIGSALE) |

---

## Problem Statement

Chef recently opened a big e-commerce website where her recipes can be bought online. It's Chef's birthday month and so she has decided to organize a big sale in which grand discounts will be provided.

In this sale, suppose a recipe should have a discount of **x** percent and its original price (before the sale) is **p**. Statistics says that when people see a discount offered over a product, they are more likely to buy it. Therefore, Chef decides to first increase the price of this recipe by **x**% (from **p**) and then offer a discount of **x**% to people.

Chef has a total of **N** types of recipes. For each **i** (1 ≤ **i** ≤ **N**), the number of recipes of this type available for sale is **quantityi**, the unit price (of one recipe of this type, before the **x**% increase) is **pricei** and the discount offered on each recipe of this type (the value of **x**) is **discounti**.

Please help Chef find the total loss incurred due to this sale, if all the recipes are sold out.

### Input

- The first line of the input contains a single integer **T** denoting the number of test cases. The description of **T** test cases follows.

- The first line of each test case contains a single integer **N** denoting the number of recipe types.

- **N** lines follow. The **i**-th of these lines contains three space-separated integers **pricei**, **quantityi** and **discounti** describing the **i**-th recipe type.

### Output

For each test case, print a single line containing one real number — the total amount of money lost. Your answer will be considered correct if it has an absolute error less than 10-2.

### Constraints

- 1 ≤ **T** ≤ 10

- 1 ≤ **N** ≤ 105

- 1 ≤ **pricei**, **quantityi** ≤ 100 for each valid **i**

- 0 ≤ **discounti** ≤ 100 for each valid **i**

### Subtasks

**Subtask #1 (30 points):** 1 ≤ **N** ≤ 100

**Subtask #2 (70 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
2
2
100 5 10
100 1 50
3
10 10 0
79 79 79
100 1 100
```

**Output**

```text
30.000000000
3995.0081000
```

**Explanation**

**Example case 1:** There are two recipes.

There are 5 recipes of the first type, each of them has a price of 100 and there is a 10% discount provided on it. Therefore, Chef first increases the price of each recipe by 10%, from 100 to 110. After that, she decreases the price by 10%, which makes the final price 99. The amount of money lost for each unit is 1, thus losing 5 for recipes of the first type.

There is only one recipe of the second type, with price 100 and a 50% discount. Therefore, Chef increases the price of the recipe by 50% from 100 to 150 and after that, she decreases its price by 50% to make its final price 75. She loses 25 for this recipe.

Overall, the amount of money Chef loses is 30.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

## PROBLEM LINK:

[Div1](http://www.codechef.com/MARCH18A/problems/BIGSALE), [Div2](http://www.codechef.com/MARCH18B/problems/BIGSALE)

[Practice](http://www.codechef.com/problems/BIGSALE)

**Author:** [Praveen Dhinwa](http://www.codechef.com/users/dpraveen)

**Tester:** [Triveni Mahatha](http://www.codechef.com/users/triveni)

**Editorialist:** [Adarsh Kumar](http://www.codechef.com/users/adkroxx)

## DIFFICULTY:

Easy

## PREREQUISITES:

None

## PROBLEM:

You are given the initial price p of a product. You need to first increase the price of this recipe by x\% (from p) and then offer a discount of x\%. You need to compute the loss which occured to you as a result of this process, for N items.

## EXPLANATION:

Original price of the product = p.

Chef decides to increase the price of recipe by x\% which means new price = p.\left(1+\frac{x}{100}\right).

Now he is going to offer a discount of x\% on this price. Hence,

Final price = $p.\left(1+\frac{x}{100}\right).\left(1-\frac{x}{100}\right)$

\Rightarrow Final price = p.\left(1-\left(\frac{x}{100}\right) ^2\right)

Since, the final price is less than original price:

Loss = Original price - final price

\Rightarrow Loss = p - p.\left(1-\left(\frac{x}{100}\right) ^2\right)

\Rightarrow Loss = p.\left(\frac{x}{100}\right) ^2

Coming back to original problem, we can use the formula for loss computed above to find loss for each recipe individually. Hence,

Answer = $\sum \limits_{i=1}^N \text{quantity$_i$}.\text{price$_i$}.\left(\frac{\text{discount$_i$}}{100}\right) ^2$

## Time Complexity:

O(N)

## AUTHOR’S AND TESTER’S SOLUTIONS

[Setter’s solution](http://www.codechef.com/download/Solutions/MARCH18/Setter/BIGSALE.cpp)

[Tester’s solution](http://www.codechef.com/download/Solutions/MARCH18/Tester/BIGSALE.cpp)

</details>
