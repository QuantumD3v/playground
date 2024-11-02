import tkinter as tk
from tkinter import ttk
import requests
import threading
import time

class InfoGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("File Server Info")
        self.geometry("300x200")
        
        # Labels to display information
        self.upload_label = ttk.Label(self, text="Uploads: 0")
        self.upload_label.pack(pady=10)

        self.download_label = ttk.Label(self, text="Downloads: 0")
        self.download_label.pack(pady=10)

        self.cpu_label = ttk.Label(self, text="CPU Usage: 0%")
        self.cpu_label.pack(pady=10)

        self.memory_label = ttk.Label(self, text="Memory Usage: 0%")
        self.memory_label.pack(pady=10)

        # Start the background thread to update info
        self.update_info()

    def fetch_info(self):
        try:
            response = requests.get("http://192.168.1.47:8111/info")
            if response.status_code == 200:
                return response.json()
        except Exception as e:
            print(f"Error fetching data: {e}")
        return None

    def update_info(self):
        # Function to continuously update the information in the GUI
        def update():
            while True:
                info = self.fetch_info()
                if info:
                    self.upload_label.config(text=f"Uploads: {info['uploads']}")
                    self.download_label.config(text=f"Downloads: {info['downloads']}")
                    self.cpu_label.config(text=f"CPU Usage: {info['cpu_usage']}%")
                    self.memory_label.config(text=f"Memory Usage: {info['memory_usage']}%")
                time.sleep(2)  # Update every 2 seconds

        # Run the update function in a separate thread to avoid freezing the GUI
        threading.Thread(target=update, daemon=True).start()

if __name__ == "__main__":
    app = InfoGUI()
    app.mainloop()
