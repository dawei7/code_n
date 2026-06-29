# Chef Up

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CHEF7UP |
| Difficulty Rating | 2494 |
| Difficulty Band | 2000 to 2500 difficulty problems |
| Path | Become 5 star |
| Lesson | 2000 to 2500 difficulty problems |
| Official Link | [CHEF7UP](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/CHEF7UP) |

---

## Problem Statement

Chef is a wanted criminal, and $N$ police officers are up for catching him. The officers want to catch Chef no matter the cost, and Chef also wants to eliminate as many officers as possible (preferably everyone) before getting caught (or before running away after eliminating everyone). Neither the officers nor Chef will run away before accomplishing their goals.

Chef and the officers are on a one-dimensional grid with coordinates ranging from $-10^{10}$ to $10^{10}$. Chef is initially standing at coordinate $C$, and the $i$-th officer is initially at coordinate $P_i$. The officers and Chef then take turns to move, with the officer team moving first.

During their turn, officers will have to move to an adjacent unoccupied cell one by one, in any order they want. Every officer will have to move. At every moment of time, no two officers can be in the same cell, and also no officer can be in the same cell as Chef. If the officer is unable to move to an adjacent unoccupied cell, he is eliminated (and the cell he was in becomes unoccupied). **Note that the officer team will try to move to eliminate as few officers as possible.** For example, with $P = [2, 3, 4]$ and $C = 6$, then the next positions of the officers can be $[1, 2, 3]$, $[1, 2, 5]$, $[1, 4, 5]$, or $[3, 4, 5]$. However, with $P = [2, 3, 4]$ and $C = 5$, the only possible set of the next positions of the officers is $[1, 2, 3]$.

After the officer team's turn, Chef also moves to an adjacent unoccupied cell, or gets caught if he cannot find any adjacent unoccupied cell. The process then repeats until either Chef is caught, or all officers are eliminated and Chef runs away.

You need to find out the maximum number of officers that can be eliminated by Chef, and if Chef can run away or not.

As a reminder, two cells with coordinates $X$ and $Y$ are *adjacent* if and only if $|X - Y| = 1$.

---

## Input Format

- The first line contains $T$ - the number of test cases. Then the test cases follow.
- The first line of each test case contains a single integer $N$ - the number of officers.
- The second line of each test case contains a single integer $C$ - the initial coordinate of Chef.
- The third line of each test case contains $N$ integers $P_1, P_2, \dots, P_N$ - the initial coordinates of the officers.

---

## Output Format

For each test case, output on a single line two space-separated integers: the first integer is the maximum number of officers that can be eliminated by Chef, and the second integer is $1$ if Chef runs away or $-1$ if Chef will be caught.

---

## Constraints

- $1 \leq T \leq 10$
- $1 \leq N \leq 10^5$
- $1 \leq C \leq 10^9$
- $1 \leq P_i \leq 10^9$
- All the coordinates are unique. That means $P_i \ne C$ for all $1 \le i \le N$, and $P_i \ne P_j$ for all $1 \le i \lt j \le N$

---

## Examples

**Example 1**

**Input**

```text
2
2
2
1 4
1
2
1
```

**Output**

```text
1 -1
1 1
```

**Explanation**

- **Test case $1$**: Chef chooses to always move to the left (i.e. to the smaller coordinate); this forces the officer at coordinate $1$ to always move to the left, and eventually being cornered and eliminated. However, the officer at coordinate $4$ cannot be eliminated, and hence Chef will be caught at the end.
- **Test case $2$**: Similarly, Chef chooses to always move to the left, and eventually eliminating the only officer, thus running away at the end.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2
2
1 4
```

**Output for this case**

```text
1 -1
```



#### Test case 2

**Input for this case**

```text
1
2
1
```

**Output for this case**

```text
1 1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/CHEF7UP)

[Contest: Division 1](https://www.codechef.com/COOK134A/problems/CHEF7UP)

[Contest: Division 2](https://www.codechef.com/COOK134B/problems/CHEF7UP)

[Contest: Division 3](https://www.codechef.com/COOK134C/problems/CHEF7UP)

***Author:*** [Ashish Kumar](https://www.codechef.com/users/ashish99hanny)

***Tester:*** [Danny Mittal](https://www.codechef.com/users/tlatoani)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

Easy - medium

#
[](#prerequisites-3)PREREQUISITES:

Sorting

#
[](#problem-4)PROBLEM:

Chef and N police officers are standing at distinct positions on a one-dimensional grid. They move in turns - first, each officer moves one step either left or right to an unoccupied square, then chef moves either left or right to an unoccupied square. An officer who cannot move is eliminated, and if Chef cannot move he is captured. Find the maximum number of officers that can be eliminated.

#
[](#quick-explanation-5)QUICK EXPLANATION

If the sorted set of positions is P_1 < P_2 < \dots < P_i < C < P_{i+1} < \dots < P_N, Chef can eliminate the longest prefix of officers starting at i+1 and the longest suffix ending at i such that such that C\pmod 2 \neq P_j\pmod 2.

#
[](#explanation-6)EXPLANATION:

Suppose Chef starts at position C. Let us concentrate only on officers whose initial positions are greater than C for now - the other case turns out to be symmetric.

Suppose we have C < P_1 < P_2 < \dots P_N.

An initial observation is that the relative parity of C and P_i always stays the same, i.e, if they are initially of the same parity, after any set of moves they will still be of the same parity; and if they are initially different and set of moves will keep them distinct.

Now, let’s look at P_1 first. There are two cases

-
C and P_1 have the same parity

In this case, P_1 can never be eliminated - in fact, none of the officers can be eliminated.

Proof

Given that they have the same parity, and must start on distinct squares at the start of each police turn, we must have P_1 \geq C+2.

This means that P_1 can always simply take one step towards Chef irrespective of the movements of other officers, and in particular will never be eliminated.

Further, because P_1 can always move left towards Chef, that movement will leave at least one empty space for P_2 to move left, which then allows P_3 to move left, and so on.

Thus, every officer always has at least one legal move, meaning none of them can be eliminated.

-
C and P_1 have different parity

In this case, P_1 can always be eliminated.

Proof

Suppose P_1 > C+1. Then, P_1 \geq C+3, so no matter what move P_1 makes, Chef can always move one step right.

Thus, the distance between Chef and P_1 either stays the same, or decreases by 2 - in particular, it does not increase.

What happens if P_1 = C+1?

P_1 then has no choice but to move right, and this allows Chef to also move right on his turn.

However, our grid is finite, and so P_1 cannot move right forever.

Thus, there will come a time when P_1 = C+1, but P_1+1, P_1+2, \dots, 10^{10} are all occupied by officers.

This will force P_1 to be eliminated, as required.

Now that P_1 has been eliminated, let’s look at P_2.

If P_2 and C have different parities, a similar argument as above tells that P_2 can also be eliminated - either after eliminating P_1 by following the same strategy, or P_2 was already eliminated before P_1 was.

On the other hand, if P_2 and C have the same parity, our first argument tells us that P_2 can never be eliminated - and hence P_i for i\geq 2 can never be eliminated.

This brings us to the following result:

**Lemma**: Let k be the smallest index such that parity(C) = parity(P_i). Then, when the police move optimally, only P_1, P_2, \dots, P_{i-1} can be eliminated, and none beyond that.

The proof follows easily from the processes described above.

Of course, the exact same result follows for officers to Chef’s left, i.e, some suffix of them with different parity from C can be eliminated, and none beyond that.

Thus, we have our final algorithm:

- Sort the set of officers.

- Among the officers to the right of Chef, choose the longest prefix such that their parity is different from C.

- Among the officers to the left of Chef, choose the longest suffix such that their parity is different from C.

The answer is the sum of the above two quantities.

Finally, Chef escapes if and only if all officers are eliminated, so print 1 if all N officers can be eliminated and -1 otherwise.

#
[](#time-complexity-7)TIME COMPLEXITY:

\mathcal{O}(N\log N) per test.

#
[](#code-8)CODE:

Setter (C++)
``#include <bits/stdc++.h>
using namespace std;
#define READ(f) freopen(f, "r", stdin)
#define WRITE(f) freopen(f, "w", stdout)

int main()
{
    int t;cin>>t;
    assert(t>=1 and t<=10);

    while(t--){

    int n;cin>>n;
    assert(n>=1 and n<=100000);

    int chef;cin>>chef;
    assert(chef>=1 and chef<=1000*1000*1000);

    int police[n];

    for(int i=0;i<n;i++){cin>>police[i];
    assert(police[i]>=1 and police[i]<=1000*1000*1000);
    assert(police[i]!=chef);
    }

    sort(police,police+n);

    int p1=lower_bound(police,police+n,chef)-police;
    int p2=upper_bound(police,police+n,chef)-police;

    int ans=0;

    p1--;
    while(p1>=0 and police[p1]%2!=chef%2){p1--;ans++;}
    while(p2<n and police[p2]%2!=chef%2){p2++;ans++;}

    cout<<ans<<' ';

    if(ans==n)cout<<1<<endl;
    else cout<<-1<<endl;
    }
}
``

Tester (Kotlin)
``import java.io.BufferedInputStream

const val BILLION = 1000000000

fun main(omkar: Array<String>) {
    val jin = FastScanner()
    repeat(jin.nextInt(10)) {
        val n = jin.nextInt(100000)
        val chef = jin.nextInt(BILLION)
        val police = IntArray(n) { jin.nextInt(BILLION, it == n - 1) }
        val left = police.filter { it < chef }.sortedDescending()
        val right = police.filter { it > chef}.sorted()
        val answer = (left.indexOfFirst { it % 2 == chef % 2 }.takeUnless { it == -1 } ?: left.size) + (right.indexOfFirst { it % 2 == chef % 2 }.takeUnless { it == -1 } ?: right.size)
        println("$answer ${if (answer == n) 1 else -1}")
    }
}

class FastScanner {
    private val BS = 1 shl 16
    private val NC = 0.toChar()
    private val buf = ByteArray(BS)
    private var bId = 0
    private var size = 0
    private var c = NC
    private var `in`: BufferedInputStream? = null

    constructor() {
        `in` = BufferedInputStream(System.`in`, BS)
    }

    private val char: Char
        private get() {
            while (bId == size) {
                size = try {
                    `in`!!.read(buf)
                } catch (e: Exception) {
                    return NC
                }
                if (size == -1) return NC
                bId = 0
            }
            return buf[bId++].toChar()
        }

    fun nextInt(): Int {
        var neg = false
        if (c == NC) c = char
        while (c < '0' || c > '9') {
            if (c == '-') neg = true
            c = char
        }
        var res = 0
        while (c >= '0' && c <= '9') {
            res = (res shl 3) + (res shl 1) + (c - '0')
            c = char
        }
        return if (neg) -res else res
    }

    fun nextInt(unused1: Int, unused2: Boolean = true) = nextInt()

    fun nextInt(unused1: Int, unused2: Int, unused3: Boolean = true) = nextInt()
}
``

</details>
