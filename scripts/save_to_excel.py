import pandas as pd
from fetch_data import fetch_crypto_data

def save_to_excel():
    data = fetch_crypto_data()
    df = pd.DataFrame(data, columns=["name", "symbol", "current_price", "market_cap", "total_volume", "price_change_percentage_24h"])
    df.rename(columns={
        "name": "Name",
        "symbol": "Symbol",
        "current_price": "Price",
        "market_cap": "MarketCap",
        "total_volume": "Volume",
        "price_change_percentage_24h": "Change_24h"
    }, inplace=True)
    df.to_excel("data/Crypto_Live_Data.xlsx", index=False)

if __name__ == "__main__":
    save_to_excel()
    print("✅ Crypto data saved to Excel!")
