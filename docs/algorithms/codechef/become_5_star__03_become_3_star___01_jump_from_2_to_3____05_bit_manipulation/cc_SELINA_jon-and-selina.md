# Jon and Selina

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SELINA |
| Difficulty Band | Jump from 2* to 3* |
| Path | Become 5 star |
| Lesson | Bit Manipulation |
| Official Link | [SELINA](https://www.codechef.com/practice/course/2to3stars/LP2TO305/problems/SELINA) |

---

## Problem Statement

Selina is Jon’s girlfriend.  They had planned to go for a date this evening, but Jon is stuck with a problem at work.

He has a string $S$ of length $N$, containing all lower case alphabets. The string contains a odd occurring character (characters that is present odd times). The task is to find the character (if not present print $-1$). Jon is already late for his date, so help him solve this as quickly as possible.

---

## Input Format

- First line will contain $T$, number of testcases. Then the testcases follow.
- Each testcase contains of a single line of input, one string $S$.

---

## Output Format

- Print the character.
- If no such character is present, print $-1$.

---

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 1000$
- sum of $N$ over all test cases doesn't exceed $10^6$

---

## Examples

**Example 1**

**Input**

```text
3
abcbacc
abcba
abccba
```

**Output**

```text
c
c
-1
```

**Explanation**

**Case 1:** $c$ is occurred $3$ times i.e odd number of times.

**Case 2:** $c$ is occurring only $1$ time.

**Case 3:** no odd occurring character is present, printed $-1$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
abcbacc
```

**Output for this case**

```text
c
```



#### Test case 2

**Input for this case**

```text
abcba
```

**Output for this case**

```text
c
```



#### Test case 3

**Input for this case**

```text
abccba
```

**Output for this case**

```text
-1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest](https://www.codechef.com/FRM12021/problems/SELINA)

**Setter:** [ sayan_kashyapi ](https://www.codechef.com/users/sayan_kashyapi)

**Tester:** [ mishra_roshan ](https://www.codechef.com/users/mishra_roshan)

**Editorialist:** [ ritik0602 ](https://www.codechef.com/users/ritik0602)

#
[](#difficulty-2)DIFFICULTY:

Cakewalk

#
[](#prerequisites-3)PREREQUISITES:

Counting frequency of elements, Bitwise XOR

#
[](#problem-4)PROBLEM:

Given a string S made up of lower case english alphabets of length N, find if an odd occuring alphabet is present or not.

#
[](#explanation-5)EXPLANATION

As the string consists of only lower case english alphabets, we can maintain a frequency array of size 26 and if the frequency of an element is odd print that letter and if none such exist print -1

Bitwise Solution:

As there is atmost one odd occuring element, taking the xor of all elements finally results in the odd occuring element (if any) or 0 if that is not present.

#
[](#time-complexity-6)TIME COMPLEXITY

Time complexity is O(N) for traversing the string.

#
[](#solutions-7)SOLUTIONS:

Setter's Solution

C++
``#include<bits/stdc++.h>
using namespace std;
int main()
{
	long long int t;
	cin >> t;
	while (t--)
	{
		string str;
		cin >> str;
		long long int x = 0;
		for (int i = 0; i < str.length(); i++)
			x ^= int(str[i]);
		if (!x)
		{
			cout << -1 << endl;
			continue;
		}
		else
		    cout<<char(x)<<endl;
	}
	return 0;
}
``

Tester's Solution

Java
``import java.util.*;
 class Dcoder
 {
   public static void main(String args[])
   {
    Scanner  sc=new Scanner(System.in);
    int t=sc.nextInt();
    while(t-->0){

      String s=sc.next();
      int[] h=new int[26];
      for(int i=0;i<s.length();i++)
        h[s.charAt(i)-97]++;
      int  ans=-1;
      for(int i=0;i<26;i++){
        if(h[i]%2!=0){
          ans=i;
          break;
        }
      }
      if(ans==-1)
        System.out.println("-1");
      else
         System.out.println((char)(ans+97));

      }
    }
 }

``

Feel free to Share your approach.

Suggestions are welcomed as always had been.

</details>
