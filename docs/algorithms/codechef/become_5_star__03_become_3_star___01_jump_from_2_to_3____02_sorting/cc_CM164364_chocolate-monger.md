# Chocolate Monger

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CM164364 |
| Difficulty Rating | 1369 |
| Difficulty Band | Level up from 1* to 2* |
| Path | Become 5 star |
| Lesson | Sorting |
| Official Link | [CM164364](https://www.codechef.com/practice/course/1to2stars/LP1TO204/problems/CM164364) |

---

## Problem Statement

There are $n$ chocolates, and you are given an array of $n$ numbers where the $i$-th number $A_i$ is the flavour type of the $i$-th chocolate. Sebrina wants to eat as many different types of chocolates as possible, but she also has to save at least $x$ number of chocolates for her little brother.

Find the maximum possible number of distinct flavour types Sebrina can have.

---

## Input Format

The first line contains an integer $T$ --- the number of test cases.
- The first line of each test case consists of two integers $n$, $x$ - The number of chocolates Sabrina has and the number of chocolates she has to save for her brother, respectively.
- The second line contains $n$ integers $A_1,\ldots, A_n$, where the $i$-th chocolate has type $A_i$.

---

## Output Format

For each test case, output a single integer denoting the maximum possible number of distinct chocolate flavours Sabrina can eat.

---

## Constraints

- $1\le T\le 10$
- $1 \le x \le  n \le 2 \cdot 10^5  $
- $1 \le A_{i} \le 10^9$
- Sum of $n$ over all test cases do not exceed $ 2 \cdot 10^5  $

---

## Examples

**Example 1**

**Input**

```text
3
2 1
1 2
4 2
1 1 1 1
5 3
50 50 50 100 100
```

**Output**

```text
1
1
2
```

**Explanation**

**Test case $1$:** In the first case, the maximum number of chocolates Sebrina can have is $1$ as she has to leave $1$ chocolate for her brother. Thus, the maximum number of distinct chocolates is also $1$.

**Test case $2$:** Sebrina has to leave $2$ chocolates for her brother. She can eat any $2$ chocolates. Since all the chocolates have the same flavor, it does not matter which chocolates she eats. The maximum number of distinct chocolates would be $1$.

**Test case $3$:** Sebrina needs to save $3$ chocolates for her brother. She can eat any $2$ chocolates. To maximize the number of distinct chocolates, she can eat chocolates $1$ and $5$ with flavors $50$ and $100$ respectively. Thus maximum number of distinct chocolates is $2$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2 1
1 2
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
4 2
1 1 1 1
```

**Output for this case**

```text
1
```



#### Test case 3

**Input for this case**

```text
5 3
50 50 50 100 100
```

**Output for this case**

```text
2
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Practice](https://www.codechef.com/problems/CM164364)

[Contest: Division 1](https://www.codechef.com/COOK128A/problems/CM164364)

[Contest: Division 2](https://www.codechef.com/COOK128B/problems/CM164364)

[Contest: Division 3](https://www.codechef.com/COOK128C/problems/CM164364)

**Author:**  [Tushar Gupta](https://www.codechef.com/users/lazywitt)

**Tester:**  [Riley Borgard](https://www.codechef.com/users/monogon)

**Editorialist:**  [Aman Dwivedi](https://www.codechef.com/users/cherry0697)

# DIFFICULTY:

Cakewalk

# PREREQUISITES:

Greedy

# PROBLEM:

You are given an array A with N integers, where i-th element A_i represents the flavor type of the i-th chocolate. Sebrina wants to eat as many different types of chocolates as possible but she also has to save at least X chocolates for her little brother.

Your task is to find the number of unique chocolates Sebrina can eat.

# EXPLANATION:

Suppose the number of unique chocolates that Sebrina initially has is S. She will save X chocolates for his brother, hence the number of chocolates that Sebrina will eat is N-X, say this value Y. Now, we can use a greedy approach to find out the number of unique chocolates that Sebrina can have. There can be two cases possible:

**Case 1:** S \ge Y

Since the number of unique chocolates that Sebrina has is greater (or equal) to the number of chocolates that she will eat. Hence she will always eat a different flavor of chocolate. Hence she will eat Y unique chocolates as the maximum chocolate that she can eat is Y.

**Case 2:** S < Y

As the number of unique chocolates that Sebrina has is less than the number of chocolates that she will eat. Hence, in this case, it is always possible to eat all the unique chocolates that she has. Therefore, she can eat S unique chocolates.

Finally, we, output the answer accordingly.

# TIME COMPLEXITY:

O(N*log(N) per test case

# SOLUTIONS:

Setter
``#include <bits/stdc++.h>

using namespace std;

int main(){
        int  t; cin >> t;
        while( t-- ){

                int n, x; cin>> n >> x  ;
                int df[n];
                for( auto &i : df ) cin >> i ;

                sort( df , df+n );

                int total_unique = 0 ;
                int total_giveaway = 0;

                int last_type = df[0];
                int cur_tot = 0 ;
                for( int i = 0 ; i < n;  ++i ){

                        if( last_type == df[i] ) cur_tot++;
                        else{

                              total_unique++;
                              total_giveaway += cur_tot-1;

                              cur_tot = 1;
                            }
                        last_type = df[i];

                    }

                total_unique++;
                total_giveaway += cur_tot-1;

                if( total_giveaway >=x ) cout << total_unique;
                else cout << total_unique - ( x- total_giveaway ) ;
                cout << '\n';
            }
    }
``

Tester
``
#include <bits/stdc++.h>

#define ll long long
#define sz(x) ((int) (x).size())
#define all(x) (x).begin(), (x).end()
#define vi vector<int>
#define pii pair<int, int>
#define rep(i, a, b) for(int i = (a); i < (b); i++)
using namespace std;
template<typename T>
using minpq = priority_queue<T, vector<T>, greater<T>>;

void solve() {
    int n, x;
    cin >> n >> x;
    vi a(n);
    rep(i, 0, n) cin >> a[i];
    sort(all(a));
    a.erase(unique(all(a)), a.end());
    cout << min(sz(a), n - x) << '\n';
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    int te;
    cin >> te;
    while(te--) solve();
}
``

Editorialist
``#include<bits/stdc++.h>
using namespace std;

#define int long long

void solve()
{
  int n,x;
  cin>>n>>x;

  set<int> s1;

  for(int i=0;i<n;i++)
  {
    int temp;
    cin>>temp;
    s1.insert(temp);
  }

  int ans=(int)s1.size();
  ans=min(ans,n-x);

  cout<<ans<<"\n";
}

int32_t main()
{
  ios_base::sync_with_stdio(0);
  cin.tie(0);

  int t;
  cin>>t;

  while(t--)
    solve();

return 0;
}

``

</details>
