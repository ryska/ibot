import pynstagram

username = 'urbanshot__'
password = 'kluza1'

def upload():
    with pynstagram.client(username, password) as client:
        client.upload('pic1.jpg', '#meow')

