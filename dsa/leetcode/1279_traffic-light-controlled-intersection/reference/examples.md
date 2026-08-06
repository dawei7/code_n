## Examples

**Example 1**

- **Input:** `cars = [1,3,5,2,4], directions = [2,1,2,4,3], arrivalTimes = [10,20,30,40,50]`
- **Output:** `["Car 1 Has Passed Road A In Direction 2","Car 3 Has Passed Road A In Direction 1","Car 5 Has Passed Road A In Direction 2","Traffic Light On Road B Is Green","Car 2 Has Passed Road B In Direction 4","Car 4 Has Passed Road B In Direction 3"]`
- **Explanation:** Road A is green initially, so cars `1`, `3`, and `5` cross without a light change. Car `2` then requests green for Road B before crossing in direction `4`; car `4` subsequently crosses Road B in direction `3` under the unchanged light.

**Example 2**

- **Input:** `cars = [1,2,3,4,5], directions = [2,4,3,3,1], arrivalTimes = [10,20,30,40,40]`
- **Output:** `["Car 1 Has Passed Road A In Direction 2","Traffic Light On Road B Is Green","Car 2 Has Passed Road B In Direction 4","Car 3 Has Passed Road B In Direction 3","Traffic Light On Road A Is Green","Car 5 Has Passed Road A In Direction 1","Traffic Light On Road B Is Green","Car 4 Has Passed Road B In Direction 3"]`
- **Explanation:** This execution finishes without deadlock. Car `1` crosses the initially green Road A. Road B becomes green for cars `2` and `3`; Road A then becomes green for car `5`; after car `5` clears the intersection, Road B becomes green again for car `4`. Because cars `4` and `5` arrive at the same time, an execution in which car `4` crosses before the switch to Road A and car `5` crosses afterward is also correct and accepted.
