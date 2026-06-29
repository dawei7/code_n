# Joker and Batman

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | JOKRBTMN |
| Difficulty Rating | 1816 |
| Difficulty Band | 1800 to 2000 difficulty problems |
| Path | Become 5 star |
| Lesson | 1800 to 1900 difficulty problems |
| Official Link | [JOKRBTMN](https://www.codechef.com/practice/course/4-star-difficulty-problems/DIFF1900/problems/JOKRBTMN) |

---

## Problem Statement

During a fight with the Joker, Batman's eyes lose the capability to distinguish between some pairs of colors.

Each color has an integer ID from $1$ to $N$. There are $M$ lists where each color belongs to exactly one list. Batman can distinguish colors belonging to different lists, but he cannot distinguish colors belonging to the same list.

Given a strip of $L$ colors, find the different number of segments Batman will see as a result of his disability. Two positions of the strip are said to belong to the same segment if they are adjacent on the strip and Batman cannot distinguish their colors. See the sample explanation for clarity.

---

## Input Format

- The first line contains an integer $T$, the number of test cases. Then the test cases follow.
- The first line contain three integers $N$, $M$, and $L$ - the number of colors, the number of lists, and the length of the strip, respectively.
- Each of the next $M$ lines describes a list. It begins with an integer $K_i$, the length of the $i$-th list, followed by $K_i$ integers $A_{i1}, A_{i2}, \ldots, A_{iK_i}$ - the color IDs of the $i$-th list.
- The next line contains $L$ integers $S_1, S_2, \ldots, S_L$ - the color IDs of the strip.

---

## Output Format

For each test case, output in a single line the answer to the problem.

---

## Constraints

- $1 \leq T \leq 10$
- $1 \leq M \leq N \leq 10^5$
- $1 \leq L \leq 10^5$
- $1 \leq K_i, A_{ij}, S_i \leq N$
- $\sum_{i=1}^{M} K_i = N$
- Each color belongs to exactly one list.

---

## Examples

**Example 1**

**Input**

```text
3
2 2 2
1 2
1 1
2 1
2 2 4
1 1
1 2
1 2 2 1
3 2 3
2 1 3
1 2
1 3 1
```

**Output**

```text
2
3
1
```

**Explanation**

**Test Case 1:** Since the strip is composed of colors from different lists, the answer is the length of the strip, which is $2$.

**Test Case 2:** The first and second index have colors from different lists, and the third and fourth index have colors from different lists. So the strip is seen to be composed of $3$ consecutive segments.

**Test Case 3:** Since the strip is composed of colors from the same list, the answer is $1$ segment.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2 2 2
1 2
1 1
2 1
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
2 2 4
1 1
1 2
1 2 2 1
```

**Output for this case**

```text
3
```



#### Test case 3

**Input for this case**

```text
3 2 3
2 1 3
1 2
1 3 1
```

**Output for this case**

```text
1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Practice](https://www.codechef.com/problems/JOKRBTMN)

[Contest: Division 3](https://www.codechef.com/START6C/problems/JOKRBTMN)

[Contest: Division 2](https://www.codechef.com/START6B/problems/JOKRBTMN)

[Contest: Division 1](https://www.codechef.com/START6A/problems/JOKRBTMN)

**Author:** [Daanish Mahajan](https://www.codechef.com/users/daanish_adm)

**Tester & Editorialist:** [Aman Dwivedi](https://www.codechef.com/users/cherry0697)

# DIFFICULTY:

Simple

# PREREQUISITES:

Hashing

# PROBLEM:

Each color has an integer ID from 1 to N. There are M lists where each color belongs to exactly one list. Batman can distinguish colors belonging to different lists, but he cannot distinguish colors belonging to the same list.

Given a strip of L colors, find the different number of segments Batman will see as a result of his disability. Two positions of the strip are said to belong to the same segment if they are adjacent on the strip and Batman cannot distinguish their colors.

# QUICK EXPLANATION:

-

In the given strip, replace the Color ID with the List ID to which the color belongs.

-

Remove the adjacent duplicates in the strip.

-

Output the count of the elements that are remaining in the strip.

# EXPLANATION:

We need to find out the number of segments that Batman would be able to see in the given strip. Let us try to find out the starting point of each of the segments. It is quite clear that the number of starting points will be equal to the number of segments in the strip since each segment will have a unique starting point.

A segment will begin from index i of the strip if the colors present at indices i and i-1 belong to different lists. Because if they come from the same list, then they are considered to be part of the same segment and then i can’t be the starting point of a new segment.

So we are left with finding out the number of starting points possible. To do so, for every index i \in [2, L] we need to find out the list IDs for the colors present at the index i and at index i-1. One way is to check every list and find out which one this color belongs to. But this is slow enough to give us a TLE verdict.

We can improve our solution by using hashing. We can simply hash the Color ID with the List ID it belongs to. And then we can easily find out the List ID in constant time for any color.  Then when we find the starting point we can simply increment our answer.

Note that the value of number of starting points (i.e. the variable that holds our answer) is initialized from 1, because the first color on the strip will always be the starting point of the first segment that batman can see.

# TIME COMPLEXITY:

O(N+L) per test case.

# SOLUTIONS:

Setter
``#include<bits/stdc++.h>
using namespace std;

const int maxl = 1e5, maxn = 1e5, maxm = 1e5, maxt = 10;

int main()
{
    int t; cin >> t;
    while(t--){
        int n, m, l; cin >> n >> m >> l;
        int id[n + 1]; memset(id, 0, sizeof(id));
        int tot = n;
        for(int i = 0; i < m; i++){
            int k; cin >> k; tot -= k;
            int x;
            for(int j = 0; j < k; j++){
                cin >> x;
                id[x] = i + 1;
            }
        }
        assert(tot == 0);
        for(int i = 1; i <= n; i++)assert(id[i] != 0);
        int pid = 0, ans = 0, s;
        for(int i = 0; i < l; i++){
            cin >> s;
            int nid = id[s];
            if(nid != pid){
                ans++;
            }
            pid = nid;
        }
        cout << ans << endl;
    }
}
``

Tester
``#include<bits/stdc++.h>
using namespace std;

#define int long long

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

void solve()
{
  int n,m,l;
  n=readIntSp(1,100000);
  m=readIntSp(1,100000);
  l=readIntLn(1,100000);

  unordered_map <int,int> m1;

  int sum=0;

  for(int i=0;i<m;i++)
  {
    int k;
    k=readIntSp(1,n);
    sum+=k;

    for(int j=0;j<k;j++)
    {
      if(j!=k-1)
      {
        int x;
        x=readIntSp(1,n);
        assert(m1[x]==0);
        m1[x]=i;
      }
      else
      {
        int x;
        x=readIntLn(1,n);
        assert(m1[x]==0);
        m1[x]=i;
      }
    }
  }

  assert(sum==n);

  int a[l];

  for(int i=0;i<l;i++)
  {
    if(i!=l-1)
      a[i]=readIntSp(1,n);
    else
      a[i]=readIntLn(1,n);
  }

  int ans=1;

  for(int i=1;i<l;i++)
  {
    if(m1[a[i]]!=m1[a[i-1]])
      ans++;
  }

  cout<<ans<<"\n";
}

int32_t main()
{
  ios_base::sync_with_stdio(0);
  cin.tie(0);

  // freopen("input.txt","r",stdin);
  // freopen("output.txt","w",stdout);

  int t;
  t=readIntLn(1,10);

  while(t--)
    solve();

  assert(getchar()==EOF);

return 0;
}

``

</details>
