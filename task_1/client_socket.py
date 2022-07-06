import hashlib
import socket
import hmac

url = '46.229.214.188'
key = 'n5AUbpMiEGV1WvAcgvjFdm75vDqrvFlm884ZN9IEBjJshGgOouCuNx'
email = 'aepre@yandex.ru'
dig = hmac.new(key=b'n5AUbpMiEGV1WvAcgvjFdm75vDqrvFlm884ZN9IEBjJshGgOouCuNx', msg=b'aepre@yandex.ru', digestmod=hashlib.sha256)
email_hmac = dig.hexdigest()
data = f'{email}:{email_hmac}'.encode()


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((url, 80))
client_socket.send(data)


