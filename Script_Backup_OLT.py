import telnetlib
import time
import getpass
import sys






host=input("Digite o IP do host:\n");
port=input("Digite a porta:\n");
user= input("Enter your remote account: \n");
password=input("Digite a senha:\n");
comando=input("Digite o comando:\n");
i='1'

while i=='1':
    tn=telnetlib.Telnet(host,port)
    print("Conectando...\n");
    time.sleep(3);
    dis=tn.read_until(b'>');
    print(dis);
    tn.write(user.encode('ascii') +b"\r\n");

    print("Enviando Login \n");
    time.sleep(3);
    dis=tn.read_until(b'>');
    print(dis);

    print('Enviando senha\n');
    tn.write(password.encode('ascii') +b'\r\n');
    time.sleep(7);







    print("Conexão estabelecida com sucesso!\n");


    print("Dowloading Autheticantion logs");
    tn.write(comando.encode('ascii') + b'\n');
    time.sleep(10);
    dis = tn.read_very_eager();
    print(dis);
    time.sleep(86400);
