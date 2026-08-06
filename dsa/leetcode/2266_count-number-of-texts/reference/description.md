## Description

Alice is texting Bob using her phone. The **mapping** of digits to letters is shown in the figure below.

<img alt="" src="https://assets.leetcode.com/uploads/2022/03/15/1200px-telephone-keypad2svg.png" style="width: 200px; height: 162px;" />
In order to **add** a letter, Alice has to **press** the key of the corresponding digit `i` times, where `i` is the position of the letter in the key.

<ul>
	<li>For example, to add the letter `'s'`, Alice has to press `'7'` four times. Similarly, to add the letter `'k'`, Alice has to press `'5'` twice.</li>
	<li>Note that the digits `'0'` and `'1'` do not map to any letters, so Alice **does not** use them.</li>
</ul>

However, due to an error in transmission, Bob did not receive Alice's text message but received a **string of pressed keys** instead.

<ul>
	<li>For example, when Alice sent the message `"bob"`, Bob received the string `"2266622"`.</li>
</ul>

Given a string `pressedKeys` representing the string received by Bob, return *the **total number of possible text messages** Alice could have sent*.

Since the answer may be very large, return it **modulo** `10^9 + 7`.
