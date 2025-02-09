import pandas as pd
import matplotlib.pyplot as plt

from analysis import analyze_data

# Load Data & Analysis
df = pd.read_csv('portfolio_data.csv')
totalInvestedAmount, currentProfitLoss, averageInvestedAmount, averageQuantity, sharesPerSymbol, sector_percentage, quantity, ticker = analyze_data()

# Create figure and subplots (2 rows, 2 columns)
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12, 8))

# Set background color for the entire figure
fig.patch.set_facecolor('#2b4457')

# Plot 1: Total Invested Amount
axes[0, 0].text(0.5, 0.5, f"Total Invested Amount: ${totalInvestedAmount:,.2f}", 
                fontsize=16, ha="center", va="center", color='white', 
                bbox=dict(facecolor='#156082', edgecolor='#156082', boxstyle='round,pad=2.25'))
axes[0, 0].set_axis_off()

# Plot 2: Average Quantity
axes[0, 1].text(0.5, 0.5, f"Average Quantity: {averageQuantity:,.0f}", 
                fontsize=16, ha="center", va="center", color='white', 
                bbox=dict(facecolor='#156082', edgecolor='#156082', boxstyle='round,pad=2.25'))
axes[0, 1].set_axis_off()


# Plot 3: Column chart
axes[1, 0].barh(ticker, quantity, color='#156082')
axes[1, 0].set_title("Number of Shares per Ticker", color="white")
axes[1, 0].set_facecolor('none')  # Transparent background
axes[1, 0].tick_params(colors='white')  
for spine in axes[1, 0].spines.values():
    spine.set_edgecolor('white')  


# Plot 4: Table for Sector %
ax3 = axes[1, 1]  
ax3.axis('off')  # Hide axes

# Create the table directly
table = ax3.table(cellText=sector_percentage.reset_index().values, 
                  colLabels=["Sector", "%"], 
                  loc="center", 
                  cellLoc="center", 
                  colLoc="center", 
                  bbox=[0, 0, 1, 1])  

# Title
ax3.text(0.5, 1.05, 'Sectors', ha='center', va='center', fontsize=14, color="white")

# Style table
table.auto_set_font_size(False)
table.set_fontsize(12)

for cell in table.get_celld().values():
    cell.set_text_props(color='white')  
    cell.set_edgecolor('white')  
    cell.set_facecolor('#2b4457')  
    cell.PAD = 0  # Minimize padding



# Show the plot
plt.tight_layout()
plt.show()