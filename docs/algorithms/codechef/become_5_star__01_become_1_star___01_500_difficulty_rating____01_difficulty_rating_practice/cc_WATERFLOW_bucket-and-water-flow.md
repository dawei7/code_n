# Bucket and Water Flow 

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | WATERFLOW |
| Difficulty Rating | 483 |
| Difficulty Band | 500 difficulty rating |
| Path | Become 5 star |
| Lesson | Less than 500 difficulty rating |
| Official Link | [WATERFLOW](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/WATERFLOW) |

---

## Problem Statement

Alice has a bucket of water initially having $W$ litres of water in it. The maximum capacity of the bucket is $X$ liters.

Alice turned on the tap and the water starts flowing into the bucket at a rate of $Y$ litres/hour. She left the tap running for exactly $Z$ hours. Determine whether the bucket has been overflown, filled exactly, or is still left unfilled.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases. The description of the test cases follows.
- Each test case consists of a single line of input containing four space-separated integers $W,\ X,\ Y,\ Z$.

---

## Output Format

For each test case, print the answer on a new line:
- If the bucket has overflown print `overflow`
- If it is exactly filled print `filled`
- If it is still unfilled, print `unfilled`

You may print each character of the string in uppercase or lowercase (for example, the strings `filled`, `FIlled`, `fiLLed`, and `FILLED` will all be treated as identical).

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq W,X,Y,Z \leq 1000$

---

## Examples

**Example 1**

**Input**

```text
4
1 2 3 4 
10 70 10 6 
2 100 4 3
3 3 2 1
```

**Output**

```text
overFlow
filled
Unfilled
overflow
```

**Explanation**

**Test case $1$:** Initially the bucket had $1$ litre of water, we then added $3$ litres of water for $4$ hours. Thus, the total bucket inflow was $1 + 3 \times 4 = 13$ litres. Since this is greater than the capacity of $2$ litres, the bucket will `OVERFLOW`

**Test case $2$:** Initially the bucket had $10$ litres of water, we then added $10$ litres of water for $6$ hours. Thus, the total bucket inflow was $10 + 10 \times 6 = 70$ litres. Since this is equal to the capacity of $70$ litres, the bucket will be `FILLED`

**Test case $3$:** Initially the bucket had $2$ litres of water, we then added $4$ litres of water for $3$ hours. Thus, the total bucket inflow was $2 + 4 \times 3 = 14$ litres. Since this is lesser than the capacity of $100$ litres, the bucket will be `UNFILLED`.

**Test case $4$:** Initially the bucket had $3$ litres of water, we then added $2$ litres of water for $1$ hours. Thus, the total bucket inflow was $3 + 2 \times 1 = 5$ litres. Since this is more than the capacity of $3$ litres, the bucket will `OVERFLOW`.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1 2 3 4
```

**Output for this case**

```text
overFlow
```



#### Test case 2

**Input for this case**

```text
10 70 10 6
```

**Output for this case**

```text
filled
```



#### Test case 3

**Input for this case**

```text
2 100 4 3
```

**Output for this case**

```text
Unfilled
```



#### Test case 4

**Input for this case**

```text
3 3 2 1
```

**Output for this case**

```text
overflow
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/LTIME108A/problems/WATERFLOW)

[Contest Division 2](https://www.codechef.com/LTIME108B/problems/WATERFLOW)

[Contest Division 3](https://www.codechef.com/LTIME108C/problems/WATERFLOW)

[Contest Division 4](https://www.codechef.com/LTIME108D/problems/WATERFLOW)

**Setter:** [S.Manuj Nanthan](https://www.codechef.com/users/munch_01)

**Tester:** [Harris Leung](https://www.codechef.com/users/gamegame)

**Editorialist:** [Trung Dang](https://www.codechef.com/users/kuroni)

#
[](#difficulty-2)DIFFICULTY:

483

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Alice has a bucket of water initially having W litres of water in it. The maximum capacity of the bucket is X liters.

Alice turned on the tap and the water starts flowing into the bucket at a rate of Y litres/hour. She left the tap running for exactly Z hours. Determine whether the bucket has been overflown, filled exactly, or is still left unfilled.

#
[](#explanation-5)EXPLANATION:

The amount of water at the end is W + Y \cdot Z. We then compare this quantity to see whether it is equal to (or larger than/smaller than) X.

#
[](#time-complexity-6)TIME COMPLEXITY:

Time complexity is O(1) per test case.

#
[](#solution-7)SOLUTION:

Preparer's Solution
``#include <bits/stdc++.h>
using namespace std;
int main()
{
    #ifndef ONLINE_JUDGE
           freopen("input.txt","r",stdin);
           freopen("output.txt","w",stdout);
    #endif

    int test_cases;
    cin>>test_cases;
    for(int tc = 1 ; tc <= test_cases ; tc++)
    {
        int initial_water , capacity , flow_rate , flow_hours;
        cin>>initial_water>>capacity>>flow_rate>>flow_hours;

        int total_water = initial_water + (flow_hours * flow_rate);

        if(total_water > capacity)
            cout<<"OverFlow"<<endl;
        else if(total_water == capacity)
            cout<<"Filled"<<endl;
        else
            cout<<"UnFilled"<<endl;

    }

    return 0;
}
``

Tester's Solution
``#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
#define fi first
#define se second
ll n;
void solve(){
	ll w,x,y,z;cin >> w >> x >> y >> z;
	if(w+y*z>x) cout << "overflow\n";
	else if(w+y*z==x) cout << "filled\n";
	else cout << "unfilled\n";
}
int main(){
	ios::sync_with_stdio(false);cin.tie(0);
	int t;cin >> t;while(t--) solve();
}
``

Editorialist's Solution
``#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int t; cin >> t;
    while (t--) {
        int w, x, y, z; cin >> w >> x >> y >> z;
        int tar = w + y * z;
        cout << (tar == x ? "filled" : tar < x ? "unfilled" : "overflow") << '\n';
    }
}
``

</details>
