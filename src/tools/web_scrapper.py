from langchain_core.tools import tool
from langchain_community.document_loaders import WebBaseLoader

@tool
def open_url(url: str):
    """
    Scrapes and returns the contents of website

    Args:
        url(str): the url of a website
    
    """

    web_loader = WebBaseLoader(url)
    document = web_loader.load()

    return document