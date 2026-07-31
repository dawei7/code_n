## Examples

**Example 1**

- Input: `Trips = [[1,1,10,1,"completed","2013-10-01"],[2,2,11,1,"cancelled_by_driver","2013-10-01"],[3,3,12,6,"completed","2013-10-01"],[4,4,13,6,"cancelled_by_client","2013-10-01"],[5,1,10,1,"completed","2013-10-02"],[6,2,11,6,"completed","2013-10-02"],[7,3,12,6,"completed","2013-10-02"],[8,2,12,12,"completed","2013-10-03"],[9,3,10,12,"completed","2013-10-03"],[10,4,13,12,"cancelled_by_driver","2013-10-03"]], Users = [[1,"No","client"],[2,"Yes","client"],[3,"No","client"],[4,"No","client"],[10,"No","driver"],[11,"No","driver"],[12,"No","driver"],[13,"No","driver"]]`

**Trips**

| id | client_id | driver_id | city_id | status | request_at |
|---:|---:|---:|---:|---|---|
| 1 | 1 | 10 | 1 | completed | 2013-10-01 |
| 2 | 2 | 11 | 1 | cancelled_by_driver | 2013-10-01 |
| 3 | 3 | 12 | 6 | completed | 2013-10-01 |
| 4 | 4 | 13 | 6 | cancelled_by_client | 2013-10-01 |
| 5 | 1 | 10 | 1 | completed | 2013-10-02 |
| 6 | 2 | 11 | 6 | completed | 2013-10-02 |
| 7 | 3 | 12 | 6 | completed | 2013-10-02 |
| 8 | 2 | 12 | 12 | completed | 2013-10-03 |
| 9 | 3 | 10 | 12 | completed | 2013-10-03 |
| 10 | 4 | 13 | 12 | cancelled_by_driver | 2013-10-03 |

**Users**

| users_id | banned | role |
|---:|---|---|
| 1 | No | client |
| 2 | Yes | client |
| 3 | No | client |
| 4 | No | client |
| 10 | No | driver |
| 11 | No | driver |
| 12 | No | driver |
| 13 | No | driver |

- Output: `[["2013-10-01",0.33],["2013-10-02",0.00],["2013-10-03",0.50]]`

| Day | Cancellation Rate |
|---|---:|
| 2013-10-01 | 0.33 |
| 2013-10-02 | 0.00 |
| 2013-10-03 | 0.50 |

- Explanation: On October 1, request `2` is excluded because its client is banned. Among the three eligible requests, one was cancelled, so the rate is $1/3 = 0.33$. On October 2, request `6` is excluded for the same reason; neither of the remaining two requests was cancelled, giving `0.00`. On October 3, request `8` is excluded, and one of the two eligible requests was cancelled, giving $1/2 = 0.50$.
