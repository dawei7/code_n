# Distinct Values

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | DIST_VALS |
| Difficulty Rating | 2236 |
| Difficulty Band | 2000 to 2500 difficulty problems |
| Path | Become 5 star |
| Lesson | 2000 to 2500 difficulty problems |
| Official Link | [DIST_VALS](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/DIST_VALS) |

---

## Problem Statement

The *beauty* value of an array is defined as the difference between the largest and second largest elements of the array. Note that the largest and second largest elements can have the same value in case of duplicates.

For example, *beauty* value of $[2, 5, 3, 1] = 5 - 3 = 2$ and *beauty* value of $[7, 6, 7] = 7 - 7 = 0$

You are given an array $A$ of length $N$. Your task is to find the total number of **distinct** *beauty* values among all *subarrays* of $A$ having length greater than $1$.

Note that, a subarray is obtained by deleting some (possibly zero) elements from the beginning and some (possibly zero) elements from the end of the array.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two lines of input.
    - The first line of each test case contains a single integer $N$ — the size of the array.
    - The second line contains $N$ space-separated numbers - $A_{1}, A_{2},\ldots ,A_{N}$, the elements of the array.

---

## Output Format

For each test case, output a single line, the total number of **distinct** beauty among all *subarrays* of $A$ having length greater than $1$.

---

## Constraints

- $1 \leq T \leq 10^{4}$
- $2 \leq N \leq 2 \cdot 10^{5}$
- $1 \leq A_i \leq 10^{9}$
- Sum of $N$ over all test cases does not exceed $2 \cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
4
2
1 1
3
4 2 1
4
8 1 7 2
5
6 9 4 2 1
```

**Output**

```text
1
2
4
4
```

**Explanation**

**Test case $1$:** The only subarray is $[1,1]$ whose beauty is $0$. Thus, there is only $1$ distinct value of beauty.

**Test case $2$:** The subarrays are $[4,2], [2,1],$ and $[4,2,1]$ having beauty $2, 1,$ and $2$ respectively. There are $2$ distinct values of beauty.

**Test case $3$:** The unique values of beauty are $7,1,6,$ and $5$.

**Test case $4$:** The unique values of beauty are $3,5,2,$ and $1$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2
1 1
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
3
4 2 1
```

**Output for this case**

```text
2
```



#### Test case 3

**Input for this case**

```text
4
8 1 7 2
```

**Output for this case**

```text
4
```



#### Test case 4

**Input for this case**

```text
5
6 9 4 2 1
```

**Output for this case**

```text
4
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/DIST_VALS)

[Contest: Division 1](https://www.codechef.com/START74A/problems/DIST_VALS)

[Contest: Division 2](https://www.codechef.com/START74B/problems/DIST_VALS)

[Contest: Division 3](https://www.codechef.com/START74C/problems/DIST_VALS)

[Contest: Division 4](https://www.codechef.com/START74D/problems/DIST_VALS)

***Author:*** [ayu_19](https://www.codechef.com/users/ayu_19)

***Testers:*** [nishant403](https://www.codechef.com/users/nishant403), [satyam_343](https://www.codechef.com/users/satyam_343)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

TBD

#
[](#prerequisites-3)PREREQUISITES:

[Finding next/previous greater element](https://www.techiedelight.com/next-greater-element/)

#
[](#problem-4)PROBLEM:

You have an array A. The beauty of a subarray is the difference between its largest and second largest element.

Find the number of distinct beauties across all subarrays.

#
[](#explanation-5)EXPLANATION

We only really care about the maximum and second maximum element of the subarray, so let’s fix one of them and try to find valid values for the other one.

In particular, let’s fix the *second* maximum of the subarray.

Let’s say that we want a subarrays where A_i is the second maximum.

For this, the subarray should definitely contain A_i, and it should certainly contain something else larger than (or at least, equal to) A_i as well.

In particular,

- Let j \lt i be the highest index such that A_j \geq A_i.

- Let k \gt i be the lowest index such that A_k \geq A_i.

Then our subarray should contain at least one of A_j and A_k (giving beauties of A_j - A_i and A_k - A_i, respectively)

In fact, these two are the only beauty values we need to care about with A_i being the second maximum!

Proof

Let’s consider a few cases:

- Suppose the subarray contains both A_j and A_k. Then, these two elements are \geq A_i, so at the very least we can ensure that A_i won’t be picked as the second maximum; and such a subarray will be taken care of when considering something else as second maximum.

- Suppose the subarray contains A_j but not A_k. Then, if A_i is the second maximum, the beauty obtained is A_j - A_i (which we do consider); and if A_i is not the second maximum this subarray will be considered when something else is chosen as second maximum.

- The same analysis applies for when it contains A_k but not A_j.

So, we have a total of (at most) 2N possible beauties, if we can compute them all quickly enough then counting the number of distinct ones is trivial: for example, put them all in a `set` and find the size of the set.

Notice that all we really need to be able to do is compute the j and k mentioned above quickly enough, for a given i.

Let’s focus on computing j first; the exact same method can be used to find k.

This is a rather classical problem, often called the “previous greater element” problem; and we can find it for every i from 1 to N in \mathcal{O}(N) time total using a stack.

How?

Let \text{prev}[i] be the value of j we’re looking for.

Keep a stack S, initially empty. Then, do the following:

- Iterate i from 1 to N.

- For a fixed i,

- While S is not empty, if A_i \gt A_{S.top}, pop the stack

- Then, if S is empty set \text{prev}[i] = -1; otherwise set \text{prev}[i] = S.top

- Finally, push i onto the stack

The idea is that S will always contain a sorted list of elements (decreasing in value from bottom to top).

When adding a new element, remove things less than whatever is being added; then the first element on the stack is the nearest greater element.

Since each index is pushed once and popped at most once, this entire algorithm runs in \mathcal{O}(N) time.

You can also read about this method [here](https://www.techiedelight.com/next-greater-element/).

Use the above method to compute the next and previous greater elements for each i, then find all 2N candidates and count the number of distinct elements among them.

#
[](#time-complexity-6)TIME COMPLEXITY:

\mathcal{O}(N\log N) per testcase.

#
[](#code-7)CODE:

Setter's code (C++)
``#include "bits/stdc++.h"
// #include "testlib.h"
using namespace std;

// #include <ext/pb_ds/assoc_container.hpp>
// using namespace __gnu_pbds;
// template<class T> using oset = tree<T,null_type,less_equal// for indexed_multiset */
// <T> ,rb_tree_tag,tree_order_statistics_node_update> ;    // order_of_key (k) -> # of elem strictly < k .
//                                                      // *(s.find_by_order(k)) -> element at index K .
#define int              long long int
using   ll=              long long;
#define ld               long double
#define endl             '\n'
#define dbg(x)           cout<<#x<<" is -> "<<x<<endl
#define speed_           ios_base::sync_with_stdio(false),cin.tie(0), cout.tie(0)
#define pb               push_back
#define po               pop_back
#define mp               make_pair
#define sab(x)           x.begin(),x.end()
#define rsab(x)          x.rbegin(),x.rend()
#define ff               first
#define ss               second
#define sz(x)            (int)x.size()
#define sp(x)            fixed<<setprecision(x)
#define uni(edge)        edge.erase(unique(edge.begin(),edge.end()),edge.end());
#define to_up(x)         transform(sab(x),x.begin(),::toupper)
#define to_low(x)        transform(x.begin(),x.end(),x.begin(),::tolower)
#define ONLINE_JUDGE

// const int M = 1000000007;
// const int MM = 998244353;
// const ld Pi= acos(-1);
// const int N=1e5+10;
// const int inf=1e18;
// const int MAXX=1e9;

vector<int>v;
int t;
int test_count=0;

void simp(){

    // dp?, graph?, bs on answer?, compress/sort queries/array?, stupid observation?

    test_count++;
    int n;
    cin>>n;
    v.resize(n);
    set<int>s;
    stack<int>st1;
    for(int i=0;i<n;i++){
        cin>>v[i];
    }
    for(int i=0;i<n;i++){
        while(st1.size() && st1.top()<=v[i]){
            int curr=st1.top();
            s.insert(v[i]-curr);
            st1.pop();
        }
        st1.push(v[i]);
    }
    while(sz(st1)){
        st1.pop();
    }
    reverse(sab(v));
    for(int i=0;i<n;i++){
        while(st1.size() && st1.top()<=v[i]){
            int curr=st1.top();
            s.insert(v[i]-curr);
            st1.pop();
        }
        st1.push(v[i]);
    }

    int ans=sz(s);
    cout<<ans;
    if(test_count!=t){
        cout<<endl;
    }

}

signed main(){

    speed_;// remove this in interactive problems

    // freopen("ouput05.txt", "r", stdin);
    // freopen("input05.txt", "w", stdout);

    // int t;
    t=1;
    cin>>t;

    // initialize();
    // solve();

    //gen_factorial(N+10);

    int curr=1;
    for(int i=0;i<t;i++){

 #ifndef ONLINE_JUDGE

 #endif
       // cout<<"Case #"<<curr++<<": ";
        simp();

    }
return 0;
}
``

Tester's code (C++)
``#include <bits/stdc++.h>
using namespace std;

/*
------------------------Input Checker----------------------------------
*/

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

            if(!(l <= x && x <= r))
            {
                cerr << l << ' ' << r << ' ' << x << '\n';
                assert(1 == 0);
            }

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

/*
------------------------Main code starts here----------------------------------
*/

#define int long long

const int MAX_T = 1e4;
const int MAX_N = 2e5;
const int MAX_SUM_N = 2e5;
const int MAX_VAL = 1e9;

#define fast ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0)

int sum_n = 0;
int max_n = 0;
int max_ans = 0;
int sum_dist = 0;

void solve()
{
    int n;
    n = readIntLn(2,MAX_N);
    max_n = max(max_n, n);
    sum_n += n;
    assert(sum_n <= MAX_SUM_N);

    int a[n];
    for(int i=0;i<n;i++) {
        if(i != n - 1) {
            a[i] = readIntSp(1 , MAX_VAL);
        } else {
            a[i] = readIntLn(1 , MAX_VAL);
        }
    }

    //observation : an array index can occur as second maximum element
    //only twice , with first greater or equal element to left and to right
    vector<int> nge(n, n),pge(n, - 1);

    vector<int> st;

    for(int i=0;i<n;i++) {
        while(!st.empty() && a[st.back()] <= a[i]) {
            nge[st.back()] = i;
            st.pop_back();
        }

        st.push_back(i);
    }

    st.clear();

    for(int i=n-1;i>=0;i--) {
        while(!st.empty() && a[st.back()] <= a[i]) {
            pge[st.back()] = i;
            st.pop_back();
        }

        st.push_back(i);
    }

    set<int> vals;

    for(int i=0;i<n;i++) {
        if(nge[i] != n) vals.insert(a[nge[i]] - a[i]) , sum_dist += (nge[i] - i);
        if(pge[i] != -1) vals.insert(a[pge[i]] - a[i]) , sum_dist += (i - pge[i]);
    }

    int ans = vals.size();

    max_ans = max(max_ans , ans);

    cout << ans << '\n';
}

signed main()
{
    int t = 1;
    t = readIntLn(1,MAX_T);

    for(int i=1;i<=t;i++)
    {
       solve();
    }

    assert(getchar() == -1);

    cerr<<"SUCCESS\n";
    cerr<<"Tests : " << t << '\n';
    cerr<<"Sum of lengths A : " << sum_n << '\n';
    cerr<<"Maximum length A : " << max_n << '\n';
    cerr<<"Maximum answer : " << max_ans << '\n';
    cerr<<"Sum of distance : "<< sum_dist << '\n';
}
``

Editorialist's code (Python)
``for _ in range(int(input())):
	n = int(input())
	a = list(map(int, input().split()))
	stack = []
	prev_big = [-1]*n
	next_big = [-1]*n
	for i in range(n):
		while len(stack) > 0:
			if a[stack[-1]] < a[i]: stack.pop()
			else: break
		if len(stack) > 0: prev_big[i] = stack[-1]
		stack.append(i)
	stack = []
	for i in reversed(range(n)):
		while len(stack) > 0:
			if a[stack[-1]] < a[i]: stack.pop()
			else: break
		if len(stack) > 0: next_big[i] = stack[-1]
		stack.append(i)
	difs = set()
	for i in range(n):
		if prev_big[i] != -1: difs.add(a[prev_big[i]] - a[i])
		if next_big[i] != -1: difs.add(a[next_big[i]] - a[i])
	print(len(difs))
``

</details>
