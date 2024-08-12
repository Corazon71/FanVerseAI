import os
from Tools import my_tool
from dotenv import load_dotenv
from crewai import Agent
from langchain_groq import ChatGroq
from crewai import Task, Crew

load_dotenv()

Model = ChatGroq(model = "llama3-70b-8192")

Theory_Finder = Agent(
    role = "Researcher",
    goal = "Find relevant Reddit posts discussing fan theories for the {query} animanga from the subreddit {sub}",
    backstory ="""A tireless digital prospector, sifting through the mountains of data on Reddit to uncover the hidden
    gems of fan speculation.""",
    tools = [my_tool],
    llm = Model,
    allow_delegation = True
)

task1 = Task(
    expected_output="Posts about {query} from the subreddit {sub}",
    description="Post about {query} from the subreddit {sub} gathered using the tool",
    agent=Theory_Finder,
)

my_crew = Crew(agents = [Theory_Finder], tasks = [task1])
crew = my_crew.kickoff(inputs = {"query" : "One Piece", "sub" : "anime"})
