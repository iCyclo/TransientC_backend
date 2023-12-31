from flask import jsonify
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI


from rlc import rlc
from rl import rl

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def index():
    return {"message": "Hello World"}

@app.get("/plot-rlc")
def getRLC(R, L, C, V, time):
    return rlc(float(R),float(L), float(C), float(V), float(time))

@app.get("/plot-rl")
def getRL(R,L,V,time):
    return rl(float(R),float(L), float(V), float(time))
   
