from browser_use import Agent
from langchain_openai import ChatOpenAI
from ai_processing import generate_test_steps, analyze_results
import asyncio

def run_qa_agent(website: str, test_type: str):
    """Runs the QA agent with step-by-step instructions and validates results.

    Args:
        website (str): The URL of the website to be tested.
        test_type (str): The specific test scenario (e.g., "Create a new user").

    Returns:
        dict: A structured response containing:
            - test_steps (str): The generated step-by-step instructions.
            - expected_result (str): The expected test outcome.
            - actual_result (str): The real test outcome from execution.
            - bug_analysis (str): AI-generated comparison of expected vs. actual results.
    """
    # Generate step-by-step test instructions and expected outcome using AI
    steps, expected_result = generate_test_steps(test_type)
    
    # Initialize the language model (GPT-4o) for Browser-Use interaction
    llm = ChatOpenAI(model="gpt-4o")

    # Create a Browser-Use agent to execute test steps on the given website
    agent = Agent(task=f"Execute the following steps on {website}: {steps}", llm=llm)
    
    # Run the agent asynchronously to perform the test in a browser environment
    result = asyncio.run(agent.run()) 

    # Extract the actual test result from the agent's output
    actual_result = result.final_result()

    # Compare actual vs expected results to detect the bugs
    bug_analysis = analyze_results(expected_result, actual_result)

    return {
        "test_steps": steps, 
        "expected_result": expected_result, 
        "actual_result": actual_result, # Browser-executed test outcome
        "bug_analysis": bug_analysis  # AI-driven bug analysis and classification
    }

