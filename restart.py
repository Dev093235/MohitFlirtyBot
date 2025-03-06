import os
import time

def restart_bot():
    while True:
        print("🚀 Starting the bot...")
        exit_code = os.system("python main.py")  # `main.py` ko start karega
        
        if exit_code != 0:
            print("❌ Bot Crashed! Restarting in 5 seconds...")
            time.sleep(5)  # 5 sec wait karega aur fir restart karega
        else:
            print("✅ Bot Stopped Normally.")
            break  # Agar bot manually band kiya gaya to loop break hoga

if __name__ == "__main__":
    restart_bot()
