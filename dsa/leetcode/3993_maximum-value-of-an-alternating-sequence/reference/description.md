## Description

You are given three integers `n`, `s`, and `m`.

A sequence `seq` of integers of length `n` is considered **valid** if:

<ul>
	<li>`seq[0] = s`.</li>
	<li>The sequence is **alternating**, meaning that either:
	<ul>
		<li>`seq[0] > seq[1] < seq[2] > ...`, or</li>
		<li>`seq[0] < seq[1] > seq[2] < ...`.</li>
	</ul>
	</li>
	<li>For every adjacent pair, `|seq[i] - seq[i - 1]| <= m`.</li>
</ul>

A sequence of length 1 is considered alternating.

Return the **maximum** possible element that can appear in any valid sequence.
