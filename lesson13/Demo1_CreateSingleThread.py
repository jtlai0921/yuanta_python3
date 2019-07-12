import threading
import time

# 執行緒工作
def job():
    for i in range(5):
        name = threading.current_thread().name
        print("%s: %d" % (name, i))
        time.sleep(1)

t = threading.Thread(target=job)
t.name = '林董'
t.start()
