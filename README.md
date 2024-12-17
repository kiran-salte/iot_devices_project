<<<<<<< HEAD
#Device Payload status
This Django project provides an API to receive payloads from IoT devices, process the payloads, and store the data in a relational database. The system ensures that duplicate payloads with the same 'fCnt' are not stored for the same device and includes functionality for decoding Base64 payload data to hexadecimal format.


### Prerequisites
- Python 3.8+
- Django 3.2+
- PostgreSQL or SQLite (default)

#1. Clone the repository
Clone this repository to your local machine:
cmd: git clone https://github.com/kiran-salte/iot-devices.git
cd iot-devices

#2. Create a virtual environment
Create and activate a virtual environment:
cmd python3 -m venv venv
source venv/bin/activate


#4.Install the required packages:
cmd: pip3 install -r requirements.txt

#4. Setup Database
Make sure you have a database configured (SQLite is used by default). Run the migrations:
cmd: python3 manage.py migrate


#5. Create a superuser (for Django Admin access)
If you want to access the Django Admin interface, create a superuser:
cmd: python3 manage.py createsuperuser


#6. Run the application
Start the development server:
cmd: python3 manage.py runserver


Your application will be accessible at 'http://127.0.0.1:8000/'

#7. API Endpoints
#7.1
- endpoint: '/devices/'
- method: 'GET'
- Description: Retrieves a list of all devices with their payloads.

#7.22.
- endpoint : '/payloads/'
- method: 'POST'
- Description: Submit a payload for a device.
=======
# iot_devices_project
Django Project for Creating Devices and maintaining the payload for IOT Devices 
>>>>>>> 913ea5f3db05ac9fa7e3991b438c89a277e10d9b
