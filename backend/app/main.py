from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models.search import Search
import utils.utils as utils
import search.search as search


app = FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/search")
def handle_search_request(req: Search):
    err = utils.validate_request(req)

    if err is not None:
        return {"error": err}

    try:
        return search.search()
    except Exception as e:
        return {'error': e}


@app.get("/")
def root():
    return {"message": "Hello, World!"}
