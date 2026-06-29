# Xor and Multiply

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | XORMUL |
| Difficulty Rating | 1739 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1700 to 1800 difficulty problems |
| Official Link | [XORMUL](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1800/problems/XORMUL) |

---

## Problem Statement

JJ has three integers $N$, $A$ and $B$ where $0 \le A, B \lt 2^N$. He wants to find a third integer $X$ such that:
- $0 \le X \lt 2^N$
- the value of $(A \oplus X) \times (B \oplus X)$ is maximum.

Here $\oplus$ represents the [Bitwise XOR](https://en.wikipedia.org/wiki/Bitwise_operation#XOR) operator.

Can you help him find such an integer $X$? If there are multiple integers which satisfy the given conditions, print any.

---

## Input Format

- The first line will contain $T$ - number of test cases. Then the test cases follow.
- The first and only line of each test case contains three integers $N$, $A$ and $B$ - the integers mentioned in the problem statement.

---

## Output Format

For each test case, output an integer $X$ which satisfies the given conditions.

If multiple answers exist, print any.

---

## Constraints

- $1 \leq T \leq 5000$
- $1 \le N \le 30$
- $0 \le A, B \lt 2^N$

---

## Examples

**Example 1**

**Input**

```text
3
1 0 0
3 4 6
2 2 1
```

**Output**

```text
1
3
0
```

**Explanation**

**Test case 1:** For $X = 1$, $(0 \oplus 1) \times (0 \oplus 1) = 1$ which can be proven to be the maximum value of this expression.

**Test case 2:** For $X = 3$, $(4 \oplus 3) \times (6 \oplus 3) = 35$ which can be proven to be the maximum value of this expression.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1 0 0
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
3 4 6
```

**Output for this case**

```text
3
```



#### Test case 3

**Input for this case**

```text
2 2 1
```

**Output for this case**

```text
0
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/START45A/problems/XORMUL)

[Contest Division 2](https://www.codechef.com/START45B/problems/XORMUL)

[Contest Division 3](https://www.codechef.com/START45C/problems/XORMUL)

[Contest Division 4](https://www.codechef.com/START45D/problems/XORMUL)

Setter: [Jeevan Jyot Singh](https://www.codechef.com/users/jeevanjyot)

Tester: [Takuki Kurokawa](https://www.codechef.com/users/tabr)

Editorialist: [Yash Kulkarni](https://www.codechef.com/users/kulyash)

#
[](#difficulty-2)DIFFICULTY:

1739

#
[](#prerequisites-3)PREREQUISITES:

[Bit Manipulation]

#
[](#problem-4)PROBLEM:

JJ has three integers N, A and B where 0 \le A, B \lt 2^N. He wants to find a third integer X such that:

- 0 \le X \lt 2^N

- the value of (A \oplus X) \times (B \oplus X) is maximum.

Can you help him find such an integer X? If there are multiple integers which satisfy the given conditions, print any.

#
[](#explanation-5)EXPLANATION:

We need to consider only the first N bits of A, B, and X because all are < 2^N. Let us consider the i^{th} bit of A and B. There are 3 possibilities:

-
i^{th} bits of both A and B are set (1). If we keep the i^{th} bit of X as 0 then the i^{th} bits in both (A \oplus X) and (B \oplus X) are set. This clearly maximizes the product.

-
i^{th} bits of both A and B are not set (0). If we keep the i^{th} bit of X as 1 then the i^{th} bits in both (A \oplus X) and (B \oplus X) are set (1). This clearly maximizes the product.

-
i^{th} bits of A and B are both different i.e. one set (1) and one not set (0). In this case irrespective of what the i^{th} bit in X is, one among the i^{th} bits in (A \oplus X) and (B \oplus X) is set (1) and the other is not set (0).

From the first two points it is clear that we can write (A \oplus X) as C + D and (B \oplus X) as C + E, such that C is the number having set (1) bits at all positions where the bits of A and B are same and has all other bits not set (0).

From the third point, D and E have a fixed sum (2^N - C -1) which is equal to that number having set (1) bits at all positions where the bits of A and B are different and has all other bits not set (0).

The product to be maximized simplifies to (C + D) \times (C + E) = C^2 + C \times (2^N - C - 1) + E \times D. The first two terms are fixed based on A, B, and N. The last term involves maximizing the product of two integers having fixed sum. For this, it is clear that we will choose X so that D and E are as close as possible.

Let us say that for D the most significant bit where A and B differ is set (1), then E should be such that it has set bits at all other positions (leaving the most significant position) where A and B differ. This is because 2^K \geq 2^{K_1} +  2^{K_2} + ... 2^{K_X}, where all K_1, K_1, … K_X are distinct and < K.

In summary, X is chosen so that:

-
(A \oplus X) and (B \oplus X) have set bits at all positions where A and B have same bits.

- Either (A \oplus X) or (B \oplus X) has a set bit at the most significant bit position where A and B differ and at all other positions it has 0 bits and vice versa.

#
[](#time-complexity-6)TIME COMPLEXITY:

O(N) for each test case.

#
[](#solution-7)SOLUTION:

Setter's solution
``using namespace std;

int main()
{
    int T; cin >> T;
    while(T--)
    {
        int n, a, b; cin >> n >> a >> b;
        int ans = 0;
        bool fst = 1;
        for(int i = n - 1; i >= 0; i--)
        {
            bool A = a >> i & 1;
            bool B = b >> i & 1;
            if(!A and !B)
                ans |= 1 << i;
            if(A and !B)
            {
                if(fst)
                    fst = false;
                else
                    ans |= 1 << i;
            }
            if(!A and B)
            {
                if(fst)
                    ans |= 1 << i, fst = false;
                else
                    ;
            }
        }
        cout << ans << endl;
    }
    return 0;
}
``

Editorialist's Solution
``using namespace std;

int main() {
	int T;
	cin >> T;
	while(T--){
	    int n,a,b;
	    cin >> n >> a >> b;
	    int c=0;
	    bool ok=true;
	    for(int i=n-1;i>=0;i--){
	        if(((1<<i)&a)==((1<<i)&b)){
	            if(((1<<i)&a)==0)c+=(1<<i);
	        }
	        else if(ok){
	            if(((1<<i)&b))c+=(1<<i);
	            ok=false;
	        }
	        else{
	            if(((1<<i)&a))c+=(1<<i);
	        }
	    }
	    cout << c << endl;
	}
	return 0;
}
``

</details>
