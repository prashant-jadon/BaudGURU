import tkinter as tk
from tkinter import scrolledtext
import threading
import requests
import json
import time

OLLAMA_API_URL = 'http://localhost:11434/api/generate'

class ChatBotApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Assistant - BaudGURU")
        
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        self.chat_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Helvetica", 12), bg="#F0F0F0", fg="#333333")
        self.chat_display.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")
        self.chat_display.config(state=tk.DISABLED)

        self.topic_entry = tk.Entry(root, width=50, font=("Helvetica", 14))
        self.topic_entry.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

        self.ask_button = tk.Button(root, text="Ask AI", command=self.start_asking_thread, font=("Helvetica", 12), bg="#28A745", fg="black")
        self.ask_button.grid(row=1, column=1, padx=5, pady=10)

        self.stop_button = tk.Button(root, text="Stop", command=self.stop_typing, font=("Helvetica", 12), bg="#DC3545", fg="black", state=tk.DISABLED)
        self.stop_button.grid(row=1, column=2, padx=5, pady=10)

        self.status_label = tk.Label(root, text="", font=("Helvetica", 10), fg="#666666")
        self.status_label.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

        self.stop_loader = False
        self.stop_typing_flag = False  

    def start_asking_thread(self):
        """Start the response fetching process in a separate thread."""
        topic = self.topic_entry.get().strip()
        if not topic:
            self.status_label.config(text="Please enter a topic.")
            return

        self.stop_loader = False
        self.stop_typing_flag = False
        self.stop_button.config(state=tk.NORMAL)  

        self.chat_display.config(state=tk.NORMAL)
        self.chat_display.insert(tk.END, f"\nYou: {topic}\n")
        self.chat_display.config(state=tk.DISABLED)
        self.topic_entry.delete(0, tk.END)

        self.start_loader()
        threading.Thread(target=self.ask_topic, args=(topic,)).start()

    def start_loader(self):
        """A simple text-based loading animation while fetching response."""
        def animate():
            while not self.stop_loader:
                for i in range(4):
                    self.status_label.config(text="AI is typing" + "." * i)
                    time.sleep(0.5)
        
        threading.Thread(target=animate).start()

    def stop_typing(self):
        """Stop the typing effect mid-response."""
        self.stop_typing_flag = True
        self.stop_loader = True
        self.status_label.config(text="Typing stopped.")
        self.stop_button.config(state=tk.DISABLED)  

    def ask_topic(self, topic):
        """Fetch the response from API and stream it in real-time."""
        try:
            response_stream = self.get_streamed_response_from_api(topic)
            
            self.stop_loader = True
            self.status_label.config(text="")

            for chunk in response_stream:
                if self.stop_typing_flag:
                    break  
                if chunk:
                    self.display_chunk(chunk)

        except requests.exceptions.RequestException as e:
            self.stop_loader = True
            self.status_label.config(text="Error fetching information.")
            print("Error:", e)

        self.stop_button.config(state=tk.DISABLED)  

    def get_streamed_response_from_api(self, topic):
        """Call the API and yield streamed chunks for real-time display."""
        payload = {
            'model': 'baudguru',
            'prompt': topic
        }

        response = requests.post(OLLAMA_API_URL, json=payload, stream=True)
        response.raise_for_status()  

        for chunk in response.iter_lines():
            if chunk:
                parsed_chunk = json.loads(chunk.decode('utf-8'))
                if 'response' in parsed_chunk:
                    yield parsed_chunk['response']

    def display_chunk(self, chunk):
        """Display each chunk of response with typing effect in chat window."""
        self.chat_display.config(state=tk.NORMAL)
        typing_speed = 0.03  

        for char in chunk:
            if self.stop_typing_flag:
                break  
            self.chat_display.insert(tk.END, char)
            self.chat_display.update_idletasks()  
            time.sleep(typing_speed)

        self.chat_display.yview(tk.END)
        self.chat_display.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatBotApp(root)
    root.geometry("700x500")  
    root.mainloop()
