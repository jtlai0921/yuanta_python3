import _thread
import time

# _thread.start_new_thread ( function, args[, kwargs] )
# 參數說明:
# function - 執行緒函数。
# args - 傳遞給執行緒函数的參數,他必須是個 tuple 類型。
# kwargs - 可選參數。

# 為執行緒定義一個函式
def run( threadName, delay):
   count = 0
   while 1:
      #time.sleep(delay)
      count += 1
      print ("%s: %s" % ( threadName, time.ctime(time.time()) ))

# 建立2個執行緒
try:
   _thread.start_new_thread( run, ("Thread-1", 0.5, ) )
   _thread.start_new_thread( run, ("Thread-2", 1, ) )
except:
   print ("Error: ")

while 1:
   pass


