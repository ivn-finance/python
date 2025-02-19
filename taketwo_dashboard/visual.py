import matplotlib.pyplot as plt
import pandas as pd

# Load data from CSV
df = pd.read_csv("data.csv", delimiter=';')

df["Month"] = pd.to_datetime(df["Month"], format='%m', errors='coerce').dt.month_name()  # Convert numeric month to month name

# Calculate total sales and profits per month
total_sales = df.groupby("Month")["Sales"].sum()
total_profits = df.groupby("Month")["Profit"].sum()

# Sort the months to ensure they are in the correct order
total_sales = total_sales.reindex([
    "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"
])
total_profits = total_profits.reindex([
    "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"
])

# Set up the figure with 1 row and 2 columns
fig, axs = plt.subplots(1, 2, figsize=(12, 6))  

# Add a big title centered
title_text = fig.suptitle("Take-Two Interactive Software, Inc. / Dashoboard - 2024", fontsize=20, fontweight='semibold', ha='center', color='white')
plt.subplots_adjust(top=0.85, bottom=0.5)

# Create a rectangle for the title background
bbox_props = dict(boxstyle="round,pad=0.5", edgecolor='none', facecolor='#5147bc')
title_text.set_bbox(bbox_props)

# Set entire figure background color
fig.patch.set_facecolor('#f4f5fe')

# Set background colors for subplots
axs[0].set_facecolor('white')  
axs[1].set_facecolor('white')  

# Chart for Total Sales
axs[0].bar(total_sales.index, total_sales, color='#5147bc') 
axs[0].set_title("Total Sales (millions)", fontsize=16)
axs[0].tick_params(axis='x', rotation=45)

# Chart for Total Profits
axs[1].bar(total_profits.index, total_profits, color='#5147bc')
axs[1].set_title("Total Profits (millions)", fontsize=16)
axs[1].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.show()
