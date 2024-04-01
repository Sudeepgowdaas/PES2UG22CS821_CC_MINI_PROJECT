from flask import Flask, render_template, request, redirect, url_for
import etcd3
import grpc

app = Flask(__name__)

# Define etcd connection
client = etcd3.client(host='localhost', port=2379)

# Function to list all keys in etcd
def list_all_keys():
    try:
        keys = []
        for key, _ in client.get_all():
            keys.append(key.decode())
        return keys
    except grpc.RpcError as e:
        print("Error listing all keys:", e)
        return []

# Function to get value for a given key
def get_value_for_key(key):
    value, _ = client.get(key)
    if value is not None:
        return value.decode()
    else:
        return None

# Function to put key-value pair into etcd
def put_key_value(key, value):
    try:
        client.put(key, value)
        return True
    except grpc.RpcError as e:
        print("Error putting key-value:", e)
        return False

# Function to delete a key from etcd
def delete_key(key):
    try:
        client.delete(key)
        return True
    except KeyError:
        return False
    except grpc.RpcError:
        return False

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html', keys=list_all_keys())

# Route for putting key-value pair
@app.route('/put', methods=['POST'])
def put():
    key = request.form['key']
    value = request.form['value']
    if put_key_value(key, value):
        return redirect(url_for('index'))
    else:
        return "Error putting key-value into etcd."

# Route for getting value for a given key
@app.route('/get_value', methods=['POST'])
def get():
    key = request.form['key']
    value = get_value_for_key(key)
    if value is not None:
        keys = list_all_keys()  # Retrieve all keys
        return render_template('index.html', value=value,keys=keys)
    else:
        return "Key not found."

# Route for deleting a key
@app.route('/delete', methods=['POST'])
def delete():
    key = request.form['key']
    if delete_key(key):
        return redirect(url_for('index'))
    else:
        return "Error deleting key from etcd."

if __name__ == '__main__':
    app.run(debug=True) 
