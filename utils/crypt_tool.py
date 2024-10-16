import base64
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

class CryptTool:
    def __init__(self) -> None:
        pass

    def encrypt_message(self, publickey: str, message: str) -> str:
        rsa_cipher = PKCS1_OAEP.new(RSA.import_key(publickey))
        encrypted_message = rsa_cipher.encrypt(message.encode('utf-8'))
        return base64.b64encode(encrypted_message).decode('utf-8')

    def decrypt_message(self, privatekey: str, message: str) -> str:
        rsa_cipher = PKCS1_OAEP.new(RSA.import_key(privatekey))
        decrypted_message = rsa_cipher.decrypt(base64.b64decode(message))
        return decrypted_message.decode('utf-8')

    def read_file(self, filepath: str) -> str:
        try:
            with open(filepath, mode='r', encoding='utf-8') as k:
                content = k.read()
            return content
        except FileNotFoundError:
            print(f"文件 {filepath} 不存在。")
            return None

    def save_file(self, filepath: str, message: bytes):
        with open(filepath, mode='wb') as f:
            f.write(message)
        print(f"文件 {filepath} 存储成功！")
