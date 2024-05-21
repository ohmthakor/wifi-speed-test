function runSpeedTest() {
    fetch('/speedtest')
        .then(response => response.json())
        .then(data => {
            document.getElementById('download').textContent = 'Download speed: ' + data.download;
            document.getElementById('upload').textContent = 'Upload speed: ' + data.upload;
            document.getElementById('ping').textContent = 'Ping: ' + data.ping;
        })
        .catch(error => console.error('Error:', error));
}
