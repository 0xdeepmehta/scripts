from Crypto import Random
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import PKCS1_v1_5
from Crypto import Hash
from base64 import b64decode, b64encode

# we're using the "SHA-256" hash.

def generate_key(key_size=256*4):
    """For generating new private and public RSA keys."""
    private_key = RSA.generate(key_size, Random.new().read)
    public_key = private_key.publickey()
    return private_key, public_key

def import_key(base64_encoded_private_key):
    """This Function will generate RSA private key object from
    already existing one, just by providing the base64 key."""
    return RSA.importKey(base64_encoded_private_key)

def encrypt_msg(msg, public_key):
    """This function will generate the encrypted msg based on
    the provided public key."""
    cipher = PKCS1_OAEP.new(public_key)
    return cipher.encrypt(msg.encode('utf-8'))

def decrpt_msg(encrypted_msg, privae_key):
    """This function will return the decrypted message on the
    basis of encrypted message and private key.
    NOTE: Here, you need to decode the base64 encoded message first
    and the provide it as a argument in the function."""
    cipher = PKCS1_OAEP.new(private_key)
    return cipher.decrypt(encrypted_msg)

def sign_msg(msg, private_key):
    signer = PKCS1_v1_5.new(private_key)
    digest = Hash.SHA256.new()
    digest.update(msg)
    return signer.sign(digest)

def verify_msg(msg, signature, public_key):
    signer = PKCS1_v1_5.new(public_key)
    digest = Hash.SHA256.new()
    digest.update(msg)
    return signer.verify(digest, signature)


private_key, public_key = generate_key()
msg = "I am a secret message."

encrypted_msg = encrypt_msg(msg, public_key)
# QUICKNOTE: Here, the encrypted_msg thus obtained from encrypt_msg
# will give you the message in binary format, so we're gonna
# encode it to the base64 format so that it'll be more human readable.
encoded_encrypted_msg = b64encode(encrypted_msg)
print('\n\n')
print("---ENCRYPTED MESSAGE---\n", encoded_encrypted_msg.decode('utf-8'))
print('\n\n')
print("[+] The PRIVATE KEY for above message: \n", private_key.exportKey().decode('utf-8'))
print('\n\n')
signature = sign_msg(encrypted_msg, private_key)
print(b64encode(signature))
print(verify_msg(encrypted_msg,signature,  public_key))