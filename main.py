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
    website: str
    test_type: str  # e.g., "add_customer", "edit_customer", "delete_customer"

@app.get("/task/{task_id}")
def get_task(task_id: str):
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
    task_id = str(uuid.uuid4())
    tasks[task_id] = {"status": "pending", "results": []}

    def run_tests():
        tasks[task_id]["status"] = "running"
        logging.info(f"Running test: {request.test_type} on {request.website}")
        try:
            results = run_qa_agent(request.website, request.test_type)
            tasks[task_id] = {"status": "finished", "results": [results]}
        except Exception as e:
            tasks[task_id] = {"status": "error", "results": [str(e)]}
            logging.error(f"Test failed: {e}")

    thread = threading.Thread(target=run_tests)
    thread.start()
    
    return {"task_id": task_id, "status": "pending"}

@app.get("/task/{task_id}")
def get_task(task_id: str):
    task = tasks.get(task_id)
    if not task:
        return {"error": "Task not found"}
    return {"task_id": task_id, **task}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
