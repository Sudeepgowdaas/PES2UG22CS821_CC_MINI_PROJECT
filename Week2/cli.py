import etcd3
import grpc

# Define etcd connection
client = etcd3.client(host='localhost', port=2379)

def list_all_keys():
    keys = []
    for key, _ in client.get_all():
        keys.append(key.decode())
    return keys

def get_value_for_key(key):
    value, _ = client.get(key)
    if value is not None:
        return value.decode()
    else:
        return None

def put_key_value():
    key = input("Enter key: ")
    value = input("Enter value: ")
    try:
        client.put(key, value)
        print(f"Key '{key}' with value '{value}' has been successfully put into etcd.")
    except grpc.RpcError as e:
        print(f"Error: {e.details()}")

def delete_key():
    key = input("Enter key to delete: ")
    try:
        client.delete(key)
        print(f"Key '{key}' has been successfully deleted from etcd.")
    except KeyError:
        print(f"Key '{key}' not found.")
    except grpc.RpcError as e:
        print(f"Error: {e.details()}")

def get_value():
    key = input("Enter key to get value: ")
    try:
        value, _ = client.get(key)
        if value is not None:
            print(f"Value for key '{key}': {value.decode()}")
        else:
            print("Key not found.")
    except grpc.RpcError as e:
        print(f"Error: {e.details()}")

def show_menu():
    print("Options:")
    print("1. Put key-value")
    print("2. Get value for key")
    print("3. Delete key")
    print("4. List all keys")
    print("5. Exit")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            put_key_value()
        elif choice == "2":
            get_value()
        elif choice == "3":
            delete_key()
        elif choice == "4":
            print("All keys: ", list_all_keys())
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
