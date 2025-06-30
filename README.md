# 🎥 YouTube Video Chat Agent with AI-Powered RAG

An AI-powered tool that extracts YouTube video transcripts and enables interactive chat conversations about the video content using Retrieval-Augmented Generation (RAG) with Ollama local models.

## 📋 Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Applications](#applications)
- [Technical Architecture](#technical-architecture)
- [Contributing](#contributing)
- [License](#license)

## ✨ Features

### YouTube Video Processing & Chat
- 🎬 **Transcript Extraction**: Automatically downloads subtitles from YouTube videos using yt-dlp
- 🧹 **Text Cleaning**: Removes timestamps, special characters, and duplicate lines
- 📄 **PDF Generation**: Converts cleaned transcripts to searchable PDF documents
- 💬 **Interactive Chat**: Chat with an AI about the video content using natural language

### AI-Powered Analysis
- 🤖 **Local AI Models**: Uses Ollama for privacy-focused local LLM processing
- 🔍 **RAG Implementation**: Retrieval-Augmented Generation for accurate content-based responses
- 📊 **Vector Database**: ChromaDB for efficient similarity search
- 🎯 **Multi-Query Retrieval**: Generates multiple query perspectives for better results
- 🗣️ **Conversational Interface**: Interactive command-line chat with video content

### User Interfaces
- 🖥️ **Command-Line Interface**: Main `yt_agent.py` for YouTube URL input and video chat
- 🌐 **Streamlit Web App**: Interactive YouTube video summarizer (optional)
- 📱 **PDF Chat Interface**: Chat with uploaded PDF documents
- 🔗 **Internet Search Integration**: Web search capabilities for enhanced responses

## 🏗️ Project Structure


```
YouTube Agent/                 # Main YouTube processing module
├── yt_agent.py               # 🎯 MAIN FILE - YouTube URL input & chat interface
├── yt_transcript.py          # Transcript extraction & cleaning
├── rag_clean.py              # RAG implementation & chat functionality
├── DejaVuSans.ttf            # Font for PDF generation
└── temp files/               # Generated transcripts & PDFs
```

## 🔧 Prerequisites

Before running this project, ensure you have:

1. **Python 3.8+** installed on your system
2. **Ollama** installed and running locally
   ```bash
   # Install Ollama (macOS)
   brew install ollama
   
   # Start Ollama service
   ollama serve
   ```
3. **Required Ollama Models**:
   ```bash
   # Pull required models
   ollama pull llama3.2
   ollama pull nomic-embed-text
   ollama pull youtube-agent  # Custom model (if available)
   ```

## 🚀 Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd "YouTube_Video_Agent"
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   # or
   venv\Scripts\activate     # On Windows
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Additional requirements**:
   ```bash
   # Install additional system dependencies if needed
   pip install streamlit fpdf2 yt-dlp
   ```

## 🎯 Usage

### 1. YouTube Video Chat Agent (Main Application)

Run the main YouTube chat agent:

```bash
python yt_agent.py
```

**How it works:**
1. Enter any YouTube URL when prompted
2. The system automatically extracts and processes the video transcript
3. Creates a searchable knowledge base from the video content
4. Start chatting about the video content with the AI
5. Type 'exit' to quit the chat

**Features:**
- Direct command-line interface
- Automatic transcript processing
- Interactive AI chat about video content
- Local processing for privacy
- RAG-powered accurate responses


### 2. Direct Transcript Processing

For direct transcript processing without chat:

```bash
python yt_transcript.py
# Follow prompts to enter YouTube URL
```

## 🎯 Applications

### Educational Use Cases
- **Interactive Learning**: Ask questions about lecture videos and get detailed explanations
- **Research Analysis**: Deep dive into academic YouTube content with targeted questions
- **Study Sessions**: Chat with educational videos to clarify concepts and test understanding

### Business Applications
- **Meeting Analysis**: Process recorded meetings and ask specific questions about decisions
- **Training Material**: Interactive learning from corporate training videos
- **Content Research**: Analyze competitor videos with specific business questions

### Personal Productivity
- **Video Understanding**: Quickly grasp complex video content through targeted questioning
- **Content Exploration**: Ask follow-up questions to dive deeper into topics
- **Knowledge Extraction**: Extract specific information without watching entire videos

## 🔧 Technical Architecture

### Core Components

1. **Main Application (`yt_agent.py`)**
   - Entry point for YouTube URL input
   - Orchestrates transcript extraction and processing
   - Initiates RAG-powered chat interface
   - Command-line interface for user interaction

2. **Transcript Extraction (`yt_transcript.py`)**
   - Uses `yt-dlp` for robust YouTube subtitle download
   - Supports multiple languages and automatic subtitles
   - Handles various video formats and edge cases

3. **Text Processing Pipeline**
   - Cleans VTT subtitle format
   - Removes timestamps and formatting artifacts
   - Deduplicates repeated content
   - Generates PDF with Unicode support

4. **RAG Implementation (`rag_clean.py`)**
   - Document chunking with overlap for context preservation
   - Vector embeddings using `nomic-embed-text`
   - ChromaDB for efficient similarity search
   - Multi-query retrieval for comprehensive results
   - Interactive chat loop for continuous conversation

5. **LLM Integration**
   - Local Ollama models for privacy
   - Customizable model selection
   - Structured prompting for consistent outputs
   - Context-aware responses based on video content

### Data Flow

```
YouTube URL → yt-dlp → VTT Subtitles → Text Cleaning → PDF Generation
                                                            ↓
PDF Document → Text Chunking → Vector Embeddings → ChromaDB Storage
                                                            ↓
User Chat Query → Multi-Query Generation → Vector Search → RAG Response
                                                            ↓
Interactive Chat Loop → Continuous Q&A → Context-Aware Responses
```

## 🛠️ Configuration

### Model Configuration

Edit the model names in the respective files:

```python
# In yt_agent.py (Main application)
MODEL_NAME = "llama3.2"  # Change to your preferred model

```

### Embedding Model

```python
# In rag_clean.py and other RAG files
EMBEDDING_MODEL = "nomic-embed-text"  # Recommended for English text
```

## 🚀 Quick Start

1. **Install dependencies**: `pip install -r requirements.txt`
2. **Start Ollama**: `ollama serve`
3. **Pull models**: `ollama pull youtube-agent` and `ollama pull nomic-embed-text`
4. **Run main application**: `python yt_agent.py`
5. **Enter YouTube URL** and start chatting about the video content!

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines

- Follow PEP 8 style guidelines
- Add docstrings to all functions
- Include error handling for edge cases
- Test with various YouTube video types
- Ensure compatibility with different PDF formats

## 📋 Dependencies

### Core Dependencies
- `ollama` - Local LLM inference
- `langchain` - LLM application framework
- `chromadb` - Vector database
- `streamlit` - Web interface
- `yt-dlp` - YouTube content extraction

### Processing Libraries
- `pdfplumber` - PDF text extraction
- `fpdf2` - PDF generation
- `sentence-transformers` - Text embeddings
- `unstructured` - Document processing

### Optional Dependencies
- `elevenlabs` - Text-to-speech (if needed)
- `pikepdf` - Advanced PDF manipulation

## 🐛 Troubleshooting

### Common Issues

1. **Ollama Model Not Found**
   ```bash
   # Make sure Ollama is running and models are pulled
   ollama list
   ollama pull llama3.2
   ```

2. **YouTube Video Not Accessible**
   - Check if video has subtitles available
   - Verify video is not private or restricted
   - Try different video URLs

3. **PDF Generation Errors**
   - Ensure `DejaVuSans.ttf` font file is present
   - Check text encoding issues
   - Verify write permissions in directory

4. **Memory Issues**
   - Reduce chunk size in text splitter
   - Use smaller embedding models
   - Process shorter videos

## 📈 Performance Tips

- Use SSD storage for vector database
- Increase RAM for better embedding performance
- Use GPU-accelerated Ollama models if available
- Batch process multiple videos for efficiency

## 🔒 Privacy & Security

- All processing happens locally with Ollama
- No data sent to external APIs (except YouTube for transcript download)
- Vector embeddings stored locally
- Full control over your data

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Ollama](https://ollama.ai/) for local LLM inference
- [LangChain](https://python.langchain.com/) for RAG framework
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) for YouTube content extraction
- [Streamlit](https://streamlit.io/) for web interface
- [ChromaDB](https://www.trychroma.com/) for vector storage

---

**Made with ❤️ for the open-source community**

For questions, issues, or contributions, please open an issue on GitHub or contact the maintainers.
