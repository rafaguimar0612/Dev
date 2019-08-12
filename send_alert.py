import json;
import socket;

def send_server(json_string):
    connection = ("127.0.0.1",7000);
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM);
    client.connect(connection);
    setence = bytes(json_string,"utf8");
    client.send(setence);
    answer = client.recv(1024);
    print("FROM SERVER:",answer);
    client.close();

  

#Abrindo arquivos de log's e gerando JSON#
arquivo = open('/var/log/snort/alert.csv', 'r');

for lines in arquivo:
    lista = arquivo.readline();
    ns = lista.split(',');
    print(ns);
       
    j = {"src_ip": ns[0], "src_port": ns[1], "dst_ip": ns[2], "dst_por": ns[3], "proto": ns[4]}
    json_string = json.dumps(j);
    send_server(json_string);
    j1 = json.loads(json_string);
    print(j1);
    break;
   
arquivo.close();



