# Power Sum

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | POWSUM |
| Difficulty Rating | 1906 |
| Difficulty Band | 1800 to 2000 difficulty problems |
| Path | Become 5 star |
| Lesson | 1900 to 2000 difficulty problems |
| Official Link | [POWSUM](https://www.codechef.com/practice/course/4-star-difficulty-problems/DIFF2000/problems/POWSUM) |

---

## Problem Statement

You are given a sequence $A$ of $N$ integers such that every element is a non-negative power of $2$.

A sequence is called `good` if its sum is a non-negative power of $2$. You would like to turn $A$ into a `good` sequence.

To achieve this, you can perform the following operation on $A$:
- Pick a non-empty subsequence of $A$, pick a positive integer $X$ such that $X \leq 2^{30}$, and multiply every element of this subsequence by $X$.

Find the minimum number of operations required to turn $A$ into a good sequence. Also, find one sequence of operations which does this. If there are multiple possible answers, you may find any of them.

---

## Input Format

- The first line of input contains a single integer $T$, denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains a single integer $N$.
- The second line of each test case contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$.

---

## Output Format

For each test case, print the answer in the following format:
- First, print one line containing an integer $M$, denoting the minimum number of moves required.
- Then, print $2M$ lines describing $M$ operations.
    - Each operation is described by $2$ lines.
    - On the first line, print two space-separated integers $K$ and $X$, denoting the size of the subsequence and the multiplier for this operation.
    - On the second line, print $K$ distinct space-separated integers denoting the indices of the elements chosen to be multiplied in this operation. These $K$ integers can be printed in any order.

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq N \leq 100$
- $1 \leq A_i \leq 2^{20} $

---

## Examples

**Example 1**

**Input**

```text
2
4
4 8 4 32
3
2 2 4
```

**Output**

```text
1
3 2
1 2 3
0
```

**Explanation**

**Test case $1$:** Multiplying the $1^{st}, 2^{nd}$ and $3^{rd}$ elements by $2$ turns the array into $[8, 16, 8, 32]$, whose sum is $64 = 2^6$.

**Test case $2$:** The array is already `good`.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/JAN222A/problems/POWSUM)

[Contest Division 2](https://www.codechef.com/JAN222B/problems/POWSUM)

[Contest Division 3](https://www.codechef.com/JAN222C/problems/POWSUM)

**Setter:** [Prasant Kumar](https://www.codechef.com/users/prasant21)

**Tester:** [Taranpreet Singh](https://www.codechef.com/users/taran_1407)

**Editorialist:** [Kanhaiya Mohan](https://www.codechef.com/users/notsoloud)

#
[](#difficulty-2)DIFFICULTY:

Easy

#
[](#prerequisites-3)PREREQUISITES:

[Binary Representation](https://en.wikipedia.org/wiki/Binary_number)

#
[](#problem-4)PROBLEM:

You are given a sequence of A on N integers such that every element is a non-negative power of 2. A sequence is called \text{good} if its sum is a non-negative power of 2. Find the minimum number of operations required to turn A into a \text{good} sequence.

An operation is defined as: Pick a non-empty subsequence of A, pick a positive integer X (X \leq 2^{30}), and multiply every element of this subsequence by X.

Find any sequence of minimum operations that turns A into \text{good} sequence.

#
[](#quick-explanation-5)QUICK EXPLANATION:

- Required number of operations is either 0 or 1.

- If the sequence is already \text{good}, the answer is 0.

- If the sequence is not \text{good}, we require only 1 operation.

- Let S be the sum of the sequence (where S is not a power of 2) and r be the smallest integer such that S < 2^r. In one operation, we choose the smallest number of the sequence (M), and multiply it with X = \frac{2^r - (S - M)}{M}.

#
[](#explanation-6)EXPLANATION:

If the sequence is already \text{good}, we need 0 operations.

If the sequence is not \text{good}, we can make it good using exactly one operation. How?

Let S be the sum of the sequence. We know that S is not a power of 2. After some number of operations, let us assume that we achieve a sum of 2^r, thus,  making the sequence \text{good}.

**S>2^r**:  This is because, in each operation we multiply some subsequence with a positive integer. This would increase the value of the elements of that subsequence and thus the overall sum.

This means that we have to increase S at least to 2^r such that 2^{r-1} < S <2^r. For this, we need to add 2^r - S to the sequence.

Let M denote the smallest element of the sequence.

**Claim:** 2^r - S is a multiple of M.

**Proof:** An important thing to note is that all numbers of the sequence are powers of 2.

Let p be the number of [trailing zeroes](https://en.wikipedia.org/wiki/Trailing_zero) in the binary representation of M (M = 2^p) and q be that of S. Also, the number of trailing zeroes in the binary representation of 2^r is r. Since M is the smallest element of the sequence, p \leq q. Similarly, since 2^r>S, r>q.

This means that the number of trailing zeroes in the binary representation of 2^r-S is also q.

A binary number with q trailing zeroes is divisible by 2^q. This implies that 2^r-S is divisible by 2^q. Also, since p\leq q, 2^r-S is divisible by 2^p, which is nothing but M. Hence proved, 2^r-S is divisible by M.

To convert S to 2^r, we can simply multiply M by \frac{2^r - (S - M)}{M}. This would take only one operation and make the sum of sequence equal to 2^r. The chosen subsequence in the operation only consists of M.

#
[](#time-complexity-7)TIME COMPLEXITY:

We have to traverse the array to find the minimum element and the sum of elements. Thus, the time complexity is O(N) per test case.

#
[](#solution-8)SOLUTION:

Setter's Solution
``#include<bits/stdc++.h>
using namespace std;
#define int long long
#define endl "\n"
const int sf=2e5+10; // size for fac and inverse fac.
int M=1e9+7; // modulus, change it if different.
// dont copy others template you will get plagiarized.
int fac[sf],invFac[sf];
int power(int a,int b){
	int ans=1;
	while(b>0){
		if(b&1){
			ans*=a;
			ans%=M;
		}
		a*=a;
		a%=M;
		b/=2;
	}
	return ans;
}
int findInv(int a){
	return power(a,M-2);
}
void preFac(){ // pre process
	fac[0]=invFac[0]=1;
	for(int i=1;i<sf;i++){
		fac[i]=(fac[i-1]*i)%M;
		invFac[i]=findInv(fac[i]);
	}
}
int nCr(int n,int r){  // call only if preprocess is done
	return ((fac[n]*invFac[r])%M * invFac[n-r])%M;
}
int msb(int n){ // change 63 to 31 if 32 bit integer is used and use __builtin_clz(n)
	return 63 - __builtin_clzll(n);
}

// => pre-process
// => change size of array, modulus if required.
// -------------------------------------------------------------------------------------------------------------------------------------------

signed main(){
	ios_base::sync_with_stdio(0) , cin.tie(0);
	int t;cin>>t;
	while(t--){
		int n;cin>>n;
		int mini=1e9,ind;
		int sum=0;
		int arr[n];
		for(int i=0;i<n;i++){
			cin>>arr[i];
			if(arr[i]<mini){
				mini=arr[i];
				ind=i;
			}
			sum+=arr[i];
		}
		if((sum&(sum-1))==0){
			cout<<0<<endl;
		}else{
			int next=1ll<<(msb(sum)+1);
			int dif=next-sum;
			cout<<1<<endl;
			cout<<1<<" "<<(dif/mini + 1)<<endl;
			cout<<ind+1<<endl;
		}
	}
	return 0;
}

``

Tester's Solution
``import java.util.*;
import java.io.*;
class POWSUM{
    //SOLUTION BEGIN
    void pre() throws Exception{}
    void solve(int TC) throws Exception{
        int N = ni();
        int[] A = new int[N];
        for(int i = 0; i< N; i++)A[i] = ni();
        int sum = 0;
        for(int x:A)sum += x;
        if((bit(sum)) == 1)pn(0);
        else{
            pn(1);
            int total = (Integer.highestOneBit(sum)<<1)-sum;
            for(int i = 0; i< N; i++){
                if(total%A[i] == 0){
                    pn("1 "+(total/A[i]+1));
                    pn(1+i);
                    return;
                }
            }
            hold(false);
        }
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
        new POWSUM().run();
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

Editorialist's Solution
``#include <bits/stdc++.h>
using namespace std;

#define sync {ios_base ::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);}
#define rep(n) for(int i = 0;i<n;i++)
#define rep1(a,b) for(int i = a;i<b;i++)
#define int long long int
#define mod 1000000007

int n;

void solve()
{
    cin>>n;
    int a[n];

    int sum = 0;
    int minm = INT_MAX;
    int min_index = 0;
    for(int i = 0; i<n; i++){
        cin>>a[i];
        if(minm > a[i]){
            minm = a[i];
            min_index = i+1;
        }
        sum += a[i];
    }

    if((sum & (sum-1)) == 0){
        cout<<0;
        return;
    }

    int no_of_bits = (int)log2(sum) + 1;
    int target = 1<<no_of_bits;
    int needed = target - (sum - minm);
    int x = needed/minm;
    cout<<1<<endl;
    cout<<1<<' '<<x<<endl;
    cout<<min_index;
}

int32_t main()
{

    #ifndef ONLINE_JUDGE
        freopen("input.txt","r",stdin);
        freopen("output.txt","w",stdout);
    #endif

    sync;
    int t = 1;
    cin>>t;
    while(t--){
        solve();
        cout<<"\n";
    }
    return 0;
}
``

</details>
