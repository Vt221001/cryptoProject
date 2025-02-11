from flask import Flask, jsonify, render_template, send_file
import pandas as pd
import os
from flask_cors import CORS

app = Flask(__name__, template_folder="templates", static_folder="static")
CORS(app)

# 📌 Correct paths based on folder structure
EXCEL_PATH = "data/Crypto_Live_Data.xlsx"  # Excel file inside 'data/' folder
PDF_PATH = "reports/Crypto_Analysis_Report.pdf"  # PDF file inside 'reports/' folder

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/api/crypto-data', methods=['GET'])
def get_crypto_data():
    if not os.path.exists(EXCEL_PATH):
        return jsonify({"error": "Excel file not found"}), 404

    df = pd.read_excel(EXCEL_PATH)

    # Debugging Output
    print("📊 Excel Data Loaded:")
    print(df.head())  # Show first 5 rows

    if df.empty:
        return jsonify({"error": "Excel file is empty"}), 200  # 🛑 Return empty message

    # ✅ Ensure correct column names & formatting
    df.columns = df.columns.str.strip()  # Remove extra spaces from column names

    # ✅ Convert data to correct format
    data = df.to_dict(orient="records")
    
    return jsonify(data)

# ✅ Route to Download Excel File
@app.route('/download/excel', methods=['GET'])
def download_excel():
    if not os.path.exists(EXCEL_PATH):
        return jsonify({"error": "File not found"}), 404
    return send_file(EXCEL_PATH, as_attachment=True)

# ✅ Route to Download PDF File
@app.route('/download/pdf', methods=['GET'])
def download_pdf():
    if not os.path.exists(PDF_PATH):
        return jsonify({"error": "File not found"}), 404
    return send_file(PDF_PATH, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
