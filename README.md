# Project Setup Guide

## Cloning the Repository
To get started, clone this repository to your local machine:
```sh
git clone <repository-url>
cd <repository-name>
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
Replace `<task_id>` with the actual task ID:
```sh
curl -X GET "http://127.0.0.1:8000/task/<task_id>"
```

## About
No description, website, or topics provided.

## Resources
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Uvicorn Documentation](https://www.uvicorn.org/)

## License
This project is licensed under [Your License Here].

