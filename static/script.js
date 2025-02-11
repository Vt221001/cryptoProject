async function fetchData() {
    try {
        const response = await fetch("/api/crypto-data");
        const data = await response.json();

        console.log("📌 API Response in JavaScript:", data);  // ✅ Debugging in Browser Console

        if (!Array.isArray(data)) {
            console.error("❌ API returned an error:", data);
            return;
        }

        const tableBody = document.querySelector("#cryptoTable tbody");
        tableBody.innerHTML = "";

        data.forEach(coin => {
            console.log("📌 Coin Data:", coin);  // ✅ Check individual data objects
            
            const row = `<tr>
                <td>${coin.name || "N/A"}</td>
                <td>${coin.symbol || "N/A"}</td>
                <td>$${coin.current_price ? coin.current_price.toFixed(2) : "N/A"}</td>
                <td>$${coin.market_cap || "N/A"}</td>
                <td>${coin.total_volume || "N/A"}</td>
                <td>${coin.price_change_percentage_24h ? coin.price_change_percentage_24h.toFixed(2) + "%" : "N/A"}</td>
            </tr>`;
            tableBody.innerHTML += row;
        });

    } catch (error) {
        console.error("❌ Error fetching data:", error);
    }
}

fetchData();
