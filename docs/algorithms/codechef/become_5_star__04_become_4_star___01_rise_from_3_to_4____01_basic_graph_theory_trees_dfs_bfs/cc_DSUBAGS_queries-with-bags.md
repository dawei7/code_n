# Queries with Bags

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | DSUBAGS |
| Difficulty Band | Rise from 3* to 4* |
| Path | Become 5 star |
| Lesson | Basic Graph Theory - Trees, DFS, BFS |
| Official Link | [DSUBAGS](https://www.codechef.com/practice/course/3to4stars/LP3TO401/problems/DSUBAGS) |

---

## Problem Statement

There are $N$ bags and $N$ magic cards which manufactured by $DSU$ $Company$
daily. Each bag and card has assigned a number between $1$ to $N$. Initially $i^{th}$ card
is in the $i^{th}$ bag. Now manager wants to club some card together.

Manager is really busy right now he needs your help to perform this task.

You have $Q$ queries to perform.

Each query can be among $3$ $Types$ :

- $Type$-$1$. $Query$ - $1$ $A$ $B$

Magic card with number $A$ and $B$ are merge into single bag if they belong to two
different bags. Its independent which bag to choose, our goal is to add both the cards with number $A$ and $B$ in the same bag.

$NOTE$ - If you merging two magic cards $A$ and $B$ together then all other card which are already merge with card $A$ and $B$ will all be in a single bag after this query.

- $Type$-$2$. $Query$ - $2$ $A$ $B$

You need to check if two magic cards with number $A$ and $B$ belongs to same bag
or not.

- $Type$-$3$. $Query$ - $3$

This query use to check how many distinct bags remained till now.

---

## Input Format

- The first line contains two space separated integer $N$ and $Q$.
- Next $Q$ line contains $3$ space separated integer for $Type$-$1$ and $Type$-$2$ query
and single integer for $Type$-$3$ query as shown in problem description.

---

## Output Format

- For $Type$-$2$ query print **"YES"** if both magic cards belong to same bag else print **"NO"** without quotes.
- For $Type$-$3$ query print a single integer that denotes number of bags remained till now.

---

## Constraints

- $1 \leq N, Q \leq 10^5$
- $1 \leq A, B \leq N$ $(A \neq B)$

---

## Examples

**Example 1**

**Input**

```text
3 8
2 1 2
3
1 1 2
3
2 1 2
1 2 3
3
2 1 3
```

**Output**

```text
NO
3
2
YES
1
YES
```

**Explanation**

- $1^{st}$ query will give ans $NO$ as card with number 1 and 2 belong to different bags.
- $2^{nd}$ query will check no of distinct bags which are $3$ as we did not perform any merge yet.
- $3^{rd}$ query will perform merge of two cards with number 1 and 2 into one bag.
- $4^{th}$ query will check no of distinct bags which are $2$ now.
- $5^{th}$ query will give ans $YES$ as card with number 1 and 2 belong to same bags.
- $6^{th}$ query will perform merge of two cards with number 2 and 3 into one bag.
- $7^{th}$ query will check no of distinct bags which is $1$. (All magic cards is in the same bag).
- $8^{th}$ query will give ans $YES$ as card with number 1 and 3 belong to same bag.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Practice](https://www.codechef.com/problems/DSUBAGS)

[ILLUMINATI SEASON 6 Contest](https://www.codechef.com/IMTI2020/problems/DSUBAGS)

***Author:***  [Mann Mehta](https://www.codechef.com/users/mann2108)

# DIFFICULTY:

EASY

# PREREQUISITES:

Data Structure, DSU- Disjoint Set Union, Implementation, Union-Find.

# PROBLEM:

You have given N bags and N magic cards. Each bag and card assigned numbers between 1 to N. Initially i^{th} magic card is in the i^{th} bag.

Now you have to perform 3 different type of queries: -

**Type 1 Query : -  ** 1 A B.

Merge card with number A and B in same bags. Note that if we merging two magic cards together then all other cards which already merge with this cards will be in the same bag after this query.

**Type 2 Query : -  ** 2 A B.

Print **“YES”** if two magic cards with number A and B belong to same bag else **“NO”**.

**Type 3 Query : -  ** 3

Print the number of distinct  bag we have. Initially there are N bags.

# QUICK EXPLANATION:

To solve this question we have to use DSU data structure DSU stands for Disjoint Set Union. Which follow to famous operations Union and Find.

Here for the query of Type 1 we need to do union of two bags numbered A and B. Using Union algorithm for DSU.

Similarly for query of Type 2 we need to do find the set parent of two bags numbers A and B if both the parent of set are same then we can say that the both belong to same bag else they are belong different bags.

For  the query of Type 3 we need to maintain a no_of_bags counter initially set to N bags. Whenever a successful merge operation performed then at a time we need to decrement that counter. Hence for the type 3 query we just need to print no)of_bags counter.

# EXPLANATION:

The solution to this problem can be implemented in many ways using array but the optimal approach is the only using DSU data structure. We will discuss the simple array brute force implementation which will give you 30 pts, then we will discuss the DSU based implementation to get perfect score.

### Brute Force:

So here one of the way to implement the brute force is to maintain a counter for each set on an array.

-

**Initialization.**

- Array of N elements initialize with 0 all ARR [ N ].

-
CNT initially assigned to 1 and use to assigned unique numbers to a array.

-
BAGS initially set to N as there are total N bags each contain 1 magic card.

-

**Before implementing brute force you need to keep some points in your mind**.

-

For Type 1 query lets say we want to merge cards with number A and B. Now you need to check the value at ARR [ A ] and ARR [ B ] you need to performed merge iff ARR [ A ]  \neq  ARR [ B ] and ARR [ A ] \neq 0 similary ARR [ B ] \neq 0. On successful merge operation decrement the BAGS variable by 1. For the merging you need to assign CNT to all values similar to  ARR [ A ] and ARR [ B ]. And increament CNT.

-

For Type 2 query we just  need to check the value of array at index A and B. if ARR [ A ] = ARR [ B ] then both the cards A and B belongs to same bag else different bags. (Note ARR [ A ], ARR [ B ] \neq 0 )

-

For Type 3 query we just print the value at variable BAGS thats it.

-

Time complexity for the brute force approach is O(N^2). Hence you only able to clear 30 points and Subtask 1.

Brute force solution using above approach
``/// @author mann2108
/// ILLUMINATI SEASON 6
/// Queries with Bags (Brute Force using Array)

#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    ll n, q;
    cin>>n>>q;
    ll arr[n+1] = {};
    ll no_of_bags = n;
    ll a,b;
    ll cnt = 1;
    while(q--){
        ll choice;
        cin>>choice;
        if(choice==1){
            cin>>a>>b;
            if(arr[a]==arr[b] and arr[a]!=0)continue;
            no_of_bags-=1;
            ll x = arr[a];
            ll y = arr[b];
            if(x==0 and y==0){
               arr[a]=cnt;
                arr[b]=cnt;
            }
            else if(x==0){
                arr[a] = cnt;
                for(ll i=1;i<=n;i++){
                    if(arr[i]==y)arr[i]=cnt;
                }
            }
            else if(y==0){
                arr[b] = cnt;
                for(ll i=1;i<=n;i++){
                    if(arr[i]==x)arr[i]=cnt;
                }
            }
            else{
                for(ll i=1;i<=n;i++){
                    if(arr[i]==x or arr[i]==y)arr[i]=cnt;
                }
            }
            cnt++;
        }
        else if(choice==2){
            cin>>a>>b;
            if(arr[a]==arr[b] and arr[a]!=0)cout<<"YES"<<endl;
            else cout<<"NO"<<endl;
        }
        else{
            cout<<no_of_bags<<endl;
        }
    }
}
``

### DSU Based Implementation:

Here I am sharing you the reference from which even I study DSU in detailed. Follow this link here you will find the complete explanation regarding DSU data structure with the mathematical proofs and some related practice problems too.

[DSU Data Structure](https://cp-algorithms.com/data_structures/disjoint_set_union.html).

Follow the below instruction after learning  the DSU from the above link.

-

Type - 1 Query (1 A B)

You need to first find the parent of find*set(A) and find*set(B) if both the parent are same means both the bags belongs to same bag else you need to perform union operation to perform union operation it can be either union by size or union by rank you can choose any one but never go for the coin based the complexity of random choose is worst compare to union by size and rank.

-

Type -2 Query  (2 A B)

You just need to find the parent find*set(A) and find*set(B) if both the parent of A and B are same means they belong to same set else they belong to different bags.

-

Type-3 Query  ( 3 )

You just need to maintain the counter of BAGS and decrease the counter whenever a successful union operation performed in Type - 1 Query. Here for Type -3 query you just need to print this counter BAGS that’s it.

# TIME COMPLEXITY:

- For each query it will take O( ?(N) ) where ?(N) is the inverse Ackermann function, which grows very slowly. In fact it grows so slowly, that it doesn’t exceed 4 for all reasonable N (approximately N < 10^{600}).

# SOLUTIONS:

Setter's Solution
``/// @author mann2108
/// ILLUMINATI SEASON 6
/// Queries with Bags

#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;

#define FAST_IO ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);

const ll MAX = 1e5+1;
vector<ll> parent(MAX);
vector<ll> unionBySize(MAX,1);

ll find_set(ll v){
    if(parent[v]==v)return v;
    return find_set(parent[v]);
}

void union_set(ll a, ll b){
    if(unionBySize[a] < unionBySize[b])swap(a,b);
    parent[b] = a;
    unionBySize[a] += unionBySize[b];
}

int main(){
    FAST_IO
    ll n,q;
    cin>>n>>q;
    for(ll i=1;i<=n;i++)parent[i]=i;
    ll a, b;
    ll no_of_bags = n;

    while(q--){
        ll query_type;
        cin>>query_type;
        if(query_type==1){
            cin>>a>>b;
            a = find_set(a);
            b = find_set(b);
            if(a!=b){
                no_of_bags--;
                union_set(a,b);
            }
        }
        else if(query_type==2){
            cin>>a>>b;
            a = find_set(a);
            b = find_set(b);

            if(a==b)cout<<"YES"<<endl;
            else cout<<"NO"<<endl;
        }
        else{
            cout<<no_of_bags<<endl;
        }
    }

}
``

Share your views, approaches and observations. We always looking for new approaches.

</details>
