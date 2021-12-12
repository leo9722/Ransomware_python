# Ransomware_python

A simply python 3 Ransmoware in AES-128 bits 

# HOW TO USE IT

Create a test directory at the root of git directory
Put some files into this directory

Do the following command line to encrypt:

`python3 chiffre.py`

Do the following command line to decrypt:

`python3 dechiffre.py`

Then all your files in your test directory will be encrypted

The key will be  :

`ZmDfcTF7_60GrrY167zsiPd67pEvs0aGOv2oasOM1Pg=`

Then all your files in your test directory will be decrypted


# HOW DOES IT WORK

The encryption used is AES 128 bits (CBC)

The key used will then be a 32-bit base64 key

the os library allows us to do operations on our files.

The fernet module of the cryptography package has built-in functions for key generation, encryption of clear-text to cipher-text and decryption of cipher-to-clear text using the encryption and decryption methods respectively. The fernet module ensures that data encrypted using it can no longer be manipulated or read without the key.

## chiffre.py

Allows recursive encryption of the target tree.

`encrypt(data)`

Encrypts data passed. The result of this encryption is known as a “Fernet token” and has strong privacy and authenticity guarantees

## dechiffre.py

Allows recursive decryption of the targeted tree structure

 `decrypt(data)`
 
Decrypts a Fernet token. If successfully decrypted you will receive the original plaintext as the result, otherwise an exception will be raised. It is safe to use this data immediately as Fernet verifies that the data has not been tampered with prior to returning it.
