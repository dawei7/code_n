# College Life 4

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | COLGLF4 |
| Difficulty Rating | 1856 |
| Difficulty Band | 1800 to 2000 difficulty problems |
| Path | Become 5 star |
| Lesson | 1800 to 1900 difficulty problems |
| Official Link | [COLGLF4](https://www.codechef.com/practice/course/4-star-difficulty-problems/DIFF1900/problems/COLGLF4) |

---

## Problem Statement

Chef and $N-1$ more of his friends go to the night canteen. The canteen serves only three items (well, they serve more, but only these three are edible!), which are omelette, chocolate milkshake, and chocolate cake. Their prices are $A$, $B$ and $C$ respectively.

However, the canteen is about to run out of some ingredients. In particular, they only have $E$ eggs and $H$ chocolate bars left. They need:
- $2$ eggs to make an omelette
- $3$ chocolate bars for a chocolate milkshake
- $1$ egg and $1$ chocolate bar for a chocolate cake

Each of the $N$ friends wants to order one item. They can only place an order if the canteen has enough ingredients to prepare all the ordered items. Find the smallest possible total price they have to pay or determine that it is impossible to prepare $N$ items.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains six space-separated integers $N$, $E$, $H$, $A$, $B$ and $C$.

### Output
For each test case, print a single line containing one integer ― the minimum cost of $N$ items, or $-1$ if it is impossible to prepare $N$ items.

### Constraints
- $1 \leq T \leq 2 \cdot 10^5$
- $1 \leq N \leq 10^6$
- $0 \leq E, H \leq 10^6$
- $1 \leq A, B, C \leq 10^6$
- the sum of $N$ over all test cases does not exceed $10^6$

### Subtasks
**Subtask #1 (30 points):** $1 \leq N \leq 100$

**Subtask #2 (70 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
3
5 4 4 2 2 2
4 5 5 1 2 3
4 5 5 3 2 1
```

**Output**

```text
-1
7
4
```

**Explanation**

**Example case 1:** The maximum number of items that can be produced using $4$ eggs and $4$ chocolates is $4$, so the answer is $-1$.

**Example case 2:** In the optimal solution, the friends should order $2$ omelettes, $1$ chocolate milkshake and $1$ chocolate cake, with cost $1 \cdot 2 + 2 \cdot 1 + 3 \cdot 1 = 7$.

**Example case 3:** In the optimal solution, the friends should order $4$ chocolate cakes, with cost $1 \cdot 4 = 4$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5 4 4 2 2 2
```

**Output for this case**

```text
-1
```



#### Test case 2

**Input for this case**

```text
4 5 5 1 2 3
```

**Output for this case**

```text
7
```



#### Test case 3

**Input for this case**

```text
4 5 5 3 2 1
```

**Output for this case**

```text
4
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/MARCH21A/problems/COLGLF4)

[Contest Division 2](https://www.codechef.com/MARCH21B/problems/COLGLF4)

[Contest Division 3](https://www.codechef.com/MARCH21C/problems/COLGLF4)

[Practice](https://www.codechef.com/problems/COLGLF4)

**Setter:** [](https://www.codechef.com/users/)

**Tester:** [Felipe Mota](https://www.codechef.com/users/fmota)

**Editorialist:** [Taranpreet Singh](https://www.codechef.com/users/taran_1407)

# DIFFICULTY

Easy

# PREREQUISITES

Basic Maths, Inequalities.

# PROBLEM

A Canteen has E eggs and H chocolate bars. Canteen serves omelette at price A which needs 2 eggs, chocolate milkshake at price B which needs three chocolate bars and chocolate cake at price C which needs one egg and one chocolate bar each.

Chef and N-1 friends each order any one of the above such that the canteen can prepare all orders, while the cost is minimized. Find this minimum cost, or determine that canteen cannot handle all N orders.

# QUICK EXPLANATION

- Write these constraints in form of inequalities, where variables are the number of omelettes, chocolate milkshake and chocolate cakes ordered.

- Iterate over the number of chocolate cakes and find the maximum possible omelettes and chocolate milkshakes possible.

- Decide between omelettes and milkshake based on cost.

- Take minimum of cost over all possible number of chocolate cakes.

# EXPLANATION

Since all we need to handle are constraints, we can write it in form of linear inequalities, along with an optimizing function.

Let x denote number of omelettes, y denote number of chocolate milkshakes and z denote the number of chocolate cakes ordered.

Then, we have

-
x+y+z = N since exactly N orders are made.

-
2*x + z \leq E due to number of eggs.

-
3*y + z \leq H due to number of chocolate bars.

-
x, y, z \in  Z^+ since number of orders are non-negative integers.

We need to minimize A*x+B*y+C*z

This general setting is known as [Integer Programming](https://en.wikipedia.org/wiki/Integer_programming), which is an NP-complete problem. Thankfully, for this problem, we can approach it in a different way.

Since \sum N \leq 10^6 in constraints, we can actually iterate over value of any one of x, y or z from 0 to N.

We can see that by iterating on z, we can find maximum bounds on both x and y from both the inequalities, so iterating on z is most useful in this problem.

Let’s say we try all values of z one by one. So we get x \leq (E-z)/2, y \leq (H-z)/3. Now canteen can prepare x omelettes and y chocolate milkshakes independent of each other. So chef can decide how to order remaining N-z items depending upon whether omelette is cheaper or chocolate milkshake. We also need to check if it’s even possible or not.

Hence, for a fixed value of z, we can compute in O(1) time the minimum cost to order N items. So, by iteratig over all values of z, we have considered all possible combinations which may be candidates for lowest cost. We can simply take minimum of these costs.

If there’s no z for which it is possible to order N items, print -1.

# TIME COMPLEXITY

The time complexity is O(N) per test case.

The memory complexity is O(1) per test case.

# SOLUTIONS

Setter's Solution
``#include <bits/stdc++.h>

using namespace std;

const int maxtn = 1e6, maxt = 2e5, maxch = 1e6, maxeg = 1e6, maxA = 1e6, maxB = 1e6, maxC = 1e6;
int n, eg, ch, A, B, C;
long long solveFull(){
    long long ans = 1e18;
    for(int i = 0; i <= n; i++){
        long long req = n;
        if(i > eg || i > ch)break;
        long long egl = eg - i, chl = ch - i;
        long long canA = egl / 2, canB = chl / 3, canC = i;
        if(canA + canB + canC < n)continue;
        long long useC = min(canC, req);
        long long val = useC * C;
        req -= useC;
        if(A < B){
            long long useA = min(canA, req);
            val += useA * A;
            req -= useA;
            val += req * B;
            // cout << useA << " " << req << " " << useC << " " << val << endl;
        }else{
            long long useB = min(canB, req);
            val += useB * B;
            req -= useB;
            val += req * A;
        }
        ans = min(ans, val);
    }
    return ans;
}
long long solvePartial(){
    long long ans = 1e18;
    for(long long useA = 0; useA <= n; useA++){
        for(long long useB = 0; useB + useA <= n; useB++){
            long long useC = n - useA - useB;
            long long egUsed = 2 * useA + useC, chUsed = 3 * useB + useC;
            if(chUsed > ch)break;
            if(egUsed > eg)continue;
            ans = min(ans, useA * A + useB * B + useC * C);
        }
    }
    return ans;
}
int main()
{
    int t; cin >> t;
    int tn = 0;
    while(t--){
        cin >> n >> eg >> ch >> A >> B >> C;
        tn += n;
        long long ans = n <= 100 ? solvePartial() : solveFull();
        // long long ans = solvePartial();
        ans = (ans > 1e12 ? -1 : ans);
        cout << ans << endl;
    }
    assert(tn <= maxtn);
}
``

Tester's Solution
``t = int(raw_input())
while t > 0:
  t -= 1
  n, eggs, bars, price_ome, price_milk, price_cake = map(int, raw_input().split(' '))
  w_eggs, w_bars = 2, 3
  if price_ome > price_milk:
    price_ome, price_milk = price_milk, price_ome
    w_eggs, w_bars = w_bars, w_eggs
    eggs, bars = bars, eggs

  ans = 10**18
  for cake in range(0, n + 1):
    if eggs >= cake and bars >= cake:
      used_ome = min(n - cake, (eggs - cake) / w_eggs)
      used_milk = min(n - cake - used_ome, (bars - cake) / w_bars)
      if cake + used_ome + used_milk == n:
        ans = min(ans, cake * price_cake + used_ome * price_ome + used_milk * price_milk)

  if ans == 10**18:
    ans = -1

  print(ans)
``

Editorialist's Solution
``import java.util.*;
import java.io.*;
class COLGLF4{
    //SOLUTION BEGIN
    void pre() throws Exception{}
    void solve(int TC) throws Exception{
        int N = ni(), E = ni(), H = ni();
        long A = ni(), B = ni(), C = ni();

        long best = Long.MAX_VALUE;
        //Iterating over number of chocolate cake
        for(int chocolateCakes = 0; chocolateCakes <= N; chocolateCakes++){
            int e = E-chocolateCakes, h = H-chocolateCakes;
            if(e < 0 || h < 0)continue;

            //Maximum omelette and chocolate milkshake possible, if x chocolate cakes are ordered
            int omelettes = e/2, chocolateMilkshakes = h/3;

            if(chocolateCakes+omelettes+chocolateMilkshakes < N)continue;//N orders not possible

            int orders = N-chocolateCakes;//number of orders to be made
            if(A <= B){
                //Prefering omelette over chocolate milkshake
                long cost = chocolateCakes*C;
                int min = Math.min(orders, omelettes);
                cost += min*A;
                orders -= min;
                min = Math.min(orders, chocolateMilkshakes);
                cost += min*B;

                best = Math.min(best, cost);
            }else{
                long cost = chocolateCakes*C;
                int min = Math.min(orders, chocolateMilkshakes);
                cost += min*B;
                orders -= min;
                min = Math.min(orders, omelettes);
                cost += min*A;

                best = Math.min(best, cost);
            }
        }
        if(best == Long.MAX_VALUE)pn(-1);
        else pn(best);
    }
    //SOLUTION END
    void hold(boolean b)throws Exception{if(!b)throw new Exception("Hold right there, Sparky!");}
    static boolean multipleTC = true;
    FastReader in;PrintWriter out;
    void run() throws Exception{
        in = new FastReader();
        out = new PrintWriter(System.out);
        //Solution Credits: Taranpreet Singh
        int T = (multipleTC)?ni():1;
        pre();for(int t = 1; t<= T; t++)solve(t);
        out.flush();
        out.close();
    }
    public static void main(String[] args) throws Exception{
        new COLGLF4().run();
    }
    int bit(long n){return (n==0)?0:(1+bit(n&(n-1)));}
    void p(Object o){out.print(o);}
    void pn(Object o){out.println(o);}
    void pni(Object o){out.println(o);out.flush();}
    String n()throws Exception{return in.next();}
    String nln()throws Exception{return in.nextLine();}
    int ni()throws Exception{return Integer.parseInt(in.next());}
    long nl()throws Exception{return Long.parseLong(in.next());}
    double nd()throws Exception{return Double.parseDouble(in.next());}

    class FastReader{
        BufferedReader br;
        StringTokenizer st;
        public FastReader(){
            br = new BufferedReader(new InputStreamReader(System.in));
        }

        public FastReader(String s) throws Exception{
            br = new BufferedReader(new FileReader(s));
        }

        String next() throws Exception{
            while (st == null || !st.hasMoreElements()){
                try{
                    st = new StringTokenizer(br.readLine());
                }catch (IOException  e){
                    throw new Exception(e.toString());
                }
            }
            return st.nextToken();
        }

        String nextLine() throws Exception{
            String str = "";
            try{
                str = br.readLine();
            }catch (IOException e){
                throw new Exception(e.toString());
            }
            return str;
        }
    }
}
``

Feel free to share your approach. Suggestions are welcomed as always.

</details>
