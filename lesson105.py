import requests
import re

class WebCrawler:

    def __init__(self):
        # We want to avoid revisiting the same website over and over again
        self.discovered_websites = []

