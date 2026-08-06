## Description

Given an array of integers `arr` and an integer `k`.

A value `arr[i]` is said to be stronger than a value `arr[j]` if `|arr[i] - m| > |arr[j] - m|` where `m` is the **centre** of the array.

If `|arr[i] - m| == |arr[j] - m|`, then `arr[i]` is said to be stronger than `arr[j]` if `arr[i] > arr[j]`.

Return *a list of the strongest `k`* values in the array. Return the answer **in any arbitrary order**.

The **centre** is the middle value in an ordered integer list. More formally, if the length of the list is n, the centre is the element in position `((n - 1) / 2)` in the sorted list **(0-indexed)**.

<ul>
	<li>For `arr = [6, -3, 7, 2, 11]`, `n = 5` and the centre is obtained by sorting the array `arr = [-3, 2, 6, 7, 11]` and the centre is `arr[m]` where `m = ((5 - 1) / 2) = 2`. The centre is `6`.</li>
	<li>For `arr = [-7, 22, 17, 3]`, `n = 4` and the centre is obtained by sorting the array `arr = [-7, 3, 17, 22]` and the centre is `arr[m]` where `m = ((4 - 1) / 2) = 1`. The centre is `3`.</li>
</ul>

<div class="simple-translate-system-theme" id="simple-translate">
<div>
<div class="simple-translate-button isShow" style="background-image: url("moz-extension://8a9ffb6b-7e69-4e93-aae1-436a1448eff6/icons/512.png"); height: 22px; width: 22px; top: 266px; left: 381px;"> </div>

<div class="simple-translate-panel " style="width: 300px; height: 200px; top: 0px; left: 0px; font-size: 13px;">
<div class="simple-translate-result-wrapper" style="overflow: hidden;">
<div class="simple-translate-move" draggable="true"> </div>

<div class="simple-translate-result-contents">
<p class="simple-translate-result" dir="auto"> 

<p class="simple-translate-candidate" dir="auto"> 

</div>
</div>
</div>
</div>
</div>
