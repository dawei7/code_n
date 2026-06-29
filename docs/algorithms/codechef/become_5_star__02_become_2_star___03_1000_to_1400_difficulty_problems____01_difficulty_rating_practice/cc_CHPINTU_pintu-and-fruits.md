# Pintu and Fruits

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CHPINTU |
| Difficulty Rating | 1313 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1200 to 1400 difficulty problems |
| Official Link | [CHPINTU](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1400/problems/CHPINTU) |

---

## Problem Statement

Chef went to Australia and saw the destruction caused by bushfires, which made him sad, so he decided to help the animals by feeding them fruits. First, he went to purchase fruits from Pintu.

Pintu sells $M$ different types of fruits (numbered $1$ through $M$). He sells them in $N$ baskets (numbered $1$ through $N$), where for each valid $i$, the $i$-th basket costs $P_i$ and it contains fruits of type $F_i$. Chef does not have too much money, so he cannot afford to buy everything; instead, he wants to choose one of the $M$ available types and purchase all the baskets containing fruits of that type.

Help Chef choose the type of fruit to buy such that he buys at least one basket and the total cost of the baskets he buys is the smallest possible.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains two space-separated integers $N$ and $M$.
- The second line contains $N$ space-separated integers $F_1, F_2, \ldots, F_N$.
- The third line contains $N$ space-separated integers $P_1, P_2, \ldots, P_N$.

### Output
For each test case, print a single line containing one integer ― the minimum price Chef must pay.

### Constraints
- $1 \le T \le 1,000$
- $1 \le M, N \le 50$
- $1 \le F_i \le M$ for each valid $i$
- $0 \le P_i \le 50$ for each valid $i$

### Subtasks
**Subtask #1 (30 points):** $M = 2$

**Subtask #2 (70 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
1
6 4
1 2 3 3 2 2
7 3 9 1 1 1
```

**Output**

```text
5
```

**Explanation**

**Example case 1:**
- The sum of all baskets with fruits of type $1$ is $7$.
- The sum of all baskets with fruits of type $2$ is $5$.
- The sum of all baskets with fruits of type $3$ is $10$.
- The sum of all baskets with fruits of type $4$ is $0$ because there are no such baskets.

Chef can only choose fruits of type $1$, $2$ or $3$. Therefore, the minimum price he has to pay is $5$.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Practice](https://www.codechef.com/problems/CHPINTU)

[Div-2 Contest](https://www.codechef.com/MARCH20B/problems/CHPINTU)

*Author:* [Manav Patel](https://www.codechef.com/users/euler_euler)

*Tester:* [Suchan Park](https://www.codechef.com/users/tncks0121)

*Editorialist:* [William Lin](https://www.codechef.com/users/tmwilliamlin)

# DIFFICULTY:

Cakewalk

# PREREQUISITES:

Ad-hoc

# PROBLEM:

There are M types of fruits and N baskets of fruits. Each basket contains one type of fruit and has a certain non-negative price. You want to select a fruit such that there exists at least one basket with that fruit and you should buy all baskets with that fruit. Find the minimum possible cost.

# QUICK EXPLANATION:

Iterate over each fruit type and check it.

# EXPLANATION:

To be able to choose a fruit i, there must be at least one basket containing fruit i. To check if fruit i can be chosen, we can loop through all baskets to find any basket with fruit i:

``bool found=false;
for(int j=0; j<n; ++j) {
	if(f[j]==i) {
		found=true;
	}
}
//if found is true then we can choose fruit i
``

Let’s calculate the cost of choosing fruit i, which will be the sum of the prices of the baskets with fruit i. We can make a few changes to our previous code:

``bool found=false;
int sum=0;
for(int j=0; j<n; ++j) {
	if(f[j]==i) {
		found=true;
		sum+=p[j];
	}
}
//if found is true then we can choose fruit i
//sum is the cost of choosing fruit i
``

Lastly, we should run the code above for each fruit i so that we can find which fruits can be chosen and the costs of those fruits. Our answer is the minimum cost out of all fruits which can be chosen.

``int ans=1e9; //some arbitrarily large value
for(int i=1; i<=m; ++i) {
	//try fruit i
	bool found=false;
	int sum=0;
	for(int j=0; j<n; ++j) {
		if(f[j]==i) {
			found=true;
			sum+=p[j];
		}
	}
	//if found is true then we can choose fruit i
	//sum is the cost of choosing fruit i
	if(found) {
		//update the answer with the cost for fruit i
		ans=min(sum, ans);
	}
}
//ans is now the answer
``

# HIDDEN TRAPS:

- It is insufficient to check if the sum of costs of the baskets for a fruit is positive to determine if a type of fruit has at least one basket. This is because the prices of baskets can be 0.

# SOLUTIONS:

Setter's Solution
``#include <bits/stdc++.h>
using namespace std;
void solve()
{
    int N, M;
    cin >> N >> M;  // M - Fruits, N - Baskets
    int F[N], P[N];
    for(int i = 0; i < N; i++)
    {
        cin >> F[i];
    }
    for(int i = 0; i < N; i++)
    {
        cin >> P[i];
    }
    int final_price = 1000000;
    for(int i = 1; i <= M; i++)
    {
        int price = 0;
        bool flag = false;
        for(int j = 0; j < N; j++)
        {
            if(F[j] == i)
            {
                price += P[j];
                flag = true;
            }
        }
        if(flag)
        {
        	if(price < final_price)
        	{
        		final_price = price;
			}
		}
    }
	cout << final_price << "\n";
}

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        solve();
    }
    return 0;
}
``

Tester's Solution
``#include <bits/stdc++.h>

const int BUFFER_SIZE = int(1.1e5);

char _buf[BUFFER_SIZE + 10];
int _buf_pos, _buf_len;

char seekChar() {
    if(_buf_pos >= _buf_len) {
        _buf_len = fread(_buf, 1, BUFFER_SIZE, stdin);
        _buf_pos = 0;
    }
    assert(_buf_pos < _buf_len);
    return _buf[_buf_pos];
}

bool seekEof() {
    if(_buf_pos >= _buf_len) {
        _buf_len = fread(_buf, 1, BUFFER_SIZE, stdin);
        _buf_pos = 0;
    }
    return _buf_pos >= _buf_len;
}

char readChar() {
    char ret = seekChar();
    _buf_pos++;
    return ret;
}

int readInt(int lb, int rb) {
    char c = readChar();
    int mul = 1;
    if(c == '-') {
        c = readChar();
        mul = -1;
    }
    assert(isdigit(c));

    long long ret = c - '0';
    char first_digit = c;
    int len = 0;
    while(!seekEof() && isdigit(seekChar()) && ++len <= 19) {
        ret = ret * 10 + readChar() - '0';
    }
    ret *= mul;

    if(len >= 2) assert(first_digit != '0');
    assert(len <= 18);
    assert(lb <= ret && ret <= rb);
    return (int)ret;
}

void readEoln() {
    char c = readChar();
    //assert(c == '\n');
    assert(c == '\n' || (c == '\r' && readChar() == '\n'));
}

void readSpace() {
    assert(readChar() == ' ');
}

void run() {
    int N = readInt(1, 50);
    readSpace();
    int M = readInt(1, 50);
    readEoln();
    std::vector<int> F(N), P(N);
    std::vector<bool> used(M);
    std::vector<int> cost(M);
    for(int i = 0; i < N; i++) {
        F[i] = readInt(1, M) - 1;
        if(i+1 < N) readSpace(); else readEoln();
        used[F[i]] = true;
    }
    for(int i = 0; i < N; i++) {
        P[i] = readInt(0, 50);
        if(i+1 < N) readSpace(); else readEoln();
        cost[F[i]] += P[i];
    }
    std::vector<int> cand;
    for(int i = 0; i < M; i++) {
        if(used[i]) cand.push_back(cost[i]);
    }
    printf("%d\n", *std::min_element(cand.begin(), cand.end()));
}

int main() {
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
#endif

    int T = readInt(1, 1000);
    readEoln();

    while(T--) {
        run();
    }
    return 0;
}
``

Editorialist's Solution
``#include <bits/stdc++.h>
using namespace std;

int n, m, f[50], p[50];

void solve() {
	//input
	cin >> n >> m;
	for(int i=0; i<n; ++i)
		cin >> f[i];
	for(int i=0; i<n; ++i)
		cin >> p[i];

	int ans=1e9; //some arbitrarily large value
	for(int i=1; i<=m; ++i) {
		//try fruit i
		bool found=false;
		int sum=0;
		for(int j=0; j<n; ++j) {
			if(f[j]==i) {
				found=true;
				sum+=p[j];
			}
		}
		//if found is true then we can choose fruit i
		//sum is the cost of choosing fruit i
		if(found) {
			//update the answer with the cost for fruit i
			ans=min(sum, ans);
		}
	}
	cout << ans << "\n";
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	int t;
	cin >> t;
	while(t--)
		solve();
}
``

Please give me suggestions if anything is unclear so that I can improve. Thanks

</details>
