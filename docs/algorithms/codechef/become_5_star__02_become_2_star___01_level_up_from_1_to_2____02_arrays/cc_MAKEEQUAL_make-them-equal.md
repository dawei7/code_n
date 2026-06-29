# Make them equal

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MAKEEQUAL |
| Difficulty Rating | 1267 |
| Difficulty Band | Level up from 1* to 2* |
| Path | Become 5 star |
| Lesson | Arrays |
| Official Link | [MAKEEQUAL](https://www.codechef.com/practice/course/1to2stars/LP1TO202/problems/MAKEEQUAL) |

---

## Problem Statement

Chef has an array $A$ having $N$ elements. Chef wants to make all the elements of the array equal by repeating the following move.

- Choose any integer $K$ between $1$ and $N$ (inclusive). Then choose $K$ distinct indices $i_1 , i_2, \dots, i_K$, and increase the values of $A_{i_1} , A_{i_2} , \dots , A_{i_K}$ by $1$.

Find the minimum number of moves required to make all the elements of the array equal.

---

## Input Format

- The first line contains $T$ denoting the number of test cases. Then the test cases follow.
- The first line of each test case contains a single integer $N$ denoting the number of elements in $A$.
- The second line of each test case contains $N$ space separated integers $A_1, A_2, \dots, A_N$.

---

## Output Format

For each test case, print a single line containing one integer denoting the minimum number of moves required to make all the elements of the array equal.

---

## Constraints

- $1 \leq T \leq 10^4$
- $1 \leq N \leq 10^5$
- $1 \leq A_i \leq 10^5$
- The sum of $N$ over all test cases does not exceed $10^5$.

---

## Examples

**Example 1**

**Input**

```text
2
3
1 3 1
3
2 2 2
```

**Output**

```text
2
0
```

**Explanation**

- **Test Case $1$**: In the first move, Chef can choose $K = 2$, and choose the indices $\{1 , 3\}$. After increasing $A_1$ and $A_3$ by $1$, the array will become $[2 , 3 , 2]$.
In the second move, Chef can choose $K = 2$, and choose the indices $\{1 , 3\}$. After increasing $A_1$ and $A_3$ by $1$, the array will become $[3 , 3 , 3]$, and hence all the elements become equal.

- **Test Case $2$**: All the elements of the array are equal, hence no move is required.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3
1 3 1
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
3
2 2 2
```

**Output for this case**

```text
0
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/START18A/problems/MAKEEQUAL)

[Contest Division 2](https://www.codechef.com/START18B/problems/MAKEEQUAL)

[Contest Division 3](https://www.codechef.com/START18C/problems/MAKEEQUAL)

[Practice](https://www.codechef.com/problems/MAKEEQUAL)

**Setter:** [Lavish Gupta](https://www.codechef.com/users/lavish315)

**Tester:** [Abhinav Sharma](https://www.codechef.com/users/inov_360)

**Editorialist:** [Taranpreet Singh](https://www.codechef.com/users/taran_1407)

#
[](#difficulty-2)DIFFICULTY

Cakewalk

#
[](#prerequisites-3)PREREQUISITES

None

#
[](#problem-4)PROBLEM

Chef has an array A having N elements. Chef wants to make all the elements of the array equal by repeatedly using the following move.

- Choose any integer K between 1 and N (inclusive). Choose K distinct indices i_1 , i_2, \cdot, i_K, and increase the values of A_{i_1} , A_{i_2} , \cdots , A_{i_K} by 1.

Find the minimum number of moves required to make all the elements of the array equal.

#
[](#quick-explanation-5)QUICK EXPLANATION

The number of operations needed is max(A_i) - min(A_i)

#
[](#explanation-6)EXPLANATION

We can pick any subset of given integers and increase elements in the chosen subset by 1. We want to make all elements equal.

One thing we can see is that we can only increase the elements. So it doesn’t make sense to include the largest element in any operation.

Let us perform the operations in the following manner. In current operations, pick all indices x such that A_x is the minimum element. This way, after the operation is performed, the minimum of A has increased by 1.

Let’s assume minimum of A is min(A_i) and maximum of A is max(A_i). In one operation, we can increase the minimum of A by 1. All the elements would be equal when min(A_i) = max(A_i). So it requires max(A_i) - min(A_i) operations.

Hence, all we need to do is to compute the minimum and maximum of given A and print their difference.

#
[](#time-complexity-7)TIME COMPLEXITY

The time complexity is O(N) per test case.

#
[](#solutions-8)SOLUTIONS

Setter's Solution
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

const int MAX_T = 10000;
const int MAX_LEN = 100000;
const int MAX_VAL = 100000;
const int MAX_SUM_LEN = 100000;

#define fast ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0)

int sum_len = 0;
int max_n = 0;
int yess = 0;
int nos = 0;
int total_ops = 0;

int n;

void solve()
{
    n = readIntLn(1 , MAX_LEN) ;
    sum_len += n ;
    int arr[n] ;
    int maxi = 0 , mini = MAX_VAL ;
    for(int i = 0 ; i < n-1 ; i++)
    {
        arr[i] = readIntSp(1 , MAX_VAL) ;
        if(arr[i] > maxi)
            maxi = arr[i] ;
        if(arr[i] < mini)
            mini = arr[i] ;
    }
    arr[n-1] = readIntLn(1 , MAX_VAL) ;
    if(arr[n-1] > maxi)
        maxi = arr[n-1] ;
    if(arr[n-1] < mini)
        mini = arr[n-1] ;

    cout << maxi - mini << '\n' ;
    return ;
}

signed main()
{

    // fast;

    int t = 1;

    t = readIntLn(1,MAX_T);
    assert(1<=t && t<=10000);

    for(int i=1;i<=t;i++)
    {
       solve();
    }

    assert(getchar() == -1);
    assert(1 <= sum_len && sum_len <= MAX_SUM_LEN) ;

    cerr<<"SUCCESS\n";
    cerr<<"Tests : " << t << '\n';
    cerr<<"Sum of lengths : " << sum_len << '\n';
    cerr<<"Maximum length : " << max_n << '\n';
    // cerr<<"Total operations : " << total_ops << '\n';
    // cerr<<"Answered yes : " << yess << '\n';
    // cerr<<"Answered no : " << nos << '\n';
}
``

Tester's Solution
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

const int MAX_T = 10000;
const int MAX_LEN = 100000;
const int MAX_VAL = 100000;
const int MAX_SUM_LEN = 100000;

#define fast ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0)

int sum_len = 0;
int max_n = 0;
int yess = 0;
int nos = 0;
int total_ops = 0;

int n;

void solve()
{
    n = readIntLn(1 , MAX_LEN) ;
    sum_len += n ;
    int arr[n] ;
    int ans = 0 ;
    for(int i = 0 ; i < n-1 ; i++)
    {
        arr[i] = readIntSp(1 , MAX_VAL) ;
    }
    arr[n-1] = readIntLn(1 , MAX_VAL) ;

    sort(arr,arr+n);
    cout<<arr[n-1]-arr[0]<<'\n';
    return ;
}

signed main()
{

    // fast;

    int t = 1;

    t = readIntLn(1,MAX_T);
    assert(1<=t && t<=10000);

    for(int i=1;i<=t;i++)
    {
       solve();
    }

    assert(getchar() == -1);
    assert(1 <= sum_len && sum_len <= MAX_SUM_LEN) ;

    cerr<<"SUCCESS\n";
    cerr<<"Tests : " << t << '\n';
    cerr<<"Sum of lengths : " << sum_len << '\n';
    cerr<<"Maximum length : " << max_n << '\n';
    // cerr<<"Total operations : " << total_ops << '\n';
    // cerr<<"Answered yes : " << yess << '\n';
    // cerr<<"Answered no : " << nos << '\n';
}
``

Editorialist's Solution
``import java.util.*;
import java.io.*;
class MAKEEQUAL{
    //SOLUTION BEGIN
    void pre() throws Exception{}
    void solve(int TC) throws Exception{
        int N = ni();
        int min = Integer.MAX_VALUE, max = Integer.MIN_VALUE;
        for(int i = 0; i< N; i++){
            int x = ni();
            min = Math.min(min, x);
            max = Math.max(max, x);
        }
        pn(max-min);
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
        new MAKEEQUAL().run();
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
