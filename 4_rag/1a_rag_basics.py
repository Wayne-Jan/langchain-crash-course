import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from get_model import generate_embeddings, get_chat_model
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import Chroma

# Define the directory containing the text file and the persistent directory
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, 'books', 'odyssey.txt')
persistent_directory = os.path.join(current_dir, 'db', 'chroma_db')

# Check if the Chroma vector store already exists
if not os.path.exists(persistent_directory):
    