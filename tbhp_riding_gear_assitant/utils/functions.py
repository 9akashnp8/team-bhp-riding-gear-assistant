from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def get_page_source(url: str) -> str:
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