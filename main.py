from fastapi import FastAPI
from model import nases_model
from starlette.middleware.cors import CORSMiddleware
import postprocessing

#from database import database as connection

from schemas import Article

app = FastAPI(title='NN',
              description= '',
              version ='1.0')

origins = [
    'http://localhost:3000'
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get('/')
async def index():
    return 'Hola mundo'

@app.post('/', description="Genera un resumen a partir de blablablalbla")
async def  create_summary(article:Article):
    resumen = nases_model.generate_summary(article.new)
    resumen = postprocessing.remove_tags(resumen)
    return resumen

 

 


