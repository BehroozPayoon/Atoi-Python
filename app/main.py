from fastapi import FastAPI

from app.api.endpoints import api

app = FastAPI(title="Atoi Project", openapi_url="/openapi.json")

app.include_router(api.router, prefix='/utilities')


if __name__ == "__main__":
    # Use this for debugging purposes only
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000,
                log_level="debug", reload=True)
