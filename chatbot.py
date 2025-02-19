# # import streamlit as st
# # import pickle
# # from llama_cpp import Llama  

# # st.set_page_config(page_title="HR Policy Chatbot", page_icon="📝", layout="wide")

# # MODEL_PATH = r"C:\Users\shalu\Hr policy chatbot\mistral-7b-instruct-v0.1-q4_k_m.gguf"
# # VECTOR_STORE_PATH = "vector_store.pkl"

# # llm = Llama(model_path=MODEL_PATH, n_ctx=2048, n_gpu_layers=10)

# # # Load preprocessed vector store
# # with open(VECTOR_STORE_PATH, "rb") as f:
# #     vector_store, all_text = pickle.load(f)

# # def query_llm(question, context):
# #     prompt = f"""
# #     Given the following HR policy document context:
    
# #     {context}
    
# #     Answer the user's question concisely and accurately.
    
# #     Question: {question}
    
# #     Provide a summarized response:
# #     """
# #     response = llm(prompt, temperature=0.3, top_p=0.95, max_tokens=512, repeat_penalty=1.2)
# #     return response["choices"][0]["text"].strip() if isinstance(response, dict) and "choices" in response else "No relevant answer found."

# # def extract_section_by_keyword(text, keyword):
# #     sections = text.split("\n\n")
# #     relevant_sections = [s for s in sections if keyword.lower() in s.lower()]
# #     return "\n".join(relevant_sections) if relevant_sections else "No relevant section found."

# # def answer_question(vector_store, question, all_text):
# #     section_content = extract_section_by_keyword(all_text, question)
# #     if section_content != "No relevant section found.":
# #         return query_llm(question, section_content)
# #     else:
# #         docs = vector_store.similarity_search(question, k=3)  
# #         context = "\n".join([doc.page_content for doc in docs])
# #         return query_llm(question, context)

# # # Initialize session state for chat history
# # if "chat_history" not in st.session_state:
# #     st.session_state.chat_history = []

# # st.markdown('<h1 style="text-align: center;">📝 HR Policy Chatbot</h1>', unsafe_allow_html=True)

# # # Display chat history
# # for chat in st.session_state.chat_history:
# #     if chat["role"] == "user":
# #         st.markdown(f'<div style="background-color:#dcf8c6;padding:10px;border-radius:10px;margin-bottom:5px;text-align:right;">{chat["message"]}</div>', unsafe_allow_html=True)
# #     else:
# #         st.markdown(f'<div style="background-color:#e3e3e3;padding:10px;border-radius:10px;margin-bottom:5px;">{chat["message"]}</div>', unsafe_allow_html=True)

# # # User Input
# # user_question = st.text_input("Ask a question:", key="question")

# # if st.button("Send", key="send"):
# #     if user_question:
# #         st.session_state.chat_history.append({"role": "user", "message": user_question})
        
# #         with st.spinner("Thinking..."):
# #             answer = answer_question(vector_store, user_question, all_text)
        
# #         st.session_state.chat_history.append({"role": "bot", "message": answer})
# #         st.rerun()

# # if st.button("Restart Conversation", key="restart"):
# #     st.session_state.chat_history = []
# #     st.rerun()
# # import streamlit as st
# # import pickle
# # from llama_cpp import Llama
# # import os
# # from PIL import Image

# # # Load your Llama model and vector store
# # MODEL_PATH = "mistral-7b-instruct-v0.1-q4_k_m.gguf"  # Change this to your model path
# # VECTOR_STORE_PATH = "vector_store.pkl"

# # llm = Llama(model_path=MODEL_PATH, n_ctx=2048, n_gpu_layers=10)

# # # Load preprocessed vector store
# # with open(VECTOR_STORE_PATH, "rb") as f:
# #     vector_store, all_text = pickle.load(f)

# # # Initialize session state for chat history and memory
# # if "chat_history" not in st.session_state:
# #     st.session_state.chat_history = []
# # if "memory" not in st.session_state:
# #     st.session_state.memory = {}

# # # Function to query LLM with limited text size
# # def query_llm(question, context):
# #     max_tokens = 2048  # Set a safe limit for tokens
# #     prompt = f"""
# #     Given the following HR policy document context:
    
# #     {context[:max_tokens]}  # Limit the context to max_tokens size
    
# #     Answer the user's question concisely and accurately.
    
# #     Question: {question}
    
# #     Provide a summarized response:
# #     """
# #     response = llm(prompt, temperature=0.3, top_p=0.95, max_tokens=512, repeat_penalty=1.2)
# #     return response["choices"][0]["text"].strip() if isinstance(response, dict) and "choices" in response else "No relevant answer found."

# # # Extract section by keyword (Limiting the text size to prevent large contexts)
# # def extract_section_by_keyword(text, keyword):
# #     sections = text.split("\n\n")
# #     relevant_sections = [s for s in sections if keyword.lower() in s.lower()]
# #     return "\n".join(relevant_sections)[:2048] if relevant_sections else "No relevant section found."

# # # Answer question with context
# # def answer_question(vector_store, question, all_text):
# #     section_content = extract_section_by_keyword(all_text, question)
# #     if section_content != "No relevant section found.":
# #         return query_llm(question, section_content)
# #     else:
# #         docs = vector_store.similarity_search(question, k=3)  
# #         context = "\n".join([doc.page_content for doc in docs])[:2048]  # Limit to 2048 tokens
# #         return query_llm(question, context)

# # # Handle user input and memory
# # st.set_page_config(page_title="Chatbot", page_icon="💼", layout="wide")  # Professional emoji added here

# # # Display logo above title
# # def display_logo():
# #     logo_path = "logo.png"  # Change this to your logo's path
# #     if os.path.exists(logo_path):
# #         logo = Image.open(logo_path)
# #         st.image(logo, width=200)

# # # Display the logo above title
# # display_logo()

# # # Customizing the page title to match the Pricol text color in the logo
# # pricol_text_color = "#006699"  # Update with the actual Pricol text color from the logo

# # # Title aligned to the left
# # st.markdown(f'<h1 style="text-align: left; color: {pricol_text_color}; margin-top: 10px; margin-left: 20px;">CHATBOT</h1>', unsafe_allow_html=True)

# # # Display chat history with memory consideration
# # for chat in st.session_state.chat_history:
# #     if chat["role"] == "user":
# #         st.markdown(f'<div style="background: linear-gradient(45deg, #00bfff, #1e90ff); padding:10px; border-radius:10px; margin-bottom:5px; text-align:right; color:white;">{chat["message"]}</div>', unsafe_allow_html=True)
# #     else:
# #         st.markdown(f'<div style="background: linear-gradient(45deg, #87CEFA, #4682B4); padding:10px; border-radius:10px; margin-bottom:5px; color:white;">{chat["message"]}</div>', unsafe_allow_html=True)

# # # User Input
# # user_question = st.text_input("Ask a question:", key="question")

# # # Add blue color for the Send button
# # send_button_style = """
# #     <style>
# #         .stButton>button {
# #             background-color: #1e90ff; /* Blue button */
# #             color: white;
# #             font-size: 16px;
# #             border-radius: 8px;
# #             width: 100%;
# #             padding: 10px;
# #             margin-top: 10px;
# #             border: 2px solid white;  /* White border */
# #         }
# #     </style>
# # """

# # # Add blue color for the Restart button
# # restart_button_style = """
# #     <style>
# #         .stButton>button {
# #             background-color: #1e90ff; /* Blue button */
# #             color: white;
# #             font-size: 16px;
# #             border-radius: 8px;
# #             width: 100%;
# #             padding: 10px;
# #             margin-top: 10px;
# #             border: 2px solid white;  /* White border */
# #         }
# #     </style>
# # """

# # st.markdown(send_button_style, unsafe_allow_html=True)

# # # Send button
# # if st.button("Send", key="send"):
# #     if user_question:
# #         # Add to chat history
# #         st.session_state.chat_history.append({"role": "user", "message": user_question})
        
# #         # Check if the bot should remember something (e.g., user’s name or preferences)
# #         if "eligibility" in user_question.lower() and "local conveyance" in user_question.lower():
# #             # Store relevant local conveyance eligibility information in memory
# #             st.session_state.memory["local_conveyance_eligibility"] = "Eligibility for the local conveyance policy depends on the grade and transportation type. It includes bus, train, auto, Uber/Ola or equivalent."
# #             response = st.session_state.memory["local_conveyance_eligibility"]
# #         else:
# #             with st.spinner("Thinking..."):
# #                 answer = answer_question(vector_store, user_question, all_text)
# #             st.session_state.chat_history.append({"role": "bot", "message": answer})

# #         st.rerun()

# # # Customizing buttons and UI colors
# # st.markdown("""
# #     <style>
# #         body {
# #             background: linear-gradient(45deg, #00bfff, #1e90ff);  /* Blue gradient background */
# #             color: white;
# #             font-family: 'Arial', sans-serif;
# #         }
# #         .stButton>button {
# #             background-color: #1e90ff;
# #             color: white;
# #             font-size: 16px;
# #             border-radius: 8px;
# #             width: 100%;
# #             padding: 10px;
# #             margin-top: 10px;
# #             border: 2px solid white;  /* White border */
# #         }
# #         .stTextInput>div>input {
# #             border-radius: 10px;
# #             padding: 10px;
# #             font-size: 14px;
# #         }
# #         .stMarkdown {
# #             font-size: 18px;
# #         }
# #         .stImage>img {
# #             border-radius: 10px;
# #         }
# #     </style>
# # """, unsafe_allow_html=True)

# # # Restart conversation
# # st.markdown(restart_button_style, unsafe_allow_html=True)
# # if st.button("Restart Conversation", key="restart"):
# #     st.session_state.chat_history = []
# #     st.session_state.memory = {}  # Clear memory
# #     st.rerun()
# import streamlit as st
# import pickle
# from llama_cpp import Llama
# import os
# from PIL import Image

# # Load your Llama model and vector store
# MODEL_PATH = "mistral-7b-instruct-v0.1-q4_k_m.gguf"  # Change this to your model path
# VECTOR_STORE_PATH = "vector_store.pkl"

# llm = Llama(model_path=MODEL_PATH, n_ctx=2048, n_gpu_layers=10)

# # Load preprocessed vector store
# with open(VECTOR_STORE_PATH, "rb") as f:
#     vector_store, all_text = pickle.load(f)

# # Initialize session state for chat history and memory
# if "chat_history" not in st.session_state:
#     st.session_state.chat_history = []
# if "memory" not in st.session_state:
#     st.session_state.memory = {}

# # Function to query LLM
# def query_llm(question, context):
#     max_tokens = 2048  # Set a safe limit for tokens
#     prompt = f"""
#     Given the following HR policy document context:
#     {context[:max_tokens]}  # Limit the context to max_tokens size
#     Answer the user's question concisely and accurately.
#     Question: {question}
#     Provide a summarized response:
#     """
#     response = llm(prompt, temperature=0.3, top_p=0.95, max_tokens=512, repeat_penalty=1.2)
#     return response["choices"][0]["text"].strip() if isinstance(response, dict) and "choices" in response else "No relevant answer found."

# # Extract section by keyword
# def extract_section_by_keyword(text, keyword):
#     sections = text.split("\n\n")
#     relevant_sections = [s for s in sections if keyword.lower() in s.lower()]
#     return "\n".join(relevant_sections)[:2048] if relevant_sections else "No relevant section found."

# # Answer question with context
# def answer_question(vector_store, question, all_text):
#     section_content = extract_section_by_keyword(all_text, question)
#     if section_content != "No relevant section found.":
#         return query_llm(question, section_content)
#     else:
#         docs = vector_store.similarity_search(question, k=3)
#         context = "\n".join([doc.page_content for doc in docs])[:2048]
#         return query_llm(question, context)

# # Custom CSS for UI styling
# st.markdown("""
#     <style>
#         body {
#             background-color: #f8f9fa;
#         }
#         .message-user {
#             background-color: #ff6666;
#             color: white;
#             padding: 10px;
#             border-radius: 10px;
#             margin-bottom: 10px;
#             text-align: left;
#         }
#         .message-bot {
#             background-color: #ffcc66;
#             color: black;
#             padding: 10px;
#             border-radius: 10px;
#             margin-bottom: 10px;
#             text-align: left;
#         }
#         .chat-container {
#             max-width: 700px;
#             margin: auto;
#         }
#     </style>
# """, unsafe_allow_html=True)

# st.title("🤖 Chatbot")

# # Display chat history in a styled format
# st.markdown('<div class="chat-container">', unsafe_allow_html=True)
# for chat in st.session_state.chat_history:
#     if chat["role"] == "user":
#         st.markdown(f'<div class="message-user">{chat["message"]}</div>', unsafe_allow_html=True)
#     else:
#         st.markdown(f'<div class="message-bot">{chat["message"]}</div>', unsafe_allow_html=True)
# st.markdown('</div>', unsafe_allow_html=True)

# # User Input
# user_question = st.text_input("What is up?", key="question")

# # Handle sending messages
# if st.button("Send"):
#     if user_question:
#         st.session_state.chat_history.append({"role": "user", "message": user_question})
        
#         if "eligibility" in user_question.lower() and "local conveyance" in user_question.lower():
#             response = "Eligibility for the local conveyance policy depends on the grade and transportation type. It includes bus, train, auto, Uber/Ola or equivalent."
#         else:
#             with st.spinner("Thinking..."):
#                 response = answer_question(vector_store, user_question, all_text)
        
#         st.session_state.chat_history.append({"role": "bot", "message": response})
#         st.rerun()

# # Restart conversation
# if st.button("Restart Conversation"):
#     st.session_state.chat_history = []
#     st.session_state.memory = {}
#     st.rerun()

import streamlit as st
import pickle
from llama_cpp import Llama
import os
from PIL import Image

# Load your Llama model and vector store
MODEL_PATH = os.path.join("models", "mistral-7b-instruct-v0.1-q4_k_m.gguf")
VECTOR_STORE_PATH = "vector_store.pkl"

llm = Llama(model_path=MODEL_PATH, n_ctx=2048, n_gpu_layers=10)

# Load preprocessed vector store
with open(VECTOR_STORE_PATH, "rb") as f:
    vector_store, all_text = pickle.load(f)

# Initialize session state for chat history and memory
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "memory" not in st.session_state:
    st.session_state.memory = {}

# Function to query LLM
def query_llm(question, context):
    max_tokens = 2048  # Set a safe limit for tokens
    prompt = f"""
    Given the following HR policy document context:
    {context[:max_tokens]}  # Limit the context to max_tokens size
    Answer the user's question concisely and accurately.
    Question: {question}
    Provide a summarized response:
    """
    response = llm(prompt, temperature=0.3, top_p=0.95, max_tokens=512, repeat_penalty=1.2)
    return response["choices"][0]["text"].strip() if isinstance(response, dict) and "choices" in response else "No relevant answer found."

# Extract section by keyword
def extract_section_by_keyword(text, keyword):
    sections = text.split("\n\n")
    relevant_sections = [s for s in sections if keyword.lower() in s.lower()]
    return "\n".join(relevant_sections)[:2048] if relevant_sections else "No relevant section found."

# Answer question with context
def answer_question(vector_store, question, all_text):
    section_content = extract_section_by_keyword(all_text, question)
    if section_content != "No relevant section found.":
        return query_llm(question, section_content)
    else:
        docs = vector_store.similarity_search(question, k=3)
        context = "\n".join([doc.page_content for doc in docs])[:2048]
        return query_llm(question, context)

# Custom CSS for UI styling
st.markdown("""
    <style>
        body {
            background-color: #f8f9fa;
        }
        .message-user {
            background-color: #1e90ff;
            color: white;
            padding: 10px;
            border-radius: 10px;
            margin-bottom: 10px;
            text-align: right;
        }
        .message-bot {
            background-color: white;
            color: black;
            padding: 10px;
            border-radius: 10px;
            margin-bottom: 10px;
            text-align: left;
            border: 1px solid #ddd;
        }
        .chat-container {
            max-width: 700px;
            margin: auto;
        }
        .input-container {
            display: flex;
            align-items: center;
            background-color: #1e90ff;
            border-radius: 10px;
            padding: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        .stTextInput>div>input {
            flex-grow: 1;
            border: none;
            padding: 10px;
            font-size: 14px;
            border-radius: 10px;
            background-color: transparent;
            color: white;
            outline: none;
        }
        .send-button {
            background-color: transparent;
            color: white;
            font-size: 20px;
            cursor: pointer;
            border: none;
            margin-left: 10px;
            padding: 5px;
        }
        .send-button:hover {
            opacity: 0.8;
        }
    </style>
""", unsafe_allow_html=True)

# Display logo
logo_path = "logo.png"
if os.path.exists(logo_path):
    logo = Image.open(logo_path)
    st.image(logo, width=200)

st.title("🤖 Chatbot")

# Display chat history in a styled format
st.markdown('<div class="chat-container">', unsafe_allow_html=True)
for chat in st.session_state.chat_history:
    if chat["role"] == "user":
        st.markdown(f'<div class="message-user">{chat["message"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="message-bot">{chat["message"]}</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# User Input with Send button inside the input box
col1, col2 = st.columns([4, 1])
with col1:
    user_question = st.text_input("", placeholder="Ask a question...", key="input_box", label_visibility="collapsed")
with col2:
    send_button = st.button("→", key="send", help="Send your message", use_container_width=True)
    if send_button and user_question:
        st.session_state.chat_history.append({"role": "user", "message": user_question})

        # Directly call the answer_question function for all cases
        with st.spinner("Thinking..."):
            response = answer_question(vector_store, user_question, all_text)

        st.session_state.chat_history.append({"role": "bot", "message": response})
        st.rerun()

# Restart conversation
if st.button("Restart Conversation"):
    st.session_state.chat_history = []
    st.session_state.memory = {}
    st.rerun()
