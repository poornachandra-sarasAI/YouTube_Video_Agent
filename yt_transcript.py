import yt_dlp
import re
from fpdf import FPDF
import os

def transcript_generator(video_url:str , file_name : str) -> None:
    """
    Generate a transcript for a YouTube video using yt-dlp.
    """
    

    # yt-dlp options
    ydl_opts = {
        "writesubtitles": True,
        "writeautomaticsub": True,
        "subtitleslangs": ["en"],
        "skip_download": True,
        "outtmpl": file_name,  # Output filename
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

    print(f"✅ Subtitle file downloaded. File name: {file_name}")


def clean_transcript(file_name) :

    """
    Clean the transcript file by removing timestamps and special characters.
    """
    with open(file_name, "r", encoding="utf-8") as file:
        vtt_data = file.readlines()

    text_lines = []
    for line in vtt_data:
        line = line[:-1]  # Remove trailing newline character (Took 20-30 mins to figure this out)
        # Skip headers, timestamps, and blank lines
        if (line == "\n" or line == '' or line == " " or line.startswith("WEBVTT") or line.startswith("Kind:") or line.startswith("Language:") or re.match(r"^\d\d:\d\d:\d\d\.\d\d\d", line) or re.search(r"<\d\d:\d\d:\d\d\.\d\d\d>", line) or "<c>" in line or "</c>" in line):
            continue

        if(len(text_lines) > 0 and line == text_lines[-1]):
            # Skip duplicate lines
            continue

        text_lines.append(line.strip())
    
    
    # Join lines into full text
    full_transcript = " ".join(text_lines)

    # Save to a .txt (optional, for verification)
    with open("transcript_cleaned.txt", "w", encoding="utf-8") as f:
        f.write(full_transcript)

    print("✅ Transcript cleaned and saved to transcript_cleaned.txt")


def pdf_generator(transcript_file:str, pdf_file_name:str) -> None:
    """
    Generate a PDF from the cleaned transcript.
    """

    with open(transcript_file, "r", encoding="utf-8") as file:
        text = file.read()

    #Create a PDF object
    pdf = FPDF()
    pdf.add_page()
    

    # Set a Unicode-capable font
    # Download font if not already present
    font_path = "DejaVuSans.ttf"
    

    pdf.add_font("DejaVu", "", font_path, uni=True)
    pdf.set_font("DejaVu", size=12)


    # Split text into lines that fit the page
    for line in text.split('\n'):
        pdf.multi_cell(0, 10, line)

    # Save PDF
    pdf.output(pdf_file_name)

    print("✅ transcript.pdf created successfully!")


# video_url = input("Enter the YouTube video URL: ")

# transcript_generator(video_url, "subtitle_file")
# clean_transcript("subtitle_file.en.vtt")
# pdf_generator("transcript_cleaned.txt", "transcript.pdf")
