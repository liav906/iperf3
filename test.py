import subprocess
import time

# Define the command to start the iperf3 server
iperf_server_command = ["iperf3", "-s", "-p", "5001"]

try:
    # Start the iperf3 server as a subprocess
    iperf_server_process = subprocess.Popen(iperf_server_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Allow some time for the server to start
    time.sleep(2)

    # Set the maximum duration for the server to run (in seconds)
    max_duration = 45  # Adjust as needed

    start_time = time.time()

    while True:
        # Check if the server process is still running
        if iperf_server_process.poll() is not None:
            # Server process has finished
            print("iperf3 server has finished.")
            break

        # Check if the maximum duration has been reached
        if time.time() - start_time >= max_duration:
            # Terminate the server process
            iperf_server_process.terinate()
            print("iperf3 server has been terminated due to reaching the maximum duration.")
            break

        # Sleep for a while before checking again
        time.sleep(1)

    # Save the bandwidth results to a file
    with open("iperf_results.txt", "w") as result_file:
        result_file.write(iperf_server_process.stdout.read())

except FileNotFoundError:
    print("iperf3 command not found. Please make sure it is installed and in your PATH.")
except Exception as e:
    print(f"An error occurred: {str(e)}")
