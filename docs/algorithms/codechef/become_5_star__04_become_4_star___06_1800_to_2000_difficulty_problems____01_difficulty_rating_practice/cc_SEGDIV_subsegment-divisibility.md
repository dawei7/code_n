# Subsegment Divisibility 

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SEGDIV |
| Difficulty Rating | 1806 |
| Difficulty Band | 1800 to 2000 difficulty problems |
| Path | Become 5 star |
| Lesson | 1800 to 1900 difficulty problems |
| Official Link | [SEGDIV](https://www.codechef.com/practice/course/4-star-difficulty-problems/DIFF1900/problems/SEGDIV) |

---

## Problem Statement

JJ challenges his friend GG to construct an array $A$ containing $N$ **distinct** elements such that the following conditions hold:
- For all $1 \le i \le N$, $1 \le A_i \le 10^5$
- For every subarray of length $\ge 2$, the sum of all the elements of the subarray is not divisible by the length of the subarray

Please help perplexed GG to complete JJ's challenge.

---

## Input Format

- The first line contains $T$ - the number of test cases. Then the test cases follow.
- The first and only line of each test case contains an integer $N$ - the size of the array $A$ to be constructed.

---

## Output Format

For each test case, output an array $A$ containing $N$ distinct elements which satisfy the given conditions.

If there are multiple arrays that satisfy the conditions, print any.

---

## Constraints

- $1 \leq T \leq 10$
- $1 \leq N \leq 500$

---

## Examples

**Example 1**

**Input**

```text
2
3
4
```

**Output**

```text
7 2 5
3 18 11 2
```

**Explanation**

**Test case-1:** Following are the subarrays of length $\ge 2$:
- $Length = 2$: $sum([7, 2]) = 9$, $sum([2, 5]) = 7$
- $Length = 3$: $sum([7, 2, 5]) = 14$

We can see that for each of these subarrays, the sum is not divisible by the length.

**Test case-2:** Following are the subarrays of length $\ge 2$:
- $Length = 2$: $sum([3, 18]) = 21$, $sum([18, 11]) = 29$, $sum([11, 2]) = 13$
- $Length = 3$: $sum([3, 18, 11]) = 32$, $sum([18, 11, 2]) = 31$
- $Length = 4$: $sum([3, 18, 11, 2]) = 34$

We can see that for each of these subarrays, the sum is not divisible by the length.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3
```

**Output for this case**

```text
7 2 5
```



#### Test case 2

**Input for this case**

```text
4
```

**Output for this case**

```text
3 18 11 2
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/SEGDIV)

[Contest: Division 3 ](https://www.codechef.com/COOK137C/problems/SEGDIV)

[Contest: Division 2 ](https://www.codechef.com/COOK137B/problems/SEGDIV)

[Contest: Division 1 ](https://www.codechef.com/COOK137A/problems/SEGDIV)

**Author:** [ Jeevan Jyot Singh ](https://www.codechef.com/users/jeevanjyot)

**Tester :** [Takuki Kurokawa](https://www.codechef.com/users/tabr)

**Editorialist:** [Kingvarun ](https://www.codechef.com/users/kingvarun)

#
[](#difficulty-2)DIFFICULTY:

Easy Medium

#
[](#prerequisites-3)PREREQUISITES:

Math , Arrays

#
[](#problem-4)PROBLEM:

You need to create a array of N distinct numbers such that the there will be no subarray of size greater than 1 whose sum is divisile is by the length of that subarray.

#
[](#explanation-5)EXPLANATION:

We can directly use brute force approach to create that N size array, such that above conditions hold.

We simply select N natural numbers starting from 1, but before select we have to check for the every subarray containing the last element that we select such that the sum of that array is not divisible by the size of that subarray,

If we found any subarray that is divisible than we exclude that number and have to check for another number greater than that.

Is this possiblle that we can’t find a number such that the all the subarrays containing  that number will not follow the above condition?

No there will always a number which satisfies our condition

Because, let’s assume we have N size array and last value we have to check is X than sum of subarrays starting from i where i ranges from 1 to N-1  and ends at N should not be divisible by their respective sizes.

Assume that the sum of subarray of size N in P

If that P is divisible by N than last numbers can be replaced by any of this numbers X+1, X+2 , … X+N-1, because than the total sum  will not able to get divisible by N, and In this N-1 possible numbers, there are also N-2 numbers which we can take such that subarray whose end points are 2 and N will not divisible by N-1 and this will aso happen for N-3 ,N-4 ,....2.

Thus we create a vector and simply push back N natural starting from 1 (not first N natural numbers) and by checking which number satisfies the above given condition.

#
[](#time-complexity-6)TIME COMPLEXITY:

O(N ) per test case

#
[](#solutions-7)SOLUTIONS:

Author's Solution
``#include <bits/stdc++.h>
using namespace std;

#define IOS ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0)

const int N = 505;

int a[N];

void solve()
{
    int n; cin >> n;
    for(int i = 1; i <= n; i++)
        cout << a[i] << " ";
    cout << "\n";
}

int32_t main()
{
    IOS;
    iota(a, a+N, 0);
    for(int i = 1; i+1 < N; i += 2)
        swap(a[i], a[i+1]);
    int T; cin >> T;
    for(int tc = 1; tc <= T; tc++)
    {
        solve();
    }
    return 0;
}
``

Tester's Solution
``// final check of input files.
#include <bits/stdc++.h>
using namespace std;

struct input_checker {
    string buffer;
    int pos;

    const string all = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
    const string number = "0123456789";
    const string upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    const string lower = "abcdefghijklmnopqrstuvwxyz";

    input_checker() {
        pos = 0;
        while (true) {
            int c = cin.get();
            if (c == -1) {
                break;
            }
            buffer.push_back((char) c);
        }
    }

    int nextDelimiter() {
        int now = pos;
        while (now < (int) buffer.size() && buffer[now] != ' ' && buffer[now] != '\n') {
            now++;
        }
        return now;
    }

    string readOne() {
        assert(pos < (int) buffer.size());
        int nxt = nextDelimiter();
        string res;
        while (pos < nxt) {
            res += buffer[pos];
            pos++;
        }
        cerr << res << endl;
        return res;
    }

    string readString(int minl, int maxl, const string &pattern = "") {
        assert(minl <= maxl);
        string res = readOne();
        assert(minl <= (int) res.size());
        assert((int) res.size() <= maxl);
        for (int i = 0; i < (int) res.size(); i++) {
            assert(pattern.empty() || pattern.find(res[i]) != string::npos);
        }
        return res;
    }

    int readInt(int minv, int maxv) {
        assert(minv <= maxv);
        int res = stoi(readOne());
        assert(minv <= res);
        assert(res <= maxv);
        return res;
    }

    long long readLong(long long minv, long long maxv) {
        assert(minv <= maxv);
        long long res = stoll(readOne());
        assert(minv <= res);
        assert(res <= maxv);
        return res;
    }

    void readSpace() {
        assert((int) buffer.size() > pos);
        assert(buffer[pos] == ' ');
        pos++;
    }

    void readEoln() {
        assert((int) buffer.size() > pos);
        assert(buffer[pos] == '\n');
        pos++;
    }

    void readEof() {
        assert((int) buffer.size() == pos);
    }
};

int main() {
    input_checker in;
    int tt = in.readInt(1, 10);
    in.readEoln();
    while (tt--) {
        int n = in.readInt(1, 500);
        in.readEoln();
        vector<int> a(n);
        a[0] = 1;
        for (int i = 1; i < n; i++) {
            a[i] = a[i - 1];
            while (true) {
                a[i]++;
                bool ok = true;
                int sum = a[i];
                int cnt = 1;
                for (int j = i - 1; j >= 0; j--) {
                    sum += a[j];
                    cnt++;
                    if (sum % cnt == 0) {
                        ok = false;
                        break;
                    }
                }
                if (ok) {
                    break;
                }
            }
        }
        for (int i = 0; i < n; i++) {
            if (i > 0) {
                cout << " ";
            }
            cout << a[i];
        }
        cout << '\n';
    }
    in.readEof();
    return 0;
}
``

Editorialist Solution
``#include<bits/stdc++.h>
using namespace std;
#define ll long long

int main() {

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

        int t;
        cin>>t;
        while(t--)
        {
            ll n,i,p=2,g=0,sum,j;
            cin>>n;
            vector<ll> v;
            v.push_back(1);

            for(i=1; i<n; i++)
            {
                p=v[i-1]+1;

                while(1)
                {
                    sum=p;
                    for(j=i-1; j>=0; j--)
                    {
                        sum+=v[j];
                        if(sum%(i-j+1)==0)
                        {
                            g=1;
                            break;
                        }

                    }
                    if(g==0)
                    {
                        v.push_back(p);
                        break;
                    }
                    else
                    {
                        g=0;
                        p++;
                    }
                }
            }

            for(i=0 ; i<n ; i++)
            {
                cout<<v[i]<<" ";
            }
            cout<<"\n";
        }

        return  0;

    }

``

</details>
