## Description

You have `n` jobs and `m` workers. You are given three arrays: `difficulty`, `profit`, and `worker` where:

<ul>
	<li>`difficulty[i]` and `profit[i]` are the difficulty and the profit of the `i^th` job, and</li>
	<li>`worker[j]` is the ability of `j^th` worker (i.e., the `j^th` worker can only complete a job with difficulty at most `worker[j]`).</li>
</ul>

Every worker can be assigned **at most one job**, but one job can be **completed multiple times**.

<ul>
	<li>For example, if three workers attempt the same job that pays `$1`, then the total profit will be `$3`. If a worker cannot complete any job, their profit is `$0`.</li>
</ul>

Return the maximum profit we can achieve after assigning the workers to the jobs.
