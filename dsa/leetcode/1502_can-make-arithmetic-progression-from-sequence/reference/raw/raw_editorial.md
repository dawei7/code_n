[TOC]



## Solution













---



### Approach 1: Sort



#### Intuition   



Let's start with the most intuitive method. Since we want to determine if `arr` can make an arithmetic progression, we can first sort the `arr` and then check if the difference between each pair of adjacent numbers is equal.



![img](images/1.png)



<br>



#### Algorithm



1) Sort `arr`.

2) Record the first pair difference `diff = arr[1] - arr[0]`.

3) Iterate over the sorted `arr` from `i = 2`, check if every pair difference equals `diff`, return `False` if not.

4) Return `True` when the iteration ends.







#### Implementation




```python
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        diff = arr[1] - arr[0]
        for i in range(2, len(arr)):
            if arr[i] - arr[i - 1] != diff:
                return False
        return True
```






#### Complexity Analysis



Let $$n$$ be the length of the input array `arr`.



* Time complexity: $$O(n\cdot\log n)$$



    - Sorting `arr` takes $$O(n\cdot\log n)$$ time on average.

    - Iterating the sorted `arr` takes $$O(n)$$ time.

    - Therefore, the overall time complexity is $$O(n\cdot\log n)$$.

    



* Space complexity: $$O(n)$$ or $$O(\log n)$$

    - Some extra space is used when we sort $$\text{arr}$$ in place. The space complexity of the sorting algorithm depends on the programming language.

        - In python, the `sort` method sorts a list using the Timsort algorithm, which is a combination of Merge Sort and Insertion Sort and uses $$O(n)$$ additional space.

        - In C++, the sort() function is implemented as a hybrid of Quick Sort, Heap Sort, and Insertion Sort, with worst-case space complexity of $$O(\log n)$$.

        - In Java, Arrays.sort() is implemented using a variant of the Quick Sort algorithm which has a space complexity of $$O(\log n)$$.

    - We then traverse both arrays and calculate the cumulative product sum, this step takes $$O(1)$$ extra space.

    - To sum up, the overall space complexity is $$O(n)$$ for Python and $$O(\log n)$$ for C++ and Java.



<br/>



---



### Approach 2: Set



#### Intuition   



Actually, we don't need to sort `arr`. Instead, we can take advantage of a feature of the arithmetic sequence: the difference between any two adjacent terms is equal. 





Let's assume we have an arithmetic sequence where the first term is `min_value` and every successive element has a common difference `diff`. Then, the difference between each number `arr[i]` and `min_value` must be divisible by `diff`. We can determine `diff` by finding the minimum and maximum values, taking their difference, and dividing by the number of elements between the minimum and maximum which is `n - 1`. `diff = (max_value - min_value) / (n - 1)`.



![img](images/2.png)



Next, we traverse `arr` and check if each element `arr[i]` belongs to this arithmetic sequence. If the difference between `arr[i]` and `min_value` is a multiple of `diff`, then `arr[i]` belongs to this sequence, otherwise, it does not. 



This strategy might not work if there are duplicate elements. For example, let `arr = [1, 2, 3, 2, 5]`. `diff` would be `(5 - 1) / 4 = 1`. The algorithm will be "tricked" since each element will pass the test (arr[i] - 1 divisible by 1).



To counteract this, we will use a set `number_set` to store all the elements we encounter. After traversing the array, if the size of the set is equal to `n`, then the numbers are distinct and must form an arithmetic sequence from `min_value` to `max_value`. As shown in the picture below, `[3, 9, 7, 1, 5]` forms an arithmetic sequence while `[2, 9, 7, 1, 5]` doesn't.



![img](images/2_1.png)



Note that we need to consider some special cases: 



- If `max_value - min_value` is not divisible by `n - 1`, it means `arr` can't form an arithmetic sequence, return `false`.

- If we have `diff = 0`, it means that all the numbers in `arr` are equal, and we can return `true` directly.



<br>



#### Algorithm



1) Find the minimum value `min_value` and the maximum value `max_value` of `arr`, let `n` be the length of `arr`.



2) Check if `max_value - min_value` is divisible by `n - 1`, return `false` if not. Otherwise, set `diff = (max_value - min_value) / (n - 1)`.



3) Initialize an empty set `number_set`.



4) Iterate over `arr`, for each number `arr[i]`:

    - Check if `arr[i] - min_value` is divisible by `diff`, return `false` if not.

    - Add `arr[i]` to `number_set`.



5) Return `true` if the size of `number_set` equals `n`, return `false` otherwise.  





#### Implementation




```python
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        min_value, max_value = min(arr), max(arr)
        n = len(arr)
        
        if max_value - min_value == 0:
            return True
        if (max_value - min_value) % (n - 1):

            return False
        
        diff = (max_value - min_value) // (n - 1)
        number_set = set()
        
        for a in arr:
            if (a - min_value) % diff:
                return False
            number_set.add(a)
        
        return len(number_set) == n
```






#### Complexity Analysis



Let $$n$$ be the length of the input array `arr`.



* Time complexity: $$O(n)$$



    - Finding the minimum and maximum values takes $$O(n)$$ time.

    - We iterate over `arr`, for each element `arr[i]`, we verify if it belongs to the arithmetic sequence then add it to the hash set, which takes $$O(1)$$ time.

    



* Space complexity: $$O(n)$$



    - We create a set to store all visited elements, there might be at most $$n$$ distinct elements in the set. 



<br/>







---



### Approach 3: In-place Modification



#### Intuition   



In the previous solution, we used a set `number_set` to store all the traversed numbers in `arr`. However, by making in-place adjustments to the original array, we can actually avoid this extra space overhead. Note that it is usually not considered good practice to modify the input and you should clarify with an interviewer. We are including this approach for completeness.





We will continue to use ideas from the previous approach. First, find the maximum value `max_value` and the minimum value `min_value` of `arr`, and calculate the common difference `diff` as `diff = (max_value - min_value) / (n - 1)`. 



![img](images/3.png)



Now we have the common difference `diff` and the first term `min_value`. Given a number `arr[i]`, we can calculate its position `j` in the arithmetic sequence as `j = (arr[i] - min_value) / diff`. 



If `j` is already equal to `i`, then this number `arr[i]` is already in the correct position and we can move on to the next `i`. Otherwise, we swap `arr[i]` with `arr[j]`. We can put one number (`arr[i]`) in its correct position with each step.





In reference to the following image, for `i = 0`, `arr[i] = 3` is not in the correct position, so we compute the correct index `j` it belongs to using `j = (arr[i] - 1) / diff = 1`, then we swap `arr[0]` with `arr[1]`. Note that we don't need to create the sorted `arr`, it is just for reference in the image.



![img](images/3_1.png)



Please refer to the following slides as an detailed example:





![Slide 1](images/slideshow_s1_s1.png)

![Slide 2](images/slideshow_s1_s2.png)

![Slide 3](images/slideshow_s1_s3.png)

![Slide 4](images/slideshow_s1_s4.png)

![Slide 5](images/slideshow_s1_s5.png)

![Slide 6](images/slideshow_s1_s6.png)

![Slide 7](images/slideshow_s1_s7.png)

![Slide 8](images/slideshow_s1_s8.png)

![Slide 9](images/slideshow_s1_s9.png)

![Slide 10](images/slideshow_s1_s10.png)





<br>



Note that we need to consider some special cases: 



- If `max_value - min_value` is not divisible by `n - 1`, it means `arr` can't form an arithmetic sequence, return `false`.

- If we have `arr[i] = arr[j], (i != j)`, return `false`. This is the case mentioned in the previous approach where duplicate elements can "trick" our strategy. In the previous approach, we used a set to detect this case.





<br>



#### Algorithm



1) Find the minimum value `min_value` and the maximum value `max_value` of `arr`, let `n` be the length of `arr`.



2) Check if `max_value - min_value` is divisible by `n - 1`, return `false` if not. Otherwise, set `diff = (max_value - min_value) / (n - 1)`.



3) Set the starting index `i` as `i = 0`, while `i < n`:

    

    - If `arr[i]` equals `min_value + i * diff`, move on by letting `i = i + 1`.

    - Else if `arr[i] - min_value` is not divisible by `diff`, return false.

    - Otherwise, find the correct index that `arr[i]` belongs to using `j = (arr[i] - min_value) / diff`. If `arr[i] = arr[j]`, return `false`, otherwise, swap `arr[i]` with `arr[j]`.



    Repeat step 3.





5) Return `true` when the while loop ends.





#### Implementation




```python
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        min_value, max_value = min(arr), max(arr)
        n = len(arr)
        if (max_value - min_value) % (n - 1):
            return False
        
        diff = (max_value - min_value) // (n - 1)
        i = 0
        
        while i < n:
            # If arr[i] is at the correct index, move on.
            if arr[i] == min_value + i * diff:
                i += 1
                
            # If arr[i] doesn't belong to this arithmetic sequence, return False.
            elif (arr[i] - min_value) % diff:
                return False
            
            # Otherwise, find the index j to which arr[i] belongs, swap arr[j] with arr[i].
            else:
                j = (arr[i] - min_value) // diff
                
                # If we find duplicated elements, return False.
                if arr[i] == arr[j]:
                    return False
                
                # Swap arr[i] with arr[j].
                arr[i], arr[j] = arr[j], arr[i]
        
        return True 
```






#### Complexity Analysis



Let $$n$$ be the length of the input array `arr`.



* Time complexity: $$O(n)$$



    - Finding the minimum and maximum values takes $$O(n)$$ time.

    - We used a while loop to help place every element `arr[i]` in its correct position. Each `arr[i]` is visited and swapped only once, thus the while loop takes at most $$O(n)$$ time as well. 





* Space complexity: $$O(1)$$



    - We modified `arr` in place.





<br/>