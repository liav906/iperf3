import iperf3
import time

# Create an iperf server instance
server = iperf3.Server()

# Bind the server to port 5000
server.bind_address = ('0.0.0.0', 5000)

# Start the server
server.daemonize()

print("Server listening on port 5000...")

while True:
    # Wait for a client to connect
    client = server.accept()
    
    # Get the bandwidth information
    result = client.results
    sender_bandwidth = result.sent_bps / 1e6  # Convert to Mbps
    receiver_bandwidth = result.received_bps / 1e6  # Convert to Mbps
    
    print(f"Sender bandwidth: {sender_bandwidth:.2f} Mbps")
    print(f"Receiver bandwidth: {receiver_bandwidth:.2f} Mbps")
    
    # Close the client connection
    client.close()

    # Sleep for a while before accepting the next client
    time.sleep(1)
