# Binary String on Steroids

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | BNSONSTR |
| Difficulty Rating | 1930 |
| Difficulty Band | 1800 to 2000 difficulty problems |
| Path | Become 5 star |
| Lesson | 1900 to 2000 difficulty problems |
| Official Link | [BNSONSTR](https://www.codechef.com/practice/course/4-star-difficulty-problems/DIFF2000/problems/BNSONSTR) |

---

## Problem Statement

A circular binary string is called *good* if it contains at least one character '1' and there is an integer $d$ such that for each character '1', the distance to the nearest character '1' clockwise is $d$.

You are given a circular binary string $S$ with length $N$. You may choose some characters in this string and flip them (i.e. change '1' to '0' or vice versa). Convert the given string into a good string by flipping the smallest possible number of characters.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains a single integer $N$.
- The second line contains a single string $S$ with length $N$.

### Output
Print a single line containing one integer ― the minimum number of flips required to transform the initial string into a good string.

### Constraints
- $1 \leq T \leq 100$
- $1 \leq N \leq 5 \cdot 10^5$
- $S$ contains only characters '0' and '1'
- the sum of $N$ over all test cases does not exceed $5 \cdot 10^5$

---

## Examples

**Example 1**

**Input**

```text
2
6
110011
4
0001
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
6
110011
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
4
0001
```

**Output for this case**

```text
0
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/COOK130A/problems/BNSONSTR)

[Contest Division 2](https://www.codechef.com/COOK130B/problems/BNSONSTR)

[Contest Division 3](https://www.codechef.com/COOK130C/problems/BNSONSTR)

[Practice](https://www.codechef.com/problems/BNSONSTR)

**Setter:** [Prasant Kumar](https://www.codechef.com/users/prasant21)

**Tester & Editorialist:** [Taranpreet Singh](https://www.codechef.com/users/taran_1407)

# DIFFICULTY

Easy

# PREREQUISITES

None

# PROBLEM

Given a circular binary string s of length N, where you can perform operations on this string, flipping character from ‘0’ to ‘1’ and vice versa.

Determine the minimum number of operations needed to obtain a good string, where a circular string is good when it contains at least one occurrence of ‘1’ and for each ‘1’, distance to next ‘1’ is the same.

# QUICK EXPLANATION

- The distance between '1’s can only be a factor of N.Try all factors of N as distance.

- For each factor, try all possible start points. i.e. For distance d, there are d positions where ‘1’ should appear, and the rest string should be filled with zeros.

- Find minimum Hamming distance of given string to any of the valid strings found above.

# EXPLANATION

### Valid distance between '1’s

Let’s define the distance between two positiions i and j in 0-based indexing as j-i if i \leq j and j+N-i otherwise. Denoting distance by d(i, j).

Let’s suppose, we have a good string with k occurrences of 1s, and the distance between each ‘1’ from the next one is d. Assuming the positions of ones are p_1, p_2 \ldots p_k, we have d(p_i, p_{i+1}) = d for all 1 \leq i < k and d(p_k, p_1) = d as well.

We can see that starting from p_1, moving to next p_i until reaching p_1 again, leads to visiting N positions exactly once. So, we can claim that d*k = N holds.

**Claim:** If a circular string of length N is good, then the distance between each ‘1’ and the next ‘1’ is a factor of N.

Hence, let us try all divisors d one by one, and compute the minimum number of operations needed to convert s into a good string with distance d between ones.

### All good string s with distance d

Let’s suppose we fix the distance between each ‘1’ and the next as d where d is a factor of N.

The circular binary string would look like ‘1’ followed by d-1 ‘0’, then ‘1’ followed by d-1 '0’s and so on, covering the whole string. For N = 6, d = 3, we get string `100100`.

But there are string `010010` and string `001001` as well with d = 3.

We need to fix the position of the first occurrence f of ‘1’ in the string, as the first occurrence, as f and d defines the whole good circular string uniquely.

Pair (f, d) represent a string with each ‘1’ having distance d from the next one, and position f contains ‘1’. We can see that for each position p, it contains ‘1’ if and only if p \bmod d = f, and ‘0’ otherwise.

### Computing minimum Hamming distance to good string

Let’s try pair (f, d), representing string T, and try to compute its hamming distance from given string s. We know that T contains exactly N/d ones, and the rest zeros, so let’s iterate on those positions. Let’s make a set A denoting the set of positions of '1’s in T.

We need to count the number of positions p in set A such that s_p = ‘0’, and number of positions not in A such that s_p = ‘1’, as the sum of these values would be the hamming distance.

Let c denote the number of ones in whole string s, and x denote the number of ones in positions in set p present in set A such that s_p = ‘1’. We can see that The hamming distance is (N/d - x) + (c-x) \implies N/d + c - 2*x.

In case you missed

N/d -x is the number of positions where T contains ‘1’, but s contains ‘0’, and (c-x) denote the number of positions where T contains ‘0’ but s contains ‘1’

We can compute c beforehand, and compute x, the number of ones at positions p such that p \bmod d = f, in time O(N/d) time by following loop.

``x = 0
for(int p = f; p < N; p += d)
    if(s[p] == '1')
        x++
``

Hence, we shall try all valid pairs (f, d) one by one, compute Hamming distance from string s, and print minimum.

### Time complexity analysis

For a fixed distance d, let’s consider all start points f. There are exactly d unique choices for f, and computing each one takes N/d iterations, leading to total N iterations.

Hence, for each factor d of N, we need O(N) time, leading to time complexity O(N*\sigma(N)), where \sigma(N) is the divisor function.

# TIME COMPLEXITY

The time complexity is O(N*\sigma(N)) per test case.

# SOLUTIONS

Setter's Solution
``#include<bits/stdc++.h>
using namespace std;

signed main(){
//	freopen("input.txt", "r", stdin);
    int t;cin>>t;
    while(t--){
	    int n;cin>>n;
	    string s;cin>>s;
	    int sum=0;
	    for(int i=0;i<n;i++){
		    sum+=s[i]-'0';
	    }
	    int ans=n;

	    for(int x=1;x<=n;x++){
		    if(n%x)continue;

		    for(int j=0;j<x;j++){
			    int temp=0;
			    for(int k=j;k<n;k+=x){
				    if(s[k]=='1'){
					    temp-=1;
				    }else temp+=1;
			    }
			    ans=min(ans,sum+temp);
		    }

	    }
	    cout<<ans<<endl;
    }

    return 0;
}
``

Tester's Solution
``import java.util.*;
import java.io.*;
class BinaryStringOnSteroid{
    //SOLUTION BEGIN
    void pre() throws Exception{}
    void solve(int TC) throws Exception{
        int N = ni();
        char[] C = n().toCharArray();
        int count = 0;
        for(int i = 0; i< N; i++)count += C[i]-'0';
        int ans = N;
        for(int d = 1; d <= N; d++){
            if(N%d != 0)continue;
            for(int st = 0; st < d; st++){
                int cur = 0;
                for(int j = st; j< N; j += d)
                    cur += C[j]-'0';
                int op = N/d+count-2*cur;
                ans = Math.min(ans, op);
            }
        }
        pn(ans);
    }
    //SOLUTION END
    void hold(boolean b)throws Exception{if(!b)throw new Exception("Hold right there, Sparky!");}
    static boolean multipleTC = true;
    FastReader in;PrintWriter out;
    void run() throws Exception{
        in = new FastReader();
        out = new PrintWriter(System.out);
        //Solution Credits: Taranpreet Singh
        int T = (multipleTC)?ni():1;
        pre();for(int t = 1; t<= T; t++)solve(t);
        out.flush();
        out.close();
    }
    public static void main(String[] args) throws Exception{
        new BinaryStringOnSteroid().run();
    }
    int bit(long n){return (n==0)?0:(1+bit(n&(n-1)));}
    void p(Object o){out.print(o);}
    void pn(Object o){out.println(o);}
    void pni(Object o){out.println(o);out.flush();}
    String n()throws Exception{return in.next();}
    String nln()throws Exception{return in.nextLine();}
    int ni()throws Exception{return Integer.parseInt(in.next());}
    long nl()throws Exception{return Long.parseLong(in.next());}
    double nd()throws Exception{return Double.parseDouble(in.next());}

    class FastReader{
        BufferedReader br;
        StringTokenizer st;
        public FastReader(){
            br = new BufferedReader(new InputStreamReader(System.in));
        }

        public FastReader(String s) throws Exception{
            br = new BufferedReader(new FileReader(s));
        }

        String next() throws Exception{
            while (st == null || !st.hasMoreElements()){
                try{
                    st = new StringTokenizer(br.readLine());
                }catch (IOException  e){
                    throw new Exception(e.toString());
                }
            }
            return st.nextToken();
        }

        String nextLine() throws Exception{
            String str = "";
            try{
                str = br.readLine();
            }catch (IOException e){
                throw new Exception(e.toString());
            }
            return str;
        }
    }
}
``

Feel free to share your approach. Suggestions are welcomed as always.

</details>
