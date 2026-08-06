## Description

You have been tasked with writing a program for a popular bank that will automate all its incoming transactions (transfer, deposit, and withdraw). The bank has `n` accounts numbered from `1` to `n`. The initial balance of each account is stored in a **0-indexed** integer array `balance`, with the `(i + 1)^th` account having an initial balance of `balance[i]`.

Execute all the **valid** transactions. A transaction is **valid** if:

<ul>
	<li>The given account number(s) are between `1` and `n`, and</li>
	<li>The amount of money withdrawn or transferred from is **less than or equal** to the balance of the account.</li>
</ul>

Implement the `Bank` class:

<ul>
	<li>`Bank(long[] balance)` Initializes the object with the **0-indexed** integer array `balance`.</li>
	<li>`boolean transfer(int account1, int account2, long money)` Transfers `money` dollars from the account numbered `account1` to the account numbered `account2`. Return `true` if the transaction was successful, `false` otherwise.</li>
	<li>`boolean deposit(int account, long money)` Deposit `money` dollars into the account numbered `account`. Return `true` if the transaction was successful, `false` otherwise.</li>
	<li>`boolean withdraw(int account, long money)` Withdraw `money` dollars from the account numbered `account`. Return `true` if the transaction was successful, `false` otherwise.</li>
</ul>
