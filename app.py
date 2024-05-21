from flask import Flask, jsonify, render_template
import speedtest # type: ignore

app = Flask(__name__)

def bytes_to_mb(bytes):
    KB = 1024
    MB = KB * 1024
    return int(bytes / MB)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/speedtest')
def run_speedtest():
    st = speedtest.Speedtest()
    st.download()
    st.upload()
    ping = st.results.ping
    down_speed = bytes_to_mb(st.results.download)
    up_speed = bytes_to_mb(st.results.upload)
    return jsonify(download=f"{down_speed} Mb/s", upload=f"{up_speed} Mb/s", ping=f"{ping} ms")

if __name__ == '__main__':
    app.run(debug=True)
