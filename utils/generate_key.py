from Crypto.PublicKey import RSA

def generate_key() -> tuple[bytes, bytes]:
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

def save_key(private_key, public_key):
    with open('./keys/private.pem', 'wb') as priv_file:
        priv_file.write(private_key)
        print('私钥 private.pem 存储成功!')
    with open('./keys/public.pem', 'wb') as pub_file:
        pub_file.write(public_key)
        print('公钥 public.pem 存储成功!')
