import yt_transcript
import rag_clean



TRANSCRIPT_FILE_NAME = "subtitle_file"
CLEANED_TRANSCRIPT_FILE = "transcript_cleaned.txt"
TRANSCRIPT_PDF = "transcript.pdf"
DOC_PATH = "./transcript.pdf"  
MODEL_NAME = "youtube-agent"
EMBEDDING_MODEL = "nomic-embed-text"
VECTOR_STORE_NAME = "simple-rag"


def main():
    # Step 1: Generate transcript from YouTube video
    video_url = input("Enter YouTube video URL: ")  
    

    yt_transcript.transcript_generator(video_url, TRANSCRIPT_FILE_NAME)
    yt_transcript.clean_transcript(TRANSCRIPT_FILE_NAME + ".en.vtt")
    yt_transcript.pdf_generator(CLEANED_TRANSCRIPT_FILE, TRANSCRIPT_PDF)


    rag_clean.rag_implementation(TRANSCRIPT_PDF,MODEL_NAME)
    


if __name__ == "__main__":
    main()