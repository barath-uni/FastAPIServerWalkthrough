from fastapi import FastAPI, Body, Request, File, UploadFile, Form, Depends, BackgroundTasks
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import time
app = FastAPI()

list_of_usernames = list()
templates = Jinja2Templates(directory="htmldirectory")

oauth_scheme = OAuth2PasswordBearer(tokenUrl="token")


def handle_email_background(email: str, data: str):
    print(email)
    print(data)
    for i in range(100):
        print(i)
        time.sleep(0.1)


@app.get("/users/email")
async def handle_email(email: str, background_task: BackgroundTasks):
    print(email)
    background_task.add_task(handle_email_background, email, "THIS IS A SAMPLE BACKGROUND TASK MANAGER")
    return {"user": "baradwaj", "message": "Mail Sent"}


@app.post("/token")
async def token_generate(form_data: OAuth2PasswordRequestForm = Depends()):
    print(form_data)
    return {"access_token": form_data.username, "token_type": "bearer"}


@app.get("/users/profilepic")
async def profile_pic(token: str = Depends(oauth_scheme)):
    print(token)
    return {
        "user": "baradwaj",
        "profile_pic": "my_face"
    }


class NameValues(BaseModel):
    name: str = None
    country: str
    age: int
    base_salary: float


@app.get("/home/{user_name}", response_class=HTMLResponse)
def write_home(request: Request, user_name: str):
    return templates.TemplateResponse("home.html", {"request": request, "username": user_name})


@app.post("/submitform")
async def handle_form(assignment: str = Form(...), assignment_file: UploadFile = File(...)):
    print(assignment)
    print(assignment_file.filename)
    content_assignment = await assignment_file.read()
    print(content_assignment)


@app.post("/postData")
def post_data(name_value: NameValues, spousal_status: str = Body(...)):
    print(name_value)
    return {
        "name": name_value.name,
        "spousal_status": spousal_status
    }
