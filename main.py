from fastapi import FastAPI, Body
from pydantic import BaseModel

app = FastAPI()

list_of_usernames = list()


class NameValues(BaseModel):
    name: str = None
    country: str
    age: int
    base_salary: float


@app.get("/home/{user_name}")
def write_home(user_name: str, query):
    return {
        "Name": user_name,
        "Age": 24,
        "query": query
    }


@app.post("/postData")
def post_data(name_value: NameValues, spousal_status: str = Body(...)):
    print(name_value)
    return {
        "name": name_value.name,
        "spousal_status": spousal_status
    }
