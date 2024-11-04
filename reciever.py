import socket

def calculate_parity_bit(number):
    # Count the number of 1s in the binary representation of the number
    binary_representation = bin(number)[2:]  # Convert to binary and strip the '0b' prefix
    ones_count = binary_representation.count('1')
    # Return 0 if count of 1s is even, else return 1 for odd
    return 0 if ones_count % 2 == 0 else 1

def main():
    # Set up the socket
    host = '0.0.0.0'  # Listen on all available interfaces
    port = 12345
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))
    sock.listen(1)
    print("Waiting for a connection...")

    connection, client_address = sock.accept()
    print(f"Connected to {client_address}")

    # Receive data
    data = connection.recv(1024).decode()
    if data:
        found = False  # Flag to indicate if we found a match
        for i in range(3, 10):  # Loop from 3 to 9
            if len(str(data)) == i:
                received_number = int(data[0:i-1])  # Extract the number
                received_parity = int(data[-1])      # Extract the parity bit
                found = True  # Set the flag to true
                break  # Exit the loop after processing

        if not found:
            print("Data length not valid.")
        else:
            # Verify the parity
            calculated_parity = calculate_parity_bit(received_number)
            if calculated_parity == received_parity:
                print("Received Data: ", received_number)
                print("Parity Bit: ", received_parity)
                print("Data received correctly with matching parity.")
            else:
                print("Received Data: ", received_number)
                print("Parity Bit: ", received_parity)
                print("Error detected in received data.")

    connection.close()

if __name__ == "__main__":
    main()