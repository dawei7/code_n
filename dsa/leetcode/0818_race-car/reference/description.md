## Description

Your car starts at position `0` and speed `+1` on an infinite number line. Your car can go into negative positions. Your car drives automatically according to a sequence of instructions `'A'` (accelerate) and `'R'` (reverse):

<ul>
	<li>When you get an instruction `'A'`, your car does the following:

	<ul>
		<li>`position += speed`</li>
		<li>`speed *= 2`</li>
	</ul>
	</li>
	<li>When you get an instruction `'R'`, your car does the following:
	<ul>
		<li>If your speed is positive then `speed = -1`</li>
		<li>otherwise `speed = 1`</li>
	</ul>
	Your position stays the same.</li>
</ul>

For example, after commands `"AAR"`, your car goes to positions `0 --> 1 --> 3 --> 3`, and your speed goes to `1 --> 2 --> 4 --> -1`.

Given a target position `target`, return *the length of the shortest sequence of instructions to get there*.
