🚀 Overview
The AI Text Summarizer is a web application that allows users to upload PDF files and get a concise summary of the content. This helps users quickly grasp key points without reading through long documents.

🛠️ Features
Upload PDFs and extract text automatically
AI-powered summarization using GPT-3.5 Turbo
Built with Streamlit – No need for HTML, CSS, or JavaScript
Fast and efficient text extraction with PyMuPDF
🔧 Technologies Used
Python
Streamlit (for the web interface)
PyMuPDF (for extracting text from PDFs)
OpenAI GPT-3.5 Turbo (for text summarization)
📥 Installation & Setup
1️⃣ Clone the repository:

bash
Copy
Edit
git clone https://github.com/your-username/ai-text-summarizer.git
cd ai-text-summarizer
2️⃣ Create a virtual environment and activate it:

bash
Copy
Edit
python -m venv myenv
source myenv/bin/activate   # On macOS/Linux
myenv\Scripts\activate      # On Windows
3️⃣ Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
4️⃣ Run the application:

bash
Copy
Edit
streamlit run app.py
📌 Usage
Upload a PDF file
Click on Summarize Paper
View the extracted text and AI-generated summary
