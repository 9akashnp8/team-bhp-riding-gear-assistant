from decouple import config
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.schema import Document
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def get_page_source(url: str) -> str:
    """extracts the html sources from the page
    of the give url

    Args:
        url (str): url of the page whose source
            is required

    Returns:
        str: html string of the page
    """
    service = Service(executable_path=ChromeDriverManager().install())
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get(url)
    return driver.page_source

def create_embeddings(docs: "list[Document]") -> None:
    """creates and persists embeddings to db"""
    embeddings = OpenAIEmbeddings(openai_api_key=config('OPENAI_API_KEY'))
    db = Chroma.from_documents(docs, embeddings, persist_directory='db')
    db.persist()

def query_db(query: str, n_results: int = 5) -> list:
    """query the vector db for similar text content"""
    embedding = OpenAIEmbeddings(openai_api_key=config('OPENAI_API_KEY'))
    db = Chroma(persist_directory='db', embedding_function=embedding)
    results = db.similarity_search(query, k=n_results)
    return [result.page_content for result in results]