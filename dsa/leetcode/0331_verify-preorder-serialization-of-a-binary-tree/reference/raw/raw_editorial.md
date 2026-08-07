[TOC]

## Solution

--- 

### Approach 1: Iteration

**Intuition**

Let's start with the simplest but not optimal solution to discuss the idea.

The binary tree could be considered as a number of slots to fulfill. At the start, there is just one slot available for a number 
or null node. Both the number and null node take one slot to be placed. For the null node, the story ends up here, whereas the number will add into the tree two slots for the child nodes. Each child node could be, again, a number or a null.  
 
> The idea is straightforward: take the nodes one by one from preorder traversal, and compute the number of available slots. If at the end all available slots are used up, the preorder traversal represents the valid serialization. 

- In the beginning, there is one available slot.   

- Each number or null consumes one slot.

- Null node adds no slots, whereas each number adds two slots for the child nodes.

![fig](images/rules.png)

**Algorithm**

- Initiate the number of available slots: `slots = 1`.

- Split preorder traversal by comma, and iterate over the resulting array. At each step :

    - Both a number and a null node take one slot: `slots = slot - 1`.
    
    - If the number of available slots is negative, the preorder traversal is invalid, return False.
    
    - Non-empty node `node != '#'` creates two more available slots: `slots = slots + 2`.
    
- Preorder traversal is valid if all available slots are used up: return `slots == 0`.

**Implementation**


```python
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        # number of available slots
        slots = 1

        for node in preorder.split(','):
            # one node takes one slot
            slots -= 1
            
            # no more slots available
            if slots < 0:
                return False
            
            # non-empty node creates two children slots
            if node != '#':
                slots += 2
        
        # all slots should be used up
        return slots == 0
```


**Complexity Analysis**

* Time complexity : $$\mathcal{O}(N)$$ to iterate over the string of length N. 

* Space complexity : $$\mathcal{O}(N)$$ to keep split array in memory. 
<br /> 
<br />


---
### Approach 2: One pass

**Intuition**

Approach 1 uses $$\mathcal{O}(N)$$ space to keep a split array in memory, and for sure that should be optimized. The idea is to iterate over the string itself and not over the array of nodes.

During the iteration, one has to update the number of available slots at each comma character. First, one should decrease the number of slots by one, because both empty and non-empty nodes take one slot. Second, if the node is a non-empty one, i.e. the character just before the comma is not equal to `#`, one should add two more slots for the child nodes. 

The last node should be considered separately since there is no comma after it.



![Slide 1](images/slideshow_331_LIS_331_slide_1.png)

![Slide 2](images/slideshow_331_LIS_331_slide_2.png)

![Slide 3](images/slideshow_331_LIS_331_slide_3.png)

![Slide 4](images/slideshow_331_LIS_331_slide_4.png)

![Slide 5](images/slideshow_331_LIS_331_slide_5.png)

![Slide 6](images/slideshow_331_LIS_331_slide_6.png)

![Slide 7](images/slideshow_331_LIS_331_slide_7.png)

![Slide 8](images/slideshow_331_LIS_331_slide_8.png)

![Slide 9](images/slideshow_331_LIS_331_slide_9.png)

![Slide 10](images/slideshow_331_LIS_331_slide_10.png)

![Slide 11](images/slideshow_331_LIS_331_slide_11.png)

![Slide 12](images/slideshow_331_LIS_331_slide_12.png)

![Slide 13](images/slideshow_331_LIS_331_slide_13.png)

![Slide 14](images/slideshow_331_LIS_331_slide_14.png)

![Slide 15](images/slideshow_331_LIS_331_slide_15.png)

![Slide 16](images/slideshow_331_LIS_331_slide_16.png)

![Slide 17](images/slideshow_331_LIS_331_slide_17.png)

![Slide 18](images/slideshow_331_LIS_331_slide_18.png)

![Slide 19](images/slideshow_331_LIS_331_slide_19.png)

![Slide 20](images/slideshow_331_LIS_331_slide_20.png)

![Slide 21](images/slideshow_331_LIS_331_slide_21.png)

![Slide 22](images/slideshow_331_LIS_331_slide_22.png)

![Slide 23](images/slideshow_331_LIS_331_slide_23.png)

![Slide 24](images/slideshow_331_LIS_331_slide_24.png)

![Slide 25](images/slideshow_331_LIS_331_slide_25.png)

![Slide 26](images/slideshow_331_LIS_331_slide_26.png)

![Slide 27](images/slideshow_331_LIS_331_slide_27.png)



**Algorithm**

- Initiate the number of available slots: `slots = 1`.

- Iterate over the string. At each comma :

    - Both a number and a null node take one slot: `slots = slot - 1`.
    
    - If the number of available slots is negative, the preorder traversal is invalid, return False.
    
    - Non-empty node, detected by non-`#` character before comma, creates two more available slots: `slots = slots + 2`.
    
- The last node should be considered separately since there is no comma after it. 
    
- Preorder traversal is valid if all available slots are used up: return `slots == 0`.

**Implementation**


```python
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        # number of available slots
        slots = 1
        
        prev = None  # previous character
        for ch in preorder:
            if ch == ',':
                # one node takes one slot
                slots -= 1

                # no more slots available
                if slots < 0:
                    return False

                # non-empty node creates two children slots
                if prev != '#':
                    slots += 2
            prev = ch
        
        # the last node
        slots = slots + 1 if ch != '#' else slots - 1 
        # all slots should be used up
        return slots == 0
```


**Complexity Analysis**

* Time complexity : $$\mathcal{O}(N)$$ to iterate over the string of length N. 

* Space complexity : $$\mathcal{O}(1)$$, it's a constant space solution.