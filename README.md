# ResourceSemaphore
Simple REST API to get informed on the resource is used or awaiting for connections.
* This is used for individually offered resources which can be blocked when used
from different IP simultaneously.
* Simple service helps share the status if the resource is busy or free to use. The
service can also be used by the browser extension to automate checks if the resource
access is browser based.

How to use:

01. Server should be started for client code to work and requests are services.
    Start the service by activating venv and running:
    cd <ResourceSemafore folder>
    venv\Scripts\activate
    python.exe ResourceSemaphoreService.py
02. Go to client page:
    http://127.0.0.1:5000/
    This is an index page and it's template (html) can be found in templates folder.
03. You can also set and get status for resource with the given 'id'.
    Run following scripts for these actions:
    python.exe SimpleClientSetResourceStatus.py
    python.exe SimpleClientGetResourceStatus.py

04. test_ResourceSemaphoreService.py uses server imitation (FlaskClient) from Flask to run
requests to API. This eliminates the need for running server in separate process.