# Chef and Queries

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CHEFQUE |
| Difficulty Rating | 2327 |
| Difficulty Band | 2000 to 2500 difficulty problems |
| Path | Become 5 star |
| Lesson | 2000 to 2500 difficulty problems |
| Official Link | [CHEFQUE](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/CHEFQUE) |

---

## Problem Statement

As part of his daily job, Chef has to solve problems involving sets. Till now, Chef has been using inefficient methods to solve his set related problem, wasting a lot of his precious time. He has agreed to pay you a lot of money for solving the following problem for him efficiently.

First, Chef needs to perform **Q** operations on a set. Each operation is either:

- 1. Add a number to the set (if this number is NOT already present in the set).

- 2. Erase a number from the set (if this number exists in the set).

Then, he needs to find the sum of all elements of the set after performing these **Q** queries. Your job is to find this sum for him quickly.

### Input
The first line of input contains four integers — **Q**, **S1**, **A**, **B**. **S1** is the first number in the operations. **A** and **B** are special constants explained later.

Every operation **Si** is represented by a single integer. If **Si** is odd, then it represents the first operation, otherwise the second type, and in both of them the integer you have to add/delete equals [**Si** / 2], where [] is the greatest integer (or floor) function.

**Si** = (**A*****Si-1** + **B**) mod **232** when **i** > 1.

**Note:** In this problem, the time limit is very tight. Using built-in data structures, such as set/unordered_set in C++ or TreeSet/HashSet in Java, may lead to a Time Limit Exceed verdict.

### Output
Output a single line containing a single integer — sum of elements in the set after **Q** queries.

### Constraints

- 1 ≤ **Q** ≤ 107

- 1 ≤ **S1, A, B** ≤ 109

### Example
`
**Input:**
5 1 1 1

**Output:**
3

**Input:**
10000000 777777777 777777777 777777777

**Output:**
5362358669068782
`

### Explanation:

The sequence {Si} is 1, 2, 3, 4, 5:

Operation 1, 1 mod 2 = 1, add number [1 / 2] = 0 to set, sum is 0.

Operation 2, 2 mod 2 = 0, erase number [2 / 2] = 1 from set, 1 is not in set, so nothing happens, sum is 0.

Operation 3, 3 mod 2 = 1, add number [3 / 2] = 1 to set, sum is 1.

Operation 4, 4 mod 2 = 0, erase number [4 / 2] = 2 from set, 2 is not in set, so nothing happens, sum is 1.

Operation 5, 5 mod 2 = 1, add number [5 / 2] = 2 to set, sum is 3.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](http://www.codechef.com/problems/CHEFQUE)

[Contest](http://www.codechef.com/COOK65/problems/CHEFQUE)

**Author:** [Misha Chorniy](https://www.codechef.com/users/mgch)

**Tester:** [Jingbo Shang](https://www.codechef.com/users/shangjingbo)

**Editorialist:** [Pushkar Mishra](https://www.codechef.com/users/pushkarmishra)

### DIFFICULTY:

Easy-Medium

### PREREQUISITES:

Hash-Table

### PROBLEM:

Given two types of queries:

- Add the number to the set of numbers being maintained.

- Remove the given number from the set if it exists in it.

The numbers to be inserted/deleted are generated according to the following scheme:

S = (a*S_{i-1} + b) mod 2^{32},

where a and b are integers.

The sum of the numbers finally remaining in the set after all the operations is to be reported.

### EXPLANATION:

Given the number of operations to be executed, i.e., q = 10^7, it should be clear that the insertions and deletions from the set are to be done in \mathcal{O}(1). Use of STL or pre-written libraries in C++/Java can’t be used since they will definitely time out because of associated overheads.

**Hash Table Solution**

One way is to write our own hash table. Editorialist’s solution provides a standard implementation of Hash-Table with chaining to handle collision. For chaining, linked list has been used in the given solution. You can read more about it over the internet.

**Bitset Solution**

A neater and more concise solution is using Bitset. Let’s think about the naive solution to this problem first. If we could simply keep an array of length 2^{32}-1, then direct insert/lookup in the array would have been possible. The the memory constraints don’t allow that big an array. However, let us look at the constraints on the number being inserted/deleted into the set. We know they lie between 0 and 2^{32}-1, i.e., they can be represented by 31 bits. Now, we can use a smart way to index numbers. Let us keep an array of length 2^{26}. This is perfectly fine with the memory limits. Now, for a 31 bit integer x, let the first 26 bits indicate the index in the array where x will reside. The rest 5 bits can be encoded in a 32 bit integer since only different 2^5 possibilities exist. Please read setter’s/tester’s solutions for this approach.

There is one more intricacy here: calculating S_i. If we use the normal mod operation present in some of the programming languages, the solution will exceed time limit. This is because mod is a complex operation and performing it 10^7 times will not work. The observation is that we have to take mod 2^{32}. If we keep the data type of S, a, b to be unsigned, in that case, we will not have to use mod operation because the range of unsigned int is 0 to 2^{32}-1. Thus, if S goes over 2^{32} it will automatically overflow around to greater than 0. In other words, the compiler will perform the mod function implicitly because of the overflow.

### COMPLEXITY:

\mathcal{O}(1) per insert and delete operation.

### SAMPLE SOLUTIONS:

[Author](http://www.codechef.com/download/Solutions/COOK65/Setter/CHEFQUE.cpp)

[Tester](http://www.codechef.com/download/Solutions/COOK65/Tester/CHEFQUE.cpp)

[Editorialist](http://www.codechef.com/download/Solutions/COOK65/Editorialist/CHEFQUE.cpp)

</details>
