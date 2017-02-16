import threading
from queue import Queue
import socket

task_lock = threading.Lock()

target = 'hackthissite.org'
#target = input("Enter Website: ")
#ip = socket.gethostbyname(target)


def portscan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        con = s.connect((target,port))
        with task_lock:
            print('port',port,'is open')
        con.close()
    except:
        pass


# The threader thread pulls an worker from the queue and processes it
def threader():
    while True:
        # gets an worker from the queue
        worker = q.get()

        # Run the example job with the avail worker in queue (thread)
        portscan(worker)

        # completed with the job
        q.task_done()

# Create the queue and threader 
q = Queue()

# how many threads are we going to allow for
for x in range(100):
     t = threading.Thread(target=threader)

     # classifying as a daemon, so they will die when the main dies
     t.daemon = True

     # begins, must come after daemon definition
     t.start()

# 100 jobs assigned.
for worker in range(1,1000):
    q.put(worker)

# wait until the thread terminates.
q.join()
