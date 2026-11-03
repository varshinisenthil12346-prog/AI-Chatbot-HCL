# AI-Chatbot-HCL

🦙 HCL Chatbot – Llama 3.2

A locally running AI chatbot built with Python, Streamlit, and Ollama (Llama 3.2). This project allows users to interact with a locally hosted Large Language Model (LLM) through a simple and interactive chat interface.

🚀 Features
🤖 Chat with the Llama 3.2 model locally.
💬 Interactive chat interface using Streamlit.
🧠 Maintains conversation history during the session.
🔒 Runs locally using Ollama.
⚙️ Environment-based configuration using .env.
🐍 Python virtual environment support.
🛠️ Technologies Used
Python – Backend programming language.
Ollama – Local LLM runtime.
Llama 3.2 – Language model.
Streamlit – Chatbot user interface.
python-dotenv – Environment variable management.
📁 Project Structure
text
ollama-chatbot/
│
├── venv/
├── .env
├── .gitignore
├── requirements.txt
├── app.py
└── README.md

📋 Prerequisites

Before running this project, make sure you have:

Python 3.9 or later.
Ollama installed.
Git installed.
⚙️ Installation and Setup
1. Clone the repository
bash
git clone https://github.com/YOUR_USERNAME/ollama-chatbot.git

2. Navigate to the project directory
bash
cd ollama-chatbot

3. Create a virtual environment
bash
python -m venv venv

4. Activate the virtual environment

Windows:

bash
venv\Scripts\activate


Linux / macOS:

bash
source venv/bin/activate

5. Install dependencies
bash
pip install -r requirements.txt

6. Download the Llama 3.2 model
bash
ollama pull llama3.2

7. Configure environment variables

Create a .env file in the root directory:

env
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=llama3.2

8. Run the application
bash
streamlit run app.py


Open your browser and navigate to:

text
http://localhost:8501

💬 How It Works
The user enters a message through the Streamlit chat interface.
The Python application receives the message.
The application sends the conversation history to the Ollama API.
Ollama processes the request using the Llama 3.2 model.
The generated response is displayed in the chat interface.
🔐 Security
Environment variables are stored in .env.
The .env file is excluded from Git using .gitignore.
The virtual environment is not included in the repository.
No external AI API key is required for local model inference.
🔮 Future Improvements
Chat history persistence.
ChatGPT-like user interface.
PDF document upload and question answering.
Retrieval-Augmented Generation (RAG).
Multiple Ollama model support.
User authentication.
Streaming responses.
🤝 Contributing

Contributions, suggestions, and improvements are
