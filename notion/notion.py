import os
import requests

class Notion(object):
    def __init__(self) -> None:
        self.secret_token = os.getenv("NOTION_SECRET")
        self.version = os.getenv("NOTION_VERSION")
        self.base_url = "https://api.notion.com/v1/"
        self.headers = {
            "Authorization": self.secret_token,
            "Notion-Version": self.version
        }
        
    def get_db(self) -> object:
        return {}
        