import argparse
from utils import CryptTool, generate_key, save_key

def main():
    crypt_tool = CryptTool()
    parser = argparse.ArgumentParser(description="密钥生成程序")
    parser.add_argument('--generate', action='store_true', help='生成RSA私钥和公钥')
    parser.add_argument('--encrypt', type=str, help='加密消息，使用公钥文件')
    parser.add_argument('--decrypt', action='store_true', help='解密消息，使用私钥文件')

    args = parser.parse_args()

    if args.generate:
        pri_key, pub_key = generate_key()
        save_key(private_key=pri_key, public_key=pub_key)
    elif args.encrypt:
        pub_key = crypt_tool.read_file('./keys/public.pem')
        msg_tobe_encrypt = crypt_tool.read_file(args.encrypt)
        if msg_tobe_encrypt:  # 确保消息被成功读取
            encrypted_msg = crypt_tool.encrypt_message(publickey=pub_key, message=msg_tobe_encrypt)
            crypt_tool.save_file('encrypted.txt', encrypted_msg.encode('utf-8'))
            print(f"加密后的消息: {encrypted_msg}")
    elif args.decrypt:
        pri_key = crypt_tool.read_file('./keys/private.pem')
        msg_tobe_decrypt = crypt_tool.read_file('encrypted.txt')
        if msg_tobe_decrypt:  # 确保消息被成功读取
            decrypted_msg = crypt_tool.decrypt_message(privatekey=pri_key, message=msg_tobe_decrypt)
            crypt_tool.save_file('decrypted.txt', decrypted_msg.encode('utf-8'))
            print(f"解密后的消息: {decrypted_msg}")
        else:
            print("解密的消息读取失败，请检查文件路径。")
    else:
        print("请使用 --generate 参数来生成密钥。")

if __name__ == '__main__':
    main()
