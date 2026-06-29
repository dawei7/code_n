# Football

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MSNSADM1 |
| Difficulty Rating | 1102 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1000 to 1200 difficulty problems |
| Official Link | [MSNSADM1](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1200/problems/MSNSADM1) |

---

## Problem Statement

A football competition has just finished. The players have been given points for scoring goals and points for committing fouls. Now, it is up to Alex to find the best player in the tournament. As a programmer, your job is to help Alex by telling him the highest number of points achieved by some player.

You are given two sequences $A_1, A_2, \ldots, A_N$ and $B_1, B_2, \ldots, B_N$. For each valid $i$, player $i$ scored $A_i$ goals and committed $B_i$ fouls. For each goal, the player that scored it gets $20$ points, and for each foul, $10$ points are deducted from the player that committed it. However, if the resulting number of points of some player is negative, this player will be considered to have $0$ points instead.

You need to calculate the total number of points gained by each player and tell Alex the maximum of these values.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains a single integer $N$.
- The second line contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$.
- The third line contains $N$ space-separated integers $B_1, B_2, \ldots, B_N$.

### Output
For each test case, print a single line containing one integer ― the maximum number of points.

### Constraints
- $1 \le T \le 100$
- $1 \le N \le 150$
- $0 \le A_i \le 50$ for each valid $i$
- $0 \le B_i \le 50$ for each valid $i$

### Subtasks
**Subtask #1 (30 points):** $1 \le N \le 2$

**Subtask #2 (70 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
2
3
40 30 50
2 4 20
1
0
10
```

**Output**

```text
800
0
```

**Explanation**

**Example case 1:** The first player gets $800$ points for scoring goals and has $20$ points deducted for fouls. Likewise, the second player gets $560$ points and the third player gets $800$ points. The third player is the one with the maximum number of points.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3
40 30 50
2 4 20
```

**Output for this case**

```text
800
```



#### Test case 2

**Input for this case**

```text
1
0
10
```

**Output for this case**

```text
0
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Div1](https://www.codechef.com/AUG19A/problems/MSNSADM1)

[Div2](https://www.codechef.com/AUG19B/problems/MSNSADM1)

[Practice](https://www.codechef.com/problems/MSNSADM1)

**Setter-**  [Md. Shafiq Newaj Shovo](https://www.codechef.com/users/leoshovo)

**Tester-**  [Suchan Park](https://www.codechef.com/users/tncks0121)

**Editorialist-** [Abhishek Pandey](https://www.codechef.com/users/vijju123)

### DIFFICULTY:

CAKEWALK

### PRE-REQUISITES:

[Basic Looping and Arrays](https://www.google.com/search?q=30+days+of+code+hackerrank&rlz=1C1EJFC_enIN840IN840&oq=30+days+of+code+hackerra&aqs=chrome.0.0j69i57j0l4.2947j0j4&sourceid=chrome&ie=UTF-8)

### PROBLEM:

Given 2 arrays A and B, find the maximum value of 20*A_i-10*B_i. If the maximum value is negative, print 0.

### QUICK-EXPLANATION:

**Key to AC-** Ability to express your logic as code.

The question can be solved using a single for loop for computing A_i*20 - B_i*10. Use the max() function in your language to conveniently find out the maximum and keep track of it.

### EXPLANATION:

There is not much to elaborate on this question, except the fact that this question just tests your basic concepts of any programming language, and a fundamental ability to code.

In case you are unfamiliar with arrays , loops etc. , go to the link at pre-requisite and see try to grasp them. Since C++ is a popular language for competitive coding, we will discuss a C++ implementation of the question. While doing so, it is assumed that you know what are loops, arrays and other fundamentals.

The first, and fortunately, the only step you need to do in the question after taking the input is to find max(A_i*20-B_i*10), as given in the problem statement itself.

So lets start with initializing our answer variable. Unintitialized variables in C++ hold garbage values, and hence we should initialize the value to a proper value. A variable which is to hold maximum of the values should be initialized with the least possible values - unless the question requires you to initialize it with another special value.  In our case, the least possible value of answer is 0 (as score is never negative as said in the problem).

On the same note, know that initializing an array of dynamic size is undefined behavior in C++ !! Example - `int arr[n]={0}` can lead to undefined behavior if `n` is not known at compile time!

Also, we will be using the max() function of C++ - this function takes in 2 numbers and returns the higher one out of the 2. Hence, you can frame the logic as below-

- Iterate through all indices i=[1,N].

- Calculate Ans=max(ans,A_i*20,B_i*10)

- Print the answer finally.

A C++ implementation of it is given below.

C++ Implementation
``        ans=0;
	    for(i=0;i<n;i++)
	    {
	        ans=max(ans,a[i]*20-b[i]*10);
	    }
	    cout<<ans<<endl;
``

And thats it, we are done with one of the first problems of this long challenge!

### SOLUTION

Setter
``#include <bits/stdc++.h>
using namespace std;
int A [156];
int B [156];
int C [156];
int main()
{

    //For the test case.
    int tc;
    cin>>tc;
    while(tc--){

    int n,c;

    // Length of the array
    cin>>n;
    assert(n>0 && n<=150);
    for(int i=0; i<n ; i++)
    {
        cin>>A[i];
        assert( A[i]>=0 && A[i]<=50 );
    }
    for(int i=0 ; i<n ; i++)
    {
        cin>>B[i];
        assert( B[i]>=0 && B[i]<=50 );

    }
      //Calculating the value of each players point
    for(int i=0 ; i<n ;  i++)
    {
        C[i]=(A[i]*20)-(B[i]*10);
    }

    int Mx= -1000;
    //Finding out the maximum point.
    for(int i=0; i<n ; i++)
    {
        Mx= max(Mx,C[i]);
    }

    if( Mx<=0 ) cout<<0<<endl;
    else cout<<Mx<<endl;

    }

}
``

Tester(KOTLIN)
``fun main(Args: Array<String>) {
  repeat(readLine()!!.toInt()) {
    val N = readLine()!!.toInt()
    val A = readLine()!!.split(" ").map{ it.toInt() }
    val B = readLine()!!.split(" ").map{ it.toInt() }
    println(maxOf(0, A.zip(B).map{ (a, b) -> 20*a - 10*b }.max()!!))
  }
}
``

Editorialist
``/*
 *
 ********************************************************************************************
 * AUTHOR : Vijju123                                                                        *
 * Language: C++14                                                                          *
 * Purpose: -                                                                               *
 * IDE used: Codechef IDE.                                                                  *
 ********************************************************************************************
 *
 Comments will be included in practice problems if it helps ^^
 */

#include <iostream>
#include<bits/stdc++.h>
using namespace std;

//I never understand why people put useless functions at top of code. Makes it so unreadable ughhhh.
int mod=pow(10,9)+7;
int fastExpo(long long a,long long n, int mod)
{
    a%=mod;
    if(n==2)return a*a%mod;
    if(n==1)return a;
    if(n&1)return a*fastExpo(fastExpo(a,n>>1,mod),2,mod)%mod;
    else return fastExpo(fastExpo(a,n>>1,mod),2,mod);
}
inline void add(vector<vector<int> > &a,vector<vector<int> > &b,int mod)
{
    for(int i=0;i<a.size();i++)for(int j=0;j<a[0].size();j++)b[i][j]=(b[i][j]+a[i][j])%mod;
}

void multiply(vector<vector<int> > &a, vector<vector<int> > &b,int mod,vector<vector<int> > &temp)
{
    assert(a[0].size()==b.size());
    int i,j;
    for(i=0;i<a.size();i++)
    {
        for(j=0;j<b[0].size();j++)
        {
            temp[i][j]=0;
            for(int p=0;p<a[0].size();p++)
            {
                temp[i][j]=(temp[i][j]+1LL*a[i][p]*b[p][j])%mod;
            }
        }
    }
}

void MatExpo(vector<vector<int> > &arr,int power,int mod)
{
    int i,j,k;
    vector<vector<int> >temp,temp2,temp3;
    vector<int> init(arr[0].size());
    for(i=0;i<arr.size();i++){temp.push_back(init);}
    temp3=temp;
    temp2=temp;
    for(i=0;i<arr.size();i++)temp3[i][i]=1;
    while(power>0)
    {
        if(power&1)
        {
            multiply(arr,temp3,mod,temp);
            swap(temp3,temp);
        }
        multiply(arr,arr,mod,temp2);
        swap(arr,temp2);
        power>>=1;
    }
    swap(arr,temp3);
}

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

vector<int> primes;
int isComposite[1000001]={1,1};
void sieve()
{
    int i,j;
    for(i=2;i<=1000000;i++)
    {
        if(!isComposite[i])
        {
            primes.push_back(i);
            isComposite[i]=i;
        }
        for(j=0;j<primes.size() and i*primes[j]<=1000000;j++)
        {
            isComposite[primes[j]*i]=i;
            if(i%primes[j]==0)break;
        }
    }
}

int main() {
	// your code goes here
	#ifdef JUDGE
	string in,out;
	cin>>in>>out;
	in+=".in";
	if(in!="z.in")
        out+=".out";
    else out+=".in";
	if(in!="z.in")
    freopen(in.c_str(), "rt", stdin);
    freopen(out.c_str(), "wt", stdout);
    #endif
	ios_base::sync_with_stdio(0);
	cin.tie(NULL);
	cout.tie(NULL);
	srand(time(NULL));
	mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());

	int t;
	cin>>t;
	while(t--)
	{
	    int n;
	    cin>>n;
	    int i;

	    int ans=0;
	    int a[n],b[n];
	    for(i=0;i<n;i++)cin>>a[i];
	    for(i=0;i<n;i++)cin>>b[i];

	    ans=0;
	    for(i=0;i<n;i++)
	    {
	        ans=max(ans,a[i]*20-b[i]*10);
	    }
	    cout<<ans<<endl;

	}

	assert(getchar()==-1);
	return 0;
}
``

Time Complexity=O(N)

Space Complexity=O(N)

### CHEF VIJJU’S CORNER

List of Common Errors

- Getting wrong answer because you are not printing 0 if max(A_i,*20-B_i*10) is negative.

- Getting a wrong answer because you are printing redundant print statements (Eg- “Enter a number”) or not printing the answer in a new line. **STICK STRICTLY TO THE INPUT OUTPUT FORMAT SPECIFIED BY THE QUESTION.**

- Getting a runtime error due to index out of bounds exception.

- Getting wrong answer due to unintialized variable - especially if its the one where you are holding the maximum.

Setter's Notes

For each test case, we have the find (A[i]*20-B[i]*10) for each player.Among them we need to find the highest points, if none of the value is positive value then answer is zero.

Related Problems

- [Appy and Contest](https://www.codechef.com/problems/HMAPPY2)

- [Chef and Rainbow Array](https://www.codechef.com/problems/RAINBOWA)

- [Cats and Dogs](https://www.codechef.com/problems/CATSDOGS)

- [Fancy Quotes](https://www.codechef.com/problems/FANCY)

</details>
