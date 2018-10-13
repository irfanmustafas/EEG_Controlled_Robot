import socket
import easygopigo3

HOST='127.0.0.1'
PORT=65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    count=0
    mean=0
    i=0
    j=0
    rbt = EasyGoPiGo3()
    with conn:
        print('Connected by', addr)
        try:
            while True:
                data = conn.recv(1024)
                if data:
                    i=i+1
                    print(i,data)
                    if(i>500):
                        print("data")
                        dat=data.decode()
                        dat=dat.splitlines()
                        # print(data.decode())
                        # print(len(dat))
                        for k in range(len(dat)):
                            # print(float(dat[i]),count)
                            if(count!=8):
                                if(len(dat[k])>=4):
                                    mean=mean+abs(float(dat[k]))
                                    count=count+1
                            if(count==8):
                                if(len(dat[k]>=4)):
                                    val=abs(float(dat[k]))
                                    mean=mean/8.0
                                    if(abs(val-mean)>100):
                                        j=j+1
                                        print("Blink",j)
                                        rbt.forward()
                                    count=0
                                    mean=0
        except KeyboardInterrupt:
            s.close()
    s.close()