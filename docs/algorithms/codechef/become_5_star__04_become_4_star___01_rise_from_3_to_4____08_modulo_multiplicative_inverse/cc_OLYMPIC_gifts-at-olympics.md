# Gifts at Olympics

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | OLYMPIC |
| Difficulty Rating | 2696 |
| Difficulty Band | Rise from 3* to 4* |
| Path | Become 5 star |
| Lesson | Modulo Multiplicative Inverse |
| Official Link | [OLYMPIC](https://www.codechef.com/practice/course/3to4stars/LP3TO408/problems/OLYMPIC) |

---

## Problem Statement

The Olympic Games, world's foremost sports competition,
will be hosted by London next month.
Tens of thousands of participants from over 200 nations will be participating this year.
Each game has only 3 winners, so the organizers have decided to give special chocolate gift pack to each participant.

A huge number of chocolates have just arrived from **N** different villages, numbered 1 to **N**.
The organizers have decided the number of chocolates to be given to each participant.
This is given in **count**, where **count**[*i*] is the number of chocolates from *i*th village,
to be placed in each gift pack.
Now they need to order boxes for these chocolates.
A box of size **S** can store at most **S** chocolates.
A gift pack is made as follows.

Each of the **N** villages is assigned a unique colored box
and chocolates from a village are placed only in boxes assigned to it.
The organizers always want to minimize the number of boxes in each gift pack.
E.g., for given **N** = 3 villages and **count** = {3, 12, 7}, suppose colors assigned are *A*, *B*, *C*.
If size of each box is **S** = 4, then we need 1 box of color A, 3 boxes of color B and 2 boxes of color C.
All the boxes for a gift pack are then packed in a row using transparent wrapper.
So in the above example, a gift pack can be "*ABBBCC*" or "*ABCBCB*" etc.

To make everyone feel special, no two participants are given same gift packs.
Two gift packs are different if and only if they have the different order of colored boxes, even in reverse order.
For example "*ABBBCC*" is same as "*ABBBCC*" and also same as "*CCBBBA*".
Given **Q** queries, each specifying the size of a box **S**,
find the total number of different gift packs possible if we use boxes of size **S** each.
Output the result modulo 1000000007 (109+7).

### Input

The first line has an integer **N**. The second line has the array **count**, **N** space separated integers.
The next line has integer **Q**, followed by **Q** lines, each having an integer size **S**.

1 ≤ **N**, **count**[*i*], **Q** ≤ 100000 (105)

1 ≤ sum of all **count**[*i*] ≤ 100000 (105)

1 ≤ **S** ≤ 1000000000 (109)

### Output

Output **Q** lines, one for each query,
the total number of different gift packs possible, using boxes of size **S**, specified in that query modulo 1000000007 (109+7).

### Example

`
**Input:**
3
5 3 12
4
4
5
2
12

**Output:**
30
10
2320
3
`

**Explanation:**

In the last query, size of each box **S** = 12.

Suppose the colors assigned to the 3 villages are *A*, *B*, *C* respectively,
we need 1 box of each color.

Only 3 different gift packs can be made. They are "*ABC*", "*ACB*", "*BAC*".

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

## PROBLEM LINKS

[Practice](http://www.codechef.com/problems/OLYMPIC)

[Contest](http://www.codechef.com/COOK23/problems/OLYMPIC)

## DIFFICULTY

EASY-MEDIUM

## PREREQUISITES

sorting, factorials, inverse modulo a prime, basic combinatorics

## PROBLEM

The problem is, given count[1…n], the number of chocolates to be included from each village, we need to pack the chocolates into minimum number of boxes of a given size S. No two chocolates from different villages should be places in same box. Given that different villages get different colored boxes, find the total number of distinct gift packs possible. Two gift packs are considered same if and only if they have the same order of colored boxes, even in reverse. “ABC” is same as “ABC” and “CBA”.

## EXPLANATION

First lets see how we can solve the problem of uniquely counting distinct gift packs by taking care of reverse order too. Suppose there are B1 boxes of type 1, B2 boxes of type 2 , … Bk boxes of type K, then the total number of gift packs possible can be found using the following multinomial.

SUM = B1 + B2 + … + Bk

Total possible ways, T = ( SUM! / ( B1! B2! B3! … Bk! ) )

But T may include duplicate items, where two items are same if reversed. Consider “AABBC”. T counts both “AABBC” and “CBBAA” differently and we need to take care of this.

Let P = total number of palindromic strings, where a string is palindrome if its exactly same as its reversed string.

Let U = total number of non-palindromic strings

Our desired answer = ( U + P ) , but the value of T = ( 2 * U + P ), as it counts each non-palindromic

string twice. Finding the number of non-palindromic strings directly may not be easy, so instead we will

find the value of P, the number of palindromic strings. A palindromic string is uniquely defined by its first half, so we will half the counts of each character and find the number of possible halves. Note that P = 0, if the number of characters having odd count > 1 , as only one character can take the middle position in case of odd count.

SUM2 = B1/2 + B2/2 + … + Bk/2

Total number of palindromes, P = ( SUM2! / ( (B1/2)! (B2/2)! … (Bk/2)! ) )

If we have the values of T and P, we can find the desired answer = U + P = ( T + P ) / 2

So the problem is reduced to finding the values of T and P. Till this part, its a common approach. For further main part of the solution, refer any of setter’s or tester’s approach below.

## SETTER’S SOLUTION

Can be found [here](http://www.codechef.com/download/Solutions/COOK23/Setter/OLYMPIC.c)

## APPROACH

Consider count[i] = 20 and find the number of boxes needed, if size S varies from 1 to 20.

      Size of each box S
      1
      2
      3
      4
      5
      6
      7
      8
      9
      10
      11
      12
      13
      14
      15
      16
      17
      18
      19
      20

      Number of boxes Bi
      20
      10
      7
      5
      4
      4
      3
      3
      3
      2
      2
      2
      2
      2
      2
      2
      2
      2
      2
      1

The main idea is, instead of finding the value Bi for each size of the box S, we only visit the indices where there is a change in the number of boxes Bi required. Once we have this, we can scan the array linearly and propagate the values among the indices in between. The good part of it is, we mark the changes for each count[i] in the same array and propagate the values in O(n) time, once for all. So, given count[i] , here is how we can visit only the changes.

*Each size in the interval [lo…hi] requires **x** boxes*

*Initially*, lo = count[i], hi = count[i], x = 1;

while(lo>1)

{

hi = lo - 1;

x = (n+hi-1)/hi;

lo = (n+x-1)/x;

}

We maintain the SUM array and DEN array, for finding the numerator and denominator respectively, as shown in the equation for T above. Initially, for all indices i, SUM[i] = 0 and DEN[i] = 1. These arrays store the change in the values from previous index.

In the table above, B[2] = 10 and B[3] = 7

We store the change as SUM[3] += -3 and DEN[3] *= 10!/7!

After noting all these changes for all the **K** types of boxes, a linear prefix sum is run on the array SUM, so that SUM[i] now has the desired numerator as shown in equation for T above. Similarly, we run a linear prefix product on the array DEN, so that DEN[i] has the desired denominator as shown in equation for T above. A similar approach is used to find the arrays SUM2[] , DEN2[] and ODDCOUNT[] , to find the value of P. Once we have these arrays, each query can be answered in constant time.

## TESTER’S SOLUTION

Can be found [here](http://www.codechef.com/download/Solutions/COOK23/Tester/OLYMPIC.cpp)

## APPROACH

(needs further improvement)

Here we describe the method for counting palindromic strings P and finding the value of T is similar.

Sort the queries at first, such that S[1](http://www.codechef.com/problems/OLYMPIC) < S[2](http://www.codechef.com/COOK23/problems/OLYMPIC) < … < S[Q].

Suppose, at first S = 1, and it is increasing.

Let

SUM = sum of count[i]/2 (integer division)

ODD = the number of odd elements of count

FACT = SUM! / (count[1]/2)! / (count[2]/2)! / … / (count[N]/2)! be precalculated.

Then, the answer for S = 1 is FACT if ODD ? 1, 0 if ODD ? 2.

Let k = ceil(count[i] / j), then when S goes from k-1 to k, the number of boxes corresponding to count[i] will go from j+1 to j.

Precalculate all time of decreasing the number of box, and sort this array.

After that, all we just need to simulate as follows.

When count[i] decreases,

if(count[i] is even)

{

FACT will be multiplied inverse_of(SUM) * count[i]

SUM will be SUM-1

ODD will be ODD+1

count[i] will be count[i]-1

}

else

{

ODD will be ODD-1

count[i] will be count[i]-1

}

-

*We will try to explain the tester’s approach with more clarity soon. Feel free to add your own approach till then*

</details>
