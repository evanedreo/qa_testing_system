from browser_use import Agent
from langchain_openai import ChatOpenAI
from ai_processing import generate_test_steps, analyze_results
import asyncio

def run_qa_agent(website: str, test_type: str):
    """Runs the QA agent with step-by-step instructions and validates results."""
    steps, expected_result = generate_test_steps(test_type)
    
    llm = ChatOpenAI(model="gpt-4o")
    agent = Agent(task=f"Execute the following steps on {website}: {steps}", llm=llm)
    
    result = asyncio.run(agent.run()) 
    actual_result = result.final_result()

    # Compare actual vs expected results
    bug_analysis = analyze_results(expected_result, actual_result)

    return {
        "test_steps": steps,
        "expected_result": expected_result,
        "actual_result": actual_result,
        "bug_analysis": bug_analysis  # Now includes classification and confidence score
    }

