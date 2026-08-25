from langchain.agents import create_agent
from langchain.agents.middleware import SummarizationMiddleware, PIIMiddleware
from langchain_openai import ChatOpenAI
from langgraph.checkpoint.memory import  InMemorySaver

from tools.math import add, multiply, divide, subtract, root, power
from tools.web_scrapper import open_url
from tools.websearch import search, search_news

from dotenv import load_dotenv
load_dotenv()

#class ChatBot(): 

agent = create_agent(
    
)