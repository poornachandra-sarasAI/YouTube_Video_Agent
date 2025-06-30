# 🎥 YouTube Video Summarizer with AI-Powered RAG

A comprehensive AI-powered project that extracts, processes, and summarizes YouTube video content using Retrieval-Augmented Generation (RAG) with Ollama local models.

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

### YouTube Video Processing
- 🎬 **Transcript Extraction**: Automatically downloads subtitles from YouTube videos using yt-dlp
- 🧹 **Text Cleaning**: Removes timestamps, special characters, and duplicate lines
- 📄 **PDF Generation**: Converts cleaned transcripts to searchable PDF documents

### AI-Powered Analysis
- 🤖 **Local AI Models**: Uses Ollama for privacy-focused local LLM processing
- 🔍 **RAG Implementation**: Retrieval-Augmented Generation for accurate content analysis
- 📊 **Vector Database**: ChromaDB for efficient similarity search
- 🎯 **Multi-Query Retrieval**: Generates multiple query perspectives for better results

### User Interfaces
- 🌐 **Streamlit Web App**: Interactive YouTube video summarizer
- 📱 **PDF Chat Interface**: Chat with uploaded PDF documents
- 🔗 **Internet Search Integration**: Web search capabilities for enhanced responses

## 🏗️ Project Structure

```
Ollama Project/
├── README.md                   # This file
├── requirements.txt            # Python dependencies
├── app.py                     # Main PDF chat application
├── internet_search.py         # Web search functionality
├── pdf-rag.py                 # PDF processing utilities
├── data/                      # Document storage
│   └── NLP.pdf               # Sample PDF
└── YouTube Agent/             # YouTube processing module
    ├── yt_agent_ui.py        # Streamlit YouTube summarizer
    ├── yt_agent.py           # Core YouTube processing
    ├── yt_transcript.py      # Transcript extraction & cleaning
    ├── rag_ui.py             # RAG implementation
    ├── rag_clean.py          # Data cleaning utilities
    ├── DejaVuSans.ttf        # Font for PDF generation
    └── temp files/           # Generated transcripts & PDFs
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
   cd "Ollama Project"
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

### 1. YouTube Video Summarizer

Launch the YouTube video summarizer web interface:

```bash
cd "YouTube Agent"
streamlit run yt_agent_ui.py
```

**Features:**
- Paste any YouTube URL
- Automatically extracts video transcript
- Generates AI-powered summary
- Download cleaned transcript as PDF
- Interactive web interface

### 2. PDF Chat Application

Run the main PDF chat application:

```bash
streamlit run app.py
```

**Features:**
- Upload PDF documents
- Ask questions about PDF content
- RAG-powered responses
- Persistent vector database

### 3. Command Line Usage

For direct transcript processing:

```bash
cd "YouTube Agent"
python yt_transcript.py
# Follow prompts to enter YouTube URL
```

## 🎯 Applications

### Educational Use Cases
- **Lecture Summarization**: Quickly summarize educational YouTube videos
- **Research Analysis**: Extract key insights from academic content
- **Note Generation**: Create structured notes from video lectures

### Business Applications
- **Meeting Transcription**: Process recorded meetings and webinars
- **Content Analysis**: Analyze competitor videos and presentations
- **Training Material**: Create summaries of training videos

### Personal Productivity
- **Learning Acceleration**: Quickly grasp video content
- **Content Curation**: Extract highlights from long-form content
- **Knowledge Management**: Build searchable knowledge base

## 🔧 Technical Architecture

### Core Components

1. **Transcript Extraction (`yt_transcript.py`)**
   - Uses `yt-dlp` for robust YouTube subtitle download
   - Supports multiple languages and automatic subtitles
   - Handles various video formats and edge cases

2. **Text Processing Pipeline**
   - Cleans VTT subtitle format
   - Removes timestamps and formatting artifacts
   - Deduplicates repeated content
   - Generates PDF with Unicode support

3. **RAG Implementation (`rag_ui.py`)**
   - Document chunking with overlap for context preservation
   - Vector embeddings using `nomic-embed-text`
   - ChromaDB for efficient similarity search
   - Multi-query retrieval for comprehensive results

4. **LLM Integration**
   - Local Ollama models for privacy
   - Customizable model selection
   - Structured prompting for consistent outputs

### Data Flow

```
YouTube URL → yt-dlp → VTT Subtitles → Text Cleaning → PDF Generation
                                                            ↓
PDF Document → Text Chunking → Vector Embeddings → ChromaDB Storage
                                                            ↓
User Query → Multi-Query Generation → Vector Search → RAG Response
```

## 🛠️ Configuration

### Model Configuration

Edit the model names in the respective files:

```python
# In yt_agent_ui.py
MODEL_NAME = "youtube-agent"  # Change to your preferred model

# In app.py
MODEL_NAME = "llama3.2"      # Change to your preferred model
```

### Embedding Model

```python
# In rag_ui.py
EMBEDDING_MODEL = "nomic-embed-text"  # Recommended for English text
```

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
