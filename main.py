from fastapi import FastAPI

app = FastAPI()

list_of_usernames = list()

@app.get("/home/{user_name}")
def write_home(user_name: str, query):
    return {
        "Name": user_name,
        "Age": 24,
        "query": query
    }


@app.put("/username/{user_name}")
def put_data(user_name: str):
    print(user_name)
    list_of_usernames.append(user_name)
    return {
        "username": user_name
    }


@app.post("/postData")
def post_data(user_name: str):
    list_of_usernames.append(user_name)
    return {
        "usernames":list_of_usernames
    }


@app.delete("/deleteData/{user_name}")
def delete_data(user_name: str):
    list_of_usernames.remove(user_name)
    return {
        "usernames": list_of_usernames
    }


@app.api_route("/homedata", methods=['GET', 'POST', 'PUT', 'DELETE'])
def handle_homedata(username: str):
    print(username)
    return {
        "username":username
    }