from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app=FastAPI()

@app.get("/web", response_class=HTMLResponse)
async def read_items():
    html_content="""
    <html>
    <head>
    <title> Hello World! </title>
    </head>
    <body> <h1> Hi! World! </h1> </body>
    </html>"""
    return HTMLResponse(content=html_content, status_code=200)
