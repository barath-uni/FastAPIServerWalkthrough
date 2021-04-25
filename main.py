from fastapi import FastAPI, Body, Request
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

list_of_usernames = list()
templates = Jinja2Templates(directory="htmldirectory")


class NameValues(BaseModel):
    name: str = None
    country: str
    age: int
    base_salary: float


@app.get("/home/{user_name}", response_class=HTMLResponse)
def write_home(request: Request, user_name: str):
    return templates.TemplateResponse("home.html", {"request": request, "username": user_name})


@app.post("/postData")
def post_data(name_value: NameValues, spousal_status: str = Body(...)):
    print(name_value)
    return {
        "name": name_value.name,
        "spousal_status": spousal_status
    }
