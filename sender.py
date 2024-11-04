import socket

def calculate_parity_bit(number):
    # Count the number of 1s in the binary representation of the number
    binary_representation = bin(number)[2:]  # convert to binary and strip the '0b' prefix
    ones_count = binary_representation.count('1')
    # Return 0 if count of 1s is even, else return 1 for odd
    return 0 if ones_count % 2 == 0 else 1

def main():
    # Set up the socket
    host = '192.168.1.33'  # replace with your laptop's IP
    port = 12345
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    
    # Ask the user to input a one-digit number
    number = int(input("Enter a number to send: "))
    # if number < 0 or number > 9:
    #     print("Please enter a one-digit number only!")
    #     return

    # Calculate the parity bit and prepare the data to send
    parity_bit = calculate_parity_bit(number)
    data = f"{number}{parity_bit}"
    print(f"Sending data with parity bit: {data}")
    
    # Send the data
    sock.sendall(data.encode())
    sock.close()

if __name__ == "__main__":
    main()
