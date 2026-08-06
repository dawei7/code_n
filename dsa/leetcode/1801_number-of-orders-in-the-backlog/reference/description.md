## Description

You are given a 2D integer array `orders`, where each `orders[i] = [price_i, amount_i, orderType_i]` denotes that `amount_i`_ orders have been placed of type `orderType_i` at the price `price_i`. The `orderType_i` is:



<ul>
	<li>`0` if it is a batch of `buy` orders, or</li>
	<li>`1` if it is a batch of `sell` orders.</li>
</ul>

Note that `orders[i]` represents a batch of `amount_i` independent orders with the same price and order type. All orders represented by `orders[i]` will be placed before all orders represented by `orders[i+1]` for all valid `i`.



There is a **backlog** that consists of orders that have not been executed. The backlog is initially empty. When an order is placed, the following happens:



<ul>
	<li>If the order is a `buy` order, you look at the `sell` order with the **smallest** price in the backlog. If that `sell` order's price is **smaller than or equal to** the current `buy` order's price, they will match and be executed, and that `sell` order will be removed from the backlog. Else, the `buy` order is added to the backlog.</li>
	<li>Vice versa, if the order is a `sell` order, you look at the `buy` order with the **largest** price in the backlog. If that `buy` order's price is **larger than or equal to** the current `sell` order's price, they will match and be executed, and that `buy` order will be removed from the backlog. Else, the `sell` order is added to the backlog.</li>
</ul>

Return *the total **amount** of orders in the backlog after placing all the orders from the input*. Since this number can be large, return it **modulo** `10^9 + 7`.
