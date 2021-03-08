import os  #導入OS模塊到當前程序

ip_list = ["8.8.8.8", "8.8.4.4", "192.168.1.1"]
for ip in ip_list:
        response = os.popen(f"ping {ip}").read()  #response 像伺服器傳送OS popen對象的屬性的ip
        if "Received =4" in response:
            print(f"UP {ip} Ping Successful")
        else:
            print(f"DOWN {ip} Ping Unsuccessful")