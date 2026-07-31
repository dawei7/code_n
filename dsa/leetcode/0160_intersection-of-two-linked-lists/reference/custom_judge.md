## Custom Judge

The judge uses the following auxiliary values to construct each test, but they are not passed to your function:

- `intersectVal`: The value at the shared node, or `0` when the lists do not intersect.
- `listA`: The values read from the head of the first list.
- `listB`: The values read from the head of the second list.
- `skipA`: The number of nodes before the shared node in `listA`.
- `skipB`: The number of nodes before the shared node in `listB`.

From those values, the judge builds the linked structure and passes only `headA` and `headB`. A submission is accepted when it returns the actual shared node object, not merely a matching value.
