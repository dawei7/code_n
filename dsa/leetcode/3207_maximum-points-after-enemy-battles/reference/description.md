## Description

You are given an integer array `enemyEnergies` denoting the energy values of various enemies.

You are also given an integer `currentEnergy` denoting the amount of energy you have initially.

You start with 0 points, and all the enemies are unmarked initially.

You can perform **either** of the following operations **zero **or multiple times to gain points:

<ul>
	<li>Choose an **unmarked** enemy, `i`, such that `currentEnergy >= enemyEnergies[i]`. By choosing this option:

	<ul>
		<li>You gain 1 point.</li>
		<li>Your energy is reduced by the enemy's energy, i.e. `currentEnergy = currentEnergy - enemyEnergies[i]`.</li>
	</ul>
	</li>
	<li>If you have **at least** 1 point, you can choose an **unmarked** enemy, `i`. By choosing this option:
	<ul>
		<li>Your energy increases by the enemy's energy, i.e. `currentEnergy = currentEnergy + enemyEnergies[i]`.</li>
		<li>The <font face="monospace">e</font>nemy `i` is **marked**.</li>
	</ul>
	</li>
</ul>

Return an integer denoting the **maximum** points you can get in the end by optimally performing operations.
