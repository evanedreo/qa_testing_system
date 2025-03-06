# Project Name
Q-AI Test

## About
Sick of doing a manual testing? This is an AI-driven QA agent that will help you to test your buggy website!

## Tech Stack
### Backend
- Python – Main programming language for API and automation.
- FastAPI – High-performance web framework for building APIs.
- Uvicorn – ASGI server to run the FastAPI application.

### AI & Automation
- LangChain – Framework for integrating OpenAI models.
- OpenAI GPT-4o – LLM used for test generation and analysis.
- Browser-Use – AI-powered browser automation for web testing.

## Future Improvement:
- Can use Deepseek (30 times cheaper than OpenAI) instead of OpenAI (because browser-use consumes a lot of tokens (expensive)) 
source = https://docs.browser-use.com/customize/supported-models
- fine tune the prompting even more
- find a way for browser-use to be able to open developer tools and read the codes the log errors


# Project Setup Guide

## Cloning the Repository
To get started, clone this repository to your local machine:
```sh
git clone https://github.com/evanedreo/qa_testing_system
cd qa_testing_system
```

## Setting Up the Environment

### 1️⃣ Delete the old virtual environment
If you have an existing virtual environment, remove it:
```sh
rm -rf .venv
```

### 2️⃣ Create a new virtual environment using Python 3.11
```sh
python3.11 -m venv .venv
```

### 3️⃣ Activate the new virtual environment
- **MacOS/Linux:**
  ```sh
  source .venv/bin/activate
  ```
- **Windows (PowerShell):**
  ```sh
  .venv\Scripts\Activate
  ```

### 4️⃣ Verify that Python 3.11 is now being used
```sh
python --version
```
✅ Expected output:
```sh
Python 3.11.x
```

### 5️⃣ Install dependencies
```sh
pip install --upgrade pip
pip install fastapi uvicorn browser-use
```

## Running the FastAPI App
Start the FastAPI server by running:
```sh
python -m uvicorn main:app --reload
```

## Testing the API
### Create a Task
"website" can be any website
"test_type" can be anything (generate a new report, generate a new customer, search for bugs in the website, etc)

Run the following command to create a task:
```sh
curl -X POST "http://127.0.0.1:8000/create_task" \
     -H "Content-Type: application/json" \
     -d '{
           "website": "https://qacrmdemo.netlify.app/dashboard",
           "test_type": "generate a new report"
         }'
```

### Retrieve a Task
When the program already finished, run the following command below

Replace `<task_id>` with the actual task ID that you get after you run the create task above:
```sh
curl -X GET "http://127.0.0.1:8000/task/<task_id>"
```

## Resources
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Uvicorn Documentation](https://www.uvicorn.org/)
- [Browser-Use Documentation](https://docs.browser-use.com/quickstart)


