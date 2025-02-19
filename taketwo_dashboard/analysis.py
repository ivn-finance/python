import pandas as pd

def data_analysis():
    
    # Load data
    df = pd.read_csv("data.csv", delimiter=';')

    # Columns conversion & clean up
    numeric_columns = ["Profit Margin"]

    for column in numeric_columns:
        df[column] = (
            df[column]
            .astype(str)                         
            .str.replace(r"[^\d.-]", "", regex=True) 
            .astype(float)                       
        )

    # Analysis
    total_sales = df["Sales"].sum()
    total_profit = df["Profit"].sum()

    average_profit_margin = df["Profit Margin"].mean()
    average_profit = df["Profit"].sum()
    
    region_distribution = df.groupby("Region")["Sales"].sum()
    
    region_percentage = (region_distribution / total_sales) * 100
    region_percentage = region_percentage.round(2)
    region_percentage = region_percentage.sort_values(ascending=False)
    
    return total_sales, total_profit, average_profit_margin, average_profit, region_distribution, region_percentage
