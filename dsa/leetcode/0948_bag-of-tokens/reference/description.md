## Description

You start with an initial **power** of `power`, an initial **score** of `0`, and a bag of tokens given as an integer array `tokens`, where each `tokens[i]` denotes the value of token*_i*.

Your goal is to **maximize** the total **score** by strategically playing these tokens. In one move, you can play an **unplayed** token in one of the two ways (but not both for the same token):

<ul>
	<li>**Face-up**: If your current power is **at least** `tokens[i]`, you may play token*_i*, losing `tokens[i]` power and gaining `1` score.</li>
	<li>**Face-down**: If your current score is **at least** `1`, you may play token*_i*, gaining `tokens[i]` power and losing `1` score.</li>
</ul>

Return *the **maximum** possible score you can achieve after playing **any** number of tokens*.
