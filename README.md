
# 📦 **Pricing Engine - THRD Coding Challenge**

A Python-based pricing engine that dynamically adjusts product prices using stock and sales data based on defined business rules.

## 💡 **Problem Statement**
A pricing engine that adjusts product prices based on:
- **Inventory levels** – the current stock of products.
- **Recent sales performance** – quantity of products sold in the last 30 days.

---

## 📂 **Files**
- **`products.csv`**: Contains SKU (Stock Keeping Unit), current price, cost price, and stock.
- **`sales.csv`**: Contains SKU and quantity sold for the last 30 days.
- **`updated_prices.csv`**: Generated file with the old and new prices after applying the business rules.

---

## ⚙️ **Pricing Rules Applied**

1. **Rule 1: Low Stock, High Demand**  
   - **Condition**: If stock is less than 20 and quantity sold is greater than 30, increase the price by 15%.
   - **Reason**: Low stock combined with high demand justifies a price increase.

2. **Rule 2: Dead Stock**  
   - **Condition**: If stock is greater than 200 and quantity sold is zero, decrease the price by 30%.
   - **Reason**: Dead stock that hasn't been sold requires a price reduction to clear inventory.

3. **Rule 3: Overstocked Inventory**  
   - **Condition**: If stock is greater than 100 and quantity sold is less than 20, decrease the price by 10%.
   - **Reason**: Overstocked items with low sales need price adjustments to stimulate demand.

4. **Rule 4: Minimum Profit Constraint**  
   - **Condition**: Ensure the new price is at least 20% above the cost price.
   - **Reason**: This rule ensures that every product maintains a healthy profit margin.

---

## 💻 **How to Run**
1. Clone this repository to your local machine.
2. Place your `products.csv` and `sales.csv` files in the root folder of the project.
3. Install the required library:
```bash
pip install pandas
```
4. Run the script to update prices:
```bash
python update_prices.py
```
5. The updated prices will be saved in the `updated_prices.csv` file.

---

## 📑 **Example Output**

After running the script, the `updated_prices.csv` will look like:

```
sku,old_price,new_price
A123,649.99 INR,600.00 INR
B456,699.00 INR,803.85 INR
C789,999.00 INR,699.30 INR
```

---

## 📝 **Conclusion**

This project demonstrates how a pricing engine can automatically adjust prices based on stock and sales data while maintaining a minimum profit margin.
