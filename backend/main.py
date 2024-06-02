from controllers.api_v1.routes import *
from fastapi.requests import Request


@app.get("/")
def root(request: Request):
    print(request.url ) 
    context = {
        "home": "Code Commmerze API V1", 
    }
    return context

