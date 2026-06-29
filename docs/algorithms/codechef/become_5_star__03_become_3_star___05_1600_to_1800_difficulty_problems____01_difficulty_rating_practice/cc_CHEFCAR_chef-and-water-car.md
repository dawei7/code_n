# Chef and Water Car

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CHEFCAR |
| Difficulty Rating | 1683 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1600 to 1700 difficulty problems |
| Official Link | [CHEFCAR](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1700/problems/CHEFCAR) |

---

## Problem Statement

Chef is a great mechanic. As the cost of petrol is increasing day by day he decided to build a water car to take his girlfriend Natasha on a date. Water car has great build quality but is able to travel only $1$ Km on every $1$ liter of water. To show off his water car to Natasha he took her to the formula racing track which is an ($N-1$) km long road with checkpoints numbered $1$ to $N$ from left to right. The distance between two adjacent checkpoints is $1$ Km.

Initially, Chef is at checkpoint number $1$ and the tank of the water car is empty. At every checkpoint, there is a water station, but the cost of filling $1$ liter of water at a checkpoint is equal to the checkpoint number. Chef can not store more than $V$ liters of water in the tank of a car. Chef is interested in both minimum as well as the maximum cost of filling that can happen to reach the checkpoint number $N$.

You shouldn't have any water left after reaching $N^{th}$ checkpoint. Also, you are not allowed to pour out water.

---

## Input Format

- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains two space-separated integers $N, V$.

---

## Output Format

For each test case, output two integers separated by space representing the maximum and minimum cost of filling respectively.

---

## Constraints

- $1 \le T \le 10^3$
- $1 \le N, V \le 10^9$

---

## Examples

**Example 1**

**Input**

```text
3
3 1
4 2
4 3
```

**Output**

```text
3 3
6 4
6 3
```

**Explanation**

**Test case $1$**: Given $N = 3$ and $V = 1$, Chef will start at checkpoint $1$, fill $1$ liter of water at a cost of $1$ and move $1$ Km right to reach checkpoint $2$. At checkpoint $2$, Chef will fill $1$ liter of water again at a cost of $2$  and move $1$ Km right to reach the destination i.e checkpoint $3$. Hence total cost incurred is $3$. There is no other way to reach the destination with a different expense.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3 1
```

**Output for this case**

```text
3 3
```



#### Test case 2

**Input for this case**

```text
4 2
```

**Output for this case**

```text
6 4
```



#### Test case 3

**Input for this case**

```text
4 3
```

**Output for this case**

```text
6 3
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)Problem Link:

[Practice](https://www.codechef.com/problems/CHEFCAR)

[Contest: Division 1](https://www.codechef.com/LTIME101A/problems/CHEFCAR)

[Contest: Division 2](https://www.codechef.com/LTIME101B/problems/CHEFCAR)

[Contest: Division 3](https://www.codechef.com/LTIME101C/problems/CHEFCAR)

***Author:*** [Akshat mangal](https://www.codechef.com/users/iamakshat01)

***Tester:*** [ Radostin Chonev](https://www.codechef.com/users/ronniechonev)

***Editorialist:*** [ Ritesh Gupta](https://www.codechef.com/users/rishup_nitdgp)

#
[](#difficulty-2)DIFFICULTY:

EASY

#
[](#prerequisites-3)PREREQUISITES:

Math, Observation

#
[](#problem-4)PROBLEM:

Initially, you are at 1 with empty tank and need to travel at N with your car. To travel 1 Km, you need 1 liter of water. There is a gas station after each 1 Km means at 1, 2, …, N, but the cost of filling 1 liter of gas at a gas station is equal to the number of gas station. you can not store more than V liters of gas in the tank of a car. Find both minimum as well as the maximum cost of filling that can happen to reach at N.

#
[](#quick-explanation-5)QUICK EXPLANATION:

As cost of the gas is increasing by going towards the N and we need only 1 liter of gas to reach from i-th station to (1+1)-th station

- which means that to maximise the cost, we can only take 1 liter of gas at each station. So, we need to travel total N-1 Km and we are starting from 1 that means (N*(N-1))/2 is the maximum cost.

- which means that to minimise the cost, we can try to fill the tank as soon as there is some empty space. So, we are filling the tank with V liters at station 1 and after that at each station we are consuming 1 liter to reach there so filling that 1 liter at that station itself. This way minimum cost is ((N - V)*(N - V + 1))/2 + V - 1 but if the tank capacity V is more or equal to N-1 then the minimum cost is (N-1) only.

#
[](#explanation-6)EXPLANATION:

##
[](#maximum-cost-7)Maximum Cost:

As cost of filling the gas at each station is more then it’s previous one, to maximise the cost we try to buy gas from a station which is giving us in more money. Or if we have a choice that we can buy the gas either from i-th station or (i+x)-th station where x > 0 then we better choice would be to choose (i+x) station.

So, at any station will buy only the gas which will help us to reach the next station.

- at station 1, we take 1 liter gas which cost us 1 and we can go upto station 2

- at station 2, we take 1 liter gas which cost us 1 and we can go upto station 3

…

- at station N-1, we take 1 liter gas which cost us N-1 and we can go upto station N

Overall cost is (1 + 2 + ... + (N-1)) or (N*(N-1))/2

##
[](#minimum-cost-8)Minimum Cost:

As cost of filling the gas at each station is more then it’s previous one, to minimise the cost, we need to do the opposite of the maximum or if we have a choice that we can buy the gas either from i-th station or (i+x)-th station where x > 0 then we better choice would be to choose (i) station.

Now, if we have enough capacity in the tank then we can fill the tank at station 1 only with the required gas and complete the journey. Mathematically, if V >= (N-1) then minimum cost will be (N-1)

Otherwise, we try to fill the tank as soon as possible.

- at station 1, we take V liter gas which cost us V and we reach station 2

- at station 2, we take 1 liter gas which cost us 2 and we reach station 3

…

- at station N-V, we take 1 liter gas which cost us N-V and we reach station N-V+1

- at station N-V+1, we take 0 liter gas which cost us 0 and we reach station N-V+2

…

- at station N-2, we take 0 liter gas which cost us 0 and we reach station N-1

- at station N-1, we take 0 liter gas which cost us 0 and we reach station N

Overall cost is (V + 2 + 3 + ... + (N-V)) or ((N - V)*(N - V + 1))/2 + V - 1

#
[](#time-complexity-9)TIME COMPLEXITY:

O(1) per testcase

#
[](#code-10)CODE:

Setter (C++)
`#include
typedef long long ll;
using namespace std;

void pre()
{

}

void solve()
{
  ll n,v;
  cin>>n>>v;
  ll min_cost;
  if(n-1<=v)
  min_cost=n-1;
  else
  min_cost=v+(n-v)*(n-v+1)/2-1;

  cout<<n*(n-1)/2<<" "<<min_cost<<'\n';

}
int main()
{
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    cout<<fixed<>t;
    for(ll tt=1;tt<=t;tt++)
    {
        // cout<<"Test Case #"<<tt<<": \n";
        solve();
    }
    return 0;
}

`

Tester (C++)
`#include
using namespace std ;

int n , v ;

void input ( ) {
    cin >> n >> v ;
}

void solve ( ) {
    if ( v >= n - 1 ) {
        cout << 1LL * n * ( n - 1 ) / 2 << " " << n - 1 << "\n" ;
    }
    else {
        cout << 1LL * n * ( n - 1 ) / 2 << " " << v + ( 1LL * ( n - v + 1 ) * ( n - v ) / 2 - 1 ) <> t ;
    while ( t -- ) {
        input ( ) ;
        solve ( ) ;
    }
    return 0 ;
}

`

Editorialist (C++)
`#include
using namespace std;

int main() {
	int t;
	cin >> t;

	while(t--) {
	   long long n,v;
	   cin >> n >> v;

	   if (v >= n-1) {
	      cout << (n*(n-1))/2 << " " << n-1 << endl;
	   } else {
	      cout << (n*(n-1))/2 << " " << ((n-v)*(n-v+1))/2 + v - 1 << endl;
	   }
	}

	return 0;
}

`

</details>
