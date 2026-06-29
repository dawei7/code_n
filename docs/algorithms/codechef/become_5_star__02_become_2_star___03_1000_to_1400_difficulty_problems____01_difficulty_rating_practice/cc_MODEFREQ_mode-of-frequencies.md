# Mode of Frequencies

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MODEFREQ |
| Difficulty Rating | 1234 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1200 to 1400 difficulty problems |
| Official Link | [MODEFREQ](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1400/problems/MODEFREQ) |

---

## Problem Statement

Chef opted for Bio-Statistics as an Open-Elective course in his university, but soon got bored, and decided to text his friends during lectures. The instructor caught Chef, and decided to punish him, by giving him a special assignment.

There are $N$ numbers in a list $A = A_1, A_2, \ldots, A_N$. Chef needs to find the [mode](https://en.wikipedia.org/wiki/Mode_(statistics)) of the frequencies of the numbers. If there are multiple modal values, report the smallest one. In other words, find the frequency of all the numbers, and then find the frequency which has the highest frequency. If multiple such frequencies exist, report the smallest (non-zero) one.

More formally, for every $v$ such that there exists at least one $i$ such that $A_i = v$, find the number of $j$ such that $A_j = v$, and call that the frequency of $v$, denoted by $freq(v)$. Then find the value $w$ such that $freq(v) = w$ for the most number of $v$s considered in the previous step. If there are multiple values $w$ which satisfy this, output the smallest among them.

As you are one of Chef's friends, help him complete the assignment.

###Input:

- The first line contains an integer $T$, the number of test cases.
- The first line of each test case contains an integer $N$, the number of values in Chef's assignment.
- The second line of each test case contains $N$ space-separated integers, $A_i$, denoting the values in Chef's assignment.

###Output:
For each test case, print the mode of the frequencies of the numbers, in a new line.

###Constraints
- $1 \le T \le 100$
- $1 \le N \le 10000$
- $1 \le A_i \le 10$

###Subtasks
- 30 points : $1 \leq N \leq 100$
- 70 points : Original constraints.

---

## Examples

**Example 1**

**Input**

```text
2
8
5 9 2 9 7 2 5 3
9
5 9 2 9 7 2 5 3 1
```

**Output**

```text
2
1
```

**Explanation**

- **Test case 1:** $(2$, $9$ and $5)$ have frequency $2$, while $(3$ and $7)$ have frequency $1$. Three numbers have frequency $2$, while $2$ numbers have frequency $1$. Thus, the mode of the frequencies is $2$.

- **Test case 2:** $(2$, $9$ and $5)$ have frequency $2$, while $(3$, $1$ and $7)$ have frequency $1$. Three numbers have frequency $2$, and $3$ numbers have frequency $1$. Since there are two modal values $1$ and $2$, we report the smaller one: $1$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
8
5 9 2 9 7 2 5 3
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
9
5 9 2 9 7 2 5 3 1
```

**Output for this case**

```text
1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Practice](https://www.codechef.com/problems/MODEFREQ)

[Contest](https://www.codechef.com/LTIME87B/problems/MODEFREQ)

**Setter:** [Akash Bhalotia](https://www.codechef.com/users/akash_adm)

**Tester:** [Yash Chandnani](https://www.codechef.com/users/yash_chandnani)

**Editorialist:** [Ishmeet Singh Saggu](https://www.codechef.com/users/psychik)

# DIFFICULTY:

Cakewalk

# PREREQUISITES:

[Frequency Array](https://www.geeksforgeeks.org/frequency-of-each-element-of-an-array-of-small-ranged-values/) and Ad-hoc.

# PROBLEM:

You are given N numbers ranging from 1 to 10. You have to compute the mode of the frequencies of the numbers present in the array. If there are multiple frequencies with the same frequency output the smallest one.

# EXPLANATION:

First, you have to compute the number of occurrence(frequency) of number ranging from 1 to 10 present in the array this can be done using frequency array. To avoid confusion let us refer to the frequency of the number i as B_i. Now we have to find the mode of array B(note we don’t have to consider B_i, which is equal to 0 as these elements are not present in the original array). Now to find the number of occurrence(frequency) of number present in B using frequency array(note the magnitude of B_i can reach upto 10,000 as maximum value of N is 10,000 so we will make a frequency array for B till 10,000). And the maximum value in the frequency array of B will be our answer. In the case of repeated maximum values in the frequency array take the smallest B_i for which frequency is maximum.

# TIME COMPLEXITY:

-
O(N) per test case.

# SOLUTIONS:

Setter's Solution
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
            int a[]=new int[N];
            String[] s=br.readLine().trim().split(" ");
            for(i=0;i<N;i++) a[i]=Integer.parseInt(s[i]);

            int[] freq=new int[11]; //To find the frequency of numbers
            int[] freqOfFreq=new int[N+1]; //To find the frequency of frequencies

            for(i=0;i<N;i++) freq[a[i]]++;
            for(i=1;i<=10;i++) freqOfFreq[freq[i]]++;

            int ans=1,max=freqOfFreq[1];
            for(i=2;i<=N;i++) //Finding the mode
            {
                if(freqOfFreq[i]>max)
                {
                    max=freqOfFreq[i];
                    ans=i;
                }
            }
            sb.append(ans).append("\n");
        }
        System.out.println(sb);
    }
}
``

Tester's Solution
``#include <bits/stdc++.h>
using namespace std;

void __print(int x) {cerr << x;}
void __print(long x) {cerr << x;}
void __print(long long x) {cerr << x;}
void __print(unsigned x) {cerr << x;}
void __print(unsigned long x) {cerr << x;}
void __print(unsigned long long x) {cerr << x;}
void __print(float x) {cerr << x;}
void __print(double x) {cerr << x;}
void __print(long double x) {cerr << x;}
void __print(char x) {cerr << '\'' << x << '\'';}
void __print(const char *x) {cerr << '\"' << x << '\"';}
void __print(const string &x) {cerr << '\"' << x << '\"';}
void __print(bool x) {cerr << (x ? "true" : "false");}

template<typename T, typename V>
void __print(const pair<T, V> &x) {cerr << '{'; __print(x.first); cerr << ','; __print(x.second); cerr << '}';}
template<typename T>
void __print(const T &x) {int f = 0; cerr << '{'; for (auto &i: x) cerr << (f++ ? "," : ""), __print(i); cerr << "}";}
void _print() {cerr << "]\n";}
template <typename T, typename... V>
void _print(T t, V... v) {__print(t); if (sizeof...(v)) cerr << ", "; _print(v...);}
#ifndef ONLINE_JUDGE
#define debug(x...) cerr << "[" << #x << "] = ["; _print(x)
#else
#define debug(x...)
#endif

#define rep(i, n)    for(int i = 0; i < (n); ++i)
#define repA(i, a, n)  for(int i = a; i <= (n); ++i)
#define repD(i, a, n)  for(int i = a; i >= (n); --i)
#define trav(a, x) for(auto& a : x)
#define all(x) x.begin(), x.end()
#define sz(x) (int)(x).size()
#define fill(a)  memset(a, 0, sizeof (a))
#define fst first
#define snd second
#define mp make_pair
#define pb push_back
typedef long double ld;
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
long long readInt(long long l,long long r,char endd){
	long long x=0;
	int cnt=0;
	int fi=-1;
	bool is_neg=false;
	while(true){
		char g=getchar();
		if(g=='-'){
			assert(fi==-1);
			is_neg=true;
			continue;
		}
		if('0'<=g && g<='9'){
			x*=10;
			x+=g-'0';
			if(cnt==0){
				fi=g-'0';
			}
			cnt++;
			assert(fi!=0 || cnt==1);
			assert(fi!=0 || is_neg==false);

			assert(!(cnt>19 || ( cnt==19 && fi>1) ));
		} else if(g==endd){
			if(is_neg){
				x= -x;
			}
			assert(l<=x && x<=r);
			return x;
		} else {
			assert(false);
		}
	}
}
string readString(int l,int r,char endd){
	string ret="";
	int cnt=0;
	while(true){
		char g=getchar();
		assert(g!=-1);
		if(g==endd){
			break;
		}
		cnt++;
		ret+=g;
	}
	assert(l<=cnt && cnt<=r);
	return ret;
}
long long readIntSp(long long l,long long r){
	return readInt(l,r,' ');
}
long long readIntLn(long long l,long long r){
	return readInt(l,r,'\n');
}
string readStringLn(int l,int r){
	return readString(l,r,'\n');
}
string readStringSp(int l,int r){
	return readString(l,r,' ');
}
void pre(){

}
int cnt[11];
int a[10009];
void solve(){
	int n = readIntLn(1,10000);
	rep(i,n-1){
		a[i] = readIntSp(1,10);
	}
	a[n-1] = readIntLn(1,10);
	fill(cnt);
	rep(i,n) cnt[a[i]]++;
	map<int,int> m;
	repA(i,1,10) if(cnt[i])	{
		m[cnt[i]]++;
	}
	int ans = 0,mx=0;
	trav(i,m) if(i.snd>mx) mx=i.snd,ans=i.fst;
	cout<<ans<<'\n';

}

int main() {
	cin.sync_with_stdio(0); cin.tie(0);
	cin.exceptions(cin.failbit);
	pre();
	int n=readIntLn(1,100);
	rep(i,n) solve();
	assert(getchar()==EOF);
	return 0;
}
``

Editorialist's Solution
``#include <bits/stdc++.h>
using namespace std;

void solveTestCase() {
	int N;
	cin >> N;
	vector<int> freq(11, 0);
	for(int i = 0; i < N; i ++) {
		int in;
		cin >> in;
		freq[in] ++;
	}
	vector<int> freq_of_freq(10001, 0);
	for(int i = 1; i <= 10; i ++) {
		if(freq[i]) {
			freq_of_freq[freq[i]] ++;
		}
	}
	int maxFreq = 0, id = -1;
	for(int i = 1; i <= 10000; i ++) {
		if(freq_of_freq[i] > maxFreq) {
			maxFreq = freq_of_freq[i];
			id = i;
		}
	}
	cout << id << '\n';
}

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);

	int testCase;
	cin >> testCase;
	for(int i = 1; i <= testCase; i ++) {
		solveTestCase();
	}

	return 0;
}

``

Feel free to share your approach. In case of any doubt or anything is unclear please ask it in the comment section. Any suggestions are welcomed.

</details>
