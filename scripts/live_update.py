from save_to_excel import save_to_excel
import time

def update_data():
    while True:
        print("🔄 Updating crypto data...")
        save_to_excel()
        print("✅ Data updated!")
        time.sleep(60)  # Refresh every 60 seconds

if __name__ == "__main__":
    update_data()
