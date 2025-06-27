from PIL import Image

def encrypt_image(image_path, key):
    img = Image.open(image_path)
    pixels = img.load()

    for i in range(img.size[0]):  # width
        for j in range(img.size[1]):  # height
            r, g, b = pixels[i, j]
            # Encrypt by adding key to RGB
            pixels[i, j] = ((r + key) % 256, (g + key) % 256, (b + key) % 256)

    img.save("encrypted_image.png")
    print("✅ Encrypted image saved as encrypted_image.png")

def decrypt_image(image_path, key):
    img = Image.open(image_path)
    pixels = img.load()

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b = pixels[i, j]
            # Decrypt by subtracting key
            pixels[i, j] = ((r - key) % 256, (g - key) % 256, (b - key) % 256)

    img.save("decrypted_image.png")
    print("✅ Decrypted image saved as decrypted_image.png")

# ========== Main Program ==========
choice = input("Do you want to encrypt or decrypt? (e/d): ").lower()
key = int(input("Enter a number key (e.g. 50): "))

if choice == 'e':
    encrypt_image("image.jpg", key)
elif choice == 'd':
    decrypt_image("encrypted_image.png", key)
else:
    print("❌ Invalid option.")
