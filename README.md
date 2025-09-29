Create a honeypot that simulates vulnerable services (like SSH or HTTP) to attract and log attacker behavior.

- Why? This teaches you attacker tactics and builds skills in network security and monitoring.


Create requirements.txt with Flask, paramiko, cryptography
Create requirements.txt with Flask, paramiko, cryptography
 Create ssh_honeypot.py: Paramiko-based SSH server on port 22, logs auth attempts
 Create http_honeypot.py: Flask app on port 80 with login page logging credentials
 Create https_honeypot.py: Flask app on port 443 with SSL, login page logging credentials
 Generate self-signed SSL certificate for HTTPS
 Create honeypot.py: Main script to start all services in threads
 Update logging to append to log.txt
 Test the honeypot (run and check logs)