
import requests
from bs4 import BeautifulSoup
import pandas as pd
import landtags_urls as urls
from datetime import datetime


class WikifetcherLandtag:

    def __init__(self):
        self.r = requests.get(urls.sachsenUrl).content
        self.get_politicians_landtag_sachsen()
