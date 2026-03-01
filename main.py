from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def root(): return {"msg": "短视频文案API"}
@app.get("/random")
def random(category: str = "励志"):
    return {"success": True, "文案": "今天也要加油呀！"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
