import sys
import os
import uvicorn

# Force current directory into python path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000)