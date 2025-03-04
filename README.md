1️⃣ **Delete the old virtual environment**
```sh
rm -rf .venv
```

2️⃣ **Create a new virtual environment using Python 3.11**
```sh
python3.11 -m venv .venv
```

3️⃣ **Activate the new virtual environment**
```sh
source .venv/bin/activate
```

4️⃣ **Verify that Python 3.11 is now being used**
```sh
python --version
```
✅ **Expected output:**
```
Python 3.11.x
```

5️⃣ **Reinstall dependencies**
```sh
pip install --upgrade pip
pip install fastapi uvicorn browser-use
```

6️⃣ **Run the FastAPI app again**
```sh
python -m uvicorn main:app --reload
```

---
