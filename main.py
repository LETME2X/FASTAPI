from fastapi import FastAPI
app=FastAPI()

@app.get("/")
async def root():
    return {"message":"Hello I'm Shivendra"}

@app.get("/test")
async def root():
    return {"message":"this is test"}
    