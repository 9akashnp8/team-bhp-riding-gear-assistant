import typer
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pathlib import Path

from api.endpoints import router

app = typer.Typer()

@app.command()
def serve():
    api_app = FastAPI(title='main_app')
    api_app.include_router(router, prefix='')

    spa_app = FastAPI(title='spa_app')
    path = Path(__file__).parent
    static_files_dir = path / 'frontend'

    spa_app.mount('/api', api_app)
    spa_app.mount(
        '/',
        StaticFiles(
            directory=static_files_dir,
            html=True
        ),
        name='static'
    )

    import uvicorn
    uvicorn.run(spa_app, host='127.0.0.1', port=7680, log_level='info')

def main():
    app()

if __name__ == '__main__':
    main()
    
