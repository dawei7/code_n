# Chef and Groups

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | GROUPS |
| Difficulty Rating | 1176 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1000 to 1200 difficulty problems |
| Official Link | [GROUPS](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1200/problems/GROUPS) |

---

## Problem Statement

There are $N$ seats in a row. You are given a string $S$ with length $N$; for each valid $i$, the $i$-th character of $S$ is '0' if the $i$-th seat is empty or '1' if there is someone sitting in that seat.

Two people are friends if they are sitting next to each other. Two friends are always part of the same group of friends. Can you find the total number of groups?

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains a single string $S$.

### Output
For each test case, print a single line containing one integer ― the number of groups.

### Constraints
- $1 \leq T \leq 50$
- $1 \leq N \leq 10^5$

### Subtasks
**Subtask #1 (100 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
4
000
010
101
01011011011110
```

**Output**

```text
0
1
2
4
```

**Explanation**

**Example case 1:** Since all seats are empty, the number of groups is $0$.

**Example case 2:** Since only one seat is occupied, the number of groups is $1$.

**Example case 3:** Here, two seats are occupied, but since they are not adjacent, the people sitting on them belong to different groups.

**Example case 4:** Here, we have $4$ groups of friends with size $1$, $2$, $2$ and $4$ respectively. That is, first group is sitting at $2$nd seat, second group at $4$th and $5$th seat, third group at  $7$th and $8$th seat and fourth group at $10$th to $13$th seat.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
000
```

**Output for this case**

```text
0
```



#### Test case 2

**Input for this case**

```text
010
```

**Output for this case**

```text
1
```



#### Test case 3

**Input for this case**

```text
101
```

**Output for this case**

```text
2
```



#### Test case 4

**Input for this case**

```text
01011011011110
```

**Output for this case**

```text
4
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/MARCH21A/problems/GROUPS)

[Contest Division 2](https://www.codechef.com/MARCH21B/problems/GROUPS)

[Contest Division 3](https://www.codechef.com/MARCH21C/problems/GROUPS)

[Practice](https://www.codechef.com/problems/GROUPS)

**Setter:** [](https://www.codechef.com/users/)

**Tester:** [Felipe Mota](https://www.codechef.com/users/fmota)

**Editorialist:** [Taranpreet Singh](https://www.codechef.com/users/taran_1407)

# DIFFICULTY

Simple

# PREREQUISITES

None

# PROBLEM

There are N seats in a row, each may either be empty, denoted by ‘0’, or occupied, denoted by ‘1’. People seated on consecutive seats become friends. Find the number of groups of friends.

# QUICK EXPLANATION

- The number of groups of friends is the number of blocks consisting of consecutive '1’s. So we need to count the number of segments consisting entirely of ones which cannot be extended.

- The number of segments can be found by splitting given string at each occurrence of ‘0’ and counting the number of non-empty splits.

# EXPLANATION

Interpreting story, we have a binary string of N characters and we need to find the number of segments of 1s in string.

One naive way would be to split the string at every occurrence of 0, and then count the number of non-empty strings. We can see that everytime we get a non-empty split, it must consist of 1s only, which represent one group of friends.

For example: S = `00101100111` leads to splits `"", "1", "11", "", "111"`. Among these, only three are non-empty, hence there are only three groups of friends.

This can be implemented to execute in O(|S|) and sufficient to get AC, but can we simplify implementation more? The answer is YES.

### Optional Observation

What we can notice is that every group ends either leads to substring `10` to appear in string, or `1` at the end of string. This happens because either a group is occupying all seats till end of the row, or there’s atleast one empty seat just after the group.

If we add another empty seat at end of the row, it wouldn’t affect the answer.

Hence, after adding an empty seat (or a ‘0’) at end of row (string), the number of group of friends is exactly the number of occurrences of `10` in resulting string.

No need of splitting strings anymore.

# TIME COMPLEXITY

The time complexity is O(|S|) per test case.

The memory complexity is O(|S|) per test case.

# SOLUTIONS

Setter's Solution
``#include<bits/stdc++.h>
using namespace std;

#define ll long long int
#define FIO ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0)
#define mod 1000000007

int main(){
    FIO;
    int t,n,k,i,j;
    string s;
    cin >> t;
    while(t--){
        cin >> s;
        s=s;
        j=0;
        char prv='0';
        for(char c:s){
            if(prv=='0' && c=='1')
                j++;
            prv=c;
        }
        cout << j << "\n";
    }
    return 0;
}
``

Tester's Solution
``#include <bits/stdc++.h>
using namespace std;
template<typename T = int> vector<T> create(size_t n){ return vector<T>(n); }
template<typename T, typename... Args> auto create(size_t n, Args... args){ return vector<decltype(create<T>(args...))>(n, create<T>(args...)); }
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
long long TEN(int p){ long long r = 1; while(p--) r *= 10; return r; }
int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    int t = readIntLn(1, 50);
    while(t--){
	    string s = readStringLn(1, TEN(5));
	    for(auto c : s)
		    assert(c == '0' || c == '1');
	    int ans = 0, n = s.size();
	    for(int i = 0, j = 0; i < n; i = j){
		    while(j < n && s[i] == s[j]) j++;
		    if(s[i] == '1') ans += 1;
	    }
	    cout << ans << '\n';
    }
    return 0;
}
``

Editorialist's Solution
``import java.util.*;
import java.io.*;
class GROUPS{
    //SOLUTION BEGIN
    void pre() throws Exception{}
    void solve(int TC) throws Exception{
        String S = n();
        S += "0";
        int groupCount = 0;
        for(int i = 0; i+1< S.length(); i++)
            if(S.charAt(i) == '1' && S.charAt(i+1) == '0')
                groupCount++;
        pn(groupCount);
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
        new GROUPS().run();
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
