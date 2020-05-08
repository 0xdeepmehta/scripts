#!/usr/bin/python3

from Crypto import Random
from Crypto.PublicKey import RSA
import base64

def generate_key():
    # firstly, define the modulus length, which should be greater than 1024
    # and multiple of 256
    modulus_length = 256 * 4
    privatekey = RSA.generate(modulus_length, Random.new().read)
    publickey = privatekey.publickey()
    return privatekey, publickey

def encrypt_message(msg, publickey):
    encrypted_msg = publickey.encrypt(bytes(msg.encode('utf-8')), 32)[0]
    # here *[0] is used, cause the returned value is a tuple.
    encoded_encrypted_msg = base64.b64encode(encrypted_msg)
    return encoded_encrypted_msg

def decrypt_message(encoded_encrypted_msg, privatekey):
    decoded_encrypted_msg = base64.b64decode(encoded_encrypted_msg)
    decoded_decrypted_msg = privatekey.decrypt(decoded_encrypted_msg)
    return decoded_decrypted_msg

private_key, public_key = generate_key()
msg = 'I am a secret message.'
print("\nMessage: ", encrypt_message(msg, public_key).decode('utf-8'), "\n\n")
print(private_key.exportKey().decode('utf-8'), '\n\n\n', public_key.exportKey().decode('utf-8'))



    
