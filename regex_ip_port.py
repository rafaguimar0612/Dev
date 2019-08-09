import re;
s = ('[**] [1:36:0] WINBOX ACCESS ATEMPT [**][Priority: 0]08/08-10:58:49.885707 192.168.10.48:58658 -> 45.163.172.6:8291TCP TTL:64 TOS:0x0 ID:19565 IpLen:20 DgmLen:60 DF******S* Seq: 0x79F53A33  Ack: 0x0  Win: 0xFAF0  TcpLen: 40TCP Options (5) => MSS: 1460 SackOK TS: 1980007747 0 NOP WS: 7')
filtro=re.compile('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:[0-9]+')

ip = filtro.findall(s);
print(ip[0]);
