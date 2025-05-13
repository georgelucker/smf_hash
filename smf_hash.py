import hashlib
import getpass

def smf11_hash(username: str, password: str) -> str:
    combined = username.lower() + password
    return hashlib.sha1(combined.encode('utf-8')).hexdigest()

def main():
    print("=== SMF 1.1 Password Hasher ===")
    username = input("Введите имя пользователя: ").strip()
    password = getpass.getpass("Введите пароль: ").strip()  # Не отображает пароль при вводе

    hash_result = smf11_hash(username, password)
    print(f"\nХеш (SHA-1, SMF 1.1): {hash_result}")

if __name__ == "__main__":
    main()
