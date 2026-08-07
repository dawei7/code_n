## Function Contract

**Input tables**

- `Books(book_id, name, available_from)`: the uniquely identified books and their availability dates.
- `Orders(order_id, book_id, quantity, dispatch_date)`: uniquely identified orders whose `book_id` values reference `Books`.

Let $B$ and $O$ be the numbers of rows in `Books` and `Orders`. A book is old enough when `available_from <= '2019-05-23'`. For such a book, its last-year sales are the sum of `quantity` over orders whose `dispatch_date` lies in the closed interval from `2018-06-23` to `2019-06-23`. Orders before or after that interval do not contribute.

**Return value**

- `book_id`: the identifier of a sufficiently old book whose last-year quantity total is strictly less than 10.
- `name`: that book's name.

Return each qualifying book once, in any order. A qualifying book without an order in the interval has total zero. If no book qualifies, the result is empty.
