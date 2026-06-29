# Marbles

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MARBLES |
| Difficulty Rating | 925 |
| Difficulty Band | Combinatorics |
| Path | Data Structures and Algorithms |
| Lesson | Conceptual Problems |
| Official Link | [MARBLES](https://www.codechef.com/learn/course/combinatorics/COMBI05/problems/MARBLES) |

---

## Problem Statement

Rohit dreams he is in a shop with an infinite amount of marbles. He is allowed to select $n$ marbles. \
There are marbles of $k$ different colors. From each color there are also infinitely many marbles. \
Rohit wants to have at least one marble of each color, but still there are a lot of possibilities for his selection. In his effort to make a decision he wakes up. \
Now he asks you how many possibilities for his selection he would have had. \
Assume that marbles of equal color can't be distinguished, and the order of the marbles is irrelevant.

---

## Input Format

The first line of input contains a number T <= 100 that indicates the number of test cases to follow. \
Each test case consists of one line containing $n$ and $k$, where $n$ is the number of marbles Rohit selects and $k$ is the number of different colors of the marbles.

---

## Output Format

For each test case print the number of possibilities that Rohit would have had.
You can assume that this number fits into a signed 64 bit integer.

---

## Constraints

- 1<=k<=n<=1000000

---

## Examples

**Example 1**

**Input**

```text
2
10 10
30 7
```

**Output**

```text
1
475020
```

**Separated test cases**

#### Test case 1

**Input for this case**

```text
10 10
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
30 7
```

**Output for this case**

```text
475020
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

**Explanation**

We think this question as, we put some border lines to marbles as we group them with their colors, so we create k marble group (so we need k-1 lines).

So this question will be a permutation question. We can first pick k marbles and then we need to pick n-k marbles + (k-1) border lines. So we need to order total n-1 pieces, k-1 of them and n-k of them are equal each other.

So we must calculate (n-1)! / ((k-1)!*(n-k)!) which is equal to C(n-1,k-1) which is combination.

C++ Solution

``#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;

	for(int i=1;i<=t;i++){
	    long long int n,k;
	    cin>>n>>k;

	    long long int sum =1;

	    for(long long int i=1;i<k;i++)
	    {
	        sum = sum*((n-k)+i)/i;
	    }
	    cout<<sum<<endl;
	}
	return 0;
}
``

**Python Solution**

``import math
# cook your dish here
t = int(input())
while t>0:
    n,k = map(int,input().split())
    print(math.comb(n-1,k-1))
    t -= 1
``

**Java Solution**

``/* package codechef; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class Codechef
{
	public static void main (String[] args) throws java.lang.Exception
	{
		// your code goes here
		Scanner s=new Scanner(System.in);
		int t=s.nextInt();
		while(t-->0)
		{
		    int n=s.nextInt();
		    int k=s.nextInt();
		    long a=1;
		    for(long i=1;i<k;i++)
		    {
		        a=a*((n-k)+i)/i;
		    }
		    System.out.println(a);
		}
	}
}
``

</details>
