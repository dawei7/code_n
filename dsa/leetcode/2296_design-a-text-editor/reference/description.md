## Description

Design a text editor with a cursor that can do the following:

<ul>
	<li>**Add** text to where the cursor is.</li>
	<li>**Delete** text from where the cursor is (simulating the backspace key).</li>
	<li>**Move** the cursor either left or right.</li>
</ul>

When deleting text, only characters to the left of the cursor will be deleted. The cursor will also remain within the actual text and cannot be moved beyond it. More formally, we have that `0 <= cursor.position <= currentText.length` always holds.

Implement the `TextEditor` class:

<ul>
	<li>`TextEditor()` Initializes the object with empty text.</li>
	<li>`void addText(string text)` Appends `text` to where the cursor is. The cursor ends to the right of `text`.</li>
	<li>`int deleteText(int k)` Deletes `k` characters to the left of the cursor. Returns the number of characters actually deleted.</li>
	<li>`string cursorLeft(int k)` Moves the cursor to the left `k` times. Returns the last `min(10, len)` characters to the left of the cursor, where `len` is the number of characters to the left of the cursor.</li>
	<li>`string cursorRight(int k)` Moves the cursor to the right `k` times. Returns the last `min(10, len)` characters to the left of the cursor, where `len` is the number of characters to the left of the cursor.</li>
</ul>
