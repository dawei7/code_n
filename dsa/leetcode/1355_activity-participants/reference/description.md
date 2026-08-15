### 1. Description

Table: `Friends`

```
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| name          | varchar |
| activity      | varchar |
+---------------+---------+
id is the id of the friend and the primary key for this table in SQL.
name is the name of the friend.
activity is the name of the activity which the friend takes part in.
```

Table: `Activities`

```
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| name          | varchar |
+---------------+---------+
In SQL, id is the primary key for this table.
name is the name of the activity.
```

Find the names of all the activities with neither the maximum nor the minimum number of participants.

Each activity in the `Activities` table is performed by any person in the table Friends.

Return the result table in **any order**.

The result format is in the following example.

### 2. Function Contract

**Input**

- `Friends`: the friend, friend-name, and chosen-activity table described above.
- `Activities`: the catalog of activity names described above.

Every catalog activity has at least one participating friend. Let $F$ be the number of friend rows, $A$ the number of catalog activities, and $N=F+A$.

**Return value**

Return one column:

- `activity`: the name of each activity whose number of participating friends is strictly greater than the minimum activity count and strictly less than the maximum activity count.

If several activities share either extreme, exclude all of them. The result order is unrestricted.

### 3. Examples

#### Example 1

```
- **Input:** 
Friends table:
+------+--------------+---------------+
| id   | name         | activity      |
+------+--------------+---------------+
| 1    | Jonathan D.  | Eating        |
| 2    | Jade W.      | Singing       |
| 3    | Victor J.    | Singing       |
| 4    | Elvis Q.     | Eating        |
| 5    | Daniel A.    | Eating        |
| 6    | Bob B.       | Horse Riding  |
+------+--------------+---------------+
Activities table:
+------+--------------+
| id   | name         |
+------+--------------+
| 1    | Eating       |
| 2    | Singing      |
| 3    | Horse Riding |
+------+--------------+
- **Output:** 
+--------------+
| activity     |
+--------------+
| Singing      |
+--------------+
- **Explanation:** Eating activity is performed by 3 friends, maximum number of participants, (Jonathan D. , Elvis Q. and Daniel A.)
Horse Riding activity is performed by 1 friend, minimum number of participants, (Bob B.)
Singing is performed by 2 friends (Victor J. and Jade W.)
```
