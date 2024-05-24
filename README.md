# wifi-speed-test
This project contains a Python script that measures your internet download speed, upload speed, and ping using the `speedtest-cli` library. The results are displayed in a user-friendly format.

## Features
- Measure download speed
- Measure upload speed
- Measure ping latency
- User-friendly interface

## Technologies Used
- **Backend:** Python, Flask, speedtest-cli
- **Frontend:** HTML, CSS, JavaScript

## Installation
To get a local copy up and running, follow these steps:

### Prerequisites
- Python 3.x
- pip (Python package installer)

### Setup

1. **Clone the repository:**
    ```bash
    git clone https://github.com/ohmthakor/wifi-speed-test.git
    cd wifi-speed-test
    ```

2. **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the application:**
    ```bash
    python app.py
    ```

5. **Open your browser and go to:**
    ```
    http://127.0.0.1:5000
    ```

## Usage
Click the "Start Speed Test" button to begin testing your WiFi speed. The results for download speed, upload speed, and ping will be displayed on the screen.

