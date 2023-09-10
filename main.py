import speedtest
import time
import json

st = speedtest.Speedtest()
results = []

st.get_best_server()

i, down, up = 0, [], []

while i < 5:
    print(f'test number {i+1} started..')

    download_speed = st.download()
    upload_speed = st.upload()
    
    download_speed_mbps = download_speed / 10**6
    upload_speed_mbps = upload_speed / 10**6
    
    down.append(download_speed_mbps)
    up.append(upload_speed_mbps)

    results.append({
        'download_speed': download_speed,
        'upload_speed': upload_speed,
        'download_speed_mbps': download_speed_mbps,
        'upload_speed_mbps': up_speed_mbps
    })

    print(f"Download speed: {download_speed_mbps:.2f} Mbps")
    print(f"Upload speed: {upload_speed_mbps:.2f} Mbps")

    print(f'test number {i+1} ended..')

    i =  i + 1

print(f'Avg Download speed -> {sum(down)/len(down)} mbps')
print(f'Avg Upload speed -> {sum(up)/len(up)} mbps')

print('saving results....')

with open('results.json', 'w') as file:
    file.write(json.dumps(results))
print('resutls saved in `results.json`')
