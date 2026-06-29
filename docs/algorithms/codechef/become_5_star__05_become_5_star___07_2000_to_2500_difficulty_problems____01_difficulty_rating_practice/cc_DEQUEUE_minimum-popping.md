# Minimum Popping

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | DEQUEUE |
| Difficulty Rating | 2463 |
| Difficulty Band | 2000 to 2500 difficulty problems |
| Path | Become 5 star |
| Lesson | 2000 to 2500 difficulty problems |
| Official Link | [DEQUEUE](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/DEQUEUE) |

---

## Problem Statement

You are given a double-ended queue $Q$. Initially, it contains elements $Q_1, Q_2, \ldots, Q_M$ in this order. Each of these elements is an integer between $1$ and $N$ (inclusive) and each integer between $1$ and $N$ (inclusive) occurs in the queue at least once.

We want to pop some (possibly zero) elements from the front of the queue and some (not necessarily the same number, possibly zero) elements from the back. Among all the popped elements, each integer between $1$ and $N$ (inclusive) should appear at least once. Find the smallest possible total number of elements we need to pop.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains two space-separated integers $N$ and $M$.
- The second line contains $M$ space-separated integers $Q_1, Q_2, \ldots, Q_M$.

### Output
For each test case, print a single line containing one integer — the minimum number of elements we need to pop.

### Constraints
- $1 \leq T \leq 10$
- $1 \leq N \leq 10^5$
- $N \leq M \leq 2 \cdot 10^5$
- for each $i$ ($1 \le i \le N$), there is at least one element equal to $i$ in the queue
- the sum of $N$ over all test cases does not exceed $10^5$
- the sum of $M$ over all test cases does not exceed $2 \cdot 10^5$

---

## Examples

**Example 1**

**Input**

```text
3
2 2
1 2
2 3
1 2 1
3 6
1 1 1 3 2 2
```

**Output**

```text
2
2
4
```

**Explanation**

**Example case 1:** Since $N = M$ and all elements are pairwise distinct, we have to pop everything to get each value at least once.

**Example case 2:** We can pop the first $2$ or the last $2$ elements.

**Example case 3:** We can pop the first element and the last $3$ elements, so the answer is $1 + 3 = 4$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2 2
1 2
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
2 3
1 2 1
```

**Output for this case**

```text
2
```



#### Test case 3

**Input for this case**

```text
3 6
1 1 1 3 2 2
```

**Output for this case**

```text
4
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/DEQUEUE)

[Contest: Division 1](https://www.codechef.com/START4A/problems/DEQUEUE)

[Contest: Division 2](https://www.codechef.com/START4B/problems/DEQUEUE)

[Contest: Division 3](https://www.codechef.com/START4C/problems/DEQUEUE)

**Author:** [Daanish Mahajan](https://www.codechef.com/users/daanish_adm)

**Tester:** [Manan Grover](https://www.codechef.com/users/mexomerf)

**Editorialist:** [Nandini Kapoor](https://www.codechef.com/users/costheta_z)

#
[](#difficulty-2)DIFFICULTY:

Easy

#
[](#prerequisites-3)PREREQUISITES:

Arrays, Optimization

#
[](#problem-4)PROBLEM:

You are given a doubly ended queue Q of size M containing elements in the range [1,N] **atleast once**. Find the minimum total number of elements to pop (given we can pop from either side) to get all the N distinct elements in the values we have popped.

#
[](#quick-explanation-5)QUICK EXPLANATION:

Visualizing the given dequeue as a circular array starting at index 0 and ending at M-1 with 0 and M-1 being next to each other, we will find the smallest sub-array (that must include at least one of the two extreme indices of the array) consisting of all N numbers.

#
[](#explanation-6)EXPLANATION:

**Note:** The popping of some elements from the beginning and some from the end in a doubly ended queue can be visualized as the removal of a sub array  consisting of one or both of the extreme indices of the array from a circular array. This would help in understanding the aforementioned approach. Thus we will be depicting the given array as circular array for ease in understanding.

We first find the smallest sub array starting at index 0, that contains all numbers from 1 to N and record its size as the answer.

 Considering 1 to N all numbers are present from indices 0 to X at least once, the initially chosen window would look as above.

We would then remove an element from the rear end of the window, effectively reducing its size by 1 in doing so.

- If this removal causes a deficiency of any number from 1 to N (say x) in this new window:

We fulfill this deficit by stretching the window from it’s front end (which expands backwards i.e. initially starting from index 0, we stretch it towards M-1, M-2 and so on - similar to expanding a window in a circular array) to find and accommodate x, thus changing the beginning of the window to index M-i (i being the index at which we found x for the first time while moving in the direction of the expansion of the window), and increasing its size. We then record the answer as the minimum of previous answer obtained and the current window size (window being of the form […, M-2, M-1, 0, 1, …] ).

- If the removal of last element from the window has not compromised the appearance of any number from 1 to N:

We record the answer as the size of this new window (as it is guaranteed to be one element smaller than the previous window).

We continue this process of removal and extending window till the index M-1 becomes the rear end of the window (window with rear end M-1 is the last window for which we perform the iteration).

Why stop at this point?

This is because after this point, removing the last element of the window will result in the following 3 possibilities:

- Exclusion of both indices 0 and M-1, which was a necessary condition for the sub-arrays we were interested in.

- For example in case of Q=[1, 1, 2, 3, 1], N=3, M=5. Initial window being [**1, 1, 2, 3**, 1] and final one being [1, **1, 2, 3**, 1].

- Returning to the initial window.

- For example in case of Q=[1, 2, 3, 1], N=3, M=4. Initial window being [**1, 2, 3**, 1] and final one being [**1, 2, 3**, 1].

- Returning to a window including same indices as that of the initial window in a different order.

- For example in case of Q=[1, 2, 3, 4], N=4, M=4. Initial window being [**1, 2, 3, 4**] and final one being [**4, 1, 2, 3**].

Algorithm for mentioned approach

- for i=0 to M:

- if 1 to N all appeared once in Q:

- window W_1=Q[0], Q[1], ..., Q[i] found

- answer= length(window)

-
ind= index of array at which window ends

- end=M-1

-
x= number of windows found so far

- while(ind--):

- if at ind was the only appearance of number Q[ind] in x_th window:

- while(Q[end]!=Q[ind]):

- end--

- x++

- window W_x=Q[end], Q[end+1], ..., Q[M-1], Q[0], ..., Q[ind-1], Q[ind] found

- answer=\min (answer, length(W))

Let us visualize the algorithm with the help of one of the test cases given in the question:

``N = 3, M = 6
Q = {1, 1, 1, 3, 2, 2}
``

The windows found in each of the iterations of the while loop in the algorithm would be as shown in the figure below:

[

cc1360×1153 134 KB

](https://s3.amazonaws.com/discourseproduction/original/3X/3/7/37ba94783cde0861c034b924162801a76d55b155.png)

The minimum of all window lengths containing 1 to N numbers at least once is evidently 4, thus the answer is 4.

#
[](#time-complexity-7)TIME COMPLEXITY:

O(M) per test case.

#
[](#solutions-8)SOLUTIONS:

Setter
``
``

Tester
``    #include <bits/stdc++.h>
    using namespace std;
    int main(){
      ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
      int t;
      cin>>t;
      while(t--){
        int n,m;
        cin>>n>>m;
        int a[m];
        for(int i = 0; i < m; i++){
          cin>>a[i];
        }
        int x = -1;
        map<int, int> mpp;
        for(int i = 0; i < m; i++){
          x++;
          mpp[a[i]]++;
          if(mpp.size() == n){
            break;
          }
        }
        int y = m;
        int ans = x + 1;
        while(x>=0){
          mpp[a[x]]--;
          if(mpp[a[x]] == 0){
            mpp.erase(a[x]);
          }
          x--;
          while(mpp.size() < n){
            y--;
            mpp[a[y]]++;
          }
          ans = min(ans, x + 1 + m - y);
        }
        cout<<ans<<"\n";
      }
      return 0;
    }

``

Editorialist
``    #include<bits/stdc++.h>
    using namespace std;

    #define _z ios_base::sync_with_stdio(false); cin.tie(NULL);
    #define int long long int
    #define endl "\n"
    #define mod 1000000007
    #define pb_ push_back
    #define mp_ make_pair
    //______________________________z_____________________________

    void solve()
    {
        int n, m;
        cin>>n>>m;
        int a[m], occur[n]={0}, ind=0, ans=m;
        for(int i=0; i<m; i++) {
            cin>>a[i];
            if(!occur[a[i]-1]) ind=i;
            occur[a[i]-1]++;
        }
        ans=ind+1;
        for(int i=ind+1; i<m; i++) {
            occur[a[i]-1]--;
        }
        for(int i=ind, j=m-1; i>=0; i--) {
            occur[a[i]-1]--;
            if(!occur[a[i]-1]) {
                while(a[j]!=a[i]) {
                    occur[a[j]-1]++;
                    j--;
                }
                occur[a[i]-1]++;
                //cout<<i<<" "<<ans<<" "<<m-j+i<<endl;
            }
            ans=min(ans, m-j+i);
        }
        cout<<ans<<endl;
    }

    int32_t main()
    {
        _z;
        int t=1;
        cin>>t;
        while(t--)
        {
            solve();
        }
    }
``

</details>
