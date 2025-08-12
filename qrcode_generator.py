# Project 4: QR code generator

import qrcode # type: ignore

data = input("Enter the text / URL: ").strip()
filename = input("Enter the file name (without extension): ").strip()

# Ensure the filename ends with .png
if not filename.lower().endswith(".png"):
    filename += ".png"

# Create QR code
qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)
qr.make(fit=True)

# Generate image
image = qr.make_image(fill_color="black", back_color="white")

# Save image
try:
    image.save(filename)
    print(f"QR code saved as: {filename}")
except Exception as e:
    print(f"Failed to save QR code: {e}")
