import pandas as pd

def process_crypto_data(data):
    df = pd.DataFrame(data, columns=["name", "symbol", "current_price", "market_cap", "total_volume", "price_change_percentage_24h"])

    top_5 = df.nlargest(5, "market_cap")
    avg_price = df["current_price"].mean()
    max_change = df.loc[df["price_change_percentage_24h"].idxmax()]
    min_change = df.loc[df["price_change_percentage_24h"].idxmin()]

    print("\n🔹 Top 5 Crpto:\n", top_5)
    print("\n🔹 average price:", avg_price)
    print("\n🔹 maximum increase crpto:\n", max_change)
    print("\n🔹 minimum decrease crpto:\n", min_change)

    return df
