import socket;
import json;
from paramiko import SSHClient;
import paramiko;
import time;


control = [];


def ssh_conn (rules):
    class SSH:
        def __init__(self, host, porta, usuario, senha):
            self.ssh = SSHClient();
            self.ssh.load_system_host_keys();
            self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy());
            self.ssh.connect();
            self.ssh.exec_command(cmd);


def firewall_rules(sentence):
    json_rule = json.loads(sentence);
    dst_add = json_rule['dst_add'];
    dst_port =  json_rule['dst_port'];
    action = "drop";
    if (dst_add == host):
        chain = "input";
    else:
        chain = "forward";
    if(json_rule['proto']!= "UDP")or(json_rule['proto']!= "UDP"!="TCP")or(json_rule['proto']!= "UDP"!="ICMP"):
        for i in range(0,2):
            if(i == 0):
                i = i+1;
                proto = "UDP";
                comando = "ip firewall filter "+chain+" "+dst_add+" "+dst_port+proto

            if(i == 1):
                i = i+1;
                proto = "TCP";
                comando = "ip firewall filter "+chain+" "+dst_add+" "+dst_port+proto

    else:
        comando = "ip firewall filter "+chain+" "+dst_add+" "+dst_port+proto   
     






#SOCKET_SEVER
addrs=('127.0.0.1',7000);

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM);
server.bind(addrs);
print("LISTEN");
server.listen(1);


while 1:
    conn, addr = server.accept();
    sentence = conn.recv(1024);
   
    print(sentence);
    if sentence not in control:
        print("Adicionar regras \n");
        control = sentence;      
        firewall_rules(sentence.decode("utf-8"));       
    
    conn.close();



