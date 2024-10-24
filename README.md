
# AI Chatbot -BUADGURU

This project is an AI chatbot with real-time streamed responses which give 21 days plan of learning anything using a Tkinter-based GUI. The chatbot simulates a typing effect similar to ChatGPT, using the Ollama API for natural language processing.

## Features
- **Real-time typing effect**: Responses stream in character by character.
- **Simple, intuitive UI**: Built using Tkinter for an easy-to-use graphical interface.
- **Stop button**: Allows users to interrupt the response typing at any time.

## Requirements

- **Python 3.x**
- **Ollama API** (running locally)
- **Tkinter** (included with Python on most systems)

## Installation Instructions

### Step 1: Clone the Repository

First, clone this repository to your local machine:

```bash
git clone https://github.com/prashant-jadon/BaudGURU.git
cd BaudGuru
```

### Step 2: Install Dependencies

Install the required Python packages by running:

```bash
pip install -r requirements.txt
```

The dependencies include:
- `Flask`: For the web backend (if you choose to extend it)
- `requests`: For making API calls to Ollama

### Step 3: Install and Run Ollama

You need to have Ollama running locally to handle the natural language processing for the chatbot.

#### 1. **Install Ollama**:
   Visit the [Ollama website](https://ollama.com) and download the appropriate version for your system.

#### 2. **Start Ollama**:
   Once installed, run Ollama locally by executing:
   ```bash
   ollama serve
   ```

Ollama should now be running on port `11434`. You can check this by visiting `http://localhost:11434/api` in your browser.

#### 3. **Install the Required Models** (Optional):
   If your project uses specific models, like `baudguru`, download them by running:
   ```bash
   ollama create baudguru -f modelfile 
   ```

### Step 4: Configure the Ollama API URL (Optional)

By default, the application will use `http://localhost:11434/api/generate` as the Ollama API URL. If Ollama is running on a different machine or port, set the URL by exporting an environment variable:

```bash
export OLLAMA_API_URL="http://your-server-address:port/api/generate"
```

### Step 5: Running the Chatbot

To run the Tkinter-based chatbot application, execute the following command:

```bash
python3 app.py
```

This will launch the GUI, where you can interact with the chatbot by entering queries and viewing the real-time typing effect.

### Step 6: Optional - Stop Typing

If at any point you want to stop the chatbot mid-response, click the **Stop** button in the GUI to immediately halt the typing.

## Screenshots

![Chatbot UI] (https://github.com/prashant-jadon/BaudGURU/blob/8687565796f47e6efdd781662818ebdacf45070b/img1.png)
![Chatbot UI] (https://github.com/prashant-jadon/BaudGURU/blob/8687565796f47e6efdd781662818ebdacf45070b/img2.png))

## Troubleshooting

### Common Issues:

- **Ollama not running**: Ensure Ollama is running by checking `http://localhost:11434/api` in your browser.
- **API connection error**: If the chatbot cannot connect to Ollama, verify that the API URL is correct and reachable.

## License

This project is licensed under the MIT License.
