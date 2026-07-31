## General

Process the array from left to right while maintaining a strictly increasing stack of the positive value levels whose regions can still extend through the processed prefix. A sentinel `0` stays at the bottom.

For a new `value`, pop every stack level greater than it. Such a level cannot extend across this position: before that larger value could be selected as a subarray minimum, the smaller current value would have to be removed, creating a zero barrier. After the pops, there are two possibilities. If `value` equals the top, its existing active region can include this occurrence across any intervening larger values, so no new operation is forced. If `value` is greater than the top, this is the beginning of a distinct active region for that value; push it and count one operation. A zero simply pops all positive levels and is never pushed.

Each counted push is necessary because no earlier equal level remains connected past a smaller value, so those occurrences cannot be zeroed by the same operation. Conversely, removing levels from smaller to larger realizes exactly one operation for every push: an active level's occurrences lie in one segment until a lower barrier closes it. The count is therefore both achievable and a lower bound, making it minimal.

## Complexity detail

Let $n$ be the length of `nums`. Each value is pushed at most once for its position and popped at most once, so all stack work takes $O(n)$ time. In a strictly increasing array, the stack contains all $n$ positive values, giving $O(n)$ auxiliary space.

## Alternatives and edge cases

- **Process distinct values with repeated array scans:** Counting active segments for every value is correct but can require $O(n^2)$ time when all values differ.
- **Recursive minimum splitting:** Choosing a segment minimum and recursing around its occurrences mirrors the operation, but repeated minimum searches can be quadratic and deep recursion can overflow.
- **Difference-array increments:** Summing positive adjacent rises solves a decrement-by-one range problem, not this operation that zeros all copies of a minimum at once.
- **Zeros:** A zero is a permanent separator between useful positive subarrays and resets the stack to its sentinel.
- **Repeated equal levels:** Equal values separated only by larger values share one operation; equality with the stack top must not create another count.
- **Smaller intervening value:** A lower positive value closes every larger active level, even though it is not yet zero.
- **Strictly increasing or decreasing input:** Every positive value begins a distinct level, so the answer equals the array length.
