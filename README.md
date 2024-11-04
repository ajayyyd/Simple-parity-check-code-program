# Sender-Receiver Parity Check Program

This project demonstrates a simple client-server program in Python to send an integer number from one computer to another on the same network with basic error detection using a parity bit. The sender calculates the parity bit of the number and sends both the number and the parity bit to the receiver. The receiver checks the parity to confirm data integrity.

## Features
- **Single Integer Transmission**: The sender can transmit any integer number.
- **Parity Check**: Adds a parity bit to detect errors in data transmission.
- **Client-Server Communication**: Uses Python’s `socket` library for network communication.

## Requirements
- Python 3.x installed on both devices.
- Both devices (PC and Laptop) must be connected to the same network.
- Firewall permissions for the selected port (default: 12345) if needed.

## Files
- **sender.py**: The sender script that allows the user to input a number, calculate its parity bit, and send both to the receiver.
- **receiver.py**: The receiver script that listens for incoming data, extracts the number and parity bit, and verifies the parity.

## Usage

### Step 1: Clone the Repository
  - **git clone https://github.com/your-username/sender-receiver-parity-check.git
  - **cd sender-receiver-parity-check

## Step 2: Set Up the Receiver (on the Laptop)
Open a terminal on the laptop.

Run the receiver script:

bash
Copy code
python receiver.py
The receiver will start listening on port 12345 for incoming data.

## Step 3: Set Up the Sender (on the PC)
Open a terminal on the PC.

Run the sender script:

bash
Copy code
python sender.py
Enter any integer number to send to the receiver. The sender will calculate the parity bit and transmit both the number and the parity bit.

Example
Sender (PC) Input:

sql
Copy code
Enter any integer to send: 12345
Receiver (Laptop) Output:

vbnet
Copy code
Connected to ('sender_ip_address', 12345)
Received message: 12345
Data received correctly with matching parity.
Project Structure
bash
Copy code
sender-receiver-parity-check/
├── sender.py       # Script to send a number with a parity bit
├── receiver.py     # Script to receive the number and verify the parity
└── README.md       # Project documentation
## How It Works
- **Sender: Accepts an integer input from the user, calculates its parity bit, and sends both the number and parity to the receiver.
- **Receiver: Listens for incoming data, separates the number and the parity bit, calculates the expected parity, and verifies it against the received parity.
Future Improvements
- **Add support for more data types.
-** Implement additional error detection mechanisms.
- **Add a graphical interface to make the tool easier to use.
