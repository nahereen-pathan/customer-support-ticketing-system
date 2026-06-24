from fastapi import APIRouter, UploadFile, File
import os

router = APIRouter(
    prefix="/attachments",
    tags=["Attachments"]
)

UPLOAD_DIR = "uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):

    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    return {
        "message": "File uploaded successfully",
        "filename": file.filename
    }

@router.get("/")
def get_files():
    return {
        "files": os.listdir(UPLOAD_DIR)
    }

