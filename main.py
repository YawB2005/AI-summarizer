# Import necessary libraries
import pymupdf  # For extracting text from PDF files
import streamlit as st  # For building the web app
from openai import OpenAI  # For using OpenAI's GPT model

# Initialize OpenAI client using the API key stored in Streamlit secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Initialize session state variables
# 'ai_model' stores the model name, defaulting to 'gpt-3.5-turbo'
if "ai_model" not in st.session_state:
    st.session_state["ai_model"] = "gpt-3.5-turbo"

# 'messages' keeps track of previous chat interactions
if "message" not in st.session_state:
    st.session_state.messages = []

# Display previous chat messages in the chat interface
for message in st.session_state.messages:
    with st.chat_message(message["role"]):  # Show the message based on the role (user/assistant)
        st.markdown(message["content"])  # Display message content in Markdown format

# Function to extract text from a PDF file using PyMuPDF (pymupdf)
def extract_text(file):
    doc = pymupdf.open(file)  # Open the PDF file
    text = ""

    # Loop through each page and extract text
    for page in doc:
        text += page.get_text()
    
    return text  # Return the extracted text

# Set the title of the Streamlit web app
st.title("AI Text Summarizer")

# Description of the app
st.write("Upload a file and have it summarized😌")

# File uploader widget for uploading PDFs
pdf_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])

# Check if a file has been uploaded
if pdf_file:
    st.subheader("Extracted text")  # Section title
    
    # Extract text from the uploaded PDF
    file_text = extract_text(pdf_file)
    
    # Display a preview of the extracted text (limited to 1000 characters)
    st.text_area("Text preview", file_text[:1000] + "...." if len(file_text) > 1000 else file_text, height=200)

    # If the "Summarize paper" button is clicked, generate a summary using OpenAI
    if st.button("Summarize paper"):
        # Create a prompt instructing the AI to summarize the extracted text
        prompt = f"""
            Summarize the information in the extract, making sure the summarized text contains the vital points.
            {file_text}
        """

        # Display the assistant's message while generating the summary
        with st.chat_message("assistant"):
            # Generate a response from OpenAI using the chosen model
            stream = client.chat.completions.create(
                model=st.session_state["ai_model"],  # Use the selected AI model
                messages=[
                    {"role": "user", "content": prompt}  # User's message containing the extracted text
                ],
                stream=True,  # Enable streaming response
            )

            # Display the summarized text
            st.subheader("Summarized text")
            response = st.write_stream(stream)  # Stream the AI response in real time
        
        # Store the assistant's response in session state for future reference
        st.session_state.messages.append({"role": "assistant", "content": response})