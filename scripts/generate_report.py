from fpdf import FPDF
import pandas as pd

def generate_pdf_report(excel_file="data/Crypto_Live_Data.xlsx", pdf_file="reports/Crypto_Analysis_Report.pdf"):
    # Read data from Excel
    df = pd.read_excel(excel_file)

    # Extract insights
    top_5 = df.nlargest(5, "market_cap")
    avg_price = df["current_price"].mean()
    max_change = df.loc[df["price_change_percentage_24h"].idxmax()]
    min_change = df.loc[df["price_change_percentage_24h"].idxmin()]

    # Create PDF
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", "", 12)  # ✅ Uses default built-in font (No installation needed)

    pdf.cell(200, 10, "Crypto Analysis Report", ln=True, align="C")
    pdf.ln(10)

    pdf.cell(200, 10, f"Average Price: ${avg_price:.2f}", ln=True)

    pdf.ln(5)
    pdf.cell(200, 10, "Top 5 Cryptocurrencies:", ln=True)
    for i, row in top_5.iterrows():
        pdf.cell(200, 10, f"{row['name']} ({row['symbol']}) - ${row['current_price']:.2f}", ln=True)

    pdf.ln(5)
    pdf.cell(200, 10, f"Highest Gainer: {max_change['name']} ({max_change['symbol']}) +{max_change['price_change_percentage_24h']:.2f}%", ln=True)
    pdf.cell(200, 10, f"Biggest Loser: {min_change['name']} ({min_change['symbol']}) {min_change['price_change_percentage_24h']:.2f}%", ln=True)

    # ✅ Save PDF without encoding issues
    pdf.output(pdf_file, "F")
    print(f"✅ PDF report generated: {pdf_file}")

# Run report generation
if __name__ == "__main__":
    generate_pdf_report()
