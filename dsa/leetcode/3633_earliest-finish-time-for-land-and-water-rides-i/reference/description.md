## Description

<p data-end="143" data-start="53">You are given two categories of theme park attractions: <strong data-end="122" data-start="108">land rides</strong> and <strong data-end="142" data-start="127">water rides</strong>.

<ul>
	<li data-end="163" data-start="147"><strong data-end="161" data-start="147">Land rides</strong>

	<ul>
		<li data-end="245" data-start="168"><code data-end="186" data-start="168">landStartTime[i]</code> – the earliest time the `i^th` land ride can be boarded.</li>
		<li data-end="306" data-start="250"><code data-end="267" data-start="250">landDuration[i]</code> – how long the `i^th` land ride lasts.</li>
	</ul>
	</li>
	<li><strong data-end="325" data-start="310">Water rides</strong>
	<ul>
		<li><code data-end="351" data-start="332">waterStartTime[j]</code> – the earliest time the `j^th` water ride can be boarded.</li>
		<li><code data-end="434" data-start="416">waterDuration[j]</code> – how long the `j^th` water ride lasts.</li>
	</ul>
	</li>
</ul>

<p data-end="569" data-start="476">A tourist must experience <strong data-end="517" data-start="502">exactly one</strong> ride from <strong data-end="536" data-start="528">each</strong> category, in <strong data-end="566" data-start="550">either order</strong>.

<ul>
	<li data-end="641" data-start="573">A ride may be started at its opening time or <strong data-end="638" data-start="618">any later moment</strong>.</li>
	<li data-end="715" data-start="644">If a ride is started at time <code data-end="676" data-start="673">t</code>, it finishes at time <code data-end="712" data-start="698">t + duration</code>.</li>
	<li data-end="834" data-start="718">Immediately after finishing one ride the tourist may board the other (if it is already open) or wait until it opens.</li>
</ul>

<p data-end="917" data-start="836">Return the <strong data-end="873" data-start="847">earliest possible time</strong> at which the tourist can finish both rides.
