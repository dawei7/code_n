[TOC]

## Solution

### Approach 1: Using Hash Map

**Intuition**

The intuition behind using a hash map is pretty clear in this case. We are given that the array would be of size `N` and it should contain numbers from `1` to `N`. However, some of the numbers are missing. All we have to do is keep track of which numbers we encounter in the array and then iterate from $$1 \cdots N$$ and check which numbers did not appear in the hash table. Those will be our missing numbers. Let's look at a formal algorithm based on this idea and then an animation explaining the same with the help of a simple example.

**Algorithm**

1. Initialize a hash map, `hash` to keep track of the numbers that we encounter in the array. Note that we can use a `set` data structure as well in this case since we are not concerned about the frequency counts of elements.

    <center>
    <img src="images/anim1.png" width="700"/>
    </center>
    
    > Note that for the purposes of illustration, we have use a hash map of size 14 and have ordered the keys of the hash map from 0 to 14. Also, we will be using a simple hash function that directly maps the array entries to their corresponding keys in the hash map. Usually, the mapping is not this simple and is dependent upon the hash function being used in the implementation of the hash map. 
  
2. Next, iterate over the given array one element at a time and for each element, insert an entry in the hash map. Even if an entry were to exist before in the hash map, it will simply be over-written. For the above example, let's look at the final state of the hash map once we process the last element of the array.

    <center>
    <img src="images/anim9.png" width="700"/>
    </center>

3. Now that we know the `unique` set of elements from the array, we can simply find out the missing elements from the range $$1 \cdots N$$.
4. Iterate over all the numbers from $$1 \cdots N$$ and for each number, check if there's an entry in the hash map. If there is no entry, add that missing number to a result array that we will return from the function eventually. 

<center>



![Slide 1](images/slideshow_448_Disappeared_Nums_anim1.png)

![Slide 2](images/slideshow_448_Disappeared_Nums_anim2.png)

![Slide 3](images/slideshow_448_Disappeared_Nums_anim3.png)

![Slide 4](images/slideshow_448_Disappeared_Nums_anim4.png)

![Slide 5](images/slideshow_448_Disappeared_Nums_anim5.png)

![Slide 6](images/slideshow_448_Disappeared_Nums_anim6.png)

![Slide 7](images/slideshow_448_Disappeared_Nums_anim7.png)

![Slide 8](images/slideshow_448_Disappeared_Nums_anim8.png)

![Slide 9](images/slideshow_448_Disappeared_Nums_anim9.png)



</center>


```python
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        # Hash table for keeping track of the numbers in the array
        # Note that we can also use a set here since we are not 
        # really concerned with the frequency of numbers.
        hash_table = {}
        
        # Add each of the numbers to the hash table
        for num in nums:
            hash_table[num] = 1
        
        # Response array that would contain the missing numbers
        result = []    
        
        # Iterate over the numbers from 1 to N and add all those
        # that don't appear in the hash table. 
        for num in range(1, len(nums) + 1):
            if num not in hash_table:
                result.append(num)
                
        return result        
```



**Complexity Analysis**

* Time Complexity : $$O(N)$$
* Space Complexity : $$O(N)$$
<br/>
<br/>

---

### Approach 2: O(1) Space InPlace Modification Solution

**Intuition**

We definitely need to keep track of all the `unique` numbers that appear in the array. However, we don't want to use any extra space for it. This solution that we will look at in just a moment springs from the fact that

> All the elements are in the range [1, N]

Since we are given this information, we can make use of the input array itself to somehow `mark visited` numbers and then find our missing numbers. Now, we don't want to change the actual data in the array but who's stopping us from changing the `magnitude` of numbers in the array? That is the basic idea behind this algorithm. 

> We will be negating the numbers seen in the array and use the sign of each of the numbers for finding our missing numbers. We will be treating numbers in the array as indices and mark corresponding locations in the array as negative.

**Algorithm**

1. Iterate over the input array one element at a time.
2. For each element `nums[i]`, mark the element at the corresponding location negative if it's not already marked so i.e. $$nums[\; nums[i] \;- 1\;] \times -1$$ .
3. Now, loop over numbers from $$1 \cdots N$$ and for each number check if `nums[j]` is negative. If it is negative, that means we've seen this number somewhere in the array. 
4. Add all the numbers to the resultant array which don't have their corresponding locations marked as negative in the original array.

<center>



![Slide 1](images/slideshow_448_Disappeared_Nums_2_anim21.png)

![Slide 2](images/slideshow_448_Disappeared_Nums_2_anim22.png)

![Slide 3](images/slideshow_448_Disappeared_Nums_2_anim23.png)

![Slide 4](images/slideshow_448_Disappeared_Nums_2_anim24.png)

![Slide 5](images/slideshow_448_Disappeared_Nums_2_anim25.png)

![Slide 6](images/slideshow_448_Disappeared_Nums_2_anim26.png)

![Slide 7](images/slideshow_448_Disappeared_Nums_2_anim27.png)

![Slide 8](images/slideshow_448_Disappeared_Nums_2_anim28.png)

![Slide 9](images/slideshow_448_Disappeared_Nums_2_anim29.png)

![Slide 10](images/slideshow_448_Disappeared_Nums_2_anim30.png)

![Slide 11](images/slideshow_448_Disappeared_Nums_2_anim31.png)

![Slide 12](images/slideshow_448_Disappeared_Nums_2_anim32.png)

![Slide 13](images/slideshow_448_Disappeared_Nums_2_anim33.png)

![Slide 14](images/slideshow_448_Disappeared_Nums_2_anim34.png)

![Slide 15](images/slideshow_448_Disappeared_Nums_2_anim35.png)

![Slide 16](images/slideshow_448_Disappeared_Nums_2_anim36.png)

![Slide 17](images/slideshow_448_Disappeared_Nums_2_anim37.png)



</center>


```python
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        # Iterate over each of the elements in the original array
        for i in range(len(nums)):
            
            # Treat the value as the new index
            new_index = abs(nums[i]) - 1
            
            # Check the magnitude of value at this new index
            # If the magnitude is positive, make it negative 
            # thus indicating that the number nums[i] has 
            # appeared or has been visited.
            if nums[new_index] > 0:
                nums[new_index] *= -1
        
        # Response array that would contain the missing numbers
        result = []    
        
        # Iterate over the numbers from 1 to N and add all those
        # that have positive magnitude in the array 
        for i in range(1, len(nums) + 1):
            if nums[i - 1] > 0:
                result.append(i)
                
        return result        
```


**Complexity Analysis**

* Time Complexity : $$O(N)$$
* Space Complexity : $$O(1)$$ since we are reusing the input array itself as a hash table and the space occupied by the output array doesn't count toward the space complexity of the algorithm. 
<br/>
<br/>