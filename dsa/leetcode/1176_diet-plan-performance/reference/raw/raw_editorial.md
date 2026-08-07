### Approach: Sliding Window

#### Intuition

The most straightforward approach is to traverse the array and calculate the total calories for each $k$-day period, then compare it with $\textit{low}$ and $\textit{high}$. The time complexity of this method is $O(k*(n-k))$, which will cause a timeout in this problem.

The above method counts each number multiple times. We can use the sliding window idea to record the sum of the current $k$ numbers and calculate the total calorie value of all subarrays with window size $k$ in one pass. Below, we simulate the running process of the sliding window through an animation:

![fig1](images/1176_1.gif)

#### Algorithm

1. Calculate the $\textit{sum}$ of the first $k$ numbers.
2. Traverse the array starting from index $k$. At this point, the window size is $k$. Compare $\textit{sum}$ with $\textit{low}$ and $\textit{high}$. Then subtract the number at index $i - k$, which is the leftmost number in the window, and add the next number entering the window, repeating the operation.

#### Implementation


```python
class Solution:
    def dietPlanPerformance(
        self, calories: List[int], k: int, lower: int, upper: int
    ) -> int:
        score = 0
        sum_calories = sum(calories[:k])
        for i in range(k, len(calories)):
            if sum_calories < lower:
                score -= 1
            elif sum_calories > upper:
                score += 1
            sum_calories += calories[i] - calories[i - k]
        if sum_calories < lower:
            score -= 1
        elif sum_calories > upper:
            score += 1
        return score
```


#### Complexity Analysis

Let $n$ be the length of the array $\textit{calories}$.

- Time complexity: $O(n)$.
  
  Sliding window traverses the array once.

- Space complexity: $O(1)$.

---