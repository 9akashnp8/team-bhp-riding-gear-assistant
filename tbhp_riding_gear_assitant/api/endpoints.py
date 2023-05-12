from fastapi import APIRouter
from langchain.llms import OpenAI

from api.models import Query
from core.comments_loader import TBHPCommentsLoader
from core.prompts import prompt_template
from utils.functions import create_embeddings, query_db

router = APIRouter()
llm = OpenAI(max_tokens=-1)

@router.get('/create-embeddings')
def generate_embeddings(n_page: int):
    """
    create embeddings of the comments from page 1
    to n_page of the "TBHP Riding Gear" Thread
    """
    loader = TBHPCommentsLoader().get_instance()
    docs = loader.get_comment_documents(n=n_page)
    create_embeddings(docs=docs)
    return {"message": "embeddings created successfuly"}

@router.post('/query')
def ask_query(payload: Query):
    """
    core endpoint that takes query from user, queries
    context via similarity search and passes the result(s)
    along with the question to OpenAI.

    Args:
        payload (Query): a JSON object with "query" key
        containing the actual user query
    """
    query = payload.query
    context = query_db(query=query)
    prompt = prompt_template.format(context=" ".join(context), question=query)
    return {"response": llm(prompt)}