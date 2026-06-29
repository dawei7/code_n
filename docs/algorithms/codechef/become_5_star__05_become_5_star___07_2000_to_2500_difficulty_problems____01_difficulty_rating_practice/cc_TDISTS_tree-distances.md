# Tree Distances

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | TDISTS |
| Difficulty Rating | 2383 |
| Difficulty Band | 2000 to 2500 difficulty problems |
| Path | Become 5 star |
| Lesson | 2000 to 2500 difficulty problems |
| Official Link | [TDISTS](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/TDISTS) |

---

## Problem Statement

A tree is defined as a connected, undirected graph with $n$ vertices and $n−1$ edges. The distance between two vertices in a tree is equal to the number of edges on the unique simple path between them.

You are given two integers $x$ and $y$. Construct a tree with the following properties:
- The number of pairs of vertices with an **even** distance between them equals $x$.
- The number of pairs of vertices with an **odd** distance between them equals $y$.

By a pair of vertices, we mean an ordered pair of two (possibly, the same or different) vertices.

### Input
The first line of the input contains a single integer $T$ denoting the number of test cases. Each test case consists of one line containing two space-separated integers $x$ and $y$.

### Output
For each test case, if there is no tree satisfying the given properties, print ``"NO"`` (without quotes).

Otherwise, on the first line print ``"YES"`` (without quotes). Then print integer $n$ denoting the number of vertices in the tree, followed by $n−1$ lines describing the edges of the tree in any order. Vertices are numbered from $1$ to $n$. If there are multiple answers, print any of them.

### Constraints
- $1 \leq T \leq 100$
- $1 \leq x,y \leq 10^9$
- $x + y \leq 10^9$

### Example Input
```
4
2 2
29 20
3 12
6 3
```

### Example Output
```
YES
2
1 2
YES
7
1 2
1 3
2 4
2 5
3 6
3 7
NO
NO
```

### Explanation
In the first test case,  the pairs $(1 ,1)$ and $(2 ,2)$ have an even distance, while the pairs $(1 ,2)$ and $(2 ,1)$ have an odd distance.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Practice](https://www.codechef.com/problems/TDISTS)

[Contest: Division 1](https://www.codechef.com/COOK128A/problems/TDISTS)

[Contest: Division 2](https://www.codechef.com/COOK128B/problems/TDISTS)

[Contest: Division 3](https://www.codechef.com/COOK128C/problems/TDISTS)

**Author:**  [Hazem Issa](https://www.codechef.com/users/zoooma13)

**Tester:**  [Riley Borgard](https://www.codechef.com/users/monogon)

**Editorialist:**  [Aman Dwivedi](https://www.codechef.com/users/cherry0697)

# DIFFICULTY:

Easy

# PREREQUISITES:

Tree, Greedy

# PROBLEM

You are given two integers x and y. Your task is to construct a tree with the following properties:

- The number of pairs of vertices with an **even** distance between them equals x.

- The number of pairs of vertices with an **odd** distance between them equals y.

By a pair of vertices, we mean an ordered pair of two (possibly, the same or different) vertices.

# EXPLANATION:

The first basic observation that we can draw is that the summation of x and y should be a perfect square.

Why ?

Since every vertex forms a pair with every other vertex of a tree including itself. Hence for any tree of N vertices, the total number of ordered pairs of vertices will be N^2.

As a summation of x and y represent the total number of ordered pairs of vertices which is a perfect square. Hence x+y should be a perfect square.

Now, we are left with finding whether it is possible to have a tree that has x pair of vertices with an even distance between them and y pair of vertices with an odd distance between them.

As its quite clear that any vertex of the tree can either be at an even level or an odd level. Root of the tree being at the even level (0- based indexing). Let’s find out the number of pairs of vertices that have an odd distance between them.

**Claim:** Any pair of vertices (x, y) has an odd distance between them if the vertices x and y comes from opposite parity levels.

Proof

Let the vertex x is present at an even level and vertex y at an odd level. The distance between two nodes can be obtained in terms of the lowest common ancestor (lca). Below is the formula for the same:

dis(x,y)=dis(root,x)+dis(root,y)-2*dis(root,lca)

Since x is present at even level so dis(root,x) is even while y is at odd level therefore dis(root,y) is odd. Hence we can see:

dis(x,y) = Even + Odd - Even

That means that if the vertices are from opposite parity levels, then the distance between them is odd.

Now let’s calculate the number of pairs of vertices which has an odd distance between them. For odd distances, every vertex that is present at an odd level will form a pair with every vertex that is present at even level and vice versa.

Let us suppose [e_1,e_2,e_3....e_i] and [o_1,o_2,o_3....o_j] are the vertices that are present at even and odd level respectively. Now for every vertex that is present at an even level, it will form a pair with every vertex that is present at the odd level and vice-versa. Hence:

Odd_{pairs}' = e_1*o_1+e_1*o_2+\dots+e_1*o_j+\dots+e_i*o_1+\dots+e_i*o_j

Odd_{pairs}' = (e_1+e_2+e_3+\dots+e_i)*(o_1+o_2+o_3+\dots+o_j)

Odd_{pairs}' = E*O

, where E and O represents the number of nodes that are present at even and odd level respectively.

Since we looking for the ordered pairs of two hence the number of the above pairs will be doubled. As if (x,y) is a pair that has the odd distance between them then (y,x) will also have an odd distance between them. Hence:

Odd_{pairs}= 2*E*O

That means we only care about the number of vertices that are present at even levels and odd levels. The root is the only node that is present at the 0^{th} level, now if we want more nodes at an even level then there must exist at least one vertex at an odd level. Now we can check for every possibility and can find if there exists such an arrangement of vertices that satisfy x and y of the problem. If so, we can output the tree.

# TIME COMPLEXITY:

O(sqrt(X+Y)) per test case

# SOLUTIONS:

Setter
``#include <bits/stdc++.h>
using namespace std;

int sqr(int n){ return n*n; }

void solve(){
    int x ,y; //x even ,y odd
    scanf("%d%d",&x,&y);

    int n = 1;
    while(sqr(n) < x+y)
        n++;
    if(sqr(n) != x+y){
        printf("NO\n");
        return;
    }

    for(int i=1; i<n; i++)
        if(sqr(i)+sqr(n-i) == x && 2*i*(n-i) == y)
        {
            printf("YES\n");
            printf("%d\n",n);
            for(int j=1; j<=n-i; j++)
                printf("1 %d\n",j+1);
            for(int j=2; j<=i; j++)
                printf("2 %d\n",n-i+j);
            return;
        }

    printf("NO\n");
}

int main()
{
    int t;
    scanf("%d",&t);
    while(t--)
        solve();
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
    ll x, y;
    cin >> x >> y;
    ll n = 1;
    while(n * n < x + y) n++;
    if(n * n != x + y) {
        cout << "NO\n";
        return;
    }
    // (a, b)
    // a + b = n
    // 2ab = y
    // a <= b
    for(ll a = 1; 2 * a * a <= y; a++) {
        ll b = n - a;
        if(1 <= a && a <= n && 1 <= b && b <= n && 2 * a * b == y) {
            cout << "YES\n";
            cout << n << '\n';
            // 1..a red nodes, a+1..n blue nodes
            for(ll i = a + 1; i <= n; i++) {
                cout << 1 << ' ' << i << '\n';
            }
            for(ll i = 2; i <= a; i++) {
                cout << a + 1 << ' ' << i << '\n';
            }
            return;
        }
    }
    cout << "NO\n";
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
  int x,y;
  cin>>x>>y;

  int n=1;

  while(n*n<x+y)
    n++;

  if(n*n!=x+y)
  {
    cout<<"NO"<<"\n";
    return;
  }

  if(n==1)
  {
    if(x==1)
    {
      cout<<"YES"<<"\n";
      cout<<1<<"\n";
    }
    else
      cout<<"NO"<<"\n";

    return;
  }

  int even_lev=1,odd_lev=n-1;
  int flag=0;

  while(odd_lev>=1)
  {
    int odd_pairs=even_lev*odd_lev*2;
    if(odd_pairs==y)
    {
      flag=1;
      break;
    }
    even_lev++;
    odd_lev--;
  }

  if(!flag)
  {
    cout<<"NO"<<"\n";
    return;
  }

  cout<<"YES"<<"\n";
  cout<<n<<"\n";

  for(int i=1;i<=odd_lev;i++)
    cout<<1<<" "<<i+1<<"\n";

  for(int i=1;i<even_lev;i++)
    cout<<2<<" "<<odd_lev+i+1<<"\n";
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
