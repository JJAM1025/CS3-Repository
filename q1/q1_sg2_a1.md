# Annex A: Computational Thinking Exercise: "Smart School Canteen Queue"
**Section:** 9 - Pinatubo\
**Score:** ____________\
**C# / Name:** 10 - Mancao, Jaime Jesus A.\
11 - Manlapaz, Lorenzo Karl P.\
12 - Navarro, Angelo Derick M.\
**Date:** August 13, 2026

### Scenario
The PSHS school canteen is small and often gets crowded during lunch break. Students line up to buy food, but the process is slow because:
- Some students take too long to decide what to order.
- The cashier has to manually calculate totals and give change.
- There is no system to track which food items are running out.
- Your group’s task is to decompose this problem into smaller, manageable parts that could be solved with computational thinking (CT) Skills.

### Step 1: Identify the Big Problem
Main Problem: The canteen is too small and gets crowded during lunch.

### Step 2: Identify three to four Sub-Problems
Please list possible sub-problems:
1. Students order too long in the line.
2. The cashier has to calculate the change on the spot, making the line longer.
3. The food menu does not get updated about sold out stocks.

### Step 3: Define Computational Thinking Approaches
For each sub-problem, apply CT skills:
| Sub-problem | CT Skills | Example Solution |
| ----------- | ----------- | ----------- |
| Students order too long in the line. | Algorithm Design | Make an algorithm that allows students to pre-order their meals online. |
| The cashier has to calculate the change on the spot, making the line longer. | Abstraction, Algorithm Design | Make online payment the norm. An alternative that could be achieved if a student can’t pay online, make an algorithm that allows the cashier people to properly calculate the change easily by just inputting the food items and amount of money received. |
| The food menu does not get updated about sold out stocks. | Algorithm Design | Use the same algorithm solving the cashier problem. Input the stock of food items and once it sells out based on the inputting of food items, it lists on the online food menu that it is sold out. |

### Step 4: Draw a flowchart or write a pseudocode for the identified sub-problem

*Note: This pseudocode is for the cashier problem (Sub-problem no. 2)*

> 1. START 
> 2. DEFINE dataset menu with fields: item_name, price, quantity
> 3. DEFINE dataset orders with fields: item_name, quantity
> 4. DEFINE variable total = 0
> 5. DEFINE variable payment = 0
> 6. DEFINE variable change = 0
> 7. FOR EACH item ordered:
>    - INPUT selected_item, ordered_quantity
>    - STORE selected_item and ordered_quantity into orders dataset
>    - GET item_price from menu corresponding to selected_item
>    - CALCULATE item_total = ordered_quantity * item_price
>    - ADD item_total to total  
> 8. INPUT payment
> 9. CALCULATE change = payment - total
> 10. DISPLAY total and change
> 11. END
