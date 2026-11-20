import sys
import qrcode

url = sys.argv[1] if len(sys.argv) > 1 else input("Adresse du chatbot (https://...) : ").strip()
img = qrcode.make(url)
img.save("qr_chatbot.png")
print("QR code créé : qr_chatbot.png ->", url)
