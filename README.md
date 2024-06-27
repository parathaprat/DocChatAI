# DocChatAI

The DocChatAI App is a Python-based application for engaging with multiple PDF documents using an LLM-integrated RAG pipeline. Users can pose natural language queries regarding the PDF contents, receiving precise responses based on document analysis. Leveraging large language models, the application ensures accurate information retrieval tailored to the loaded PDFs.

This application has implementations for both OpenAI and HuggingFace LLMs.

Working: 

![image](https://github.com/parathaprat/DocChatAI/assets/84290855/01dd4572-9b70-409d-afbe-8ba745ee741b)

The application follows these steps to provide responses to your questions:
- PDF Loading: The app reads multiple PDF documents and extracts their text content.
- Text Chunking: The extracted text is divided into smaller chunks that can be processed effectively.
- Language Model: The application utilizes a language model (either OpenAI or HuggingFace) to generate vector representations (embeddings) of the text chunks.
- Similarity Matching: When you ask a question, the app compares it with the text chunks and identifies the most semantically similar ones.
- Response Generation: The selected chunks are passed to the language model, which generates a response based on the relevant content of the PDFs.

Results:

![image](https://github.com/parathaprat/DocChatAI/assets/84290855/396c9bce-a82b-4f53-9b7a-16213a460c93)

![image](https://github.com/parathaprat/DocChatAI/assets/84290855/e64c033f-d2b2-4476-ad0f-79d0a8e4c001)



To use the DocChatAI app on your local machine, clone the repositoy to your local machine, install required dependencies, add your OpenAI and HuggingFace key to the ```.env``` file, and run ```app.py``` using streamlit.

Technologies used - Python, Langchain, Streamlit, OpenAI, HuggingFace

Thank you yt/Alejandro AO - Software & Ai for providing step by step instructions to building this project
