import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from .auth.router import router as auth_router
from .games.router import router as games_router

# Routing
app = FastAPI(title='Game look')

origins = [
    "http://localhost",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"],
    allow_headers=["Content-Type", "Set-Cookie", "Access-Control-Allow-Header", "Access-Control-Allow-Origin",
                   "Authorization"],
)


app.include_router(auth_router)
app.include_router(games_router)

if __name__ == "__main__":
    uvicorn.run(app, host='localhost', port=8000)
