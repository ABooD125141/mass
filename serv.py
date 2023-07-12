import socket

# معلومات الاتصال للخادم
server_ip = '192.168.1.152'  # عنوان IP للخادم
server_port = 5000  # رقم المنفذ للاتصال

# إنشاء كائن الخادم
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((server_ip, server_port))
server_socket.listen(1)  # قم بزيادة القيمة إذا كنت ترغب في استقبال اتصالات متعددة

print(f"Lis:{server_ip}:{server_port}")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"IP:{client_address[0]}:{client_address[1]}")

    while True:
        data = client_socket.recv(1024).decode("utf-8")
        if not data:
            break

        print(f": {data}")

    client_socket.close()
