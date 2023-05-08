from core.comments_loader import TBHPCommentsLoader
from utils.functions import create_embeddings

loader = TBHPCommentsLoader().get_instance()
docs = loader.get_comment_documents(n=10)
create_embeddings(docs=docs)