import requests
import random
import string

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
        "street": "123 Main Street",
        "city": "Anytown",
        "country": "USA"
    }
}

# Make a POST request to create a new student
response = requests.post(url, json=student_data)

# Print the response status code and body
print("Status code:", response.status_code)
print("Response body:", response.json())
