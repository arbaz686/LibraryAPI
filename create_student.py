# create_student.py

import requests

# Define the URL for the endpoint
url = 'http://127.0.0.1:8000/students'

# Generate a random name
def random_name():
    return ''.join(random.choice(string.ascii_letters) for _ in range(10))

# Generate a random age between 18 and 25
def random_age():
    return random.randint(18, 25)

# Define the student data to send in the request body
student_data = {
    "name": random_name(),
    "age": random_age(),
    "address": {
        "city": "New York",
        "country": "USA"
    }
}

# Send a POST request to create a new student
response = requests.post(url, json=student_data)

# Check the response status code and content
print('Response status code:', response.status_code)
print('Response content:', response.json())
