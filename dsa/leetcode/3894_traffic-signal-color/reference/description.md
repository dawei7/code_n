## Description

You are given an integer `timer` representing the remaining time (in seconds) on a traffic signal.

The signal follows these rules:

<ul>
	<li>If `timer == 0`, the signal is `"Green"`</li>
	<li>If `timer == 30`, the signal is `"Orange"`</li>
	<li>If `30 < timer <= 90`, the signal is `"Red"`</li>
</ul>

Return the current state of the signal. If none of the above conditions are met, return `"Invalid"`.
