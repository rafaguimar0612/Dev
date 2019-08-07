#Cliente SSH
import paramiko;
import time;
control = 1;
class SSH:
	def __init__(self,host,porta,usuario,senha):
		self.ssh = SSHClient();
		self.ssh.load_system_host_keys();
		self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy());
		self.ssh.connect(hostname=host,port=porta,username=usuario,password=senha);
	def exec_cmd(self, cmd):
		screen = self.ssh.exec_command(cmd);
		
	






host=input('Digite o IP do Host:\n');
porta = input('Digite a porta ssh:\n');
usuario = input('Digite o nome do usuário:\n');
senha = input ('Digite a senha ssh:\n');



ssh=SSH(host,porta,usuario,senha);

while True:
    comando = input("Digite o comando a ser enviado\n");
    ssh.exec_cmd(comando);
    control = int(input("1- DIGITE NOVO COMANDO:\n2-Sair\n"));
    if(control != 1):  
        break 

print("Comando executado!!!!");
