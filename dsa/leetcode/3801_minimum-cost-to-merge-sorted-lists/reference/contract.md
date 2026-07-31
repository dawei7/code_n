## Function Contract

**Inputs**

- `lists`: An array of nonempty integer arrays, each already sorted in non-decreasing order.

After every operation, the chosen pair is replaced by its complete sorted merge. The insertion position of that merged list does not restrict which pair may be selected next.

**Return value**

Return an integer equal to the smallest attainable sum of merge costs after combining all input lists into one sorted list.
