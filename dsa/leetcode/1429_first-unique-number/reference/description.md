## Description

A queue of integers begins with every value in `nums`, in the order given. A value is **unique** when it occurs exactly once in the queue. Among all values that are currently unique, the first unique value is the one whose sole occurrence appears earliest.

Implement a `FirstUnique` object that supports inspecting this value while the queue grows. Construction places the complete initial array into the queue. Calling `add(value)` appends one more occurrence of `value`; existing elements never leave the underlying queue, although a repeated value stops being unique.

Calling `showFirstUnique()` returns the first unique integer at that moment. If every value has occurred at least twice, return `-1`.
