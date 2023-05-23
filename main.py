from dotenv import load_dotenv

from notion.todo import Todo

load_dotenv()  # take environment variables from .env.
todo = Todo()

print(todo.get_this_week_tasks())