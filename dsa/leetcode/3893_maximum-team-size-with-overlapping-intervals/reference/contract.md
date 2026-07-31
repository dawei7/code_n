## Function Contract

**Inputs**

- `startTime`: An array whose element at index $i$ is employee $i$'s start time.
- `endTime`: An equally sized array whose element at index $i$ is employee $i$'s end time.

The two values at the same index form one employee's closed interval. Every start time is strictly smaller than its paired end time.

**Return value**

Return the maximum team size for which some member's interval overlaps every other member's interval.
