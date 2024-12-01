from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# In-memory dictionary to store resource statuses
resources = {}


# Serve the HTML page for the Resource Status Manager
@app.route('/')
def index():
    return render_template('ClientSetGetAutoUpdate.html')


# Set the status of a resource (free or busy)
@app.route('/resource/<resource_id>/status', methods=['POST'])
def set_resource_status(resource_id):
    status = request.json.get('status')

    if status not in ['free', 'busy']:
        return jsonify({"error": "Invalid status. Use 'free' or 'busy'."}), 400

    resources[resource_id] = status
    return jsonify({"message": f"Resource {resource_id} is now {status}."})


# Get the current status of a resource
@app.route('/resource/<resource_id>/status', methods=['GET'])
def get_resource_status(resource_id):
    status = resources.get(resource_id, 'unknown')
    return jsonify({"resource_id": resource_id, "status": status})


if __name__ == '__main__':
    app.run(debug=True)
