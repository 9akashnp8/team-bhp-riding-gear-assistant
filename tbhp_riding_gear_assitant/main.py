from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class Main():
    __instance = None

    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = Main()
        return cls.__instance
        
    def get_page_source(self, url: str) -> str:
        """extracts the html sources from the page
        of the give url

        Args:
            url (str): url of the page whose source
                is required

        Returns:
            str: html string of the page
        """
        service = Service(executable_path=ChromeDriverManager().install())
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.get(url)
        return driver.page_source

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

    def get_all_comments(self, n: int) -> "list[str]":
        """get all comments from 1st to nth page number.

        Args:
            n (int): number of pages to extract comments
                from (starting from 1)

        Returns:
            list[str]: a list of all comments made
        """
        all_comments = []
        for i in range(1, n+1):
            page_source = self.get_page_source(f'https://www.team-bhp.com/forum/ride-safe/42000-riding-gear-thread-{i}.html')
            page_comments = self.get_comments_from_page(page_source=page_source)
            all_comments.extend(page_comments)
        return all_comments