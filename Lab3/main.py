from pydantic import BaseModel
from fastapi import FastAPI
import pymysql.cursors

app = FastAPI()

connection = pymysql.connect(
    host='127.0.0.1',
    port=3301,
    user='root',
    password='',
    database=search_db,
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

@app.post("/create_table_book")
def create_table_book():
    with connection.cursor() as cursor:
        sql =""""""
        cursor.execute(sql)
    connection.commit()


class Book(BaseModel):
    int: int
    name: str


@app.post("/insert_to_book")
def insert_to_book(item: Book):
    pass


@app.put("/update_book/{id}")
def insert_to_book(id):
    pass


@app.delete("/delete_book/{id}")
def delete_book(id):
    pass
