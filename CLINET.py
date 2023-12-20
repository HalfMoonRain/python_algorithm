import socket

def test_client(host='127.0.0.1', port=6000, num_tests=3):
    received_data = []

    for i in range(num_tests):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))
            message = f"Test message {i+1}"
            s.sendall(message.encode())
            data = s.recv(1024).decode()
            received_data.append(data)
            print(f"Received from server (Test {i+1}): {data}")

    if all(datum == received_data[0] for datum in received_data):
        print("All tests received the same data.")
    else:
        print("Different data received in different tests.")

if __name__ == "__main__":
    test_client()
