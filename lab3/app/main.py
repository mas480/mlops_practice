from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from function import *

class Request_params(BaseModel):
    count_data: int

app = FastAPI()

@app.get("/")
def read_root():
    return "Mlops_homework_3"

@app.post("/do_work/")
async def do_work_fun(req_params: Request_params):
    print(req_params)
    result = model_reg(req_params.count_data)
    return f'Model test accuracy is: {result}'
