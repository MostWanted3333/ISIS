from src.api.users import router as users_router
from fastapi import APIRouter
from src.api.dashboard import router as dashboard_router
main_router = APIRouter()

main_router.include_router(users_router)
main_router.include_router(dashboard_router)