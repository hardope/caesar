from fastapi import FastAPI, APIRouter, Depends, HTTPException, status, File, UploadFile, Form
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
from caesar import caesar_cipher, rot13_cipher, atbash_cipher, crot13
from uuid import uuid4
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Caesar Cipher API",
    description="A simple API for Caesar cipher",
    version="1.0.0",
    docs_url="/docs",
    redoc_url='/redoc'
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

router = APIRouter()


class Caesar(BaseModel):
    text: str
    shift: int
    option: str

class Default(BaseModel):
    text: str

class CaesarFile(BaseModel):
    shift: int = Form(...)
    option: str = Form(...)

@router.get("/")
async def index():
    return {
        "message": "Welcome to the Caesar cipher API!",
        "docs": "caesar.hardope.tech/docs"
    }

@router.post("/rot13")
async def rot13_api(val: Default):
    return {
        "message": rot13_cipher(val.text)
    }

@router.post("/atbash")
async def atbash_api(val: Default):
    return {
        "message": atbash_cipher(val.text)
    }

@router.post("/caesar")
async def caesar_api(caesar: Caesar):
    return {
        "message": caesar_cipher(caesar.text, caesar.shift, caesar.option)
    }

@router.post("/crot13")
async def crot13_api(val: Caesar):
    return {
        "message": crot13(val.text, val.shift, val.option)
    }

@router.post("/caesar/file")
async def caesar_file_api(file: UploadFile = File(...), shift: int = Form(...), option: str = Form(...) ):
    try:    
        contents = await file.read()
        out = caesar_cipher(contents.decode("utf-8"), shift, option)
        new_file = f"files/{uuid4()}.{file.filename.split('.')[1]}"
        with open(new_file, "w") as f:
            f.write(out)
    except:
        raise HTTPException(status_code=400, detail="Invalid file")
    return {
        "message": "File uploaded successfully!", "file": new_file
    }

@router.post("/crot13/file")
async def crot13_file_api(file: UploadFile = File(...), shift: int = Form(...), option: str = Form(...) ):
    try:    
        contents = await file.read()
        out = crot13(contents.decode("utf-8"), shift, option)
        new_file = f"files/{uuid4()}.{file.filename.split('.')[1]}"
        with open(new_file, "w") as f:
            f.write(out)
    except:
        raise HTTPException(status_code=400, detail="Invalid file")
    return {
        "message": "File uploaded successfully!", "file": new_file
    }

@router.post("/rot13/file")
async def rot13_file_api(file: UploadFile = File(...)):
    try:    
        contents = await file.read()
        out = rot13_cipher(contents.decode("utf-8"))
        new_file = f"files/{uuid4()}.{file.filename.split('.')[1]}"
        with open(new_file, "w") as f:
            f.write(out)
    except:
        raise HTTPException(status_code=400, detail="Invalid file")
    return {
        "message": "File uploaded successfully!", "file": new_file
    }

@router.post("/atbash/file")
async def atbash_file_api(file: UploadFile = File(...)):
    try:    
        contents = await file.read()
        out = atbash_cipher(contents.decode("utf-8"))
        new_file = f"files/{uuid4()}.{file.filename.split('.')[1]}"
        with open(new_file, "w") as f:
            f.write(out)
    except:
        raise HTTPException(status_code=400, detail="Invalid file")
    return {
        "message": "File uploaded successfully!", "file": new_file
    }

app.include_router(router, prefix="")
app.mount("/files", StaticFiles(directory="files"), name="files")
