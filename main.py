# main.py

from fastapi import FastAPI, HTTPException, Body, Query
from pymongo import MongoClient
from bson import ObjectId
import random
import string

app = FastAPI()

# Connect to MongoDB Atlas M0 cluster
try:
    client = MongoClient("mongodb+srv://ahmad:ahmad1000@cluster0.sr2nhsw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    db = client["library_db"]
    students_collection = db["students"]
    books_collection = db["books"]
except Exception as e:
    print("Failed to connect to MongoDB:", e)

# Define root endpoint
@app.get("/", status_code=200)
async def root():
    """
    Welcome message for the API.
    """
    return {"message": "Welcome to the Library Management System API!"}

# Student endpoints

@app.post("/students", status_code=201)
async def create_student(student: dict = Body(...)):
    """
    Create a new student.
    """
    try:
        # Validate input data before insertion
        if "name" not in student or "age" not in student:
            raise HTTPException(status_code=400, detail="Name and age are required fields.")
        if not isinstance(student["age"], int):
            raise HTTPException(status_code=400, detail="Age must be an integer.")
        
        result = students_collection.insert_one(student)
        return {"id": str(result.inserted_id)}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to create student: " + str(e))

@app.get("/students", status_code=200)
async def list_students(country: str = Query(None, description="To apply filter of country."), 
                        age: int = Query(None, description="Only records which have age greater than equal to the provided age should be present in the result.")):
    """
    List all students.
    """
    try:
        query = {}
        if country:
            query["address.country"] = country
        if age:
            query["age"] = {"$gte": age}

        students = students_collection.find(query, {"_id": 0})
        formatted_students = []

        for student in students:
            formatted_student = {
                "student_id": str(student.get("_id")),  # Assuming you have an _id field for each student
                "name": student.get("name"),
                "age": student.get("age"),
                "address": student.get("address"),
                "library_card_number": student.get("library_card_number", ""),  # Add library card number if available
                "books_borrowed": []  # Initialize an empty list for books borrowed
            }
            formatted_students.append(formatted_student)

        return {"students": formatted_students}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to list students: " + str(e))

# Book endpoints

@app.post("/books", status_code=201)
async def create_book(book: dict = Body(...)):
    """
    Create a new book.
    """
    try:
        # Validate input data before insertion
        if "title" not in book or "author" not in book:
            raise HTTPException(status_code=400, detail="Title and author are required fields.")
        
        result = books_collection.insert_one(book)
        return {"id": str(result.inserted_id)}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to create book: " + str(e))

@app.get("/books", status_code=200)
async def list_books():
    """
    List all books.
    """
    try:
        books = books_collection.find({}, {"_id": 0})
        return {"books": list(books)}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to list books: " + str(e))
