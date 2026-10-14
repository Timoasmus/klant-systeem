from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.data_router import data_router
import uvicorn
import logging
from routers.agent_router import agent_router

logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    )

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(data_router)
app.include_router(agent_router)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)