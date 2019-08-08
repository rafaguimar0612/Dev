import socket

connection=("127.0.0.1",7000);
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM);
client.connect(connection);
token = input("Digite o token:");
setence=bytes(token,"utf8");
client.send(setence);
answer=client.recv(1024);
print("FROM SERVER:",answer);
client.close();

