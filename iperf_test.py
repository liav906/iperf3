import iperf3

# Create an iperf client instance
client = iperf3.Client()

# Set the server's IP and port
client.server_hostname = '172.20.10.4'  # Replace with your server's IP address
client.port = 5000

# Set the number of iterations
iterations = 10

total_sender_bandwidth = 0
total_receiver_bandwidth = 0

for _ in range(iterations):
    # Run the iperf test
    result = client.run()
    
    sender_bandwidth = result.sent_bps / 1e6  # Convert to Mbps
    receiver_bandwidth = result.received_bps / 1e6  # Convert to Mbps
    
    print(f"Sender bandwidth: {sender_bandwidth:.2f} Mbps")
    print(f"Receiver bandwidth: {receiver_bandwidth:.2f} Mbps")
    
    total_sender_bandwidth += sender_bandwidth
    total_receiver_bandwidth += receiver_bandwidth

# Calculate the sums
print("\nTotal Sender Bandwidth:", total_sender_bandwidth, "Mbps")
print("Total Receiver Bandwidth:", total_receiver_bandwidth, "Mbps")
