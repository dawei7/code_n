## Description

You have a data structure of employee information, including the employee's unique ID, importance value, and direct subordinates' IDs.

You are given an array of employees `employees` where:

<ul>
	<li>`employees[i].id` is the ID of the `i^th` employee.</li>
	<li>`employees[i].importance` is the importance value of the `i^th` employee.</li>
	<li>`employees[i].subordinates` is a list of the IDs of the direct subordinates of the `i^th` employee.</li>
</ul>

Given an integer `id` that represents an employee's ID, return *the **total** importance value of this employee and all their direct and indirect subordinates*.
