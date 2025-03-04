from langchain_openai import ChatOpenAI
from browser_use import Agent
from dotenv import load_dotenv
load_dotenv()

import asyncio

llm = ChatOpenAI(model="gpt-4o")

async def main():
    agent = Agent(
        task="run a QA test (inspect the web pages and see the element and console to find any warning and errors) to found bugs in this website 'https://qacrmdemo.netlify.app/report-details' ",
        llm=llm,
    )
    result = await agent.run()
    print(result)

asyncio.run(main())