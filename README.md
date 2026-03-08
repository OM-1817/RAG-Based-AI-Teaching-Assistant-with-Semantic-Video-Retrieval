🎥 RAG-Based AI Teaching Assistant with Semantic Video Retrieval

This project is an AI-powered question answering system for video courses. It allows users to ask questions related to a course and automatically finds which video and timestamp contains the answer.

The system processes course videos, converts them into transcripts, generates embeddings, and retrieves the most relevant segments using semantic similarity search and a local language model.

⚠️ Note:
The repository does not include video files because they are large. You must add your own course videos inside the videos/ folder before running the project.

🚀 Features

Convert videos → audio
Generate transcripts using Whisper
Split transcripts into meaningful text chunks
Generate vector embeddings
Perform semantic similarity search
Use an LLM to generate human-readable answers
Suggest exact video and timestamp where the topic is explained

⚙️ How the System Works
1️⃣ Video to Audio Conversion

Course videos are converted to audio files using FFmpeg.
videos/tutorial.mp4 → audios/tutorial.mp3

2️⃣ Audio Transcription

Audio files are transcribed using Whisper (large-v2) to generate subtitles.
Each subtitle contains:
video number
video title
start timestamp
end timestamp
spoken text
The results are stored as JSON files.

3️⃣ Chunk Processing

Subtitle segments are grouped into larger text chunks to improve semantic search performance.
Each chunk contains:
video number
video title
start timestamp
end timestamp
combined text

4️⃣ Embedding Generation

Each chunk is converted into a vector embedding using a local embedding model (bge-m3).
These embeddings are saved in:
embeddings.joblib

5️⃣ Question Answering

When the user asks a question:
The question is converted into an embedding
Cosine similarity finds the most relevant transcript chunks
A local LLM generates a response explaining:
which video contains the answer
the timestamp where the concept is explained