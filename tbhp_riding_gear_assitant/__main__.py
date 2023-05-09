import typer
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pathlib import Path

app = typer.Typer()

@app.command()
def serve():
    server = FastAPI()
    path = Path(__file__).parent
    static_files_dir = path / "frontend"
    server.mount(
        '/',
        StaticFiles(directory=static_files_dir, html=True),
        name="static"
    )
    import uvicorn
    uvicorn.run(server, host="127.0.0.1", port=8000)

def main():
    app()

if __name__ == "__main__":
    main()
    
