import pandas as pd

def analyze_data():
    # Raw data
    df = pd.read_csv("portfolio_data.csv")

    # Columns to convert
    numeric_columns = ["Current Price", "Quantity", "Entry Price", "Profit/Loss", "Invested Amount", "Current Amount"]

    # Clean and convert columns
    for column in numeric_columns:
        df[column] = (
            df[column]
            .astype(str)                         
            .str.replace(r"[^\d.-]", "", regex=True) 
            .astype(float)                       
        )

    # Analysis
    totalInvestedAmount = df["Invested Amount"].sum()
    currentProfitLoss = df["Profit/Loss"].sum()
    
    sector_distribution = df.groupby("Sector")["Invested Amount"].sum()
    sectorPercentage = (sector_distribution / totalInvestedAmount) * 100
    sectorPercentage = sectorPercentage.round(2)
    sectorPercentage = sectorPercentage.sort_values(ascending=False)  # Sort descending

    quantity = df['Quantity']
    ticker = df['Ticker']

    sharesPerSymbol = df.groupby('Ticker')['Quantity'].sum()

    averageInvestedAmount = df["Invested Amount"].mean()
    averageQuantity = df["Quantity"].mean()

    return totalInvestedAmount, currentProfitLoss, averageInvestedAmount, averageQuantity, sharesPerSymbol, sectorPercentage, quantity, ticker

