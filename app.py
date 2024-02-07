import fastapi
import uvicorn

app = fastapi.FastAPI()


@app.get("/")
async def _():
    return fastapi.responses.FileResponse("index.html")


@app.get("/{all_path:path}")
async def _(all_path):
    return fastapi.responses.FileResponse(all_path)


if __name__ == "__main__":
    uvicorn.run("__main__:app", host="127.0.0.1", port=5500)
