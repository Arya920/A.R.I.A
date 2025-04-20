# A.R.I.A (Advanced Responsive Intelligence Assistant) 🤖

<div align="center">

![Python](https://img.shields.io/badge/python-3.9+-blue.svg)
![Flask](https://img.shields.io/badge/flask-2.0+-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

</div>

A sophisticated voice-enabled AI assistant that combines advanced language understanding with real-time web search capabilities. A.R.I.A provides intelligent, context-aware responses through an intuitive, modern web interface.

## ✨ Key Features

- **Multi-Modal Interaction**
  - Voice-based input with real-time speech recognition
  - Modern spectrum-based audio visualization
  - Fallback text input support
  - Natural speech synthesis for responses

- **Intelligent Processing Modes**
  - 🌐 Web Search: Enhanced responses with real-time web context
  - 🧠 Reasoning: Systematic problem-solving with step-by-step analysis
  - 🎨 Creative: Imaginative responses with analogies and vivid descriptions

- **Advanced AI Integration**
  - Powered by SmolLM2-360M-Instruct model
  - Real-time DuckDuckGo web search integration
  - Context-aware response generation
  - Professional and natural conversational tone

- **Modern UI/UX**
  - Clean, responsive interface with glass-morphism design
  - Real-time status indicators and visual feedback
  - Smooth animations and transitions
  - Cross-browser compatibility

## 🚀 Getting Started

### Prerequisites
- Python 3.9+
- Docker (optional)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/aria-assistant.git
cd aria-assistant
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python app.py
```

### Docker Deployment

Build and run using Docker:
```bash
docker build -t aria-assistant .
docker run -p 7860:7860 aria-assistant
```

## 🛠️ Technical Architecture

- **Frontend**: HTML5, TailwindCSS, JavaScript (Web Speech API)
- **Backend**: Flask, Python
- **AI Model**: HuggingFace Transformers (SmolLM2-360M-Instruct)
- **External Services**: DuckDuckGo Search API
- **Deployment**: Docker, Gunicorn

## 🔧 Configuration

The application can be configured through environment variables:
- `FLASK_ENV`: Set to 'development' or 'production'
- `PORT`: Server port (default: 7860)
- `HOST`: Server host (default: 0.0.0.0)

## 📚 API Documentation

### Speech Modes

1. **Web Search Mode**
   - Enhances responses with real-time web context
   - Best for factual queries and current information

2. **Reasoning Mode**
   - Provides structured, logical analysis
   - Ideal for problem-solving and complex queries

3. **Creative Mode**
   - Generates imaginative and descriptive responses
   - Perfect for creative writing and brainstorming

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.