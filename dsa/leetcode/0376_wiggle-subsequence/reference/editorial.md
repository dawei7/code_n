[TOC]

## Summary

We need to find the length of the longest wiggle subsequence. A wiggle subsequence consists of a subsequence with numbers which appears in alternating ascending / descending order.

## Solution
### Approach #1 Brute Force

Here, we can find the length of every possible wiggle subsequence and find the maximum length out of them. To implement this, we use a recursive function, $\text{calculate}(\text{nums}, \text{index}, \text{isUp})$ which takes the array $\text{nums}$, the $\text{index}$ from which we need to find the length of the longest wiggle subsequence, boolean variable $\text{isUp}$ to tell whether we need to find an increasing wiggle or decreasing wiggle respectively. If the function $\text{calculate}$ is called after an increasing wiggle, we need to find the next decreasing wiggle with the same function. If the function $\text{calculate}$ is called after a decreasing wiggle, we need to find the next increasing wiggle with the same function.

```java
public class Solution {
    private int calculate(int[] nums, int index, boolean isUp) {
        int maxcount = 0;
        for (int i = index + 1; i < nums.length; i++) {
            if ((isUp && nums[i] > nums[index]) || (!isUp && nums[i] < nums[index]))
                maxcount = Math.max(maxcount, 1 + calculate(nums, i, !isUp));
        }
        return maxcount;
    }

    public int wiggleMaxLength(int[] nums) {
        if (nums.length < 2)
            return nums.length;
        return 1 + Math.max(calculate(nums, 0, true), calculate(nums, 0, false));
    }
}
```

**Complexity Analysis**

* Time complexity : $O(n!)$. $\text{calculate}()$ will be called maximum $n!$ times.
* Space complexity : $O(n)$. Recursion of depth $n$ is used.

---
### Approach #2  Dynamic Programming

**Algorithm**

To understand this approach, take two arrays for dp named $up$ and $down$.

Whenever we pick up any element of the array to be a part of the wiggle subsequence, that element could be a part of a rising wiggle or a falling wiggle depending upon which element we have taken prior to it.

$\text{up}[i]$ refers to the length of the longest wiggle subsequence obtained so far considering $i^{th}$ element as the last element of the wiggle subsequence and ending with a rising wiggle.

Similarly, $\text{down}[i]$ refers to the length of the longest wiggle subsequence obtained so far considering $i^{th}$ element as the last element of the wiggle subsequence and ending with a falling wiggle.

$\text{up}[i]$ will be updated every time we find a rising wiggle ending with the $i^{th}$ element. Now, to find $\text{up}[i]$, we need to consider the maximum out of all the previous wiggle subsequences ending with a falling wiggle i.e. $\text{down}[j]$, for every $j<i$ and $\text{nums}[i]>\text{nums}[j]$. Similarly, $\text{down}[i]$ will be updated.

```java
public class Solution {
    public int wiggleMaxLength(int[] nums) {
        if (nums.length < 2)
            return nums.length;
        int[] up = new int[nums.length];
        int[] down = new int[nums.length];
        for (int i = 1; i < nums.length; i++) {
            for(int j = 0; j < i; j++) {
                if (nums[i] > nums[j]) {
                    up[i] = Math.max(up[i],down[j] + 1);
                } else if (nums[i] < nums[j]) {
                    down[i] = Math.max(down[i],up[j] + 1);
                }
            }
        }
        return 1 + Math.max(down[nums.length - 1], up[nums.length - 1]);
    }
}
```

**Complexity Analysis**

* Time complexity : $O(n^2)$. Loop inside a loop.
* Space complexity : $O(n)$. Two arrays of the same length are used for dp.

---
### Approach #3 Linear Dynamic Programming

**Algorithm**

Any element in the array could correspond to only one of the three possible states:

1. up position, it means $\text{nums}[i] > nums[i-1]$
2. down position, it means $\text{nums}[i] < nums[i-1]$
3. equals to position, $\text{nums}[i] = nums[i-1]$

The updates are done as:

If $\text{nums}[i] > nums[i-1]$, that means it wiggles up. The element before it must be a down position. So $\text{up}[i] = down[i-1] + 1$, $\text{down}[i]$ remains the same as $down[i-1]$.
If $\text{nums}[i] < nums[i-1]$, that means it wiggles down. The element before it must be a up position. So $\text{down}[i] = up[i-1] + 1$, $\text{up}[i]$ remains the same as $up[i-1]$.
If $\text{nums}[i] = nums[i-1]$, that means it will not change anything becaue it didn't wiggle at all. So both $\text{down}[i]$ and $\text{up}[i]$ remain the same as $down[i-1]$ and $up[i-1]$.

At the end, we can find the larger out of $up[length-1]$ and $down[length-1]$ to find the max. wiggle subsequence length, where $length$ refers to the number of elements in the given array.

The process can be illustrated with the following example:

<!--![Wiggle gif](images/376_Wiggle_Subsequence.gif)-->

![Slide 1](images/slideshow_376_Wiggle_376_WiggleSlide1.PNG)

![Slide 2](images/slideshow_376_Wiggle_376_WiggleSlide2.PNG)

![Slide 3](images/slideshow_376_Wiggle_376_WiggleSlide3.PNG)

![Slide 4](images/slideshow_376_Wiggle_376_WiggleSlide4.PNG)

![Slide 5](images/slideshow_376_Wiggle_376_WiggleSlide5.PNG)

![Slide 6](images/slideshow_376_Wiggle_376_WiggleSlide6.PNG)

![Slide 7](images/slideshow_376_Wiggle_376_WiggleSlide7.PNG)

![Slide 8](images/slideshow_376_Wiggle_376_WiggleSlide8.PNG)

![Slide 9](images/slideshow_376_Wiggle_376_WiggleSlide9.PNG)

![Slide 10](images/slideshow_376_Wiggle_376_WiggleSlide10.PNG)

![Slide 11](images/slideshow_376_Wiggle_376_WiggleSlide11.PNG)

![Slide 12](images/slideshow_376_Wiggle_376_WiggleSlide12.PNG)

```java
public class Solution {
    public int wiggleMaxLength(int[] nums) {
        if (nums.length < 2)
            return nums.length;
        int[] up = new int[nums.length];
        int[] down = new int[nums.length];
        up[0] = down[0] = 1;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] > nums[i - 1]) {
                up[i] = down[i - 1] + 1;
                down[i] = down[i - 1];
            } else if (nums[i] < nums[i - 1]) {
                down[i] = up[i - 1] + 1;
                up[i] = up[i - 1];
            } else {
                down[i] = down[i - 1];
                up[i] = up[i - 1];
            }
        }
        return Math.max(down[nums.length - 1], up[nums.length - 1]);
    }
}
```

**Complexity Analysis**

* Time complexity : $O(n)$. Only one pass over the array length.
* Space complexity : $O(n)$. Two arrays of the same length are used for dp.

---

### Approach #4 Space-Optimized Dynamic Programming

**Algorithm**

This approach relies on the same concept as [Approach #3](https://leetcode.com/articles/wiggle-subsequence/#approach-3-linear-dynamic-programming-accepted). But we can observe that in the DP approach, for updating elements $\text{up}[i]$ and $\text{down}[i]$, we need only the elements $up[i-1]$ and $down[i-1]$. Thus, we can save space by not using the whole array, but only the last elements.

```java
public class Solution {
    public int wiggleMaxLength(int[] nums) {
        if (nums.length < 2)
            return nums.length;
        int down = 1, up = 1;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] > nums[i - 1])
                up = down + 1;
            else if (nums[i] < nums[i - 1])
                down = up + 1;
        }
        return Math.max(down, up);
    }
}
```

**Complexity Analysis**

* Time complexity : $O(n)$. Only one pass over the array length.
* Space complexity : $O(1)$. Constant space is used.

---

### Approach #5 Greedy Approach

**Algorithm**

We need not necessarily need dp to solve this problem. This problem is equivalent to finding the number of alternating max. and min. peaks in the array. Since, if we choose any other intermediate number to be a part of the current wiggle subsequence, the maximum length of that wiggle subsequence will always be less than or equal to the one obtained by choosing only the consecutive max. and min. elements.

This can be clarified by looking at the following figure:
![Wiggle Peaks](images/376_Wiggle_Subsequence.PNG)

From the above figure, we can see that if we choose **C** instead of **D** as the 2nd point in the wiggle subsequence, we can't include the point **E**. Thus, we won't obtain the maximum length wiggle subsequence.

Thus, to solve this problem, we maintain a variable $\text{prevdiff}$, where $\text{prevdiff}$ is used to indicate whether the current subsequence of numbers lies in an increasing or decreasing wiggle. If $\text{prevdiff} > 0$, it indicates that we have found the increasing wiggle and are looking for a decreasing wiggle now. Thus, we update the length of the found subsequence when $\text{diff}$ ($\text{nums}[i]-nums[i-1]$) becomes negative. Similarly, if $\text{prevdiff} < 0$, we will update the count when $\text{diff}$ ($\text{nums}[i]-nums[i-1]$) becomes positive.

When the complete array has been traversed, we get the required count, which represents the length of the longest wiggle subsequence.

```java
public class Solution {
    public int wiggleMaxLength(int[] nums) {
        if (nums.length < 2)
            return nums.length;
        int prevdiff = nums[1] - nums[0];
        int count = prevdiff != 0 ? 2 : 1;
        for (int i = 2; i < nums.length; i++) {
            int diff = nums[i] - nums[i - 1];
            if ((diff > 0 && prevdiff <= 0) || (diff < 0 && prevdiff >= 0)) {
                count++;
                prevdiff = diff;
            }
        }
        return count;
    }
}
```

**Complexity Analysis**

* Time complexity : $O(n)$. We traverse the given array once.

* Space complexity : $O(1)$. No extra space is used.