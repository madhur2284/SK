from fastapi import FastAPI, UploadFile, File
import tempfile

from Services.resume_parser import extract_text_from_pdf
from Services.ats_scoring import generate_ats_score
from app.kernel_setup import create_kernel

app = FastAPI()

kernel = create_kernel()


@app.post("/ats-score")

async def ats_score(file: UploadFile = File(...)):

    # Save uploaded file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp:
        temp.write(await file.read())
        temp_path = temp.name

    # Extract resume text
    resume_text = extract_text_from_pdf(temp_path)

    # Get ATS score
    result = await generate_ats_score(kernel, resume_text)

    return {
        "analysis": result
    }