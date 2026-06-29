# Maximum Product Subarray

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PREP48 |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Dynamic Programming |
| Official Link | [PREP48](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_14/problems/PREP48) |

---

## Problem Statement

Given an array $A$ consisting of $N$ integers.

Find a subarray that has the **maximum** product of elements and output the product.

Note:
- A subarray is formed by deleting some (possibly zero or all) elements from the beginning and some (possibly zero or all) elements from the end of the array.
- The product of any subarray is guaranteed to fit in a $64$-bit integer.

---

## Input Format

- The first line of input will contains a single integer $T$, denoting the number of test cases.
- Each test case consists of two lines of input:
    - The first line of each test case an integer $N$ - the size of the array $A$.
    - The next line contains $N$ space-separated integers - the array $A$.

---

## Output Format

For each test case, output on a new line, the **maximum** product of a subarray of $A$.

The product of any subarray is guaranteed to fit in a $64$-bit integer.

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq N \leq 10^5$
- $-10 \leq A_i \leq 10$
- The product of any subarray is guaranteed to fit in a $64$-bit integer.
- The sum of $N$ over all test cases won't exceed $2\cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
3
4
3 5 -2 -4
5
2 4 3 5 6
3
-1 -3 -4
```

**Output**

```text
120
720
12
```

**Explanation**

**Test case $1$:** Given $A$ as $[3, 5, -2, -4]$.
- All the possible non-empty contiguous subarrays of $A$ are $\{[3], [5], [-2], [-4], [3,5], [5,-2], [-2,-4], [3,5,-2], [5,-2,-4], [3,5,-2,-4]\}$.
- The product of these subarrays are $\{3, 5, -2, -4, 15, -10, 8, -30, 40,120 \}$ respectively.
- So, the maximum product is $120$.

**Test case $2$:** Given $A$ as $[2, 4, 3, 5, 6]$.
- Since all the elements in $A$ are positive, the maximum product is $720$ after multiplying all the elements.

**Test case $3$:** Given $A$ as $[-1, -3, -4]$.
- All the possible non-empty contiguous subarrays of $A$ are $\{[-1], [-3], [-4], [-1,-3], [-3,-4], [-1,-3,-4]\}$.
- The product of these subarrays are $\{-1, -3, -4, 4, 12, -12\}$ respectively.
- So, the maximum product is $12$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4
3 5 -2 -4
```

**Output for this case**

```text
120
```



#### Test case 2

**Input for this case**

```text
5
2 4 3 5 6
```

**Output for this case**

```text
720
```



#### Test case 3

**Input for this case**

```text
3
-1 -3 -4
```

**Output for this case**

```text
12
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# Editorial: Maximum Product Subarray

In this lesson, we explore two effective approaches to solve the problem of finding a contiguous subarray with the maximum product. The array may contain positive numbers, negative numbers, and zeros, and the key challenge is handling the sign flips caused by negative numbers. We'll discuss each approach in detail.

---

## Approach 1: Dynamic Programming (Kadane's Algorithm for Product)

### Idea:
We can improve efficiency using a dynamic programming approach that is an adaptation of Kadane's algorithm. Here, in addition to the maximum product ending at the current index, we also maintain the minimum product ending at that index since a negative number multiplied by a minimum (negative) product can turn into the maximum.

### Explanation:
- **Procedure:**
  For each element $x$, update the temporary maximum and minimum products as follows:

  $$\text{temp\_max} = \max(x, x \times \text{maxProduct}, x \times \text{minProduct})$$
  $$\text{temp\_min} = \min(x, x \times \text{maxProduct}, x \times \text{minProduct})$$

  Then assign:

  $$\text{maxProduct} = \text{temp\_max}$$
  $$\text{minProduct} = \text{temp\_min}$$
  and update the global result with $$\max(\text{result}, \text{maxProduct})$$.

- **Time Complexity:**
  This approach runs in $$O(n)$$ time, making it suitable for large inputs.

### Code Implementations:

#### C++ Code:
```cpp
#include
#include
#include
#include
using namespace std;

long long maxProductSubarray(const vector& nums) {
    int n = nums.size();
    long long maxProd = nums[0];
    long long minProd = nums[0];
    long long res = nums[0];
    for (int i = 1; i < n; i++) {
        long long x = nums[i];
        long long temp_max = max({x, x * maxProd, x * minProd});
        long long temp_min = min({x, x * maxProd, x * minProd});
        maxProd = temp_max;
        minProd = temp_min;
        res = max(res, maxProd);
    }
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    while(T--) {
        int N;
        cin >> N;
        vector A(N);
        for (int i = 0; i < N; i++){
            cin >> A[i];
        }
        cout << maxProductSubarray(A) << "\n";
    }
    return 0;
}
```

#### Python Code:
```python
def max_product_subarray(nums):
    n = len(nums)
    max_prod = nums[0]
    min_prod = nums[0]
    res = nums[0]
    for num in nums[1:]:
        temp_max = max(num, num * max_prod, num * min_prod)
        temp_min = min(num, num * max_prod, num * min_prod)
        max_prod = temp_max
        min_prod = temp_min
        res = max(res, max_prod)
    return res

T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    print(max_product_subarray(A))
```

---

## Approach 2: Segmentation by Zero Boundaries

### Idea:
Zeros naturally divide the array because any subarray containing zero has a product value of zero. We can split the array into segments that do not contain any zeros and solve the problem for each segment individually.

### Explanation:
1. **Segmenting the Array:**
   Iterate over the array and split it into segments whenever a zero is encountered. Also, consider zero itself as a candidate for the maximum product.

2. **Handling Each Segment:**
   - Compute the total product of the segment.
   - If the total product is positive, the entire segment provides the maximum product.
   - If the total product is negative (due to an odd number of negative numbers), calculate two potential candidates:
     - $$\text{candidate1} = \frac{\text{total product}}{\text{prefix product (up to and including the first negative element)}}$$
     - $$\text{candidate2} = \frac{\text{total product}}{\text{suffix product (up to and including the last negative element)}}$$
   - The maximum product for that segment is the maximum of these two candidates.

3. **Global Maximum:**
   Update the overall maximum product by comparing the maximum from each segment with the candidate value for zero.

- **Time Complexity:**
  This approach runs in $$O(n)$$ time since we process each element a constant number of times.

### Code Implementations:

#### C++ Code:
```cpp
#include
#include
#include
#include
using namespace std;

long long maxProductInSegment(const vector& seg) {
    if(seg.empty()) return LLONG_MIN;
    long long total = 1;
    for (int num : seg) {
        total *= num;
    }
    if(total > 0) return total;
    long long candidate1 = total;
    long long prefix = 1;
    for (int num : seg) {
        prefix *= num;
        if(num < 0) {
            candidate1 = total / prefix;
            break;
        }
    }
    long long candidate2 = total;
    long long suffix = 1;
    for (auto it = seg.rbegin(); it != seg.rend(); ++it) {
        suffix *= *it;
        if(*it < 0) {
            candidate2 = total / suffix;
            break;
        }
    }
    return max(candidate1, candidate2);
}

long long segmentedMaxProduct(const vector& nums) {
    long long ans = LLONG_MIN;
    vector seg;
    for(int num : nums) {
        if(num == 0) {
            ans = max(ans, (long long)0);
            if(!seg.empty()) {
                long long segAns = maxProductInSegment(seg);
                ans = max(ans, segAns);
                seg.clear();
            }
        } else {
            seg.push_back(num);
        }
    }
    if(!seg.empty()) {
        long long segAns = maxProductInSegment(seg);
        ans = max(ans, segAns);
    }
    return ans;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    while(T--){
        int N;
        cin >> N;
        vector A(N);
        for(int i = 0; i < N; i++){
            cin >> A[i];
        }
        cout << segmentedMaxProduct(A) << "\n";
    }
    return 0;
}
```

#### Python Code:
```python
def max_product_in_segment(seg):
    if not seg:
        return float('-inf')
    total = 1
    for num in seg:
        total *= num
    if total > 0:
        return total
    candidate1 = total
    prefix = 1
    for num in seg:
        prefix *= num
        if num < 0:
            candidate1 = total // prefix
            break
    candidate2 = total
    suffix = 1
    for num in reversed(seg):
        suffix *= num
        if num < 0:
            candidate2 = total // suffix
            break
    return max(candidate1, candidate2)

def segmented_max_product(nums):
    ans = float('-inf')
    seg = []
    for num in nums:
        if num == 0:
            ans = max(ans, 0)
            if seg:
                ans = max(ans, max_product_in_segment(seg))
                seg = []
        else:
            seg.append(num)
    if seg:
        ans = max(ans, max_product_in_segment(seg))
    return ans

T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    print(segmented_max_product(A))
```

---

## Conclusion

We examined two approaches:

1. **Dynamic Programming:**
   An efficient solution with $$O(n)$$ time complexity by maintaining both maximum and minimum products, ideal for interview settings.

2. **Segmentation by Zero Boundaries:**
   Utilizes zeros to divide the array into independent segments, carefully handling negative numbers to maximize the product.

For most practical scenarios, the **Dynamic Programming approach** is typically recommended due to its simplicity and efficiency. However, understanding both approaches equips you with valuable strategies for tackling similar problems.

Happy coding and best of luck in your interviews!

</details>
