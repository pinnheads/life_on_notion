import os

from notion.databases import Databases


class Todo(Databases):
    def __init__(self) -> None:
        self.id = os.getenv("TODO_DB_ID")
        Databases.__init__(self, self.id)
        self.this_week_filter = {
            "filter": {
                "and": [
                    {
                        "property": "Due",
                        "date": {
                            "is_not_empty": True
                        }
                    },
                    {
                        "property": "Due",
                        "date": {
                            "this_week": {}
                        }
                    }
                ]
            }
        }
        
    def get_this_week_tasks(self) -> list:
        return self.query_db(self.this_week_filter).json()["results"]
    
    def prettify_week_tasks(self) -> None:
        # get this week tasks and based on the 'label' put emojis and time
        # write a function to randomize the emoji selection
        pass