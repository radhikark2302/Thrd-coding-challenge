# 📦 Pricing Engine - THRD Coding Challenge
A Python-based pricing engine that dynamically adjusts product prices using stock and sales data based on defined business rules.

## 💡 Problem Statement
A pricing engine that adjusts product prices based on:
- Inventory levels.
- Recent sales performance.

---

## 📂 Files
- `products.csv`: Contains SKU, current price, cost price, and stock.
- `sales.csv`: Contains SKU and quantity sold.
- `updated_prices.csv`: Generated file with old and new prices.

---

## ⚙️ Pricing Rules Applied
1. **Rule 1: Low Stock, High Demand**
2. **Rule 2: Dead Stock**
3. **Rule 3: Overstocked Inventory**
4. **Rule 4: Minimum Profit Constraint**

---

## 💻 How to Run
1. Clone this repo.
2. Place your `products.csv` and `sales.csv` in the root folder.
3. Run:
```bash
python update_prices.py
