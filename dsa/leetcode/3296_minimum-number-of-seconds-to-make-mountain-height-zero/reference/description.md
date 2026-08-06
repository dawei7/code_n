## Description

You are given an integer `mountainHeight` denoting the height of a mountain.

You are also given an integer array `workerTimes` representing the work time of workers in **seconds**.

<p data-end="203" data-start="76">Each worker may reduce the mountain's height by any **non-negative integer** amount. If worker <code data-end="170" data-start="167">i</code> reduces the height by <code data-end="196" data-start="193">x</code>, then:

<ul data-end="415" data-start="208">
	<li data-end="275" data-section-id="66oopy" data-start="208">reducing the first unit of height takes <code data-end="266" data-start="250">workerTimes[i]</code> seconds,</li>
	<li data-end="340" data-section-id="9o9grm" data-start="278">reducing the second unit takes <code data-end="331" data-start="311">workerTimes[i] * 2</code> seconds,</li>
	<li data-end="348" data-section-id="1o23ba" data-start="343">...</li>
	<li data-end="413" data-section-id="1brl21f" data-start="351">reducing the <code data-end="369" data-start="366">x</code>-th unit takes <code data-end="404" data-start="384">workerTimes[i] * x</code> seconds.</li>
</ul>

<p data-end="516" data-start="418">The total time spent by worker <code data-end="452" data-start="449">i</code> is the sum of the times required for all <code data-end="497" data-start="494">x</code> units they reduce. As all workers operate simultaneously, the total time required is the **maximum** time spent by any worker.

Return an integer representing the **minimum** number of seconds required for the workers to make the height of the mountain 0.
