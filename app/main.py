import sys
sys.stdout.flush()

from fastapi import FastAPI,Response,status,HTTPException,Depends

from . import models,schemas,utils
from .database import engine,SessionLocal,get_db
from .routers import  user, auth,admin
from .config import settings
from fastapi.middleware.cors import CORSMiddleware
models.Base.metadata.create_all(bind=engine)

import os
# from fastapi_limiter import FastAPILimiter
# from fastapi_limiter.depends import RateLimiter
# from redis.asyncio import Redis


app = FastAPI(title="First Project",
              description="This is a very simple project, with auto docs for the API and everything",
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(user.router)
app.include_router(auth.router)
app.include_router(admin.router)


@app.get("/")
def root():
    return {"message": "khela hobe!!!"}


