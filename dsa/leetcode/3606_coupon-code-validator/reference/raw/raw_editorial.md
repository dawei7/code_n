### Approach: Category + Sorting

#### Intuition

We can determine whether a coupon is valid through a judgment function $\textit{check}$, which checks whether its $\textit{code}$ meets the standard and whether $\textit{isActive}$ is $\textit{true}$.

Then we classify the coupons by business categories, sort the coupons in each category in lexicographical order of $\textit{code}$, and finally concatenate all the categories’ coupons and return them.

#### Implementation


```python
class Solution:
    def check(self, code: str, isActive: bool) -> bool:
        if not code:
            return False
        for char in code:
            if char != "_" and not char.isalnum():
                return False
        return isActive

    def validateCoupons(
        self, code: List[str], businessLine: List[str], isActive: List[bool]
    ) -> List[str]:
        groups = [[] for _ in range(4)]
        ans = []
        business_mapping = {
            "electronics": 0,
            "grocery": 1,
            "pharmacy": 2,
            "restaurant": 3,
        }
        for i in range(len(code)):
            if code[i] and self.check(code[i], isActive[i]):
                biz_line = businessLine[i]
                if biz_line in business_mapping:
                    group_index = business_mapping[biz_line]
                    groups[group_index].append(code[i])
        for group in groups:
            group.sort()
            ans.extend(group)
        return ans
```


#### Complexity Analysis

Let $n$ be the length of $\textit{code}$ and $L$ be the average length of $\textit{code}[i]$. If $L$ is small, it simplifies to $O(n \log n)$.

- Time complexity: $O(n L \log n)$.
  
  The main cost comes from sorting.

- Space complexity: $O(n L)$.

---