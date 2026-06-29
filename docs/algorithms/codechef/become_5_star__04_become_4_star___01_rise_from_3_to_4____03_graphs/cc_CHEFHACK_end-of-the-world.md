# End Of The World

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CHEFHACK |
| Difficulty Rating | 1730 |
| Difficulty Band | Rise from 3* to 4* |
| Path | Become 5 star |
| Lesson | Graphs |
| Official Link | [CHEFHACK](https://www.codechef.com/practice/course/3to4stars/LP3TO403/problems/CHEFHACK) |

---

## Problem Statement

**Important!!! Human's are in Danger... It may be The End of the Universe!!!**

**Aliens** had stolen the important data about the **Birth of the Human beings** and they kept this data in their secured **Data Center**. With the help of these data along with the advanced technologies Aliens had initiated a project called **It's The End** to get rid of the human beings and occupy the Earth.

On the other side, **Chef Po** is a good and very well-known **Hacker**. He is a great human lover, so he decided to get the data back from the Aliens by hacking their Data Center.

The Aliens Data Center contains various servers arranged in **N** rows and **N** columns and the Master Server will be at the last row and the last column of the Data Center. Denote the server at the intersection of the **i**-th row and the **j**-th column of the Data Center as **Server[i][j]** (**1** ≤ **i**, **j** ≤ **N**). So in this notation Master Server is **Server[N][N]**. Two servers are connected to each other if they are located either at the same row and consecutive columns or at the same column and consecutive rows. In other words, **Server[i][j]** and **Server[i-1][j]** are connected to each other for all **i** and **j** such that **2** ≤ **i** ≤ **N** and **1** ≤ **j** ≤ **N**. Also **Server[i][j]** and **Server[i][j-1]** are connected to each other for all **i** and **j** such that **1** ≤ **i** ≤ **N** and **2** ≤ **j** ≤ **N**.

Aliens had divided the **Data File** with the data about the Birth of the Human beings into **N * N** parts denoted as **F[i][j]** (**1** ≤ **i**, **j** ≤ **N**) and placed the part **F[i][j]** at the **Server[i][j]**. Each server has a password which is some non-negative integer. Chef Po needs to crack all the servers in order to get all parts of the **Data File**.

Aliens are really strange beings so they single out three types of passwords:

- **Prime Password**, which is the prime number. The list of prime numbers starts as **2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, ...**

- **Even Password**, which is the even non-prime number. This list starts as **0, 4, 6, 8, 10, 12, 14, ...** Note, that we exclude **2** since it is a prime.

- **Odd Password**, which is the odd non-prime number. This list starts as **1, 9, 15, 21, 25, 27, 33, 35, 39, 45, 49, ...** So it is the list of all odd positive numbers where primes are excluded.

For simplicity we call server secured by the Even Password as Even Server. Similarly we define notion of Odd Server and Prime Server.

Each Odd or Even server has a friendly screen with the color indicator. Assume that you enter the password trying to guess the actual password at this server. Then indicator will become green if you enter the number which is smaller than the actual password, it will become red if your number is greater than the actual password or you will get the access to the server (and, thus, to the needed part of the Data File) if the password is correct.

On the other hand, each Prime Server has no such screen and the only way to crack it is to try all prime numbers until you find out the correct password. So our Chef simply iterate over the list of primes in increasing order and try them until he finds the correct password.

Probably most of you think that to crack servers with friendly screen Chef Po will use binary search. But he is quite weird Hacker and doesn't know this concept. To crack server with the friendly screen he will use the following strategy. He will try all even numbers starting from 0 (even number 2) until he either finds the correct password or the indicator becomes red which automatically would mean that the password is odd and equals to the **K-1** where **K** is the even number that was entered at last. So he enters **K-1** in the latter case and get the access to the server.

Let's consider some examples.

- Let the password be **4**. It is an Even Password so Chef will see the friendly screen which means for him that the server is either Even or Odd. Hence he will try passwords in the order **0, 2, 4** making 2 unsuccessful tries.

- Let the password be **9**. It is an Odd Password so again Chef will see the friendly screen which means for him that the server is either Even Server or Odd Server. Hence he will try passwords in the order **0, 2, 4, 6, 8, 10, 9** making 6 unsuccessful tries. Note that after he enters **8** the indicator becomes green indicating that the password is greater than **8**, on the other hand, after he enters **10** the indicator becomes red indicating that the password is less than **10**. Since the only integer number greater than **8** and less than **10** is **9** he will enter it at the last step getting the access to the server.

- Finally, let the password be **11**. It is a Prime Password so Chef will not see the friendly screen which means for him that the server is Prime Server. Hence he will try passwords in the order **2, 3, 5, 7, 11** making 4 unsuccessful tries.

The Alien Data Center has very interesting vulnerability, that Chef has noticed by analyzing Alien's secured correspondence. If Chef crack some Even Server **S** then all Even Servers connected to **S** become cracked as well, and all Even Servers connected to these servers also become cracked and so on. More formally, the Even Server **S'** becomes cracked if it is connected with **S** via possibly other Even Servers. That is, there exists a sequence of Even Servers such that each two consecutive servers in this sequence are connected, the first server is **S** and the last server is **S'**. Chef calls this vulnerability as **"Grid Hacking Mechanism"**. The same is true for Odd Servers. By it is no longer true for Prime Servers. So each Prime Server should be cracked individually.

Now the final tactic for Chef is the following.

- He will consider the servers in row-major order.

- That is, at first he consider servers of the first row in the order **Server[1][1]**, **Server[1][2]**, ..., **Server[1][N]**. Then he considers servers of the second row in the order **Server[2][1]**, **Server[2][2]**, ..., **Server[2][N]** and so on until he reaches the last server in the last row (which is the Master Server).

- For each server he at first check whether it is already cracked by the **"Grid Hacking Mechanism"**.

- If yes then he gathers the corresponding part of the Data File and move on.

- Otherwise he checks for the friendly screen at this server and apply one of the cracking tactics described above.

- That is, when he sees the friendly screen he will enter even numbers starting from zero until he finds the password in the way described above. After that he gathers the corresponding part of the Data File and also some other servers become cracked by the **"Grid Hacking Mechanism"**.

- And when he doesn't see the screen he will enter prime numbers in increasing order until he finds the password. After that he again gathers the corresponding part of the Data File but no other servers become cracked since **"Grid Hacking Mechanism"** does not work for Prime Servers.

- Finally he will reach the Master Server, crack it and gather the last part of the Data File.

But the only way to recombine the original file is to use special Alien utility called **winripzar** on the Master Server. It also has the password. Chef Po is a great hacker, so he found out using his special skills that the password for **winripzar** equals to the number of unsuccessful tries used by him to crack all the servers in the Data Center.

After cracking all the servers and gathering all the parts of the Data File Chef became so happy that forgot the number of unsuccessful tries he made during this cracking marathon. But he noted down passwords for all the servers and now asks you for help. Calculate the number of unsuccessful tries Chef did during cracking of all the servers and let him save the Earth!

### Input

The first line of the input contains an integer **T** denoting the number of test cases. The description of **T** test cases follows. The first line of each test case contains a single integer **N**. Each of the following **N** lines contains **N** space separated integers. The **j**-th number at the **i**-th line denotes the password at the **Server[i][j]**.

### Output

For each test case, output a single line containing the number of unsuccessful tries used to crack all the servers in the Data Center.

### Constraints

- **1** ≤ **T** ≤ **8**

- **1** ≤ **N** ≤ **350**

- **0** ≤ **each password** < **107**

---

## Examples

**Example 1**

**Input**

```text
2
3
2 6 4
4 8 9
7 9 4
2
8 4
15 4
```

**Output**

```text
20
13
```

**Explanation**

**Example case 1.**

The type of each server can be found in the following table.

PrimeEvenEven

EvenEvenOdd

PrimeOddEven

Now the process of cracking of servers by the Chef will be the following.

- At first Chef cracks the **Server[1][1]** secured by the password **2** which is a prime number. Hence Chef does not see the friendly screen and tries prime numbers in increasing order. Since **2** is the smallest prime number he cracks this server without unsuccessful tries. Since it is a Prime Server than **"Grid Hacking Mechanism"** does not work here.

- Next Chef cracks the **Server[1][2]** secured by the password **6** which is an Even Password (even non-prime number). Hence Chef sees the friendly screen and tries even numbers in order **0, 2, 4, 6** making 3 unsuccessful tries to crack this server. Since it is an Even Server than by **"Grid Hacking Mechanism"** the following 3 servers also become cracked: **Server[1][3]**, **Server[2][1]** and **Server[2][2]** since they all Even Servers and connected to the **Server[1][2]** via other Even Servers (see the above table). Note, that Even **Server[3][3]** does not become cracked since it is not connected to **Server[1][2]** via other Even Servers.

- Next Chef consider the **Server[1][3]**. As was mentioned above it was already cracked so Chef simply gatheres the corresponding part of the Data File without entering any numbers.

- The same is true for the next two servers **Server[2][1]** and **Server[2][2]**.

- But **Server[2][3]** is secured by the odd non-prime number **9** so it is an Odd Server and Chef tries numbers in order **0, 2, 4, 6, 8, 10, 9** making 6 unsuccessful tries to crack it. Applying **"Grid Hacking Mechanism"** for this server has no effect since it is not connected to any other Odd Server.

- The **Server[3][1]** is Prime and Chef tries numbers in order **2, 3, 5, 7** making 3 unsuccessful tries to crack it.

- The **Server[3][2]** is Odd and was not cracked earlier. Hence Chef tries numbers in order **0, 2, 4, 6, 8, 10, 9** making 6 unsuccessful tries to crack it.

- The **Server[3][3]** is Even and was not cracked earlier. Hence Chef tries numbers in order **0, 2, 4** making 2 unsuccessful tries to crack it.

Summarizing we see that Chef made 20 unsuccessful tries in all. Their distribution among servers can be found in the following table.

030

006

362

**Example case 2.**

The type of each server can be found in the following table.

EvenEven

OddEven

Now the process of cracking of servers by the Chef will be the following.

- The **Server[1][1]** is Even and Chef tries numbers in order **0, 2, 4, 6, 8** making 4 unsuccessful tries to crack it.

- The **Server[1][2]** is Even and already cracked by the **"Grid Hacking Mechanism"**.

- The **Server[2][1]** is Odd and Chef tries numbers in order **0, 2, 4, 6, 8, 10, 12, 14, 16, 15** making 9 unsuccessful tries to crack it.

- The **Server[2][2]** is Even and already cracked by the **"Grid Hacking Mechanism"**.

Thus, Chefs made 13 unsuccessful tries and their distribution among servers can be found in the following table.

40

90

### Warning!
The input file size could reach almost 8MB so be sure you are using fast I/O method.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### SUGGESTION:

Before posting your question with asking for help try [this test](http://pastebin.com/raw.php?i=j6UWCAZ5).

The answer should be 436746489.

If it is hard to debug this test for you, [here](http://pastebin.com/raw.php?i=Q5hGmk0W) is the helpful information.

It contains the number of unsuccessful tries for each cell

or -1 if the cell was hacked by the “Grid Hacking Mechanism”.

If it still hard to debug try [another smaller test](http://pastebin.com/raw.php?i=dcLeXChd) that contains answer and similar debug information as above.

If you pass this test then read carefully the bold tip in the QUICK EXPLANATION section.

If you follow this tip but still have WA then post your question and we will help you.

### PROBLEM LINK:

[Practice](http://www.codechef.com/problems/CHEFHACK)

[Contest](http://www.codechef.com/JAN13/problems/CHEFHACK)

**Author:** [Khadar Basha](http://www.codechef.com/users/khadarbasha)

**Tester:** [Anton Lunyov](http://www.codechef.com/users/anton_lunyov)

**Editorialist:** [Anton Lunyov](http://www.codechef.com/users/anton_lunyov)

### DIFFICULTY:

EASY

### PREREQUISITES:

[Connected component](http://en.wikipedia.org/wiki/Connected_component_%28graph_theory%29), [Depth-first search](http://en.wikipedia.org/wiki/Depth-first_search), [Flood fill algorithm](http://en.wikipedia.org/wiki/Flood_fill), [Sieve of Eratosthenes](http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes)

### PROBLEM:

You are given **N × N** grid filled by non-negative integers. We single out 3 types of numbers on the grid: primes, even non-primes and odd non-primes. For each number we define the cost as follows: for the prime number it is the id of this prime in the 0-based list of all primes, for even non-prime number **X** it is **X / 2**, and for odd non-prime number **Y** it is **(Y + 3) / 2** (the cost of a number is the shortcut for the number of unsuccessful tries to crack the server secured by the password equals to this number; the mentioned formulas for cost in all three cases are clear from the problem statement).

Two even non-prime numbers that share a side on the grid are connected to each other. The same is true for odd non-prime numbers. But prime number is not connected to any other number. In this way all cells of the grid form a bidirectional graph that has several connected components (each cell having prime number is a separate component). The cost of the component is defined as the cost of the first cell in this component that we meet traversing the grid in row-major order. Now your task is to find the sum of costs over all components.

### QUICK EXPLANATION:

Actually, most of the job has already made while we reformulated the problem above. Now you simply need to loop over all cells of the grid in row-major order and if we meet the unvisited cell we add its cost to the answer and run DFS from this cell in the graph constructed above to mark other cells of its connected component as visited.

**Tip: the total cost could overflow 32-bit integer type. Use 64-bit type instead.**

To be able to find the cost of the prime cell fast enough we need to run Sieve of Eratosthenes in advance (even before input the very first test) in order to find all prime numbers. Then we need to create the array of size **107** that contains for each prime its id. Now the cost of each number can be found in **O(1)**.

The overall complexity is **O(K * log log K + T * N * N)**.

### EXPLANATION:

As mentioned above at first we run Sieve of Eratosthenes to identify all prime numbers:

`
isPrime[0] = false
isPrime[1] = false
for i = 2 to K do
    isPrime[i] = true
for i = 2 to sqrt(K) do
    if isPrime[i] then
        for j = i * i to K with step i do
            isPrime[j] = false
`

where **K = 107 ? 1**.

Next we fill array of costs. We maintain variable `prime_id` which is equal to the number of primes we met so far:

`
prime_id = 0
for i = 0 to K do
    if isPrime[i] then
        cost[i] = prime_id
        prime_id = prime_id + 1
    else
        cost[i] = i div 2 + (i mod 2) * 2
`

Note the formula for the cost for non-prime number.

Now we can input grids and traverse them. We use two-dimensional array `A[][]` for the initial grid. Also we use another two-dimensional array `visited[][]` to check visited cells, which could be filled by `false` while input the grid:

`
for i = 1 to N do
    for j = 1 to N do
        read A[i][j]
        visited[i][j] = false
`

Now we can traverse the grid. If we meet visited cell we skip it. Otherwise we always add its cost to the answer and if it is non-prime then run DFS to fill its connected component:

`
total_cost = 0 // this should be a variable of 64-bit integer type!
for i = 1 to N do
    for j = 1 to N do
        if (visited[i][j]) then
            continue
        total_cost = total_cost + cost[A[i][j]]
        if (not isPrime[A[i][j]]) then
            DFS(i, j)
`

**DFS(i, j)** is the recursive routine that traverse the grid passing from the cell **(i, j)** to its neighbors in the graph constructed above:

`
DSF(i, j)
    if (not visited[i][j]) then
        visited[i][j] = true
        for (x, y) in {(i+1, j), (i-1, j), (i, j-1), (i, j+1)} do
            if (not isPrime[A[x][y]]) and (A[x][y] is of the same parity as A[i][j]) then
                DFS(x, y)
`

Note that we pass to the cell **(x, y)** only if the number in it is non-prime and of the same parity as in the cell **(i, j)**. Missing of any of these checks will definitely lead to WA. Also see [tester’s solution](http://www.codechef.com/download/Solutions/2013/January/Tester/CHEFHACK.cpp) as a reference to one of the convenient ways how to implement loop:

`
        for (x, y) in {(i+1, j), (i-1, j), (i, j-1), (i, j+1)} do
`

### ALTERNATIVE SOLUTION:

For some languages (like Java or Python) the recursive implementation of DFS could lead to runtime error due to stack overflow. In this case you need to implement either non-recursive DFS or BFS ([breadth-first search](http://en.wikipedia.org/wiki/Breadth-first_search)) to mark cells of each connected component. Another alternative is to use disjoint-set data structure to do the same job. But this way requires some additional thinking.

The alternative very fast method to find all primes is to use [Atkin Sieve](http://en.wikipedia.org/wiki/Atkin_Sieve) invented in 2004 by Atkin and Bernstein. It allows to find all primes up to **K** using **O(K / log log K)** operations. Check it out first 6 related problems to train yourself at fast implementation of sieve.

The remaining 3 problems involves flood fill algorithm.

### AUTHOR’S AND TESTER’S SOLUTIONS:

Author’s solution can be found [here](http://www.codechef.com/download/Solutions/2013/January/Setter/CHEFHACK.cpp).

Tester’s solution can be found [here](http://www.codechef.com/download/Solutions/2013/January/Tester/CHEFHACK.cpp).

### RELATED PROBLEMS:

[SPOJ - 6488. Printing some primes - TDPRIMES](http://www.spoj.com/problems/TDPRIMES/)

[SPOJ - 6470. Finding the Kth Prime - TDKPRIME](http://www.spoj.com/problems/TDKPRIME/)

[SPOJ - 6488. Printing some primes (Hard) - PRIMES2](http://www.spoj.com/problems/PRIMES2/)

[SPOJ - 6489. Finding the Kth Prime (Hard) - KPRIMES2](http://www.spoj.com/problems/KPRIMES2/)

[SPOJ - 3505. Prime Number Theorem - CPRIME](http://www.spoj.com/problems/CPRIME/)

[SPOJ - 11844. Binary Sequence of Prime Number - BSPRIME](http://www.spoj.com/problems/BSPRIME/)

[UVA - 352 - The Seasonal War](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=288)

[UVA - 469 - Wetlands of Florida](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=410)

[UVA - 785 - Grid Colouring](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=726)

</details>
