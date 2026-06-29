# Bear and Candies 123

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CANDY123 |
| Difficulty Rating | 1028 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1000 to 1200 difficulty problems |
| Official Link | [CANDY123](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1200/problems/CANDY123) |

---

## Problem Statement

Bears love candies and games involving eating them. Limak and Bob play the following game. Limak eats 1 candy, then Bob eats 2 candies, then Limak eats 3 candies, then Bob eats 4 candies, and so on. Once someone can't eat what he is supposed to eat, he loses.

Limak can eat at most **A** candies in total (otherwise he would become sick), while Bob can eat at most **B** candies in total.
Who will win the game?
Print "Limak" or "Bob" accordingly.

### Input

The first line of the input contains an integer **T** denoting the number of test cases. The description of **T** test cases follows.

The only line of each test case contains two integers **A** and **B** denoting the maximum possible number of candies Limak can eat and the maximum possible number of candies Bob can eat respectively.

### Output

For each test case, output a single line containing one string — the name of the winner ("Limak" or "Bob" without the quotes).

### Constraints

- 1 ≤ **T** ≤ 1000

- 1 ≤ **A, B** ≤ 1000

---

## Examples

**Example 1**

**Input**

```text
10
3 2
4 2
1 1
1 2
1 3
9 3
9 11
9 12
9 1000
8 11
```

**Output**

```text
Bob
Limak
Limak
Bob
Bob
Limak
Limak
Bob
Bob
Bob
```

**Explanation**

**Test case 1.** We have **A** = 3 and **B** = 2. Limak eats 1 candy first, and then Bob eats 2 candies. Then Limak is supposed to eat 3 candies but that would mean 1 + 3 = 4 candies in total. It's impossible because he can eat at most **A** candies, so he loses. Bob wins, and so we print "Bob".

**Test case 2.** Now we have **A** = 4 and **B** = 2. Limak eats 1 candy first, and then Bob eats 2 candies, then Limak eats 3 candies (he has 1 + 3 = 4 candies in total, which is allowed because it doesn't exceed **A**). Now Bob should eat 4 candies but he can't eat even a single one (he already ate 2 candies). Bob loses and Limak is the winner.

**Test case 8.** We have **A** = 9 and **B** = 12. The game looks as follows:

- Limak eats 1 candy.

- Bob eats 2 candies.

- Limak eats 3 candies (4 in total).

- Bob eats 4 candies (6 in total).

- Limak eats 5 candies (9 in total).

- Bob eats 6 candies (12 in total).

- Limak is supposed to eat 7 candies but he can't — that would exceed **A**. Bob wins.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3 2
```

**Output for this case**

```text
Bob
```



#### Test case 2

**Input for this case**

```text
4 2
```

**Output for this case**

```text
Limak
```



#### Test case 3

**Input for this case**

```text
1 1
```

**Output for this case**

```text
Limak
```



#### Test case 4

**Input for this case**

```text
1 2
```

**Output for this case**

```text
Bob
```



#### Test case 5

**Input for this case**

```text
1 3
```

**Output for this case**

```text
Bob
```



#### Test case 6

**Input for this case**

```text
9 3
```

**Output for this case**

```text
Limak
```



#### Test case 7

**Input for this case**

```text
9 11
```

**Output for this case**

```text
Limak
```



#### Test case 8

**Input for this case**

```text
9 12
```

**Output for this case**

```text
Bob
```



#### Test case 9

**Input for this case**

```text
9 1000
```

**Output for this case**

```text
Bob
```



#### Test case 10

**Input for this case**

```text
8 11
```

**Output for this case**

```text
Bob
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](https://www.codechef.com/problems/CANDY123)

[Contest](https://www.codechef.com/COOK81/problems/CANDY123)

**Author:** [Kamil Debowski](https://www.codechef.com/users/errichto)

**Primary Tester:** [Marek Soko?owski](https://www.codechef.com/users/mnbvmar)

**Secondary Tester:** [Praveen Dhinwa](https://www.codechef.com/users/dpraveen)

**Editorialist:** [Praveen Dhinwa](https://www.codechef.com/users/dpraveen)

### DIFFICULTY:

cakewalk

### PREREQUISITES:

none, knowledge of for or while loops in any programming language

### PROBLEM:

Limak and Bob are friends who play a game involving eating candies. They take turns alternately with Limak starting first. Initially Limak eats 1 candy, then Bob eats 2 candies, then Limak 3 followed by Bob eating 4 candies and so on. Limak can eat at most A candies, whereas Bob can eat at most B candies. The person who is not able to eat the required candies in his turn will lose the game. Find out the winner of the game.

Problem constraints mention that A and B can be at max 1000. The idea of the solution is to implement the turns of the game. We iterate over the number of candies being eaten in the current starting from 1 onwards and check whether the current player can eat the desired amount of candies or not. We can find the current player by checking the parity of number of candies in the turn being eaten. You can see that Limak always eats odd number of candies, while Bob even number of candies. If the current player is not able to eat the required amount of candies, he will lose. Pseudo code follows.

``limakCandies = 0 // denotes number of candies eaten by Limak.
bobCandies = 0 // denotes number of candies eaten by Bob.
c = 1;
while (true)
    // In this turn the person should eat exactly c candies.
    // if c is odd, then it is Limak's turn, otherwise Bob's.
    if c % 2 == 1:
        limakCandies += c;
        if (limakCandies > A):
            // limak can't eat these c candies, so Bob will win.
            winner = "Bob";
            break;
    else:
        bobCandies += c;
        if (bobCandies > B):
            // Bob can't eat these c candies, so Limak will win.
            winner = "Limak";
            break;

    c += 1;
``

Notice that the while loop can have at most A + B iterations, i.e. at most 2000 iterations. There are 1000 test cases. So, total number of operations will be around 2000 * 1000 = 2 * 10^6 which is sufficient to pass under a sec. For a rough guideline, you can assume that around 10^8 operations take a second to execute. Please note that this is a rough guideline, actual number of operations depend very much on the implementation of the solution and also on the architecture of the machine on which your code is being judged. You should also account for the extra constant factor due to your implementation.

In fact, if you analyze carefully, you can prove that number of iterations of the while loop will much less than 2000, they will be around \sqrt{2000}, around 45. This is because we are subtracting c candies each time, c going from 1 to 2 to 3 and so on. As we know that sum of 1 + 2 + \dots + n = \frac{n \cdot (n+1)}{2} = \mathcal{O}(n^2). Therefore, c will become greater than A or B in around \sqrt{A + B} operations.

### AUTHOR’S AND TESTER’S SOLUTIONS:

[Setter](http://www.codechef.com/download/Solutions/COOK81/Setter/CANDY123.cpp)

[Tester1](http://www.codechef.com/download/Solutions/COOK81/Tester1/CANDY123.cpp)

[Tester2](http://www.codechef.com/download/Solutions/COOK81/Tester2/CANDY123.java)

</details>
