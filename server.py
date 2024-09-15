from fastapi import APIRouter, FastAPI
from sqlalchemy.orm import sessionmaker
from api import router


def create_server(
        session_maker:sessionmaker=None,
        debug:bool=True,
        # router:APIRouter=router,
        # *routers:APIRouter
):
    server = FastAPI(debug=debug)
    server.include_router(router)
    server.session_maker = session_maker
    return server
