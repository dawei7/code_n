# Maximum Trio

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MXMTRIO |
| Difficulty Rating | 1349 |
| Difficulty Band | Level up from 1* to 2* |
| Path | Become 5 star |
| Lesson | Time Complexity |
| Official Link | [MXMTRIO](https://www.codechef.com/practice/course/1to2stars/LP1TO205/problems/MXMTRIO) |

---

## Problem Statement

You are given an array $A$ of $N$ elements. For any ordered triplet $(i, j, k)$ such that $i$, $j$, and $k$ are pairwise distinct and $1 \le i, j, k \le N$, the value of this triplet is $(A_i-A_j)\cdot A_k$. You need to find the **maximum** value among all possible ordered triplets.

**Note:** Two ordered triplets $(a, b, c)$ and $(d, e, f)$ are only equal when $a = d$ **and** $b = e$ **and** $c = f$. As an example, $(1, 2, 3)$ and $(2, 3, 1)$ are two different ordered triplets.

---

## Input Format

- The first line of the input contains a single integer $T$ - the number of test cases. The test cases then follow.
- The first line of each test case contains an integer $N$.
- The second line of each test case contains $N$ space-separated integers $A_1, A_2, \dots, A_N$.

---

## Output Format

For each test case, output the maximum value among all different ordered triplets.

---

## Constraints

- $1 \le T \le 100$
- $3 \le N \le 3 \cdot 10^5$
- $1 \le A_i \le 10^6$
- Sum of $N$ over all testcases won't exceed $3 \cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
3
3
1 1 3
5
3 4 4 1 2
5
23 17 21 18 19
```

**Output**

```text
2
12
126
```

**Explanation**

- **Test case $1$**: The desired triplet is $(3, 2, 1)$, which yields the value of $(A_3 - A_2) \cdot A_1 = (3 - 1) \cdot 1 = 2$.
- **Test case $2$**: The desired triplet is $(2, 4, 3)$, which yields the value of $(A_2 - A_4) \cdot A_3 = (4 - 1) \cdot 4 = 12$.
- **Test case $3$**: The desired triplet is $(1, 2, 3)$, which yields the value of $(A_1 - A_2) \cdot A_3 = (23 - 17) \cdot 21 = 126$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3
1 1 3
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
5
3 4 4 1 2
```

**Output for this case**

```text
12
```



#### Test case 3

**Input for this case**

```text
5
23 17 21 18 19
```

**Output for this case**

```text
126
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/LTIME103A/problems/MXMTRIO)

[Contest Division 2](https://www.codechef.com/LTIME103B/problems/MXMTRIO)

[Contest Division 3](https://www.codechef.com/LTIME103C/problems/MXMTRIO)

[Practice](https://www.codechef.com/problems/MXMTRIO)

**Setter:** [S.Manuj Nanthan](https://www.codechef.com/users/munch_01)

**Tester:** [Nishank Suresh](https://www.codechef.com/users/iceknight1093)

**Editorialist:** [Taranpreet Singh](https://www.codechef.com/users/taran_1407)

#
[](#difficulty-2)DIFFICULTY

Simple

#
[](#prerequisites-3)PREREQUISITES

Sorting

#
[](#problem-4)PROBLEM

You are given an array A containing N elements. For any ordered triplet (i, j, k) such that i, j, and k are pairwise distinct and 1 \le i, j, k \le N, the value of this triplet is (A_i-A_j)\cdot A_k. You need to find the **maximum** value among all possible ordered triplets.

**Note:** Two ordered triplets (a, b, c) and (d, e, f) are only equal when a = d **and** b = e **and** c = f. As an example, (1, 2, 3) and (2, 3, 1) are two different ordered triplets.

#
[](#quick-explanation-5)QUICK EXPLANATION

- Sort the array A in increasing order.

- The maximum possible value among all possible triplets is (A_N-A_1) * A_{N-1}.

#
[](#explanation-6)EXPLANATION

The slow approach would be to iterate over all triplets and take maximum, but that would take O(N^3) time which won’t work.

Since we want to maximize the value of (A_i - A_j) * A_k, and all elements in A are positive, it is best to maximize both (A_i-A_j) and A_k. There are two options

- Select largest and smallest element in A as A_i and A_j, and choose second maximum element in A as A_k. The value of trio is (A_N-A_1)*A_{N-1}

- Choose the maximum element as A_k and choose the second maximum element, and the minimum element as A_i and A_j, getting a triplet of value (A_{N-1}-A_1)*A_N.

Since A_{N-1} \leq A_N, we can prove that (A_N-A_1)*A_{N-1}  \geq (A_{N-1}-A_1)*A_N.

Hence, the maximum value we can obtain is (A_N-A_1)*A_{N-1} after sorting array A.

###
[](#bonus-7)Bonus

- What if A contains negative values as well?

- Assume constraint i \lt j \lt k while choosing triplets. Can we still sort?

#
[](#time-complexity-8)TIME COMPLEXITY

The time complexity is O(N*log(N)) per test case due to sorting.

#
[](#solutions-9)SOLUTIONS

Setter's Solution
``test_cases = int(input())
for _ in range(test_cases):
    N=int(input())
    A=list(map(int,input().split()))
    A.sort()
    print(A[N-2]*(A[N-1]-A[0]))
``

Tester's Solution
``for _ in range(int(input())):
    n = int(input())
    a = sorted(list(map(int, input().split())))
    print((a[n-1] - a[0])*a[n-2])
``

Editorialist's Solution
``import java.util.*;
import java.io.*;
class MXMTRIO{
    //SOLUTION BEGIN
    void pre() throws Exception{}
    void solve(int TC) throws Exception{
        int N = ni();
        int[] A = new int[N];
        for(int i = 0; i< N; i++)A[i] = ni();
        Arrays.sort(A);
        long ans = Math.max(A[N-1] *(long) (A[N-2]-A[0]), A[N-2]*(long)(A[N-1]-A[0]));
        pn(ans);
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
        new MXMTRIO().run();
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
