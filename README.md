## Library Management System API

This API serves as a backend system for managing a library, including functionalities for handling students and books. It utilizes FastAPI framework for building RESTful APIs and MongoDB as the database.

### Requirements
- FastAPI==0.68.0
- uvicorn==0.15.0
- pymongo[srv]==3.12.0
- requests==2.26.0

### Usage

#### Setting Up

1. Clone this repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Ensure you have MongoDB Atlas M0 cluster set up with necessary configurations.

#### Running the Server

Run the following command to start the server:
```bash
uvicorn main:app --reload
```
This command will start the FastAPI server, and you can access the API at `https://fastapi-sr95.onrender.com/`.

#### Endpoints

##### Root Endpoint

- `GET /`: Returns a welcome message for the API.

##### Student Endpoints

- `POST /students`: Creates a new student. Requires a JSON body with `name`, `age`, and `address` fields.
- `GET /students`: Lists all students. Supports optional query parameters like `country` and `age` for filtering students.

##### Book Endpoints

- `POST /books`: Creates a new book. Requires a JSON body with `title` and `author` fields.
- `GET /books`: Lists all books.

### Additional Scripts

#### `create_student.py`

This script sends a POST request to the `/students` endpoint to create a new student with random name, age, and address. You can run this script to test the API functionality.

#### MongoDB Connection

The API connects to a MongoDB Atlas M0 cluster for data storage. Ensure the MongoDB URI is correctly configured in the `main.py` file.

### Notes

- Sample books are added to the database upon initialization.
- Students are assigned random library card numbers and may have random books borrowed from the available book collection.

### Contributors
- Arbaz Ahmad: [GitHub](https://github.com/arbaz686)

Feel free to contribute by submitting pull requests or opening issues for any improvements or bugs found.
