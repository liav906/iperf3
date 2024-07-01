# Open the file for reading
with open('/Users/liav/PycharmProjects/iperf_tests/iperf_results.txt', 'r') as file:
    lines = file.readlines()

# Initialize variables to store the values

last_line = lines[-1]
second_last_line = lines[-2]

value = last_line.split()
receiver_value = value[-3]
value = second_last_line.split()
sender_value = value[-3]


# Print the extracted values
print("Sender Value:", sender_value)
print("Receiver Value:", receiver_value)
