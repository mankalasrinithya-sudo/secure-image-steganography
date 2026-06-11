from PIL import Image

def binary_to_text(binary_data):

    text = ""

    for i in range(0, len(binary_data), 8):

        byte = binary_data[i:i+8]

        if len(byte) == 8:
            text += chr(int(byte, 2))

    return text

def decode_image(image_path):

    image = Image.open(image_path).convert("RGB")

    pixels = image.load()

    binary_data = ""

    for y in range(image.height):
        for x in range(image.width):

            r, g, b = pixels[x, y]

            binary_data += str(r & 1)
            binary_data += str(g & 1)
            binary_data += str(b & 1)

    # First 32 bits contain message length
    message_length = int(binary_data[:32], 2)

    # Extract actual message bits
    message_bits = binary_data[32:32 + message_length]

    return binary_to_text(message_bits)