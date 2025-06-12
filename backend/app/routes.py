from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def health_check():
    return {"message": "App is running!"}
