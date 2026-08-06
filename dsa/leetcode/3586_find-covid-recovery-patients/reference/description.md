## Description

Table: `patients`

```

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| patient_id  | int     |
| patient_name| varchar |
| age         | int     |
+-------------+---------+
patient_id is the unique identifier for this table.
Each row contains information about a patient.

```

Table: `covid_tests`

```

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| test_id     | int     |
| patient_id  | int     |
| test_date   | date    |
| result      | varchar |
+-------------+---------+
test_id is the unique identifier for this table.
Each row represents a COVID test result. The result can be Positive, Negative, or Inconclusive.

```

Write a solution to find patients who have **recovered from COVID** - patients who tested positive but later tested negative.

<ul>
	<li>A patient is considered recovered if they have **at least one** **Positive** test followed by at least one **Negative** test on a **later date**</li>
	<li>Calculate the **recovery time** in days as the **difference** between the **first positive test** and the **first negative test** after that **positive test**</li>
	<li>**Only include** patients who have both positive and negative test results</li>
</ul>

Return *the result table ordered by *`recovery_time`* in **ascending** order, then by *`patient_name`* in **ascending** order*.

The result format is in the following example.
