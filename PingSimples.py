import os

print("#" * 60)

ip_or_host = input("Digite o Ip ou Host a ser verificado: ")

print("-*-" * 20)

os.system('ping -n 6 {}'.format(ip_or_host))

