# Cats and Dogs

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CATSDOGS |
| Difficulty Rating | 1389 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1200 to 1400 difficulty problems |
| Official Link | [CATSDOGS](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1400/problems/CATSDOGS) |

---

## Problem Statement

Chef is a farmer and a pet lover. He has a lot of his favorite pets cats and dogs in the barn. He knows that there are $C$ cats and $D$ dogs in the barn. Also, one day went to field and found that there were $L$ legs of the animals touching the ground. Chef knows that cats love to ride on the dogs. So, they might ride on the dogs, and their legs won't touch the ground and Chef would miss counting their legs. Chef's dogs are strong enough to ride at max two cats on their back.

It was a cold foggy morning, when Chef did this counting. So he is now wondering whether he counted the legs properly or not. Specifically, he is wondering whether it is possible that he counted correctly. Please help Chef in finding it.

### Input

- First line of the input contains an integer $T$, denoting number of test cases. $T$ test cases follow.

- The only line of each test case contains three space separated integers $C, D, L$, denoting number of the cats, number of the dogs and number of legs of animals counted by Chef, respectively.

### Output

For each test case, output a single line containing a string **yes** or **no**, according to the situation.

### Constraints

- $1 \le T \le 10^5$
- $0 \le C, D, L \le 10^9$

### Subtasks

**Subtask #1 (20 points):**

- $1 \le T \le 10^4$
- $0 \le C, D \le 100$

**Subtask #2 (30 points):**

- $1 \le T \le 10^5$
- $0 \le C, D \le 1000$

**Subtask #3 (50 points):**

- Original constraints

---

## Examples

**Example 1**

**Input**

```text
3
1 1 8
1 1 4
1 1 2
```

**Output**

```text
yes
yes
no
```

**Explanation**

**Example 1:** There is one cat and one dog. The number of legs of these animals on the ground are $8$, it can be possible when both cat and dog are standing on the ground.

**Example 2:** There is one cat and one dog. The number of legs of these animals on the ground are $4$, it can be possible if the cat will ride on the dog, so its legs won't be counted by Chef, only the dog's legs will be counted.

**Example 3:** There is one cat and one dog. The number of legs of these animals are $2$, it can not be true at all, Chef might have made some mistake. Hence, the answer is **no**.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1 1 8
```

**Output for this case**

```text
yes
```



#### Test case 2

**Input for this case**

```text
1 1 4
```

**Output for this case**

```text
yes
```



#### Test case 3

**Input for this case**

```text
1 1 2
```

**Output for this case**

```text
no
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

[Practice](https://www.codechef.com/problems/CATSDOGS)

[Contest](https://www.codechef.com/JAN17/problems/CATSDOGS)

**Author:**  [Praveen Dhinwa](https://www.codechef.com/users/dpraveen)

**Tester:**  [Istvan Nagy](https://www.codechef.com/users/iscsi)

**Editorialist:** [Misha Chorniy](https://www.codechef.com/users/mgch)

## Difficulty:

Cakewalk

# Pre-Requisites:

None

## Problem Statement

There are C cats and D dogs, and L legs touching the ground. Some of the cats can ride on dogs, but every dog can’t have more than 2 cats on his back. Can this be true?

## Explanation

Let’s make some obvious observations:

- 	Every cat has 4 legs.

- 	Every dog has 4 legs.

If we have X cats and Y dogs staying on the ground then, the number of legs in the barn equal 4 * (X+Y). Therefore if L not divisible by 4, the answer is “no”.

## Subtask 1 and 2

Constraints are chosen in such way that solutions with complexity O(D+C) per test case can pass.

Iterate over possible numbers of the cats on Chef’s dogs back G(G must be in the range between 0 and 2*D due to the condition of the dog and 2 cats on his back, and not more than the total number of cats). Hence in the barn 4*(C-G+D) legs on the ground, if 4*(C-G+D) = L for some G, then the answer is “yes”, and “no” otherwise.

## Subtask 3

There is possible to solve problem with O(1) solution per test case.

Let G number of the cats on the backs of the dogs, 0 ? G ? min(C,2*D)

4*(C-G)+4*D = L , there are C-G cats on the ground, therefore total number of legs = 4*(C-G)+4*D

C-G+D = L/4 , divide both parts of the equation by 4

C+D-L/4 = G , add G-L/4 to both parts of the equation

if G will be in the range between 0 and 2*D answer is “yes”, and “no” otherwise.

The overall time complexity of this approach is O(1) per test case.

## Solution:

Setter’s solution can be found [here](http://www.codechef.com/download/Solutions/JAN17/Setter/CATSDOGS.cpp)

Tester’s solution can be found [here](http://www.codechef.com/download/Solutions/JAN17/Tester/CATSDOGS.cpp)

**Please feel free to post comments if anything is not clear to you.**

</details>
