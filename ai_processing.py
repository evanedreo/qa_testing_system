from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

# Load API keys from .env file
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Hardcoded instructions for test execution
IMPORTANT_NOTES = """    
ALWAYS FOLLOW THESE RULES:
- Do NOT press any WEBSITE LINK
- Do NOT open any new website (only stay in the CURRENT website)
"""

# Using LLM to generate/ breakdown test steps to get a more detailed steps for browser-use
# To ensure that the user won’t need to enter a lot of details for the debugging
def generate_test_steps(test_type: str):
    """Generates step-by-step test actions and expected results using LLM.
    
    Args:
        test_type (str): The type of test to be performed on the website.

    Returns:
        tuple: (steps, expected_result) where:
            - steps (str): A breakdown of test actions.
            - expected_result (str): The expected outcome if the test is successful.
    """
    llm = ChatOpenAI(model="gpt-4o") # Initialize OpenAI LLM client
    #prompting for the LLM agent to breakdown steps and give expected result from the input (test_type)
    prompt = f""" 
    Break down the following website test request into step-by-step actions. YOU MUST NOT TEST a LINK but you can use the navigation bar
    
    Task: {test_type}

    Example of a detailed response (do NOT copy it, just use it as an example for the structure):
    \"    
    ALWAYS WRITE and USE this notes: {IMPORTANT_NOTES}
    
    Steps:
    1. Open the website.
        - Enter the website URL in a web browser to access the homepage.
    2. Locate the 'Create New User' button and click it.
        - Navigate to the section of the website where user management is handled.
        - Identify and click the "Create New User" button to open the user creation form.
    3. Generate random user details and input them into the form.
        - Use a random data generator or manually create fictional user details (e.g., name, email, username, password).
        - Fill in the form fields with the generated data.
    4. Click submit and verify user creation.
        - Click the "Submit" button to create the new user.
        - Verify that the user is successfully created by:
            -Checking for a confirmation message or notification.
            -Searching for the new user in the user list or database.
            -Ensuring the user details match the input data.

    Expected Outcome:
    - The system successfully creates a new user.
    - The new user entry appears in the **customer list** with the correct details.
    - If validation fails, the user should see an **appropriate error message**.
    - The form should not allow incorrect inputs (e.g., empty fields, invalid email format).
    - The system should handle errors gracefully without crashing or unresponsive behavior.
    - 
    \"
    """

    # Get the response from OpenAI
    response = llm.invoke(prompt)
    
    # Convert AI message object to string
    response_text = response.content  # extract the content safely

    # Extract the expected result from response
    if "Expected Outcome:" in response_text:
        steps, expected_result = response_text.split("Expected Outcome:")
    else:
        steps = response_text
        expected_result = "Not specified"

    return steps.strip(), expected_result.strip()

#An AI powered analyzer which compare the expected and actual result to give insights about the bugs
def analyze_results(expected: str, actual: str):
    """
    Compares expected vs actual results to detect discrepancies or bugs using LLM.

    Args:
        expected (str): The anticipated outcome of the test.
        actual (str): The real outcome observed during the test.

    Returns:
        str: Analysis of the test result, including bug classification, explanation, and suggestions.
    """
    llm = ChatOpenAI(model="gpt-4o")
    
    prompt = f"""
    Analyze the following test execution:

    **Expected Outcome:** 
    {expected}

    **Actual Outcome:** 
    {actual}

    Identify if there is a bug by comparing both results. Consider the following EXAMPLE (do NOT copy it, just use it as an example for the structure):
    - Are **error messages missing, unclear, or misleading**, leading to difficulties in debugging or troubleshooting?
    - Is the **layout or UI rendering incorrect** (e.g., broken styling, overlapping elements, misaligned buttons)?
    - Are there any **functions, components, or UI elements that do not behave as expected** (e.g., buttons not clickable, forms not submitting, missing UI elements)?
    - Are there any **unexpected behaviors, performance issues, or crashes** that disrupt the user experience?
    
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

    Bugs Analysis:
    1. first bug
    2. second bug
    """
    
    response = llm.invoke(prompt)
    return response.content  # extract and return response text safely1

