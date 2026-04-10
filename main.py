from fastapi import FastAPI

app = FastAPI(title="Docker Desktop K8s Lab from Nadezhda.v2")

@app.get("/")
def root():
    return {"msg": "hello from nadezhda docker-desktop k8s"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/crash")
def crash():
    import os
    os._exit(1)

@app.get("/slow")
def slow():
    import time
    time.sleep(20)
    return {"msg": "slow response"}
