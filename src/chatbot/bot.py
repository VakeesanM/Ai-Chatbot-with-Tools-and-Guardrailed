from langchain.agents import create_agent
from langchain.agents.middleware import SummarizationMiddleware, PIIMiddleware
from langchain_openai import ChatOpenAI
from middleware.content_blocker import WordBlockMiddleWare
from langgraph.checkpoint.memory import  InMemorySaver

from tools.math import add, multiply, divide, subtract, root, power
#from tools.web_scrapper import open_url
#from tools.websearch import search, search_news

from dotenv import load_dotenv
load_dotenv()

class ChatBot(): 
    def __init__(self):
        self.model = ChatOpenAI(model='gpt-4o-mini', temperature=0.8) 

        summary_ware = SummarizationMiddleware(
            model = self.model,
            trigger= ('tokens', 2500),
            keep= ('messages', 10)

        )

        system_prompt = """ 
        You are a AI Chatbot, whose purpose is to help and talk with the user.
        ### TASKS
        * Answer the user questions with you knowledge
        * Never Lie to the user
        * Help them to best of your ability

        ### Important
        * Keep responses short
        * NO filbustering
        * NO inapproiate language or curse words
        * State when you don't something
        * Use the tools given to you if you think they are helpful to user's current query

        """
        memory = InMemorySaver()
        self.agent = create_agent(
            model=self.model,
            tools=[add, multiply, divide, subtract, root, power],
            checkpointer=memory,
            middleware=[
                summary_ware,
                PIIMiddleware(pii_type='credit_card', strategy='redact'),
                PIIMiddleware(pii_type='email', strategy='mask'),
                PIIMiddleware(pii_type='ip', strategy='redact'),
                WordBlockMiddleWare(['ignore instructions', 'system prompt', 'admin', 'disregard the above'])
            ],
            system_prompt= system_prompt
            
        )
        self.config = {
            'configurable' : {'thread_id': "user-01"}
        }

    def talk(self, message):
        message = {
            'messages': [{'role': 'user',
                         'content': message}]
        }

        response = self.agent.invoke(
            message,
            config=self.config

        )

        return response


    def stream(self, message):
        message = {
                'messages': [{'role': 'user',
                                'content': message}]
            }
        for chunk, _ in self.agent.stream(message, config=self.config, stream_mode='messages'):
            if chunk.content:
                yield chunk.content