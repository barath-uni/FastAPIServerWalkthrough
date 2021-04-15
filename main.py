from fastapi import FastAPI

app = FastAPI()


@app.get("/home/{user_name}")
def write_home(user_name: str, query):
    return {
        "Name": user_name,
        "Age": 24,
        "query": query
    }
