# College Admissions

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | ADMIT |
| Difficulty Rating | 2496 |
| Difficulty Band | 2000 to 2500 difficulty problems |
| Path | Become 5 star |
| Lesson | 2000 to 2500 difficulty problems |
| Official Link | [ADMIT](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/ADMIT) |

---

## Problem Statement

College admissions are starting and Chef has also recently completed his high school. There are $N$ colleges, numbered from $1$ to $N$, and they are ranked from $1$ to $N$. Each college has only a single seat left. To apply for the colleges, every student has to give a common exam, the result of which decides their destiny, i.e, the student having best rank (scoring max marks) gets to choose the college of their preference first.

Each student has a list of colleges that they like. They will want to get to the best-ranked college from their list. If they can't get into it, they will want to get into the second-ranked college from among their list, and so on.

If the single vacant seat of a college gets filled, the admission for that year is closed in that college. Then, the people who have applied for that college have to look for a lower-ranked college in their preference list provided that it still has vacancies.

Given information about $M$ students, about their marks scored in the exam (given as ranks) and the id’s of the college they are applying for, find which college Chef will land into given that he is the student with $id = 1$.

Every student tries to get into the highest-ranked college on his list which has a vacancy and if not possible to get into any of the colleges on his list, he won’t join any college this year.

###Input:

- First line will contain $T$, number of testcases. Then the testcases follow.
- Each testcase contains $M + 3$ lines of input.
- First line contains $2$ space separated integers $N$, $M$, the total number of colleges, and total number of students respectively.
- Second line contain $N$ distinct space separated integers $R_i$, rank of the $i^{th}$ college. Here $1$ denotes a higher rank and $N$ denotes a lower rank.
- Third line contains $M$ distinct space separated integers $S_i$, the rank of the $i^{th}$ student in the exam. Here $1$ denotes a higher rank, i.e, maximum marks scored and $M$ denotes a lower rank, i.e, minimum marks scored.
- Next $M$ lines contain $K + 1$ space separated integers which the first integer $K$ is the number of colleges $i^{th}$ student will apply to and the next $K$ integers describe the same.

###Output:
For each testcase, output in a single line the college in which Chef applies and $0$ if he won't be joining any college this year.

###Constraints
- $1 \leq N, M \leq 5*10^4$
- $R$ is the permutation of integers from $[1, N]$
- $S$ is the permutation of integers from $[1, M]$
- Sum of $N$ over all tests is atmost $3* 10^5$
- Sum of $M$ over all tests is atmost $3.5 * 10^5$
- Sum of $K$ over all students over all tests is atmost $1.5*10^6$
- Every student applies to atleast $1$ college and all the applied colleges are different.

**Note:** Language multiplier for $Java$ is $3$ and for $python$ is $5$ and its recommended to use **Fast Input-Output** for this problem.

---

## Examples

**Example 1**

**Input**

```text
3
2 2
2 1
1 2
2 1 2
2 1 2
1 2
1
2 1
1 1
1 1
2 1
1 2
1
2 2 1
```

**Output**

```text
2
0
1
```

**Explanation**

**Case 1:** Here since Chef has the highest rank, he gets to choose the highest rank college in his preference list first, that is college with $id = 2$.

**Case 2:** Here since there is only $1$ college and Chef stood second, he won't be able to apply to any of the colleges this year, so we print $id = 0$.

**Case 3:** Here since Chef is the only student and thus has the highest rank, he gets to choose the highest rank college in his preference list first, that is college with $id = 1$.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/START1A/problems/)

[Contest Division 2](https://www.codechef.com/START1B/problems/)

[Contest Division 3](https://www.codechef.com/START1C/problems/)

[Practice](https://www.codechef.com/problems/)

**Setter:** [](https://www.codechef.com/users/)

**Tester:** [Istvan Nagy](https://www.codechef.com/users/iscsi)

**Editorialist:** [Taranpreet Singh](https://www.codechef.com/users/taran_1407)

# DIFFICULTY

Easy

# PREREQUISITES

Implementation

# PROBLEM

Given N colleges ranked from 1 to N from best to worst, each having exactly one seat available, and M students ranked by their performance in an entrance exam, and a list of colleges preferred by each student, all students are considered in order of their rank in exam. Student gets admission in college with best rank having a vacant seat, or none if no college in student’s preference has a seat.

Determine the college in which first student is admitted, or not admitted at all.

# QUICK EXPLANATION

Just simulate the whole process, considering students in order of their rank while maintaining the status of seats available in each college.

# EXPLANATION

This problem is mostly implementation, simulating the process of admission in colleges. First we reorder the students in the order of their rank. Hence student with rank 1 shall be admitted first, then student with second rank and so on.

The idea here is that we also need to keep track of lists corresponding to a student, so that when we reorder the students, the list is also reordered.

The best way to keep this relationship would be to encapsulate all information about the student, i.e. student id, student rank and list of college student has applied to, in a single object, so that we can reorder the whole information of student simultaneously.

An object would have class definition something like this

``class Student{
    int id, rank;
    list<Integer> appliedTo;
}
``

For colleges, all we need to do is to keep track whether the seat in that college is vacant or not, which can be done by a boolean array.

Hence, we consider all students one by one. For current student, we iterate over all college this student applied to, find the one having best rank among those having vacant seat. If no such college is found, this student doesn’t get admission. Otherwise this student is admitted in that particular college, and that college no longer has vacant seat.

Hence, by simulation of this process, we can find all colleges having vacant seats when student 1 is processed, easily finding the college with best rank among these, to which student 1 applied.

This college is the required answer.

If having trouble with implementation, refer solutions below.

# TIME COMPLEXITY

# SOLUTIONS

Setter's Solution
``#include<bits/stdc++.h>

using namespace std;

const int maxt = 1e5, maxn = 1e5, maxm = 1e5, maxapp = 1e6, maxtn = 250000, maxtm = 250000;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    int t; cin >> t;
    int tn = 0, tm = 0, tapp = 0;
    while(t--){
        int n, m; cin >> n >> m;
        tn += n; tm += m;
        int rank[n + 1]; set<int> urank; urank.clear();
        int prank;
        for(int i = 1; i <= n; i++){
            cin >> prank;
            rank[i] = prank; urank.insert(prank);
        }
        assert(urank.size() == n);

        int mark[m + 1]; set<int> umark; umark.clear();
        int pmark;
        for(int i = 1; i <= m; i++){
            cin >> pmark;
            mark[pmark] = i; umark.insert(pmark);
        }
        assert(umark.size() == m);

        vector<int> app[m + 1]; bool inc[m + 1]; memset(inc, false, sizeof(inc));
        for(int i = 1; i <= m; i++){
            app[i].clear();
            int k; cin >> k;
            tapp += k;
            int id;
            for(int j = 1; j <= k; j++){
                cin >> id;
                app[i].push_back(id);
            }
            sort(app[i].begin(), app[i].end(), [&rank](int &a, int &b){return rank[a] < rank[b];});
        }

        int ans[m + 1]; memset(ans, 0, sizeof(ans));
        for(int i = 1; i <= m; i++){
            vector<int> papp = app[mark[i]];
            for(int x : papp){
                if(!inc[x]){
                    ans[mark[i]] = x;
                    inc[x] = true;
                    break;
                }
            }
        }
        cout << ans[1] << endl;
    }
}
``

Tester's Solution
``#include <iostream>
#include <cassert>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <random>
#include <limits>

#ifdef HOME
#define NOMINMAX
#include <windows.h>
#endif

#define all(x) (x).begin(), (x).end()
#define rall(x) (x).rbegin(), (x).rend()
#define forn(i, n) for (int i = 0; i < (int)(n); ++i)
#define for1(i, n) for (int i = 1; i <= (int)(n); ++i)
#define ford(i, n) for (int i = (int)(n) - 1; i >= 0; --i)
#define fore(i, a, b) for (int i = (int)(a); i <= (int)(b); ++i)

template<class T> bool umin(T& a, T b) { return a > b ? (a = b, true) : false; }
template<class T> bool umax(T& a, T b) { return a < b ? (a = b, true) : false; }

using namespace std;

long long readInt(long long l, long long r, char endd) {
    long long x = 0;
    int cnt = 0;
    int fi = -1;
    bool is_neg = false;
    while (true) {
	    char g = getchar();
	    if (g == '-') {
		    assert(fi == -1);
		    is_neg = true;
		    continue;
	    }
	    if ('0' <= g && g <= '9') {
		    x *= 10;
		    x += g - '0';
		    if (cnt == 0) {
			    fi = g - '0';
		    }
		    cnt++;
		    assert(fi != 0 || cnt == 1);
		    assert(fi != 0 || is_neg == false);

		    assert(!(cnt > 19 || (cnt == 19 && fi > 1)));
	    }
	    else if (g == endd) {
		    assert(cnt > 0);
		    if (is_neg) {
			    x = -x;
		    }
		    assert(l <= x && x <= r);
		    return x;
	    }
	    else {
		    assert(false);
	    }
    }
}

string readString(int l, int r, char endd) {
    string ret = "";
    int cnt = 0;
    while (true) {
	    char g = getchar();
	    assert(g != -1);
	    if (g == endd) {
		    break;
	    }
	    // 		if(g == '\r')
	    // 			continue;

	    cnt++;
	    ret += g;
    }
    assert(l <= cnt && cnt <= r);
    return ret;
}
long long readIntSp(long long l, long long r) {
    return readInt(l, r, ' ');
}
long long readIntLn(long long l, long long r) {
    return readInt(l, r, '\n');
}
string readStringLn(int l, int r) {
    return readString(l, r, '\n');
}
string readStringSp(int l, int r) {
    return readString(l, r, ' ');
}

int main(int argc, char** argv)
{
#ifdef HOME
    if (IsDebuggerPresent())
    {
	    freopen("../ADMIT_0.in", "rb", stdin);
	    freopen("../out.txt", "wb", stdout);
    }
#endif
    int T = readIntLn(1, 2'500'000);
    forn(tc, T)
    {
	    int N = readIntSp(1, 2'500'000);
	    int M = readIntLn(1, 3'000'000);
	    vector<int> A(N);
	    vector<bool> UA(N);
	    forn(i, N)
	    {
		    if (i + 1 == N)
			    A[i] = readIntLn(1, N);
		    else
			    A[i] = readIntSp(1, N);
		    A[i]--;
		    assert(UA[A[i]] == false);
		    UA[A[i]] = true;
	    }
	    vector<int> S(M);
	    vector<bool> US(M);
	    forn(i, M)
	    {
		    if (i + 1 == M)
			    S[i] = readIntLn(1, M);
		    else
			    S[i] = readIntSp(1, M);
		    --S[i];
		    assert(US[S[i]] == false);
		    US[S[i]] = true;
	    }
	    vector<pair<int, vector<int>>> KV(M);
	    forn(i, M)
	    {
		    KV[i].first = i;
		    int K = readIntSp(1, 1'500'000);
		    forn(j, K)
		    {
			    int tmp;
			    if (j + 1 == K)
				    tmp = readIntLn(1, N);
			    else
				    tmp = readIntSp(1, N);
			    --tmp;
			    KV[i].second.push_back(tmp);
		    }
	    }

	    int res = 0;
	    vector<bool> student(M);
	    vector<bool> coll(N);
	    forn(i, M)
	    {
		    //find the best available student
		    int bestStId = -1, bestStVal = M + 1;
		    forn(j, M)
		    {
			    if (student[j] == false && bestStVal > S[j])
			    {
				    bestStId = j;
				    bestStVal = S[j];
			    }
		    }
		    student[bestStId] = true;
		    //find best available college
		    int bestCollId = -1, bestCollVal = N + 1;
		    const auto& actkv = KV[bestStId];
		    for(const auto actkvi : actkv.second)
		    {
			    if (coll[actkvi] == false && bestCollVal > A[actkvi])
			    {
				    bestCollId = actkvi;
				    bestCollVal = A[actkvi];
			    }
		    }
		    if (bestCollId != -1)
		    {
			    coll[bestCollId] = true;
			    if (bestStId == 0)
			    {
				    res = bestCollId + 1;
				    break;
			    }
		    }
	    }
	    printf("%d\n", res);

// 		int res = 0;
// 		vector<bool> coll(N);
// 		sort(KV.begin(), KV.end(), [&S](const auto& a, const auto& b)->bool {
// 			return S[a.first] < S[b.first];
// 			});
// 		for (auto& kvi : KV)
// 		{
// 			int act = kvi.first;
// 			auto& akv = kvi.second;
// 			sort(akv.begin(), akv.end(), [&A](const auto& a, const auto& b)->bool {
// 				return A[a] < A[b];
// 				});
// 			for (const auto& akvi : akv)
// 			{
// 				if (coll[akvi] == false)
// 				{
// 					if (act == 0)
// 						res = akvi + 1;
// 					coll[akvi] = true;
// 					break;
// 				}
// 			}
// 		}
// 		printf("%d\n", res);
    }
    assert(getchar() == -1);
    return 0;
}
``

Editorialist's Solution
``import java.util.*;
import java.io.*;
class ADMIT{
    //SOLUTION BEGIN
    void pre() throws Exception{}
    void solve(int TC) throws Exception{
        //zero based indexing everywhere
        int N = ni(), M = ni();
        int[] collegeRank = new int[N];
        for(int i = 0; i< N; i++)collegeRank[i] = ni()-1;
        int[] score = new int[M];
        for(int i = 0; i< M; i++)score[i] = ni()-1;
        Student[] students = new Student[M];
        for(int i = 0; i< M; i++){
            int[] applied = new int[ni()];
            for(int j = 0; j< applied.length; j++)applied[j] = ni()-1;
            students[i] = new Student(i, score[i], applied);
        }
        Arrays.sort(students);
        boolean[] available = new boolean[N];
        Arrays.fill(available, true);
        int ans = -1;
        for(Student s:students){
            int assigned = -1;
            for(int college:s.appliedTo){
                if(!available[college])continue;
                if(assigned == -1 || collegeRank[college] < collegeRank[assigned])assigned = college;
            }
            if(assigned != -1)available[assigned] = false;
            if(s.id == 0){
                ans = assigned;
                break;
            }
        }
        pn(1+ans);
    }
    class Student implements Comparable<Student>{
        int id, rank;
        int[] appliedTo;
        public Student(int id, int rank, int[] applied){
            this.id = id;
            this.rank = rank;
            appliedTo = applied;
        }
        public int compareTo(Student s){return Integer.compare(rank, s.rank);}
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
        new ADMIT().run();
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

# VIDEO EDITORIAL:

Feel free to share your approach. Suggestions are welcomed as always.

</details>
