import os
from dotenv import load_dotenv
from langchain_community.tools.reddit_search.tool import RedditSearchRun
from langchain_community.utilities.reddit_search import RedditSearchAPIWrapper
from langchain_community.tools.reddit_search.tool import RedditSearchSchema
from crewai_tools import tool

load_dotenv()


@tool("RedditSearcher")
def my_tool(sub: str, query:str, limit: int = 10) -> str:
    """This tool dives into the depths of Reddit to collect specific posts based on your instructions. It's like a
    research assistant that never sleeps, tirelessly sifting through subreddits for the information you need. Give the
    get_reddit_posts function the input and the subreddit to search for the information"""
    Search = RedditSearchRun(
        api_wrapper=RedditSearchAPIWrapper()
    )
    Search_param = RedditSearchSchema(query=query, limit=limit, subreddit=sub, sort="new", time_filter="week")
    results = Search.run(tool_input=Search_param.dict())
    return results



