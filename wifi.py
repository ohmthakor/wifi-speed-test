import speedtest


def bytes_to_mb(bytes):
    KB = 1024
    MB = KB * 1024
    return int(bytes/MB)

st = speedtest.Speedtest()

start = input("Click Enter to Start")
down_speed = str(bytes_to_mb(st.download()))
up_speed = str(bytes_to_mb(st.upload()))
ping = str(st.results.ping)

print('download: ' + down_speed + 'mb/s')
print('upload: ' + up_speed + 'mb/s')
print('ping: ' + ping)