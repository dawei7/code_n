## Description

You are given a **0-indexed** integer array `batteryPercentages` having length `n`, denoting the battery percentages of `n` **0-indexed** devices.

Your task is to test each device `i` **in order** from `0` to `n - 1`, by performing the following test operations:

<ul>
	<li>If `batteryPercentages[i]` is **greater** than `0`:

	<ul>
		<li>**Increment** the count of tested devices.</li>
		<li>**Decrease** the battery percentage of all devices with indices `j` in the range `[i + 1, n - 1]` by `1`, ensuring their battery percentage **never goes below** `0`, i.e, `batteryPercentages[j] = max(0, batteryPercentages[j] - 1)`.</li>
		<li>Move to the next device.</li>
	</ul>
	</li>
	<li>Otherwise, move to the next device without performing any test.</li>
</ul>

Return *an integer denoting the number of devices that will be tested after performing the test operations in order.*
