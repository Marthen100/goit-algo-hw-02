import queue
import random
import time

# Create a queue of applications
requests_queue = queue.Queue()

# The generate_request() function
def generate_request():
    # Create a new request with a unique number
    request_id = random.randint(1, 1000)
    print(f"Generated request: {request_id}")
    # Add the request to the queue
    requests_queue.put(request_id)

# Function process_request()
def process_request():
    # If the queue is not empty
    if not requests_queue.empty():
        # Remove a request from the queue
        request_id = requests_queue.get()
        # Process the request
        print(f"Processing request: {request_id}")
    else:
        # Display a message that the queue is empty
        print("The queue is empty")

# The main cycle of the program 
try:
    while True:
        # Execute generate_request() to create new requests
        generate_request()
        # Execute process_request() to process requests
        process_request()
        # Simulate some delay between operations
        time.sleep(1)

except KeyboardInterrupt:
    print("Exiting the application.")