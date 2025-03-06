from fastapi import FastAPI
from pydantic import BaseModel
import uuid
import threading
import logging
from qa_agent import run_qa_agent

app = FastAPI()
tasks = {}
logging.basicConfig(level=logging.INFO)


class TaskRequest(BaseModel): 
    """
    Model for incoming task requests.
    Attributes:
        website (str): The website URL to be tested.
        test_type (str): The type of test to perform (e.g., "create a new user", "generate a new report").
    """
    website: str
    test_type: str  


@app.get("/task/{task_id}")
def get_task(task_id: str): 
    """
    Retrieve the status and results of a specific task.
    
    Args:
        task_id (str): Unique identifier of the task.
    
    Returns:
        dict: Task details if found, otherwise an error message.
    """
    task = tasks.get(task_id) 
    if not task:
        return {"error": "Task not found"}
    
    return {
        "task_id": task_id,
        "status": task["status"],
        "results": task["results"],
    }


@app.post("/create_task")
def create_task(request: TaskRequest): 
    """
    Create a new asynchronous task for running a website test.
    
    Args:
        request (TaskRequest): The request containing the task details.
    
    Returns:
        dict: The task ID and its initial status.
    """
    task_id = str(uuid.uuid4()) # Generate a unique task ID
    tasks[task_id] = {"status": "pending", "results": []} # Initialize task status and result

    def run_tests():
        """Executes the test in a separate thread and updates the task status."""
        tasks[task_id]["status"] = "running"
        logging.info(f"Running test: {request.test_type} on {request.website}")

        try:
            # Execute the test using the QA agent
            results = run_qa_agent(request.website, request.test_type) 
            tasks[task_id] = {"status": "finished", "results": [results]} # store results
        except Exception as e:
            # Handle errors and log failure
            tasks[task_id] = {"status": "error", "results": [str(e)]}
            logging.error(f"Test failed: {e}")

    # Start the test execution in a new thread
    thread = threading.Thread(target=run_tests)
    thread.start()
    
    return {"task_id": task_id, "status": "pending"}  #returns the task ID and initial status

if __name__ == "__main__":
    # Run the FastAPI application using Uvicorn
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
