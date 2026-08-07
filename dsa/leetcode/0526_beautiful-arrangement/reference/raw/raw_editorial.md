[TOC]

## Solution

---
### Approach #1 Brute Force [Time Limit Exceeded]

#### Algorithm

In the brute force method, we can find out all the arrays that can be formed using the numbers from 1 to N(by creating every possible permutation of the given elements). Then, we iterate over all the elements of every permutation generated and check for the required conditions of divisibility.

In order to generate all the possible pairings, we make use of a function `permute(nums, current_index)`. This function creates all the possible permutations of the elements of the given array.

To do so, `permute` takes the index of the current element $$current_index$$ as one of the arguments. Then, it swaps the current element with every other element in the array, lying towards its right, so as to generate a new ordering of the array elements. After the swapping has been done, it makes another call to permute but this time with the index of the next element in the array. While returning back, we reverse the swapping done in the current function call.

Thus, when we reach the end of the array, a new ordering of the array's elements is generated. The following animation depicts the process of generating the permutations.



![Slide 1](images/slideshow_561_Array_561_ArraySlide1.PNG)

![Slide 2](images/slideshow_561_Array_561_ArraySlide2.PNG)

![Slide 3](images/slideshow_561_Array_561_ArraySlide3.PNG)

![Slide 4](images/slideshow_561_Array_561_ArraySlide4.PNG)

![Slide 5](images/slideshow_561_Array_561_ArraySlide5.PNG)

![Slide 6](images/slideshow_561_Array_561_ArraySlide6.PNG)

![Slide 7](images/slideshow_561_Array_561_ArraySlide7.PNG)

![Slide 8](images/slideshow_561_Array_561_ArraySlide8.PNG)

![Slide 9](images/slideshow_561_Array_561_ArraySlide9.PNG)

![Slide 10](images/slideshow_561_Array_561_ArraySlide10.PNG)

![Slide 11](images/slideshow_561_Array_561_ArraySlide11.PNG)



#### Implementation


```python
class Solution:
    def __init__(self):
        self.count = 0

    def countArrangement(self, N: int) -> int:
        nums = [i for i in range(1, N + 1)]
        self.permute(nums, 0)
        return self.count

    def permute(self, nums, l):
        if l == len(nums) - 1:
            for i in range(1, len(nums) + 1):
                if nums[i - 1] % i != 0 and i % nums[i - 1] != 0:
                    break
            else:
                self.count += 1
        for i in range(l, len(nums)):
            nums[i], nums[l] = nums[l], nums[i]
            self.permute(nums, l + 1)
            nums[i], nums[l] = nums[l], nums[i]
```


#### Complexity Analysis

* Time complexity : $$O(n!)$$. A total of $$n!$$ permutations will be generated for an array of length $$n$$.

* Space complexity : $$O(n)$$. The depth of the recursion tree can go upto $$n$$. $$nums$$ array of size $$n$$ is used.

---
### Approach #2 Better Brute Force [Accepted]

#### Algorithm

In the brute force approach, we create the full array for every permutation and then check the array for the given divisibilty conditions. But this method can be optimized to a great extent. To do so, we can keep checking the elements while being added to the permutation array at every step for the divisibility condition and  can stop creating it any further as soon as we find out the element just added to the permutation violates the divisiblity condition. 

#### Implementation


```python
class Solution(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        self.count = 0
        nums = [i + 1 for i in range(N)]
        self.permute(nums, 0)
        return self.count

    def permute(self, nums, l):
        if l == len(nums):
            self.count += 1
        for i in range(l, len(nums)):
            nums[i], nums[l] = nums[l], nums[i]
            if nums[l] % (l + 1) == 0 or (l + 1) % nums[l] == 0:
                self.permute(nums, l + 1)
            nums[i], nums[l] = nums[l], nums[i]
```


#### Complexity Analysis

* Time complexity : $$O(k)$$. $$k$$ refers to the number of valid permutations.

* Space complexity : $$O(n)$$. The depth of recursion tree can go upto $$n$$. Further, $$nums$$ array of size $$n$$ is used, where, $$n$$ is the given number.

---

### Approach #3 Backtracking [Accepted]

#### Algorithm


The idea behind this approach is simple. We try to create all the permutations of numbers from 1 to N. We can fix one number at a particular position and check for the divisibility criteria of that number at the particular position. But, we need to keep a track of the numbers which have already been considered earlier so that they aren't reconsidered while generating the permutations. If the current 
number doesn't satisfy the divisibility criteria, we can leave all the permutations that can be generated with that number at the particular position. This helps to prune the search space of the permutations to a great extent. We do so by trying to place each of the numbers at each position.


We make use of a visited array of size $$N$$. Here, $$visited[i]$$ refers to the $$i^{th}$$ number being already placed/not placed in the array being formed till now(True indicates that the number has already been placed).

We make use of a `calculate` function, which puts all the numbers pending numbers from 1 to N(i.e. not placed till now in the array), indicated by a $$False$$ at the corresponding $$visited[i]$$ position, and tries to create all the permutations with those numbers starting from the $$pos$$ index onwards in the current array. While putting the $$pos^{th}$$ number, we check whether the $$i^{th}$$ number satisfies the divisibility criteria on the go i.e. we continue forward with creating the permutations with the number $$i$$ at the $$pos^{th}$$ position only if the number $$i$$ and $$pos$$ satisfy the given criteria. Otherwise, we continue with putting the next numbers at the same position and keep on generating the permutations.

Look at the animation below for a better understanding of the methodology:



![Slide 1](images/slideshow_526_Beautiful_526_BeautifulSlide1.PNG)

![Slide 2](images/slideshow_526_Beautiful_526_BeautifulSlide2.PNG)

![Slide 3](images/slideshow_526_Beautiful_526_BeautifulSlide3.PNG)

![Slide 4](images/slideshow_526_Beautiful_526_BeautifulSlide4.PNG)

![Slide 5](images/slideshow_526_Beautiful_526_BeautifulSlide5.PNG)

![Slide 6](images/slideshow_526_Beautiful_526_BeautifulSlide6.PNG)

![Slide 7](images/slideshow_526_Beautiful_526_BeautifulSlide7.PNG)

![Slide 8](images/slideshow_526_Beautiful_526_BeautifulSlide8.PNG)

![Slide 9](images/slideshow_526_Beautiful_526_BeautifulSlide9.PNG)

![Slide 10](images/slideshow_526_Beautiful_526_BeautifulSlide10.PNG)

![Slide 11](images/slideshow_526_Beautiful_526_BeautifulSlide11.PNG)

![Slide 12](images/slideshow_526_Beautiful_526_BeautifulSlide12.PNG)

![Slide 13](images/slideshow_526_Beautiful_526_BeautifulSlide13.PNG)

![Slide 14](images/slideshow_526_Beautiful_526_BeautifulSlide14.PNG)

![Slide 15](images/slideshow_526_Beautiful_526_BeautifulSlide15.PNG)

![Slide 16](images/slideshow_526_Beautiful_526_BeautifulSlide16.PNG)

![Slide 17](images/slideshow_526_Beautiful_526_BeautifulSlide17.PNG)

![Slide 18](images/slideshow_526_Beautiful_526_BeautifulSlide18.PNG)

![Slide 19](images/slideshow_526_Beautiful_526_BeautifulSlide19.PNG)

![Slide 20](images/slideshow_526_Beautiful_526_BeautifulSlide20.PNG)

![Slide 21](images/slideshow_526_Beautiful_526_BeautifulSlide21.PNG)

![Slide 22](images/slideshow_526_Beautiful_526_BeautifulSlide22.PNG)

![Slide 23](images/slideshow_526_Beautiful_526_BeautifulSlide23.PNG)

![Slide 24](images/slideshow_526_Beautiful_526_BeautifulSlide24.PNG)

![Slide 25](images/slideshow_526_Beautiful_526_BeautifulSlide25.PNG)

![Slide 26](images/slideshow_526_Beautiful_526_BeautifulSlide26.PNG)



#### Implementation


```python
class Solution:
    def __init__(self):
        self.count = 0

    def countArrangement(self, N):
        visited = [False] * (N + 1)
        self.calculate(N, 1, visited)
        return self.count

    def calculate(self, N, pos, visited):
        if pos > N:
            self.count += 1
            return
        for i in range(1, N + 1):
            if not visited[i] and (pos % i == 0 or i % pos == 0):
                visited[i] = True
                self.calculate(N, pos + 1, visited)
                visited[i] = False
```


#### Complexity Analysis

* Time complexity : $$O(k)$$. $$k$$ refers to the number of valid permutations.

* Space complexity : $$O(n)$$. $$visited$$ array of size $$n$$ is used. The depth of recursion tree will also go upto $$n$$. Here, $$n$$ refers to the given integer $$n$$.

---