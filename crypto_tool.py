import sys
# ---Project 2 Internship
def caesar_encrypt(plain_text, shift):
    cipher_text = ""
    for char in plain_text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - start + shift) % 26 + start)
            cipher_text += new_char
        else:
            cipher_text += char
    return cipher_text

def caesar_decrypt(cipher_text, shift):
    return caesar_encrypt(cipher_text, -shift)

def vigenere_encrypt(plain_text, key):
    cipher_text = ""
    key = key.lower()
    key_index = 0
    for char in plain_text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            shift = ord(key[key_index % len(key)]) - ord('a')
            new_char = chr((ord(char) - start + shift) % 26 + start)
            cipher_text += new_char
            key_index += 1
        else:
            cipher_text += char
    return cipher_text

def vigenere_decrypt(cipher_text, key):
    dec_text = ""
    key = key.lower()
    key_index = 0
    for char in cipher_text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            shift = ord(key[key_index % len(key)]) - ord('a')
            new_char = chr((ord(char) - start - shift) % 26 + start)
            dec_text += new_char
            key_index += 1
        else:
            dec_text += char
    return dec_text

def main():
    # --- SELF-TEST ---

    print("🤖 RUNNING INITIAL SELF-TEST...", flush=True)
    test_msg = "Hello World"
    c_enc = caesar_encrypt(test_msg, 4)
    print(f"Caesar Test Success! '{test_msg}' -> '{c_enc}'", flush=True)
    print("------------------------------------\n", flush=True)

    while True:
        print("====================================", flush=True)
        print(" CRYPTOGRAPHY Cypher TOOL DecodeLabs ", flush=True)
        print("====================================", flush=True)
        print("1. Caesar Cipher (Custom Shift)", flush=True)
        print("2. Vigenère Cipher (Keyword Shift)", flush=True)
        print("3. Exit", flush=True)
        
        # Force the terminal to show everything before asking for input
        sys.stdout.flush() 
        choice = input("Select an option (1-3): ").strip()

        if choice == '1':
            print("\n--- Caesar Cipher Mode ---", flush=True)
            text = input("Enter your plaintext: ")
            try:
                shift = int(input("Enter a custom shift key (integer): "))
            except ValueError:
                print("⚠️ Invalid integer. Defaulting to a shift of 3.", flush=True)
                shift = 3
                
            encrypted = caesar_encrypt(text, shift)
            decrypted = caesar_decrypt(encrypted, shift)
            
            print("\n--- 📊 Mathematical Results ---", flush=True)
            print(f"Original Text:  {text}", flush=True)
            print(f"Shift Applied:  {shift}", flush=True)
            print(f"Ciphertext:     {encrypted}", flush=True)
            print(f"Decrypted Text: {decrypted}\n", flush=True)

        elif choice == '2':
            print("\n--- Vigenère Cipher Mode ---", flush=True)
            text = input("Enter your plaintext: ")
            key = input("Enter an alphabetic keyword: ").strip()
            
            if not key.isalpha() or len(key) == 0:
                print("⚠️ Error: The key must contain letters only.", flush=True)
                continue
                
            encrypted = vigenere_encrypt(text, key)
            decrypted = vigenere_decrypt(encrypted, key)
            
            print("\n--- 📊 Mathematical Results ---", flush=True)
            print(f"Original Text:  {text}", flush=True)
            print(f"Keyword Used:   {key}", flush=True)
            print(f"Ciphertext:     {encrypted}", flush=True)
            print(f"Decrypted Text: {decrypted}\n", flush=True)
            
        elif choice == '3':
            print("\nExiting tool. Keep experimenting! 🚀", flush=True)
            break
        else:
            print("⚠️ Invalid choice. Please select 1, 2, or 3.", flush=True)

if __name__ == "__main__":
    main()