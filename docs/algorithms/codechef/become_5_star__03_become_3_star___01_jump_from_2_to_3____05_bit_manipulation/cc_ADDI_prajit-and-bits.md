# Prajit and bits

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | ADDI |
| Difficulty Band | Jump from 2* to 3* |
| Path | Become 5 star |
| Lesson | Bit Manipulation |
| Official Link | [ADDI](https://www.codechef.com/practice/course/2to3stars/LP2TO305/problems/ADDI) |

---

## Problem Statement

Prajit was trying to solve a tricky problem .As we all know he is a noob he failed to solve that and he gave up for the day.He left the problem and went to sleep.Can you solve it?

 There is a number $N$.We need to find total unset bits of that number.
### Input:
First line contains $T$,Test cases.

Second line contains a single integer $N$ .

### Output:
Print a single integer.

### Constraints:
- $1\leq T \leq 1000$
- $1\leq N \leq 10^{18}$

---

## Examples

**Example 1**

**Input**

```text
2
10
1
```

**Output**

```text
2
0
```

**Separated test cases**

#### Test case 1

**Input for this case**

```text
10
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
1
```

**Output for this case**

```text
0
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Practice](https://www.codechef.com/problems/ADDI)

[Contest](https://www.codechef.com/ENAU2019/problems/ADDI)

**Author:** [Praji Benerjee](https://www.codechef.com/users/coldnights1)

**Tester:** [Md Shahid](https://www.codechef.com/users/dshahid380_)

**Editorialist:** [Md Shahid](https://www.codechef.com/users/dshahid380_)

# DIFFICULTY:

Cakewalk

# PREREQUISITES:

Bits

# PROBLEM:

Given any positive number N and you need to find total number of unset bits

# EXPLANATION:

This problem is very easy. First of all convert the number N into string of binary numbers( 0 or 1). Now count the number of zeros from binary form. For example, you have number N=10, binary form of this number will be S="1010", now count number of zeros i.e, 2 so answer will be 2.

## Time Complexity :

Converting a decimal number into binary takes O(logN) time.

# SOLUTIONS:

Author's Solution
``#include<bits/stdc++.h>
#define int long long int
#define fast ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
using namespace std;

signed main(){
    fast
    int t ;cin>>t;
    while(t--){
        int n; cin>>n;
        int ans=__builtin_popcount(n);
        int total=(int)log2(n)+1;
        int nigga=total-ans;
        cout<<nigga<<endl;
    }
    return 0;
}
``

Tester & Editorialist Solution
``for _ in range(int(input())):
	N = int(input())
	b = bin(N)
	print(b.count('0')-1)
``

All the suggestions are welcome.

</details>
