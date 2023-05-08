from bs4 import BeautifulSoup
from langchain.schema import Document

from .utils.functions import get_page_source

class TBHPCommentsLoader():
    """
    Custom 'Document Loader' to extract comments
    from TBHP Riding Gear thread for indexing
    via langchain's VectorstoreIndexCreator
    """
    __instance = None

    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = TBHPCommentsLoader()
        return cls.__instance

    def get_comments_from_page(self, page_source: str) -> "list[str]":
        """extracts all the comments from a give teambhp page.
        how: all comments are located inside the td element
        containing the class "mod2022-postbit-messagearea"

        Args:
            page_source (str): html data from which comments to
                extract

        Returns:
            list[str]: a list of all the comments made.
        """
        soup = BeautifulSoup(page_source, 'html.parser')
        comments = soup.find_all('td', {'class': 'mod2022-postbit-messagearea'})
        return [comment.text for comment in comments]

    def get_comment_documents(self, n: int) -> "list[str]":
        """create Document objects for indexing via VectorstoreIndexCreator.

        Args:
            n (int): number of pages to extract comments
                from (starting from 1)

        Returns:
            list[str]: a list of all comments made
        """
        docs = []
        for i in range(1, n+1):
            page_source = get_page_source(
                f'https://www.team-bhp.com/forum/ride-safe/42000-riding-gear-thread-{i}.html'
            )
            page_comments = self.get_comments_from_page(page_source=page_source)
            comment_documents = [
                Document(page_content=comment, metadata={"index": index})
                for index, comment in enumerate(page_comments)
            ]
            docs.extend(comment_documents)
        return docs