from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from model import nases_model
from schemas import Article
import postprocessing
import logging

logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s')


app = FastAPI(
    title='NN',
    description='''National News Summarizer API
    
    This API provides text summarization capabilities using the NASES model.
    It can generate concise summaries from longer articles or text content.
    ''',
    version='1.0',
    docs_url='/docs',
    redoc_url='/redoc'
)

# CORS configuration
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

@app.get('/', summary="Root Endpoint", response_model=str)
async def index() -> str:
    """
    Root endpoint to check if the API is running.
    """
    return 'Hola mundo'


@app.post(
    '/',
    summary="Generate Summary",
    description=''' 
    Generates a summary from the provided article text.
    
     - **text**: The article content to be summarized
     - Returns a concise summary of the input text
    
     Example:
     ```json
     {
        "text": "This is a long article about artificial intelligence..."
     }
     ```  
    ''',
    response_model=str
)
async def create_summary(article: Article) -> str:
    """
        Generate a summary for the given article.
    
    Args:
        article (Article): The article to summarize
        
    Returns:
        str: The generated summary
        
    Raises:
        HTTPException: If there's an error during summary generation
    """
    try:
        summary = nases_model.generate_summary(article.text)
        summary = postprocessing.remove_tags(summary)
        return summary
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

