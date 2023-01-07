# Richest Customer

You are given an `m x n` integer grid `accounts` where `accounts[i][j]` is the amount of money the `i<sup>th</sup>` customer has in the `j<sup>th</sup>` bank. Return* the **wealth** that the richest customer has.*

A customer's **wealth** is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum  **wealth** .

**Example 1:**

 <pre><strong>Input:</strong> accounts = [[1,2,3],[3,2,1]]
> <strong>Output:</strong> 6<br>
> <strong>Explanation</strong><strong>:</strong>
> <code>1st customer has wealth = 1 + 2 + 3 = 6
> </code><code>2nd customer has wealth = 3 + 2 + 1 = 6
> </code>Both customers are considered the richest with a wealth of 6 each, so return 6.
> </pre>

**Example 2:**

<pre><strong>Input:</strong> accounts = [[1,5],[7,3],[3,5]]
> <strong>Output:</strong> 10
> <strong>Explanation</strong>:
> 1st customer has wealth = 6
> 2nd customer has wealth = 10
> 3rd customer has wealth = 8
> The 2nd customer is the r ichest with a wealth of 10.</pre>

**Example 3:**

 <pre><strong>Input:</strong> accounts = [[2,8,7],[7,1,3],[1,9,5]]
> <strong>Output:</strong> 17</pre>
