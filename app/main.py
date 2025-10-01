from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hi Snake!! Using my CICD with Jenkins, testing pipeline"}