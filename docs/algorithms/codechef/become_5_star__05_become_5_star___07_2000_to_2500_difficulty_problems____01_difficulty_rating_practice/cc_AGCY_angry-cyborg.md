# Angry Cyborg

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | AGCY |
| Difficulty Rating | 2072 |
| Difficulty Band | 2000 to 2500 difficulty problems |
| Path | Become 5 star |
| Lesson | 2000 to 2500 difficulty problems |
| Official Link | [AGCY](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/AGCY) |

---

## Problem Statement

Cyborg Jenish is angry.

He has so much rage that he decided to go on a demolition spree for $Q$ days.

There are $N$ cities in his world numbered $1$ to $N$, in a row from left to right. That is the $i^{th}$ city from left side is city-$i$ where $1 \leq i \leq N$. The supreme leader of the world is VSM and there are infinite statues of VSM in each city.

On each day Jenish chooses two cities $L$ and $R$. He starts at city-$L$ and moves along the row towards right side till he reaches the city-$R$. In city-$L$ he destroys $1$ statue, in the next city (i.e. city-$L+1$) he destroys $2$ statues, and so on till city-$R$ where he destroys  $R-L+1$ statues. In other words, he destroys $i-L+1$ statues in the $i^{th}$ city ( $L\leq i\leq R$ ).

Find the total number of VSM statues he destroyed in each city after $Q$ days.

### Input:
- The first line contains an integer $T$, denoting the number of test cases.
- The first line of each test case, contains two space-separated integers $N$ and $Q$ denoting the number of cities in his world and  the number of days he goes on a demolition spree respectively.
- The $i^{th}$ line of next $Q$ lines of each test case contains two space-separated integers $L$ and $R$ denoting the starting city and the ending city respectively on $i^{th}$ day.

###Output:
- For each test case, output a single line containing $N$ space-separated integers.
- The $i^{th}$ integer should denote the total number of VSM statues destroyed by cyborg Jenish in the city-$i$ after $Q$ days.

### Constraints:
- $1 \leq  T \leq 10^3$
- $ 1 \leq N \leq 10^5$
- $1 \leq Q \leq 10^5$
- $1\leq L \leq R \leq N$
- The sum of $N$ over all test cases is less than $10^{6}$
- The sum of $Q$ over all test cases is less than $10^{6}$

---

## Examples

**Example 1**

**Input**

```text
2
5 3
1 3
1 2
4 5
2 1
1 1
```

**Output**

```text
2 4 3 1 2
1 0
```

**Explanation**

In the first test case, the cyborg does the following:
- Starts at city-1 and goes till city-3, hence destroys $1$ statue in city-1, $2$ in city-2, and $3$ in city-3.
- Starts at city-1 and goes till city-2, hence destroys $1$ statue in city-1 and $2$ in city-2.
- Starts at city-4 and goes till city-5, hence destroys $1$ statue in city-4 and $2$ in city-5.
- Hence he destroyed total $2$ statues in city-1, $4$ in city-2, $3$ in city-3, $1$ in city-4, and $2$ in city-5.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5 3
1 3
1 2
```

**Output for this case**

```text
2 4 3 1 2
```



#### Test case 2

**Input for this case**

```text
4 5
2 1
1 1
```

**Output for this case**

```text
1 0
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Practice](https://www.codechef.com/BYTR20A/problems/AGCY)

*Author:* [Vaishakh SM](https://www.codechef.com/users/vaishakh_sm)

*Tester:* [ Smit Mandavia](https://www.codechef.com/users/l_returns)

*Editorialist:* [Vaishakh SM](https://www.codechef.com/users/vaishakh_sm)

# DIFFICULTY:

Easy

# PREREQUISITES:

Knowledge of [prefix sums](https://en.wikipedia.org/wiki/Prefix_sum)

# PROBLEM:

Given an array, A of size N initially filled with 0's, for each query containing two integers L,R add 1 to A[L] , 2 to A[L+1] … R-L+1 to A[R]. In general, add i+1 to A[L+i] for every L\leq i \leq R.

# QUICK EXPLANATION:

- In an array initially filled with 0's, use standard prefix sums to first add 1 to each L,R query, let this array be B.

- Subtract R-L+1 from A[R+1] for each query (store the queries beforehand)

- Take prefix sum of B and print B[1] to B[N]

# EXPLANATION:

Let us first try to solve a simpler question, how can we add 1 to each L,R query, we will later see how the original question is essentially the same as this simpler question.

For adding 1 to each L,R query, we first start with an array filled with 0's (say A), then we add 1 to each A[L] and subtract 1 from each A[R]. Then we take the prefix sum of A.

Now, observe that if we take the prefix sum of 1,1,1,-3, we get 1,2,3,0. Hence we have added 1,2,3 to A[0], A[1],A[2] respectively. Using this logic we can see that in general if we have M, 1's in an array followed by -M and if we take the prefix sum of the array we have added 1,2,... M to the first M indices of the array.

Hence, we will first add 1 in an initially empty array for each L,R query, then we will subtract R-L+1 from A[R+1] for each query and take prefix sum again to get the desired result.

## TIME COMPLEXITY

Time complexity is O(N + Q), where N is size of array and Q is number of queries for each testcase.

## SOLUTIONS

Setter's Solution
``#include<bits/stdc++.h>
using namespace std;
typedef long long int lli;

int main()
{
	lli t,n,q,l,r;

	cin>>t;

	while(t--)
	{
		cin>>n>>q;

		vector<lli> arr(n+3);

		vector<pair<lli,lli>> Indices;

		while(q--)
		{
			cin>>l>>r;

			arr[l]++;
			arr[r+1]--;
			// Adding 1 to arr[l] and subtracting 1
			// from arr[r+1] as mentioned in editorial

			Indices.push_back({l,r+1});
		}

		for(int i =1;i<=n;i++)
		{
			arr[i]+=(arr[i-1]);
		}
		// Taking prefix sum to add 1 to each L,R query

		for(auto x:Indices) arr[x.second]-=(x.second-x.first);
		// After generating the array where the queries are increased with 1
		// I am subtracting R-L+! to r+1th index

		for(int i =1;i<=n;i++)
		{
			arr[i]+=(arr[i-1]);
		}
		// Taking prefix sum again

		for(int i=1;i<=n;i++)cout<<arr[i]<<" ";
		//Final output

		cout<<endl;
	}
}
``

Tester's Solution
``    #include<bits/stdc++.h>
using namespace std;

#define ll long long int
#define FIO ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0)
#define mod 1000000007

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
            cerr << (int)g << "\n";
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

int main()
{
    FIO;
    int t,n,q,k,i,j,sum_n,sum_q;

    t=readIntLn(1,1000);
    sum_n=0;
    sum_q=0;
    while(t--){
        n=readIntSp(1,100000);
        q=readIntLn(1,100000);
        sum_n+=n;
        sum_q+=q;
        ll arr[n+3]={0};
        while(q--){
            j=readIntSp(1,n);
            k=readIntLn(j,n);
            arr[j]++;
            arr[k+1]--;
            arr[k+1]-=(k-j+1);
            arr[k+2]+=(k-j+1);
        }
        for(i=1;i<=n;i++)
            arr[i]+=arr[i-1];
        for(i=1;i<=n;i++)
            arr[i]+=arr[i-1];

        for(i=1;i<=n;i++)
            cout << arr[i] << " ";
        cout << "\n";
    }
    assert(getchar()==-1);
	assert(sum_n<=1000000);
	assert(sum_q<=1000000);
	return 0;
}
``

</details>
