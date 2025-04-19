# ARIA – AI-Responsive Interactive Assistant

ARIA is an AI-powered voice assistant that provides intelligent, web-enhanced answers to user queries. Built using a lightweight HuggingFace model, it integrates real-time web search and responds in a professional tone.

---

## 🚀 Features

- Uses `SmolLM2-135M-Instruct` for fast, efficient responses.
- Integrates web context for better accuracy using a custom search tool.
- Hosted using Flask + Gunicorn in a Hugging Face Space (Docker-based).
- Clean web UI with voice interaction (frontend via `index.html`).

---

## 🧱 Project Structure

├── Dockerfile # For Hugging Face Space deployment ├── main.py # Flask application ├── requirements.txt # Python dependencies ├── web_search_tool.py # Web search context integration └── templates/ └── index.html # Web UI

---

## 🐳 Running Locally with Docker

```bash
# Build the Docker image
docker build -t aria-assistant .

# Run the container
docker run -p 7860:7860 aria-assistant

🤖 Model Used
SmolLM2-135M-Instruct

📄 License
This project is under the MIT License.