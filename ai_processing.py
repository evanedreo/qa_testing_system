from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

# Load API keys from .env file
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def generate_test_steps(test_type: str):
    """Generates step-by-step test actions and expected results using GPT-4o."""
    llm = ChatOpenAI(model="gpt-4o")
    prompt = f"""
    Break down the following website test request into step-by-step actions. 
    Also provide the expected outcome if the test is successful.
    
    Task: {test_type}

    Example response:
    Steps:
    1. Open the website.
    2. Locate the 'Create New User' button and click it.
    3. Generate random user details and input them into the form.
    4. Click submit and verify user creation.

    Expected Outcome:
    - A new user entry appears in the customer list.
    """

    # Get the response from OpenAI
    response = llm.invoke(prompt)
    
    # Convert AIMessage object to string
    response_text = response.content  # Extract content safely

    # Extract expected result from response
    if "Expected Outcome:" in response_text:
        steps, expected_result = response_text.split("Expected Outcome:")
    else:
        steps = response_text
        expected_result = "Not specified"

    return steps.strip(), expected_result.strip()

def analyze_results(expected: str, actual: str):
    """Compares expected vs actual results and detects bugs using GPT-4o."""
    llm = ChatOpenAI(model="gpt-4o")
    
    prompt = f"""
    Analyze the following test execution:
    
    **Expected Outcome:** 
    {expected}

    **Actual Outcome:** 
    {actual}

    Identify if there is a bug by comparing both results. Consider the following:
    - Does the actual outcome **lack any key success criteria** from the expected outcome?
    - Is there any **user confusion or unclear messaging** that could impact usability?
    - Are there **missing UI elements or actions** that should have occurred?
    
    If a bug is found, classify it as one of the following:
    - **Critical Bug:** The functionality does not work at all.
    - **Major Bug:** Key expected behaviors are missing.
    - **Minor Bug:** The feature works but has usability or feedback issues.
    - **No Bug:** The behavior is correct.

    Provide:
    1. A bug classification (if applicable).
    2. A clear explanation of the issue.
    3. Suggested fixes.
    4. A confidence score (0-100%) indicating how likely this is to be a bug.
    """
    
    response = llm.invoke(prompt)
    return response.content  # Extract and return response text safely

