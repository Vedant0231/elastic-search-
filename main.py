import uvicorn

if __name__ == "__main__":
    uvicorn.run("src.app:app", host="localhost", port=int("5000"), reload=True)
