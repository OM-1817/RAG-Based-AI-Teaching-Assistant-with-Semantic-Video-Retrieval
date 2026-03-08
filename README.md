# RAG-Based AI Teaching Assistant with Semantic Video Retrieval

This project builds an AI-powered system that allows users to ask
questions about a video course and receive answers that point to the
exact moment in the course where the topic is explained.

The system processes course videos, converts spoken content into text,
organizes the information, and performs semantic search to retrieve the
most relevant parts of the course when a user asks a question. It then
uses a language model to generate a human‑friendly answer guiding the
user to the correct video section and timestamp.

⚠️ Note: Video files are not included in this repository because they
are usually very large. To use the system, place your own course videos
in the project directory before running the pipeline.

## How the System Works

### Video Processing

Course videos are first converted into audio so that speech can be
analyzed. This step extracts the spoken content from each lecture or
tutorial.

### Speech Transcription

The extracted audio is transcribed using a speech recognition model. The
result is a full transcript of the video along with timestamps
indicating when each sentence or segment occurs.

### Chunk Creation

The transcript is divided into meaningful segments of text. Each segment
contains lecture information, timestamps, and the spoken content for
that section. These chunks help the system understand and retrieve
relevant parts of the course.

### Embedding Generation

Each text chunk is converted into a numerical vector representation
called an embedding. These embeddings capture the semantic meaning of
the content, allowing the system to compare user questions with the
course material.

### Semantic Search

When a user asks a question, the system converts the question into an
embedding and compares it with stored embeddings using similarity
calculations. The most relevant course segments are retrieved.

### AI Response Generation

The retrieved segments are provided to a language model, which generates
a clear and helpful answer. The response guides the user to the exact
video and timestamp where the concept is explained.

## Technologies Used

-   Python
-   Speech recognition models
-   Vector embeddings
-   Semantic similarity search
-   Local language models
-   Data processing libraries

## Use Cases

-   Searching large programming courses
-   Finding explanations inside long tutorials
-   Quickly navigating educational video content
-   Building AI-powered learning assistants

## Author

Om Vaghani
