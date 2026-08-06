## Description

You are given a stream of **records** about a particular stock. Each record contains a **timestamp** and the corresponding **price** of the stock at that timestamp.

Unfortunately due to the volatile nature of the stock market, the records do not come in order. Even worse, some records may be incorrect. Another record with the same timestamp may appear later in the stream **correcting** the price of the previous wrong record.

Design an algorithm that:

<ul>
	<li>**Updates** the price of the stock at a particular timestamp, **correcting** the price from any previous records at the timestamp.</li>
	<li>Finds the **latest price** of the stock based on the current records. The **latest price** is the price at the latest timestamp recorded.</li>
	<li>Finds the **maximum price** the stock has been based on the current records.</li>
	<li>Finds the **minimum price** the stock has been based on the current records.</li>
</ul>

Implement the `StockPrice` class:

<ul>
	<li>`StockPrice()` Initializes the object with no price records.</li>
	<li>`void update(int timestamp, int price)` Updates the `price` of the stock at the given `timestamp`.</li>
	<li>`int current()` Returns the **latest price** of the stock.</li>
	<li>`int maximum()` Returns the **maximum price** of the stock.</li>
	<li>`int minimum()` Returns the **minimum price** of the stock.</li>
</ul>
