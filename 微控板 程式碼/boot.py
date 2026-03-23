from umqtt.simple import MQTTClient
import network, time, utime
import json
import _thread
import task
import oled
# 第一個 Wi-Fi 網路的 SSID 和密碼

ssid = '11146081'       
password = '11146081'
# 連接到指定的 Wi-Fi

wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(ssid, password)

# 等待連接
print(f'Connecting to {ssid}...')
start_time = time.time()
while not wifi.isconnected():
    time.sleep(1)

print(f"Connected to {ssid}!")
print('IP Address:', wifi.ifconfig()[0])


mq_server = "broker.mqttgo.io"
mq_id = "mqsub_abcdef"
mq_topic = "11146081/music"
 

def on_message(topic, payload):
    u_topic = topic.decode("utf-8")
    u_payload = payload.decode("utf-8")
    if u_payload[:6] == '{"id":':
        
        data = json.loads(u_payload)

        frequency_str = data['frequency']

        notes = frequency_str.split(',')
 
        melody = [(int(note.split(':')[0]), float(note.split(':')[1])) for note in notes]
        total_time=int(sum([i[1] for i in melody]))

        _thread.start_new_thread(task.play_melody,(melody,data["duty"]))
        
        _thread.start_new_thread(task.begin_countdown, (total_time,))
        
        
        oled.display_song(data['name'])
        
mqClient = MQTTClient(mq_id, mq_server)
mqClient.set_callback(on_message)
mqClient.connect()
mqClient.subscribe(mq_topic)
print("Subscribed Topic: {}".format(mq_topic))
            

while True:
    mqClient.check_msg()     
    utime.sleep_ms(200)






