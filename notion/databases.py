import requests

from requests import Response
from notion.notion import Notion


class Databases(Notion):
    def __init__(self, db_id: str) -> None:
        Notion.__init__(self)
        self.db_id = db_id
        self.database_url = self.base_url + f"databases/{self.id}"
        
    def _get_db(self) -> Response:
        """Retrieve a database

        Returns:
            Response: Returns a database object from notion
        """
        return requests.get(url=self.database_url, headers=self.headers)
    
    def _query_db(self, filter: dict) -> Response:
        """Query a database

        Args:
            filter (dict): A dictionary object that has the filter to retrieve a certain number of records

        Returns:
            Response: Returns the response from the query
        """
        return requests.post(url=self.database_url+"/query", headers=self.headers, json=filter)
        