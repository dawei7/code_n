# Chef, Chefina and Their Friendship

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CHEFSHIP |
| Difficulty Rating | 1894 |
| Difficulty Band | 1800 to 2000 difficulty problems |
| Path | Become 5 star |
| Lesson | 1800 to 1900 difficulty problems |
| Official Link | [CHEFSHIP](https://www.codechef.com/practice/course/4-star-difficulty-problems/DIFF1900/problems/CHEFSHIP) |

---

## Problem Statement

In Chefland, each person has their own non-empty personal string. When two people with personal strings $T_1$ and $T_2$ (possibly identical) become friends in Chefland, their strings are replaced by a new string $S = T_1 + T_1 + T_2 + T_2$, where $+$ denotes string concatenation.

Chef recently became friends with Chefina. However, Chefina's personal string was her favourite and she got upset when it was replaced by $S$. She wanted her personal string back. Chef does not remember $T_1$ and $T_2$ now, he only knows $S$.

Find the number of ways in which Chef can retrieve valid strings $T_1$ and $T_2$ from the given string $S$. It is also possible that Chef does not remember $S$ correctly, in which case there is no way to retrieve $T_1$ and $T_2$.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains a single string $S$.

### Output
For each test case, print a single line containing one integer ― the number of ways to retrieve $T_1$ and $T_2$ from $S$.

### Constraints
- $1 \le T \le 10^4$
- $4 \le |S| \le 10^5$
- $|S|$ is divisible by $2$
- $S$ contains only lowercase English letters
- the sum of $|S|$ over all test cases does not exceed $2 \cdot 10^6$

---

## Examples

**Example 1**

**Input**

```text
3
abcd
aaaa
ababcdccdc
```

**Output**

```text
0
1
1
```

**Explanation**

**Example case 1:** There is no way to choose $T_1$ and $T_2$.

**Example case 2:** Both $T_1$ and $T_2$ must be "a".

**Separated test cases**

#### Test case 1

**Input for this case**

```text
abcd
```

**Output for this case**

```text
0
```



#### Test case 2

**Input for this case**

```text
aaaa
```

**Output for this case**

```text
1
```



#### Test case 3

**Input for this case**

```text
ababcdccdc
```

**Output for this case**

```text
1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](https://www.codechef.com/problems/CHEFSHIP)

[Contest](https://www.codechef.com/COOK118A/problems/CHEFSHIP)

**Author:** [Ritesh Gupta](https://www.codechef.com/users/rishup_nitdgp)

**Tester:** [Raja Vardhan Reddy](https://www.codechef.com/users/raja1999)

**Editorialist:** [Akash Bhalotia](https://www.codechef.com/users/akashbhalotia)

### DIFFICULTY:

Easy

### PREREQUISITES:

[String-Matching](https://en.wikipedia.org/wiki/String-searching_algorithm), [Hashing](https://cp-algorithms.com/string/string-hashing.html), [Prefix Function](https://cp-algorithms.com/string/prefix-function.html).

### PROBLEM:

Given a string S, find the number of ways to retrieve some strings T_1 and T_2 from it, such that S=T_1+T_1+T_2+T_2, where + denotes string concatenation.

### HINTS:

Not the full solution. Just some hints to help you if you are stuck at some point. As soon as you encounter a hint that you had not thought of, try solving the problem on your own.

Hint 1:

Try learning a string-matching algorithm, which can compare strings fast, such as [hashing](https://cp-algorithms.com/string/string-hashing.html) or [kmp](https://cp-algorithms.com/string/prefix-function.html).

Now that you can compare parts of a string fast, can you solve the problem?

Hint 2:

We need to find all T_1 and T_2 such that S=T_1+T_1+T_2+T_2.

T_1+T_1=2*T_1, and T_2+T_2=2*T_2.

Both 2T_1 and 2T_2 are of even lengths.

Iterate over all the even indices, and partition the array as follows:

P_1: [0,\frac{i}{2}-1]

P_2: [\frac{i}{2},i-1]

P_3: [i,\frac{i+N}{2}-1], and

P_4: [\frac{i+N}{2},N-1]

and check if P_1=P_2 and P_3=P_4, using any efficient string matching algorithm.

### QUICK EXPLANATION:

show

Iterate over all the even indices and divide the string into two parts. The first part will be further divided into parts P_1 and P_2 of equal length, while the second part into P_3 and P_4, again, of equal length. If P_1=P_2 and P_3=P_4, increment the count. Checking for equality can be done using any popular string-matching algorithm like [kmp](https://cp-algorithms.com/string/prefix-function.html) or [hashing](https://cp-algorithms.com/string/string-hashing.html).

### EXPLANATION

show

We need to find the number of ways in which S can be represented as a combination of some T_1 and T_2 such that S=T_1+T_1+T_2+T_2.

To do this, we can **divide S into four parts P_1, P_2, P_3 and P_4** such that S=P_1+P_2+P_3+P_4 and check whether P_1 equals P_2 and P_3 equals P_4 (equal means same in length and in characters).

As an example, consider the string: aaaabaaaabaa (0 -indexed ).

There are two ways to partition it into P_1,P_2,P_3,P_4 such that P_1=P_2 and P_3=P_4.

We can choose P_1 to be [0,0], P_2 to be [1,1], P_3 to be [2,6] and then P_4 will be [7,11].

The second way is to choose P_1 to be [0,4] P_2 to be [5,9], P_3 to be [10,10] and then P_4 will be [11,11].

Since P_1 and P_2 need to be checked for equality, P_1 and P_2 should be of the same length, thus, **P_1+P_2 will have an even length**. As |S| is divisible by 2 (see problem constraints), the remaining part **P_3+P_4 will also have an even length.**

Thus, we can **iterate over all even positions** in the string  and check if they partition the string into four parts, such that the first and the seconds parts are equal, and the third and the fourth parts are equal. Keep in mind that all parts must be of positive length ( i.e. \gt 0).

To check for equality fast, we can use any popular **string matching technique**, like [hashing](https://cp-algorithms.com/string/string-hashing.html), [prefix-function](https://cp-algorithms.com/string/prefix-function.html), [z-function](https://cp-algorithms.com/string/z-function.html), etc.

I have used [hashing](https://cp-algorithms.com/string/string-hashing.html) in my implementation, as it makes solving this problem pretty straightforward.

When we receive the string, we create its [rolling-hash array](https://cp-algorithms.com/string/string-hashing.html), which enables us to get the hash value of any substring in constant time. We iterate over all the even positions such that the resulting partitions are of positive length. If the string is 0 -indexed, the parts will be as follows:

P_1: [0,\frac{i}{2}-1]

P_2: [\frac{i}{2},i-1]

P_3: [i,\frac{i+N}{2}-1], and

P_4: [\frac{i+N}{2},N-1]

Note that division here implies integer division, or taking the floor value of the division result.

When we know the end-points of the parts, we can get their hashes from the hash-array in constant time, and check P_1 and P_2, P_3 and P_4, respectively, for equality.

If P_1=P_2 and P_3=P_4, we increment the count. Then we go on to check the next even index for the next probable partition of the string, into T_1+T_1+T_2+T_2.

Thus, to solve the problem:

- Create the [rolling-hash](https://cp-algorithms.com/string/string-hashing.html) array of the string.

- Iterate over all the even indices in range [2,N-2] and check if the resulting partition P_1=P_2 and P_3=P_4, using the hash-array.

- For every successful partition that satisfies the condition, increment the count.

The setter has used the [prefix-function](https://cp-algorithms.com/string/prefix-function.html) technique, while the tester has used the [z-function](https://cp-algorithms.com/string/z-function.html) to solve this problem.

The logic for both of these is same: compute the function for the string as well as its reverse, divide it into parts as described above, and use the two functions to check for equality of the parts. The function from the original string is used to check if P_1=P_2, while the function from the reverse string is used to check if P_3=P_4.

### TIME COMPLEXITY:

show

The time complexity is: O(N) per test case,

where N is the length of the string.

**Why?**

Computing the rolling hash array of a string takes O(N) time. Then we iterate over all the even indices in O(N) time, while checking the parts for equality in constant time.

### SOLUTIONS:

Setter
``#include <bits/stdc++.h>

using namespace std;

// char input[] = "input/input00.txt";
// char output[] = "output.txt";

const int N = 200010;

int a[N],lps1[2][N],lps2[2][N];
string s;

void computeLPSArray1(int key)
{
	int len = 0;
	lps1[key][0] = 0;
	int i = 1;

	while(i < s.size())
	{
	    if(s[i] == s[len])
	    {
	        len++;
			lps1[key][i] = len;
	        i++;
	    }
	    else
	    {
	        if(len != 0)
	            len = lps1[key][len - 1];
	        else
	        {
	            lps1[key][i] = 0;
	            i++;
	        }
	    }
	}
}

void computeLPSArray2(int key)
{
	int len = 0;
	lps2[key][0] = 0;
	int i = 1;

	while(i < s.size())
	{
	    if(s[i] == s[len])
	    {
	        len++;

	        if(2*len > i+1)
	        	len = lps1[key][len - 1];

			lps2[key][i] = len;
	        i++;
	    }
	    else
	    {
	        if(len != 0)
	            len = lps1[key][len - 1];
	        else
	        {
	            lps2[key][i] = 0;
	            i++;
	        }
	    }
	}
}

int main()
{
	// freopen(input, "r", stdin);
	// freopen(output, "w", stdout);

	int t;
	cin >> t;

	while(t--)
	{
		cin >> s;

		int n = s.size();

		for(int i=0;i<n;i++)
			lps1[0][i] = lps1[1][i] = lps2[0][i] = lps2[1][i] = 0;

		computeLPSArray1(0);
		computeLPSArray2(0);
		reverse(s.begin(),s.end());
		computeLPSArray1(1);
		computeLPSArray2(1);

		int ans = 0;

		for(int i=1;i<n-2;i+=2)
		{
			if((2*lps2[0][i] == (i+1)) && (2*lps2[1][n-i-2] == (n-i-1)))
				ans++;
		}

		cout << ans << endl;
	}

	return 0;
}
``

Tester
``//raja1999

//#pragma comment(linker, "/stack:200000000")
//#pragma GCC optimize("Ofast")
//#pragma GCC target("sse,sse2,sse3,ssse3,sse4,avx,avx2")

#include <bits/stdc++.h>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <climits>
#include <utility>
#include <algorithm>
#include <cmath>
#include <queue>
#include <stack>
#include <iomanip>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
//setbase - cout << setbase (16)a; cout << 100 << endl; Prints 64
//setfill -   cout << setfill ('x') << setw (5); cout << 77 <<endl;prints xxx77
//setprecision - cout << setprecision (14) << f << endl; Prints x.xxxx
//cout.precision(x)  cout<<fixed<<val;  // prints x digits after decimal in val

using namespace std;
using namespace __gnu_pbds;
#define f(i,a,b) for(i=a;i<b;i++)
#define rep(i,n) f(i,0,n)
#define fd(i,a,b) for(i=a;i>=b;i--)
#define pb push_back
#define mp make_pair
#define vi vector< int >
#define vl vector< ll >
#define ss second
#define ff first
#define ll long long
#define pii pair< int,int >
#define pll pair< ll,ll >
#define sz(a) a.size()
#define inf (1000*1000*1000+5)
#define all(a) a.begin(),a.end()
#define tri pair<int,pii>
#define vii vector<pii>
#define vll vector<pll>
#define viii vector<tri>
#define mod (1000*1000*1000+7)
#define pqueue priority_queue< int >
#define pdqueue priority_queue< int,vi ,greater< int > >
#define int ll

typedef tree<
int,
null_type,
less<int>,
rb_tree_tag,
tree_order_statistics_node_update>
ordered_set;

//std::ios::sync_with_stdio(false);
int z[200005][2];
int solve(string s,int fl){
	int n=s.length();
	int l,r,k,i;
	l=0;
	r=0;
	f(i,1,n){
		if(i>r){
			l=i;
			r=i;
			while(r<n && s[r-l]==s[r]){
				r++;
			}
			z[i][fl]=r-l;
			r--;
		}
		else{
			k=i-l;
			if(z[k][fl]<r-i+1){
				z[i][fl]=z[k][fl];
			}
			else{
				l=i;
				while(r<n && s[r-l]==s[r]){
					r++;
				}
				z[i][fl]=r-l;
				r--;
			}
		}
	}
}
main(){
	std::ios::sync_with_stdio(false); cin.tie(NULL);
	int t;
	cin>>t;
	while(t--){
		string s;
		int ans=0,i,j;
		cin>>s;
		int n=s.length();
		string rev_s="";
		fd(i,s.length()-1,0){
			rev_s+=s[i];
		}
		solve(s,0);
		solve(rev_s,1);
		for(i=1;i<s.length();i+=2){
			j = n-i-2;
			if(j<0){
				break;
			}
			//cout<<
			if(z[i/2+1][0]>=(i+1)/2 && z[j/2+1][1]>=(j+1)/2){
				ans++;
			}
		}
		cout<<ans<<endl;
	}
	return 0;
}
``

Editorialist
``//created by Whiplash99
import java.io.*;
import java.util.*;
class A
{
	static class Hashing
	{
	    long[] hash,pow;
	    long P, MOD;
	    int N;

	    Hashing(char str[], long P, long MOD)
	    {
	        this.N=str.length;this.P=P;this.MOD=MOD;
	        hash=new long[N+1];pow=new long[N+1];
	        init(str);
	    }
	    void init(char str[])
	    {
	        pow[0]=1;
	        for(int i=N-1;i>=0;i--)
	        {
	            hash[i]=((hash[i+1]*P)%MOD+(str[i]-'a'+1))%MOD;
	            pow[N-i]=(pow[N-i-1]*P)%MOD;
	        }
	        pow[N]=(pow[N-1]*P)%MOD;
	    }
	    long getHash(){return getHash(0,N-1);}
	    long getHash(int l, int r){return (MOD-(hash[r+1]*pow[r-l+1])%MOD+hash[l])%MOD;}
	}
	public static void main(String[] args) throws IOException
	{
	    BufferedReader br=new BufferedReader(new InputStreamReader(System.in));

	    int i,N;

	    int T=Integer.parseInt(br.readLine().trim());
	    StringBuilder sb=new StringBuilder();

	    while(T-->0)
	    {
	        char str[]=br.readLine().trim().toCharArray();
	        Hashing hash=new Hashing(str,31,(int)(1e9+7)); //compute rolling-hash

	        int count=0; N=str.length;
	        for(i=2;i<=N-2;i+=2)
	        {
	            int l1=0,r1=i/2-1; //Part-1
	            int l2=r1+1,r2=i-1; //Part-2
	            int l3=i,r3=(i+N)/2-1; //Part-3
	            int l4=r3+1,r4=N-1; //Part-4

	            //Check if Part-1=Part2 and if Part-3=Part-4
	            boolean C1=hash.getHash(l1,r1)==hash.getHash(l2,r2);
	            boolean C2=hash.getHash(l3,r3)==hash.getHash(l4,r4);

	            if(C1&&C2) count++;
	        }
	        sb.append(count).append("\n");
	    }
	    System.out.println(sb);
	}
}
``

Feel free to share your approach if it differs. **You can ask your doubts below. Please let me know if something’s unclear.** I would LOVE to hear suggestions

</details>
