from langchain_core.tools import tool
from ddgs import DDGS


@tool
def search(topic:str):
    """Finds relevant websites url about a topic.
    
    Args:
        topic(str): the topic to search about
    
    Returns:
        urls(dict): relevant website name as keys and website url as value
    
    """
    urls = {}
    with DDGS() as ddgs:
        results = ddgs.text(topic, max_results=5)

        for result in results:
            website_name = result['body']
            url = result['href']
            urls[website_name] = url
    return urls


@tool
def search_news(topic: str):
    """Finds relevant news artilce urls about a topic
    
    Args:
        topic(str): the news topic to search about
    
    Returns:
        urls(dict): relevant news title as keys and article url as value
    
    """
    articles = {}
    with DDGS() as ddgs:
        news = ddgs.news("AI", max_results=5, timelimit='w')
        for new in news:
            articles[new['title']] = new['url']
    return articles


