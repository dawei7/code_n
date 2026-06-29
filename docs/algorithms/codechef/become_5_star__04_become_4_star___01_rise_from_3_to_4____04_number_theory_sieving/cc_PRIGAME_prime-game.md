# Prime Game

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PRIGAME |
| Difficulty Rating | 1792 |
| Difficulty Band | Rise from 3* to 4* |
| Path | Become 5 star |
| Lesson | Number Theory - Sieving |
| Official Link | [PRIGAME](https://www.codechef.com/practice/course/3to4stars/LP3TO404/problems/PRIGAME) |

---

## Problem Statement

Chef and Divyam are playing a game with the following rules:
- First, an integer $X!$ is written on a board.
- Chef and Divyam alternate turns; Chef plays first.
- In each move, the current player should choose a positive integer $D$ which is divisible by up to $Y$ distinct primes and does not exceed the integer currently written on the board. Note that $1$ is not a prime.
- $D$ is then subtracted from the integer on the board, i.e. if the integer written on the board before this move was $A$, it is erased and replaced by $A-D$.
- When one player writes $0$ on the board, the game ends and this player wins.

Given $X$ and $Y$, determine the winner of the game.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains two space-separated integers $X$ and $Y$.

### Output
For each test case, print a single line containing the string `"Chef"` if Chef wins the game or `"Divyam"` if Divyam wins (without quotes).

### Constraints
- $1 \leq T \leq 10^6$
- $1 \leq X,Y \leq 10^6$

### Subtasks
**Subtask #1 (5 points):** $Y=1$

**Subtask #2 (10 points):**
- $1 \leq T \leq 10^2$
- $1 \leq X \leq 6$

**Subtask #3 (85 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
3
1 2
3 1
2021 42
```

**Output**

```text
Chef
Divyam 
Divyam
```

**Explanation**

**Example case 1:** Since $D = 1$ is divisible by $0$ primes, Chef will write $0$ and win the game in the first move.

**Example case 2:** Chef must choose $D$ between $1$ and $5$ inclusive, since $D = 6$ is divisible by more than one prime. Then, Divyam can always choose $6-D$, write $0$ on the board and win the game.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1 2
```

**Output for this case**

```text
Chef
```



#### Test case 2

**Input for this case**

```text
3 1
```

**Output for this case**

```text
Divyam
```



#### Test case 3

**Input for this case**

```text
2021 42
```

**Output for this case**

```text
Divyam
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Practice](https://www.codechef.com/problems/PRIGAME)

[Div-3 Contest](https://www.codechef.com/FEB21C/problems/PRIGAME)

[Div-2 Contest](https://www.codechef.com/FEB21B/problems/PRIGAME)

[Div-1 Contest](https://www.codechef.com/FEB21A/problems/PRIGAME)

***Author:*** [Divyam Singal](https://www.codechef.com/users/div5252)

***Testers:*** [Felipe Mota](https://www.codechef.com/users/fmota) and [Radoslav Dimitrov](https://www.codechef.com/users/radoslav192)

***Editorialist:*** [Divyam Singal](https://www.codechef.com/users/div5252)

# DIFFICULTY:

Easy-Medium

# PREREQUISITES:

Game Theory, Number Theory

# PROBLEM:

Chef and Divyam are playing a game with the following rules:

- First, an integer X! is written on a board.

- Chef and Divyam alternate turns; Chef plays first.

- In each move, the current player should choose a positive integer D which is divisible by up to Y distinct primes and does not exceed the integer currently written on the board. Note that 1 is not a prime.

-
D is then subtracted from the integer on the board, i.e. if the integer written on the board before this move was A, it is erased and replaced by A?D.

- When one player writes 0 on the board, the game ends and this player wins.

Given X and Y, determine the winner of the game.

# QUICK EXPLANATION:

Let A denote the product of first (Y+1) primes. Then the first player wins if X! is not divisible by A, else second player wins.

Let the number on the board currently be N. This game can be considered as having two states, one in which N is divisible by A, call it the **divisible** state and other where N is not divisible by A, call it the **not divisible** state.

We can’t go from a **divisible** state to a **divisible** state after a move as it would mean the number which has been subtracted should also be a multiple of A which is not possible.

And we can go from a **non divisible** state to a **divisible** state, by removing the remainder of dividing N by A.

So if X! is not divisible by A, the first player can always play to ensure he gets a **non divisible** number each time, to which he converts it into a **divisible** number for the second player. As 0 is a **divisible** state, the first player would win. Similar strategy works for second player in the case X! is divisible by A.

# EXPLANATION:

We introduce a variable A, which is the product of the first (Y+1) primes.

Let us get some intuition as to why we have chosen such a number A.

**Lemma 1:** The difference between two multiples of A will have at least Y+1 distinct prime factors.

Proof of Lemma 1

Let the first Y+1 prime factors be P_1,P_2, \dots ,P_{Y+1} and let the two multiples of A be a_1 and a_2

We can write a_1 and a_2 as-

a_1=K_1P_1P_2\dots P_{Y+1}

a_2=K_2P_1P_2\dots P_{Y+1}

where k_1 and k_2 are some positive integers.

Then a_1-a_2=(K_1-K_2)P_1P_2\dots P_{Y+1}, and hence it has at least Y+1 distinct prime factors P_1,P_2, \dots ,P_{Y+1}.

**Lemma 2:** The remainder after dividing a non-multiple of A by A will have at most Y distinct prime factors.

Proof of Lemma 2

Let a non-multiple of A be a.

By the Euclid’s Division lemma, we can write a=bA+r, where 0 \le r < A.

For the sake of contradiction, let us assume that the remainder r is divisible by at least Y+1 primes.

The product of at least Y+1 distinct primes will be more than A, as A is the product of the first Y+1 primes. This will lead to contradiction due to the fact that r<A.

We now define the two states of the game. Let the number on the board currently be N.

The state is called **divisible** if N is divisible by A and the state is called **non-divisible** if N is not divisible by A.

Let us think about the transitions in these two states. Here transition means a change in state after a player’s move.

**Lemma 3:** From a **divisible** state, we are forced to go to a **non-divisible** state.

Proof of Lemma 3

For the sake of contradiction, let us assume that we can go from a **divisible** to a **divisible** state. Using Lemma 1, we know that the difference between them have at least Y+1 prime factors, which is not possible as a move consists of subtracting a number having at most Y prime factors.

So from a **divisible** state, we can only (forcefully) go to a **non-divisible** state.

**Lemma 4**: From a **non-divisible** state, we can go to a **divisible** state.

Proof of Lemma 4

From Lemma 2, we know that the remainder after dividing a non-multiple by A will have at most Y distinct prime factors. Subtracting the remainder of dividing N by A will be a valid move as it will have at most Y distinct prime factors. The number after subtracting the remainder will be a multiple of A.

Now in our game, having a **non-divisible** state is a winning state. This is because 0 is a divisible state, so the player having a **non-divisible** state can only arrive to 0.

Using Lemmas 3 and 4, we observe that a player can maintain the **non-divisible** state. This is because from a **non-divisible** state, the other player will get a **divisible** state. And from the **divisible** state, the player is helpless, leaving a **non-divisible** state for this initial player.

So Chef i.e. the first player will win the game if he starts with the **non-divisible** state, otherwise Divyam i.e. the second player will win the game.

Our problem reduces to just checking whether X! is divisible by the product of first Y+1 primes or not.

To check this, we will first find all the prime numbers from 1 to 10^6. This can be done by using the Sieve approach.

Sieve method
``for(int i=0;i<1000001;i++)
{
    prime[i]=1;    //initially every number is marked as prime
}
for(int i=2;i*i<=1000000;i++)
{
    if(prime[i]==1)
    {
        //marking multiples of i as non-prime
        for(int j=2*i;j<=1000000;j+=i)
        {
            prime[j]=0;
        }
    }
}
//Time complexity is O(nlogn)
``

Next we will find the prefix sum of the primes, which stores the count of primes not greater than it.

This is the pre-build work, which can be done in O(XlogX).

Then for each test case, all we do is compare the pref\_sum[X], which we calculated above with Y+1. If it is smaller, Chef (first player) wins and otherwise Divyam (second player) wins.

So each test case takes O(1) time.

The total time complexity is O(XlogX+T).

# SOLUTIONS:

Setter's Solution
``#include <bits/stdc++.h>
using namespace std;
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
using namespace __gnu_pbds;
#define ll long long
#define vll vector<ll>
#define ld long double
#define pll pair<ll,ll>
#define PB push_back
#define MP make_pair
#define F first
#define S second
#define oset tree<int, null_type, less<int>, rb_tree_tag, tree_order_statistics_node_update>
#define osetll tree<ll, null_type, less<ll>, rb_tree_tag, tree_order_statistics_node_update>
#define ook order_of_key
#define fbo find_by_order
const int MOD=1000000007; //998244353
long long int inverse(long long int i){
    if(i==1) return 1;
    return (MOD - ((MOD/i)*inverse(MOD%i))%MOD+MOD)%MOD;
}
ll POW(ll a,ll b)
{
    if(b==0) return 1;
    if(b==1) return a%MOD;
    ll temp=POW(a,b/2);
    if(b%2==0) return (temp*temp)%MOD;
    else return (((temp*temp)%MOD)*a)%MOD;
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    ll prime[1000001],pre[1000001];
    for(int i=0;i<1000001;i++)
    {
        prime[i]=1;
    }
    for(int i=2;i*i<=1000000;i++)
    {
        if(prime[i]==1)
        {
            for(int j=2*i;j<=1000000;j+=i)
            {
                prime[j]=0;
            }
        }
    }
    pre[0]=0;
    pre[1]=0;
    for(int i=2;i<=1000000;i++)
    {
        pre[i]=pre[i-1]+prime[i];
    }
    ll t;
    cin>>t;
    for(int i=0;i<t;i++)
    {
        ll x,y;
        cin>>x>>y;
        if(pre[x]<y+1) cout<<"Chef";
        else cout<<"Divyam";
        cout<<"\n";
    }
}
``

Tester's Solution
``#include <bits/stdc++.h>
using namespace std;
template<typename T = int> vector<T> create(size_t n){ return vector<T>(n); }
template<typename T, typename... Args> auto create(size_t n, Args... args){ return vector<decltype(create<T>(args...))>(n, create<T>(args...)); }
long long readInt(long long l,long long r,char endd){
	long long a;
	cin >> a;
	return a;
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
int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	const int maxy = 20000000;
	vector<int> factor(maxy + 1, -1), primes;
	for(int i = 2; i <= maxy; i++){
		if(factor[i] == -1){
			primes.push_back(i);
			for(int j = i; j <= maxy; j += i){
				if(factor[j] == -1)
					factor[j] = i;
			}
		}
	}
	int t = readIntLn(1, 1000000);
	while(t--){
		int x, y;
		x = readIntSp(1, 1000000);
		y = readIntLn(1, 1000000);
		if(x >= primes[y]) cout << "Divyam\n";
		else cout << "Chef\n";
	}
	return 0;
}
``

</details>
