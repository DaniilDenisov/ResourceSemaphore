import requests
import json

# URL of the Flask semaphore service
url = 'http://localhost:5000/resource/1/status'


# Function to query the resource status
def get_resource_status():
    try:
        response = requests.get(url)

        # Check if the service responded with a successful status code
        if response.status_code == 200:
            status = response.json().get("status")
            print(f"Resource status: {status}")
        else:
            print(f"Failed to get resource status: {response.status_code}, {response.text}")

    except requests.exceptions.ConnectionError:
        print("Failed to connect to the server. The service might not be running.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


# Call the client
get_resource_status()  # Query the current status
