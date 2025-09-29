import threading
import time
import logging

# Import the honeypot modules
from ssh_honeypot import start_ssh_honeypot
from http_honeypot import app as http_app
from https_honeypot import app as https_app

# Set up logging
logging.basicConfig(filename='log.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

def start_http():
    logging.info("Starting HTTP honeypot on port 80")
    http_app.run(host='0.0.0.0', port=80, debug=False, use_reloader=False)

def start_https():
    logging.info("Starting HTTPS honeypot on port 443")
    https_app.run(host='0.0.0.0', port=443, ssl_context=('cert.pem', 'key.pem'), debug=False, use_reloader=False)

if __name__ == '__main__':
    logging.info("Starting Honeypot Services")

    # Start SSH in a thread
    ssh_thread = threading.Thread(target=start_ssh_honeypot)
    ssh_thread.start()

    # Start HTTP in a thread
    http_thread = threading.Thread(target=start_http)
    http_thread.start()

    # Start HTTPS in a thread
    https_thread = threading.Thread(target=start_https)
    https_thread.start()

    # Keep main thread alive
    while True:
        time.sleep(1)
