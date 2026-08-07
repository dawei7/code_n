## Function Contract

**Input**

- `Friends`: the friend, friend-name, and chosen-activity table described above.
- `Activities`: the catalog of activity names described above.

Every catalog activity has at least one participating friend. Let $F$ be the number of friend rows, $A$ the number of catalog activities, and $N=F+A$.

**Return value**

Return one column:

- `activity`: the name of each activity whose number of participating friends is strictly greater than the minimum activity count and strictly less than the maximum activity count.

If several activities share either extreme, exclude all of them. The result order is unrestricted.
