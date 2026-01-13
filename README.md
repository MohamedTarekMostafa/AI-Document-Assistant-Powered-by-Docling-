# AI Document Assistant (Powered by Docling)

I got tired of RAG tutorials that only work on "hello world" text files. The second you try to chat with a real PDF like an NVIDIA financial report or an academic paper most parsers just break. They turn tables into a mess, and the AI ends up hallucinating because it can't read the data.

That’s why I built this. I’m using **IBM’s Docling** to do the heavy lifting. It actually understands the layout of a page, so when it sees a table or a multi-column layout, it keeps the structure intact. 

Right now, it’s set up to chat 
1. **The Math:** The original Transformer paper (*Attention is All You Need*).
2. **The Model:** The Llama 3 Technical Report.
3. **The Chips:** NVIDIA’s 2025 Annual Report.

### Why I used Docling
Most libraries just "scrape" text. Docling is different—it converts everything to clean Markdown first. If you ask about NVIDIA’s revenue, the AI actually sees a table of numbers, not just a random string of digits. It makes the answers much more reliable.

### The Stack
* **LLM:** Google Gemini 2.5 Flash (Super fast for this stuff).
* **Parsing:** Docling (The secret sauce).
* **Database:** ChromaDB (Vector store).
* **UI/API:** FastAPI + Streamlit.

### How to get it running
You'll need two terminals open.

1. **Setup:**
   `pip install docling langchain-core langchain-huggingface langchain-google-genai langchain-chroma fastapi uvicorn streamlit python-dotenv requests`

2. **Keys:** Put your `GOOGLE_API_KEY` in a `.env` file.

3. **Start the backend:**
   `uvicorn main:app --reload`

4. **Start the frontend:**
   `streamlit run app.py`

### Project structure
* `processor.py`: This is where I use Docling to split the PDFs into chunks.
* `engine.py`: This handles the RAG logic and the "Research Scientist" prompt.
* `main.py` & `app.py`: The API and the UI bits.
### ScreenShots
<img width="1204" height="889" alt="image" src="https://github.com/user-attachments/assets/8027d228-50d4-4d30-8df2-603c8ddf1be5" />
<img width="590" height="908" alt="image" src="https://github.com/user-attachments/assets/fe198061-5a88-4807-bd18-c77ad32264b6" />
<img width="477" height="742" alt="image" src="https://github.com/user-attachments/assets/7e4209d9-17a0-4b3d-9781-27f78ff9e9b4" />
<img width="804" height="881" alt="image" src="https://github.com/user-attachments/assets/b756304d-6ee3-4108-ade3-375c7033d132" />



