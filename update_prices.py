import pandas as pd

# Load CSV files
products = pd.read_csv('products.csv')
sales = pd.read_csv('sales.csv')

# Merge the data on 'sku'
merged = pd.merge(products, sales, on='sku')

results = []

for _, row in merged.iterrows():
    sku = row['sku']
    current_price = row['current_price']
    cost_price = row['cost_price']
    stock = row['stock']
    quantity_sold = row['quantity_sold']
    new_price = current_price

    # Apply pricing rules
    if stock < 20 and quantity_sold > 30:  # Rule 1
        new_price = current_price * 1.15
    elif stock > 200 and quantity_sold == 0:  # Rule 2
        new_price = current_price * 0.7
    elif stock > 100 and quantity_sold < 20:  # Rule 3
        new_price = current_price * 0.9

    # Apply minimum profit constraint (Rule 4)
    minimum_allowed_price = cost_price * 1.2
    if new_price < minimum_allowed_price:
        new_price = minimum_allowed_price

    new_price = round(new_price, 2)

    results.append({
        'sku': sku,
        'old_price': f"{round(current_price, 2)} INR",
        'new_price': f"{new_price:.2f} INR"
    })

output_df = pd.DataFrame(results)
output_df.to_csv('updated_prices.csv', index=False)

print("✅ updated_prices.csv has been created!")
