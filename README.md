
# 🚀 Crypto Market Live Data Web App

This is a **real-time cryptocurrency market tracking application** built with **Flask, JavaScript, and HTML/CSS**.  
It **fetches live crypto market data** from an external API and displays it in a table. Users can also **download reports as Excel & PDF**.

---

## 📌 Features
- ✅ Fetches **live cryptocurrency market data**
- ✅ Displays **real-time prices, market cap, volume, and price changes**
- ✅ **Download reports** in **Excel & PDF formats**
- ✅ Simple, **responsive UI**
- ✅ Built with **Flask, JavaScript, and HTML/CSS**

---

## 🛠 Tech Stack Used
- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Data Processing**: Pandas, Requests
- **APIs**: Fetches crypto data from **CoinGecko API (or specify your API)**
- **Exporting Data**: Pandas (Excel), ReportLab (PDF)

---

## 🔧 Installation & Setup

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/your-username/crypto-market-app.git
cd crypto-market-app
```

### 2️⃣ Create a Virtual Environment & Install Dependencies
```sh
python -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scriptsctivate      # For Windows

pip install -r requirements.txt
```

### 3️⃣ Run the Application
```sh
python app.py
```
Your app will run on: **http://127.0.0.1:5000**

---

## 📡 API Endpoints

| Endpoint              | Method | Description |
|----------------------|--------|-------------|
| `/api/crypto-data`   | GET    | Fetches live crypto market data |
| `/download/excel`    | GET    | Exports data as an **Excel file** |
| `/download/pdf`      | GET    | Exports data as a **PDF file** |

### Example API Response:
```json
[
  {
    "name": "Bitcoin",
    "symbol": "BTC",
    "current_price": 43000,
    "market_cap": 800000000000,
    "total_volume": 32000000,
    "price_change_percentage_24h": -1.5
  },
  {
    "name": "Ethereum",
    "symbol": "ETH",
    "current_price": 3200,
    "market_cap": 400000000000,
    "total_volume": 28000000,
    "price_change_percentage_24h": 0.8
  }
]
```

---

## 🌎 Deployment Instructions
If deploying to **MilesWeb / Heroku / Render**, follow these steps:

### 1️⃣ Create a `.env` File
```sh
FLASK_APP=app.py
FLASK_ENV=production
API_KEY=your_api_key_here  # If required
```

### 2️⃣ Install `gunicorn` (For Production)
```sh
pip install gunicorn
```

### 3️⃣ Run the App in Production Mode
```sh
gunicorn --bind 0.0.0.0:5000 app:app
```

---

## 📸 Screenshots
### 🏠 **Home Page**
![Home Page](screenshots/homepage.png)

### 📊 **Crypto Data Table**
![Data Table](screenshots/data_table.png)

---

## 🚀 Future Enhancements
- 📈 **Add Graphs/Charts** for better visualization
- 📱 **Make UI Mobile-Friendly**
- 🔔 **Real-time WebSockets** for live price updates
- 🌍 **Multi-Currency Support**

---

## 👨‍💻 Author
Developed by **[Your Name]**  
📧 Email: your-email@example.com  
🔗 LinkedIn: [your-profile-link](https://linkedin.com/in/your-profile)

---

## 📜 License
This project is licensed under the **MIT License**.

⭐ **If you found this useful, don't forget to star the repository!** ⭐
