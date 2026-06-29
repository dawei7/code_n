# Attendance

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | ATTND |
| Difficulty Rating | 1148 |
| Difficulty Band | Jump from 2* to 3* |
| Path | Become 5 star |
| Lesson | Standard Template Library |
| Official Link | [ATTND](https://www.codechef.com/practice/course/2to3stars/LP2TO304/problems/ATTND) |

---

## Problem Statement

Chef is teaching a cooking course. There are $N$ students attending the course, numbered $1$ through $N$.

Before each lesson, Chef has to take attendance, i.e. call out the names of students one by one and mark which students are present. Each student has a first name and a last name. In order to save time, Chef wants to call out only the first names of students. However, whenever there are multiple students with the same first name, Chef has to call out the full names (both first and last names) of all these students. For each student that does not share the first name with any other student, Chef may still call out only this student's first name.

Help Chef decide, for each student, whether he will call out this student's full name or only the first name.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains a single integer $N$.
- $N$ lines follow. For each valid $i$, the $i$-th of the following $N$ lines contains two space-separated strings denoting the first and last name of student $i$.

### Output
For each test case, print $N$ lines. For each valid $i$, the $i$-th of these lines should describe how Chef calls out the $i$-th student's name ― it should contain either the first name or the first and last name separated by a space.

### Constraints
- $1 \le T \le 100$
- $2 \le N \le 100$
- all first and last names contain only lowercase English letters
- the lengths of all first and last names are between $1$ and $10$ inclusive

### Subtasks
**Subtask #1 (100 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
1
4
hasan jaddouh
farhod khakimiyon
kerim kochekov
hasan khateeb
```

**Output**

```text
hasan jaddouh
farhod
kerim
hasan khateeb
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Practice](https://www.codechef.com/problems/ATTND)

[Contest: Division 1](https://www.codechef.com/LTIME71A/problems/ATTND)

[Contest: Division 2](https://www.codechef.com/LTIME71B/problems/ATTND)

**Setter:** [Hasan Jaddouh](https://www.codechef.com/users/kingofnumbers)

**Tester:** [Joud Zouzou](https://www.codechef.com/users/joudzouzou)

**Editorialist:** [Taranpreet Singh](https://www.codechef.com/users/taran_1407)

# DIFFICULTY:

Cakewalk

# PREREQUISITES:

Brute force, Maps, Multiset.

# PROBLEM:

Given a list of N names consisting of first name and last names separated by commas. You can call any person by his first name only if there is no other person with the same first name. If there exists any other person with the same first name, this person has to be called by full name only. For each person, determine how he would be called.

# QUICK EXPLANATION

-

Only those people would be called by the first name, whose first name is unique.

-

For each person, we check if there is any other person with the same first name or not which can be done using sets or maps, or even checking each record individually.

# EXPLANATION

So, when are we forced to call any person by full name? It is when there is any other person with the same first name.

So, How to check if there is any other user with the same first name? Since N is small, we can simply loop over all other names to check if there’s any other person with same first name, and if there is, we need to call this person by full name only.

The time complexity of this solution is O(N^2) per test case since for each person, we check all other people.

For a faster solution, we can use sets or maps to get time complexity down to O(N*log(N)) per test case. Maps can store the first name as a key, and number of occurrences of this first name as value, allowing us to check if there is more than one person with the same first name in O(logN) time.

# TIME COMPLEXITY

Time complexity is O(N^2) or O(N*log(N)) per test case depending upon implementation.

# SOLUTIONS:

Setter's Solution
``#include <iostream>
#include <algorithm>
#include <map>
#include <string>
#include <assert.h>
using namespace std;

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
			assert(cnt>0);
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

int T;
int n;
map<string,int> rep;

string first[111],last[111];

int main(){
	//freopen("00.txt","r",stdin);
	//freopen("00o.txt","w",stdout);
	T=readIntLn(1,100);
	while(T--){
		n=readIntLn(2,100);
		rep.clear();
		for(int i=0;i<n;i++){
			first[i]=readStringSp(1,10);
			last[i]=readStringLn(1,10);

			for(int j=0;j<first[i].size();j++){
				assert('a'<=first[i][j] && first[i][j] <='z');
			}
			for(int j=0;j<last[i].size();j++){
				assert('a'<=last[i][j] && last[i][j] <='z');
			}
			rep[first[i]]++;
		}
		for(int i=0;i<n;i++){
			for(int j=i+1;j<n;j++){
				assert(first[i] != first[j] || last[i] != last[j]);
			}
		}
		for(int i=0;i<n;i++){
			if(rep[first[i]] == 1){
				cout<<first[i]<<endl;
			} else {
				cout<<first[i]<<" "<<last[i]<<endl;
			}
		}
	}
	assert(getchar()==-1);
}
``

Tester's Solution
``     // Attendance
#include <bits/stdc++.h>
using namespace std;
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
	    assert(cnt>0);
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
map<string,int> mp;
string a[1000],b[1000];
int main()
{
    int t = readIntLn(1,100);
    while(t--)
    {
	mp.clear();
	int n = readIntLn(1,100);
	for (int i=1;i<=n;i++) {
	    a[i]=readStringSp(1,10);
	    b[i]=readStringLn(1,10);
	    mp[a[i]]++;
	}
	for (int i=1;i<=n;i++)
	    if (mp[a[i]]==1)
	        cout<<a[i]<<endl;
	    else
	        cout<<a[i]<<' '<<b[i]<<endl;
    }
    assert(getchar()==-1);
}
``

Editorialist's Solution
``	import java.util.*;
import java.io.*;
import java.text.*;
//Solution Credits: Taranpreet Singh
public class Main{
    //SOLUTION BEGIN
    //This code is not meant for understanding, proceed with caution
    void pre() throws Exception{}
    void solve(int TC) throws Exception{
	int n = ni();
	HashMap<String, Integer> map = new HashMap<>();
	String[][] name = new String[n][];
	for(int i = 0; i< n; i++){
	    name[i] = new String[]{n(), n()};
	    map.put(name[i][0], map.getOrDefault(name[i][0], 0)+1);
	}
	for(int i = 0; i< n; i++){
	    if(map.get(name[i][0])>1)pn(name[i][0]+" "+name[i][1]);
	    else pn(name[i][0]);
	}
    }
    //SOLUTION END
    void hold(boolean b)throws Exception{if(!b)throw new Exception("Hold right there, Sparky!");}
    long mod = (long)1e9+7, IINF = (long)1e18;
    final int INF = (int)1e9, MX = (int)1e6+1;
    DecimalFormat df = new DecimalFormat("0.0000000");
    double PI = 3.1415926535897932384626433832792884197169399375105820974944, eps = 1e-8;
    static boolean multipleTC = true, memory = false;
    FastReader in;PrintWriter out;
    void run() throws Exception{
	in = new FastReader();
	out = new PrintWriter(System.out);
	int T = (multipleTC)?ni():1;
//        Solution Credits: Taranpreet Singh
	pre();for(int t = 1; t<= T; t++)solve(t);
	out.flush();
	out.close();
    }
    public static void main(String[] args) throws Exception{
	if(memory)new Thread(null, new Runnable() {public void run(){try{new Main().run();}catch(Exception e){e.printStackTrace();}}}, "1", 1 << 28).start();
	else new Main().run();
    }
    long gcd(long a, long b){return (b==0)?a:gcd(b,a%b);}
    int gcd(int a, int b){return (b==0)?a:gcd(b,a%b);}
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

Feel free to Share your approach, If it differs. Suggestions are always welcomed.

</details>
