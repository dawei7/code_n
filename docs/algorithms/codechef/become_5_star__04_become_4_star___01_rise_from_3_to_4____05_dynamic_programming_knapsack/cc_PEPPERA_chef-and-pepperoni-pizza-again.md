# Chef and Pepperoni Pizza Again

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PEPPERA |
| Difficulty Rating | 2516 |
| Difficulty Band | Rise from 3* to 4* |
| Path | Become 5 star |
| Lesson | Dynamic Programming - Knapsack |
| Official Link | [PEPPERA](https://www.codechef.com/practice/course/3to4stars/LP3TO405/problems/PEPPERA) |

---

## Problem Statement

Chef is fond of pepperoni pizza, as we saw [here](https://www.codechef.com/problems/PEPPERON). Once again, he has a pepperoni pizza in the shape of a grid with $N$ rows (numbered $1$ through $N$ from top to bottom) and $N$ columns (numbered $1$ through $N$ from left to right). Some cells of this grid contain pepperoni, while other ones do not.

Chef wants to cut the pizza vertically in half and give the two halves to two of his friends. Formally, one friend should get everything in columns $1$ through $N/2$ and the other friend should get everything in the columns $N/2+1$ through $N$.

Before cutting the pizza, Chef may perform the following operation any number of times (including zero): choose an integer $x$ ($1 \le x \le N$) and reverse the $x$-th row of the grid ― in other words, for each valid $i$, the cell in the $i$-th column and $x$-th row is moved to the $N+1-i$-th column in the same row.

After the pizza is cut, let's denote the number of cells containing pepperoni in the first half and in the second half by $p_1$ and $p_2$ respectively. Chef wants to minimise their absolute difference $|p_1-p_2|$, but he is lazy, so he just wants you to perform any valid sequence of operations such that the absolute difference in the final grid is minimized.

You need to find a final grid (the grid after performing all operations) such that $|p_1 - p_2|$ for this grid is the smallest possible. If there are multiple final grids that minimise $|p_1 - p_2|$, you may find any one.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains a single integer $N$.
- $N$ lines follow. For each $i$ ($1 \le i \le N$), the $i$-th of these lines contains a string with length $N$ describing the $i$-th row of the grid; for each valid $j$, the $j$-th character of this string is '1' if the cell in the $i$-th row and $j$-th column contains pepperoni or '0' if it does not.

### Output
For each test case, print $N$ lines. For each valid $i$, the $i$-th of these lines should contain a string with length $N$ describing the $i$-th row of the grid after performing all operations, in the same format as on the input. It must be possible to obtain this grid from the initial grid using some valid sequence of operations.

### Constraints
- $1 \le T \le 30$
- $2 \le N \le 150$
- $N$ is even
- the sum of $N$ over all test cases does not exceed $300$

---

## Examples

**Example 1**

**Input**

```text
2
2
01
01
4
0111
0001
1010
1010
```

**Output**

```text
10
01
1110
0001
1010
1010
```

**Explanation**

**Example case 1:** We need to reverse either of the rows, leading to $|p_1-p_2| = 0$. Either of these solutions would be accepted.

**Example case 2:** It is optimal to reverse the first row, leading to exactly $4$ pepperoni on each side (and $|p_1-p_2| = 0$ again).

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](https://www.codechef.com/problems/PEPPERA)

[Contest](https://www.codechef.com/COOK115A/problems/PEPPERA)

**Author:** [Taranpreet Singh](https://www.codechef.com/users/taran_1407)

**Tester:** [Raja Vardhan Reddy](https://www.codechef.com/users/raja1999)

**Editorialist:** [Akash Bhalotia](https://www.codechef.com/users/akashbhalotia)

### DIFFICULTY:

Easy-Medium

### PREREQUISITES:

[Knapsack problem](https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/), [Backtracking](https://www.geeksforgeeks.org/printing-items-01-knapsack/).

### PROBLEM:

Given an N *N matrix of numbers. You are allowed to reverse the elements of each row. Minimise the difference between the sums of the elements present in columns 1 to \frac{N}{2} and the ones present in columns (\frac{N}{2}+1) to N.

### HINTS:

Not the full solution. Just some hints to help you if you are stuck at some point. As soon as you encounter a hint that you had not thought of, go back to solving the problem.

Hint 1:

Try to solve the following problem:

Given an array of numbers, divide the array into two parts, such that each element belong to exactly one of the parts, and the difference between the sum of elements of each part is minimum possible.

Hint 2:

Read about the [knapsack problem.](https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/) Can you solve the problem now?

Hint 3:

The actual division of the elements can be obtained using [backtracking.](https://www.geeksforgeeks.org/printing-items-01-knapsack/)

Hint 4:

Once you know the division of the elements into halves of the matrix, reverse the rows suitably to put each element into the half it belongs to.

### QUICK EXPLANATION:

show

Store the difference between the left and right halves of each row into an array. Perform knapsack dp on in to partition the difference into two parts, such that the difference between their sums is minimum possible. Obtain the part each element now belongs to using backtracking, and reverse the rows suitably, based on the half an element belonged to originally, compared to the half it belongs to in the optimal division.

### EXPLANATION

show

Each half of a row has a certain number of pepperoni. It is the difference in the number of pepperoni in each half that causes one of the halves to have excess pepperoni, as compared to the other half. We want that the difference between the total number of pepperoni in each half of the pizza is minimum possible. We need to minimise the difference of the total excess received by each half, by choosing an optimal way to assign the excess to one of the halves in each row.

The problem can be reduced to the following:

Given an array of positive numbers, divide the elements into two parts, such that each element is assigned to exactly one of the parts, and the absolute difference between the sum of the elements of each part is minimum possible.

For example:

1,5,6,3

can be divided into two parts: (5,3), and (1,6).

The sum of their elements is: 8 and 7, and the difference of the sums is 1, which is the minimum possible that can be obtained for this sequence.

This can be solved using [dynamic programming.](https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/)

``// excess[i] = excess contributed by the i-th row. abs(leftCount[i]-rightCount[i])
//dp[x] = is it possible to obtain a sum of x using the elements we have?
//dp[x] = -2? It is not possible.
//dp[x]!= -2? It is possible and the dp[x] will store the index
//of the first array element which made it possible to obtain this sum.
//If it is possible to obtain a sum of x, then it is also possible to obtain
//a sum of x-excess[dp[x]], and the index of the first array element which made it possible to
//obtain a sum of x-excess[dp[x]] will be stored in dp[x-excess[dp[x]]].
//This way, we can backtrack and obtain the sequence of elements which will make up x.

fill(dp,-2); //initially, no sum can be obtained
dp[0]=-1; // a sum of 0 can be obtained by not choosing any elements

for(i=0;i<N;i++) //what are the sums that can be obtained using the first (i+1) elements?
{
	for(j=sum;j>=excess[i];j--)
	{
		//if it was not possible to obtain this sum, but now it is, store the index
		//of the element which made this sum possible.
		if(dp[j]==-2&&dp[sum-excess[i]]!=-2)
			dp[j]=i;
	}
}
``

Thus, dp[x] will store the index of the most recent element which made it possible to obtain a sum of x.

When we know the sums which are possible to be obtained using the elements, we shall try to divide the elements into two parts, whose sums is as close as possible to \frac{sum}{2} each. This way the absolute difference between the sums of the two parts will minimum possible.

``//what is the minimum possible difference that can be obtained?

leftSum=0;
for(i=sum/2;i>=0;i--)
{
	//is it possible to obtain a sum of i?
	//If it is possible, then one of the parts will have a sum i,
	//and the other part will have a sum of (sum-i).
	//Their difference will be minimum possible that can be obtained.

	if(dp[i]!=-2)
		break;
}
leftSum=i;
``

Once we know the sums of the two parts, which shall result in the minimum possible difference, we can find the elements which belong to each part using [backtracking](https://www.geeksforgeeks.org/printing-items-01-knapsack/). The sum for one of the parts will be stored in leftSum.

``//We can maintain an array which stores the half each element belongs to:
//left or right.

fill(part,2) //initially all belong to the right half.
while (leftSum>0)
{
	part[dp[leftSum]=1; //This element shall now belong to the left half.
	leftSum-=excess[dp[leftSum]];
}
``

After we know which half the excess of each row belongs to, we shall reverse a row if the excess of that row belongs to a different half in the solution, than it originally was in.

### TIME COMPLEXITY:

show

The time complexity is: **O(N^3)**

**Why?**

The knapsack dp takes N*Sum operations, where Sum is the sum of all the elements in the matrix. But, the matrix only consists of 0's and 1's, so, in the worst case, Sum=N*N. Thus, the time complexity is O(N^3).

### SOLUTIONS:

Setter
``import java.util.*;
import java.io.*;

class Main{
	public static void main(String[] args) throws Exception{
	    Scanner in = new Scanner(System.in);
	    PrintWriter out = new PrintWriter(System.out);
	    for(int tc = 1, tt = in.nextInt(); tc <= tt; tc++){
	        int n = in.nextInt();
	        int[] val = new int[n];
	        String[] s = new String[n];
	        for(int i = 0; i< n; i++){
	            s[i] = in.next();
	            for(int j = 0; j< n; j++)if(s[i].charAt(j) == '1')val[i] += (j >= n/2)?1:-1;
	        }
	        int sum = 0;
	        boolean[] rev = new boolean[n];
	        for(int i = 0; i< n; i++){
	            if(val[i] < 0){
	                rev[i] ^= true;
	                val[i] = -val[i];
	            }
	            sum += val[i];
	        }
	        int[] dp = new int[1+sum];
	        Arrays.fill(dp, -2);
	        dp[0] = -1;
	        for(int i = 0; i< n; i++){
	            if(val[i] == 0)continue;
	            for(int j = sum; j >= val[i]; j--){
	                if(dp[j] == -2 && dp[j-val[i]] != -2)
	                    dp[j] = i;
	            }
	        }
	        int min = sum, p = 0;
	        for(int i = 0; i<= sum; i++){
	            if(dp[i] != -2 && min > Math.abs(i-(sum-i))){
	                min = Math.abs(i-(sum-i));
	                p = i;
	            }
	        }
	        while(p > 0){
	            rev[dp[p]] ^= true;
	            p -= val[dp[p]];
	        }
	        for(int i = 0; i< n; i++){
	            if(rev[i])out.println(new StringBuilder(s[i]).reverse().toString());
	            else out.println(s[i]);
	        }
	    }
	    out.flush();
	    out.close();
	}
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
//#define int ll

typedef tree<
int,
null_type,
less<int>,
rb_tree_tag,
tree_order_statistics_node_update>
ordered_set;

//std::ios::sync_with_stdio(false);

int vis[155][6005][2],dp[155][6005][2],nxt[155][6005][2];
int arr[155];
string s[155];
int n,iter=0;
main(){
	std::ios::sync_with_stdio(false); cin.tie(NULL);
	int t;
	cin>>t;
	//t=1;
	while(t--){
		int i,j,c=0,sum,pos,fl,fl1,lim;
		cin>>n;
		iter++;
		for(i=0;i<n;i++){
			cin>>s[i];
		}
		for(i=0;i<n;i++){
			c=0;
			for(j=0;j<n/2;j++){
				c+=(s[i][j]-'0');
			}
			for(j=n/2;j<n;j++){
				c-=(s[i][j]-'0');
			}
			arr[i]=c;
		}
		lim=6000;
		f(i,-1*lim,lim){
			fl=0;
			if(i<0){
				fl=1;
			}
			dp[n][abs(i)][fl]=abs(i);
		}
		fd(i,n-1,0){
			f(j,-1*lim,lim){
				fl=0;
				if(j<0){
					fl=1;
				}
				dp[i][abs(j)][fl]=inf;
				if(j+arr[i]<lim&&j+arr[i]>=-1*lim){
					fl1=0;
					if(j+arr[i]<0){
						fl1=1;
					}
					dp[i][abs(j)][fl]=min(dp[i][abs(j)][fl],dp[i+1][abs(j+arr[i])][fl1]);
					nxt[i][abs(j)][fl]=1;
				}
				if(j-arr[i]<lim&&j-arr[i]>=-1*lim){
					fl1=0;
					if(j-arr[i]<0){
						fl1=1;
					}
					dp[i][abs(j)][fl]=min(dp[i][abs(j)][fl],dp[i+1][abs(j-arr[i])][fl1]);
					if(dp[i][abs(j)][fl]==dp[i+1][abs(j-arr[i])][fl1]){
						nxt[i][abs(j)][fl]=-1;
					}
				}

			}
		}
		sum=0;
		pos=0;
		while(pos!=n){
			fl=0;
			if(sum<0){
				fl=1;
			}
			if(nxt[pos][abs(sum)][fl]==1){
				cout<<s[pos]<<endl;
				sum+=arr[pos];
			}
			else{
				sum-=arr[pos];
				reverse(s[pos].begin(),s[pos].end());
				cout<<s[pos]<<endl;
			}
			pos++;
		}
	}
	return 0;
}
``

Editorialist

[https://www.codechef.com/viewsolution/29952060](https://www.codechef.com/viewsolution/29952060)

``//created by Whiplash99
import java.io.*;
import java.util.*;
class A
{
	public static void main(String[] args) throws IOException
	{
	    BufferedReader br=new BufferedReader(new InputStreamReader(System.in));

	    int i,N;

	    int T=Integer.parseInt(br.readLine().trim());
	    StringBuilder sb=new StringBuilder();

	    while(T-->0)
	    {
	        N=Integer.parseInt(br.readLine().trim());
	        char str[][]=new char[N][N];

	        for(i=0;i<N;i++)
	            str[i]=br.readLine().trim().toCharArray();

	        boolean rev[]=new boolean[N]; //should we reverse this row?
	        int excess[]=new int[N]; //absolute difference of the left and right halves of each row
	        int sum=0;

	        for(i=0;i<N;i++)
	        {
	            for(int j=0;j<N;j++)
	                excess[i]+=(j<N/2)?(str[i][j]-'0'):-(str[i][j]-'0');

	            //If diff<0, reverse it. Basically, let the excess be in the right part.
	            if(excess[i]<0)
	            {
	                rev[i]=true;
	                excess[i]=-excess[i];
	            }
	            sum+=excess[i];
	        }

	        //dp[x] = Is it possible to obtain a sum of x using the elements we have?
	        // -2: No, it's not possible
	        // Others: Yes, it is possible. dp[x] will store the index of the
	        //most recent array element that made it possible to obtain a sum of x.
	        //This way, we can find the index of the element that made a sum of x-excess[dp[x]] possible, and
	        // using that, the elements that made the previous sums possible

	        int dp[]=new int[sum+5];
	        Arrays.fill(dp,-2);
	        dp[0]=-1;

	        for(i=0;i<N;i++)
	        {
	            for(int j=sum;j>=excess[i];j--)
	            {
	                if(dp[j]==-2&&dp[j-excess[i]]!=-2)
	                    dp[j]=i;
	            }
	        }

	        int leftSum=0;
	        for(i=sum/2;i>=0;i--)
	        {
	            if(dp[i]!=-2)
	            {
	                leftSum=i;
	                break;
	            }
	        }

	        //The excess that make up the answer will be put on the left side, and
	        // the others will be kept on the right side.
	        // ^true: put this excess on the left side, if it's on the right side.
	        // If it's already on the left side, leave it as it is.
	        while (leftSum>0)
	        {
	            rev[dp[leftSum]]^=true;
	            leftSum-=excess[dp[leftSum]];
	        }

	        for(i=0;i<N;i++)
	        {
	            if(rev[i])
	                for(int j=N-1;j>=0;j--) sb.append(str[i][j]);
	            else
	                for(int j=0;j<N;j++) sb.append(str[i][j]);
	             sb.append("\n");
	        }
	    }
	    System.out.println(sb);
	}
}
``

Feel free to share your approach if it differs. **You can ask your doubts below. Please let me know if something’s unclear.** I would LOVE to hear suggestions

</details>
