[TOC]

## Solution

---

### Approach 1: Brute Force (using Double Length Array) [Time Limit Exceeded]

#### Algorithm

In this method, we make use of an array $doublenums$ which is formed by concatenating two copies of the given $nums$ array one after the other. Now, when we need to find out the next greater element for $\text{nums}[i]$, we can simply scan all the elements $\text{doublenums}[j]$, such that $i < j < length(doublenums)$. The first element found satisfying the given condition is the required result for $\text{nums}[i]$. If no such element is found, we put a $\text{-1}$ at the appropriate position in the $res$ array.

```java
 public class Solution {

    public int[] nextGreaterElements(int[] nums) {
        int[] res = new int[nums.length];
        int[] doublenums = new int[nums.length * 2];
        System.arraycopy(nums, 0, doublenums, 0, nums.length);
        System.arraycopy(nums, 0, doublenums, nums.length, nums.length);
        for (int i = 0; i < nums.length; i++) {
            res[i]=-1;
            for (int j = i + 1; j < doublenums.length; j++) {
                if (doublenums[j] > doublenums[i]) {
                    res[i] = doublenums[j];
                    break;
                }
            }
        }
        return res;
    }
}
```

#### Complexity Analysis

* Time complexity : $O(n^2)$. The complete $doublenums$ array(of size $\text{2n}$) is scanned for all the elements of $nums$ in the worst case.

* Space complexity : $O(n)$. $doublenums$ array of size $\text{2n}$ is used. $res$ array of size $\text{n}$ is used.

---

### Approach 2: Better Brute Force [Accepted]

#### Algorithm

Instead of making a double length copy of $nums$ array , we can traverse circularly in the $nums$ array by making use of the $\text{modulus}$ operator. For every element $\text{nums}[i]$, we start searching in the $nums$ array(of length $n$) from the index $(i+1)\%n$ and look at the next (circularly) $n-1$ elements. For $\text{nums}[i]$ we do so by scanning over $\text{nums}[j]$, such that
$(i+1)\%n ≤ j ≤ (i+(n-1))\%n$, and we look for the first greater element found. If no such element is found, we put a $\text{-1}$ at the appropriate position in the $res$ array.

#### Implementation

```java
 public class Solution {
    public int[] nextGreaterElements(int[] nums) {
        int[] res = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            res[i] = -1;
            for (int j = 1; j < nums.length; j++) {
                if (nums[(i + j) % nums.length] > nums[i]) {
                    res[i] = nums[(i + j) % nums.length];
                    break;
                }
            }
        }
        return res;
    }
}
```

#### Complexity Analysis

* Time complexity : $O(n^2)$. The complete $nums$ array of size $n$ is scanned for all the elements of $nums$ in the worst case.

* Space complexity : $O(n)$. $res$ array of size $n$ is used.

---

### Approach 3: Using Stack [Accepted]

#### Algorithm

This approach makes use of a stack. This stack stores the indices of the appropriate elements from $nums$ array.  The top of the stack refers to the index of the Next Greater Element found so far. We store the indices instead of the elements since there could be duplicates in the $nums$ array. The description of the method will make the above statement clearer.

We start traversing the $nums$ array from right towards the left. For an element $\text{nums}[i]$ encountered, we pop all the elements
$\text{stack}[top]$ from the stack such that $nums\big[\text{stack}[top]\big] \le \text{nums}[i]$. We continue the popping till we encounter a $\text{stack}[top]$ satisfying $nums\big[\text{stack}[top]\big] > \text{nums}[i]$. Now, it is obvious that the current $\text{stack}[top]$ only can act as the
Next Greater Element for $\text{nums}[i]$(right now, considering only the elements lying to the right of $\text{nums}[i]$).

If no element remains on the top of the stack, it means no larger element than $\text{nums}[i]$ exists to its right. Along with this, we also push the index of the element just encountered($\text{nums}[i]$), i.e. $i$ over the top of the stack, so that $\text{nums}[i]$(or $\text{stack}[top]$) now acts as the Next Greater Element for the elements lying to its left.

We go through two such passes over the complete $nums$ array. This is done so as to complete a circular traversal over the $nums$ array. The first pass could make some wrong entries in the $res$ array since it considers only the elements lying to the right of $\text{nums}[i]$, without a circular traversal. But, these entries are corrected in the second pass.

Further, to ensure the correctness of the method, let's look at the following cases.

Assume that $\text{nums}[j]$ is the correct Next Greater Element for $\text{nums}[i]$, such that $i < j ≤ \text{stack}[top]$. Now, whenever we encounter $\text{nums}[j]$, if $\text{nums}[j] > nums\big[\text{stack}[top]\big]$, it would have already popped the previous $\text{stack}[top]$ and $j$ would have become the topmost element. On the other hand, if  $\text{nums}[j] < nums\big[\text{stack}[top]\big]$, it would have become the topmost element by being pushed above the previous $\text{stack}[top]$. In both the cases, if $\text{nums}[j] > \text{nums}[i]$, it will be correctly determined to be the Next Greater Element.

The following example makes the procedure clear:

<!--![Next_Greater_Element_II](images/503_Next_Greater_Element_II.gif)-->

![Slide 1](images/slideshow_503_Next_Greater2_503_Next_Greater2Slide1.JPG)

![Slide 2](images/slideshow_503_Next_Greater2_503_Next_Greater2Slide2.JPG)

![Slide 3](images/slideshow_503_Next_Greater2_503_Next_Greater2Slide3.JPG)

![Slide 4](images/slideshow_503_Next_Greater2_503_Next_Greater2Slide4.JPG)

![Slide 5](images/slideshow_503_Next_Greater2_503_Next_Greater2Slide5.JPG)

![Slide 6](images/slideshow_503_Next_Greater2_503_Next_Greater2Slide6.JPG)

![Slide 7](images/slideshow_503_Next_Greater2_503_Next_Greater2Slide7.JPG)

![Slide 8](images/slideshow_503_Next_Greater2_503_Next_Greater2Slide8.JPG)

![Slide 9](images/slideshow_503_Next_Greater2_503_Next_Greater2Slide9.JPG)

![Slide 10](images/slideshow_503_Next_Greater2_503_Next_Greater2Slide10.JPG)

![Slide 11](images/slideshow_503_Next_Greater2_503_Next_Greater2Slide11.JPG)

![Slide 12](images/slideshow_503_Next_Greater2_503_Next_Greater2Slide12.JPG)

![Slide 13](images/slideshow_503_Next_Greater2_503_Next_Greater2Slide13.JPG)

![Slide 14](images/slideshow_503_Next_Greater2_503_Next_Greater2Slide14.JPG)

![Slide 15](images/slideshow_503_Next_Greater2_503_Next_Greater2Slide15.JPG)

![Slide 16](images/slideshow_503_Next_Greater2_503_Next_Greater2Slide16.JPG)

![Slide 17](images/slideshow_503_Next_Greater2_503_Next_Greater2Slide17.JPG)

![Slide 18](images/slideshow_503_Next_Greater2_503_Next_Greater2Slide18.JPG)

![Slide 19](images/slideshow_503_Next_Greater2_503_Next_Greater2Slide19.JPG)

![Slide 20](images/slideshow_503_Next_Greater2_503_Next_Greater2Slide20.JPG)

![Slide 21](images/slideshow_503_Next_Greater2_503_Next_Greater2Slide21.JPG)

![Slide 22](images/slideshow_503_Next_Greater2_503_Next_Greater2Slide22.JPG)

![Slide 23](images/slideshow_503_Next_Greater2_503_Next_Greater2Slide23.JPG)

![Slide 24](images/slideshow_503_Next_Greater2_503_Next_Greater2Slide24.JPG)

![Slide 25](images/slideshow_503_Next_Greater2_503_Next_Greater2Slide25.JPG)

As the animation above depicts, after the first pass, there are a number of wrong entries(marked as $\text{-1}$) in the $res$ array, because only the elements lying to the corresponding right(non-circular) have been considered till now. But, after the second pass, the correct values are substituted.

#### Implementation

```java
public class Solution {

    public int[] nextGreaterElements(int[] nums) {
        int[] res = new int[nums.length];
        Stack<Integer> stack = new Stack<>();
        for (int i = 2 * nums.length - 1; i >= 0; --i) {
            while (!stack.empty() && nums[stack.peek()] <= nums[i % nums.length]) {
                stack.pop();
            }
            res[i % nums.length] = stack.empty() ? -1 : nums[stack.peek()];
            stack.push(i % nums.length);
        }
        return res;
    }
}
```

#### Complexity Analysis

* Time complexity : $O(n)$. Only two traversals of the $nums$ array are done. Further, at most $\text{2n}$ elements are pushed and popped from the stack.

* Space complexity : $O(n)$. A stack of size $n$ is used. $res$ array of size $n$ is used.