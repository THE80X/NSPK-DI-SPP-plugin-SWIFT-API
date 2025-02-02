from selenium import webdriver
from swift_api import SWIFTAPIParser
from s3p_sdk.types import S3PDocument, S3PRefer


def driver():
    """
    Selenium web driver
    """
    options = webdriver.EdgeOptions()

    # Параметр для того, чтобы браузер не открывался.
    # options.add_argument('headless')
    #
    # options.add_argument('window-size=1920x1080')
    # options.add_argument("disable-gpu")
    # options.add_argument('--start-maximized')
    # options.add_argument('disable_infobars')

    return webdriver.Edge(options)


url = 'https://developer.swift.com/apis'


parser = SWIFTAPIParser(driver=driver(), url=url, refer=S3PRefer(name='SWIFT API', id=0, type=None, loaded=None))
docs: list[S3PDocument] = parser.content()

print(*docs, sep='\n\r\n')
