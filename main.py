from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.post("/submit")
async def submit(request:Request, name:str = Form(...),email:str = Form(...), inquiry:str=Form(...)):
    # return templates.TemplateResponse("success.html",{"request":request,"name":name})
    response = {"status": "success", "message": "Message sent!"}
    return JSONResponse(content=response)

@app.get("/")
async def form(request:Request):
    return templates.TemplateResponse("form.html",{"request": request})