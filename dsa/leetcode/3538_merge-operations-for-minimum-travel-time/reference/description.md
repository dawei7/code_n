## Description

<p data-end="452" data-start="24">You are given a straight road of length `l` km, an integer `n`, an integer `k`<strong data-end="83" data-start="78">, </strong>and **two** integer arrays, `position` and `time`, each of length `n`.

<p data-end="452" data-start="24">The array `position` lists the positions (in km) of signs in **strictly** increasing order (with `position[0] = 0` and `position[n - 1] = l`).

<p data-end="452" data-start="24">Each `time[i]` represents the time (in minutes) required to travel 1 km between `position[i]` and `position[i + 1]`.

<p data-end="593" data-start="454">You **must** perform **exactly** `k` merge operations. In one merge, you can choose any **two** adjacent signs at indices `i` and `i + 1` (with `i > 0` and `i + 1 < n`) and:

<ul data-end="701" data-start="595">
	<li data-end="624" data-start="595">Update the sign at index `i + 1` so that its time becomes `time[i] + time[i + 1]`.</li>
	<li data-end="624" data-start="595">Remove the sign at index `i`.</li>
</ul>

<p data-end="846" data-start="703">Return the **minimum** **total** **travel time** (in minutes) to travel from 0 to `l` after **exactly** `k` merges.
