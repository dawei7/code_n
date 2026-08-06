## Description

Alice and Bob are playing a fantasy battle game consisting of `n` rounds where they summon one of three magical creatures each round: a Fire Dragon, a Water Serpent, or an Earth Golem. In each round, players **simultaneously** summon their creature and are awarded points as follows:

<ul>
	<li>If one player summons a Fire Dragon and the other summons an Earth Golem, the player who summoned the **Fire Dragon** is awarded a point.</li>
	<li>If one player summons a Water Serpent and the other summons a Fire Dragon, the player who summoned the **Water Serpent** is awarded a point.</li>
	<li>If one player summons an Earth Golem and the other summons a Water Serpent, the player who summoned the **Earth Golem** is awarded a point.</li>
	<li>If both players summon the same creature, no player is awarded a point.</li>
</ul>

You are given a string `s` consisting of `n` characters `'F'`, `'W'`, and `'E'`, representing the sequence of creatures Alice will summon in each round:

<ul>
	<li>If `s[i] == 'F'`, Alice summons a Fire Dragon.</li>
	<li>If `s[i] == 'W'`, Alice summons a Water Serpent.</li>
	<li>If `s[i] == 'E'`, Alice summons an Earth Golem.</li>
</ul>

Bob’s sequence of moves is unknown, but it is guaranteed that Bob will never summon the same creature in two consecutive rounds. Bob *beats* Alice if the total number of points awarded to Bob after `n` rounds is **strictly greater** than the points awarded to Alice.

Return the number of distinct sequences Bob can use to beat Alice.

Since the answer may be very large, return it **modulo** `10^9 + 7`.
