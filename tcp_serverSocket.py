import socket
token=b'1564398'
addrs=('127.0.0.1',7000);

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM);
server.bind(addrs);
print("LISTEN");
server.listen(1);

while 1:
    conn, addr = server.accept();
    sentence = conn.recv(1024);
    clientoken=(sentence);


    if (clientoken == token):
        conn.send(bytes("ACCEPT","utf8"));
        conn.close();


    else:
        conn.send(bytes("DENIED","utf8"));
        conn.close();