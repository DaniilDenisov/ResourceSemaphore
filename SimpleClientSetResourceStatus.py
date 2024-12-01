import requests
import json

# URL of the Flask semaphore service
url = 'http://localhost:5000/resource/1/status'


# Function to set the resource to "busy"
def set_resource_busy():
    data = {"status": "busy"}

    try:
        response = requests.post(url, json=data)

        # Check if the service responded with a successful status code
        if response.status_code == 200:
            print(f"Resource is now busy: {response.json()}")
        else:
            print(f"Failed to set resource busy: {response.status_code}, {response.text}")

    except requests.exceptions.ConnectionError:
        print("Failed to connect to the server. The service might not be running.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


# Test the client
set_resource_busy()  # Set the resource to "busy"
