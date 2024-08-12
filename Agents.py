import os
from dotenv import load_dotenv
from crewai import Agent
from langchain_groq import ChatGroq

load_dotenv()
Model = ChatGroq(model = "llama-3.1-405b-reasoning")

Theory_Finder = Agent(
    role = "Researcher",
    goal = "Find relevant Reddit posts discussing fan theories for the {input} animanga.",
    backstory ="""A tireless digital prospector, sifting through the mountains of data on Reddit to uncover the hidden
    gems of fan speculation.""",
    tools = [],
    llm = Model,
    allow_delegation = True
)

Theory_Curator = Agent(
    role = "Curator",
    goal = "Identify the most interesting, well-supported, and unique fan theories.",
    backstory = """A discerning critic, separating the brilliant from the bizarre in the world of fan speculation.""",
    tools = [],
    llm = Model,
    allow_delegation = True
)

Article_Writer = Agent(
    role = "Transforms curated theories into an engaging article.",
    goal = "Present the theories in a clear, concise, and compelling manner.",
    backstory = """A wordsmith, weaving together the threads of fan speculation into a captivating narrative.""",
    tools = [],
    allow_delegation = True
)