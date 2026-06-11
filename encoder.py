from PIL import Image

def text_to_binary(text):
    return ''.join(format(ord(char), '08b') for char in text)

def encode_image(image_path, secret_message, output_path):

    image = Image.open(image_path).convert("RGB")

    binary_message = text_to_binary(secret_message)

    # Store message length first
    message_length = format(len(binary_message), '032b')

    full_data = message_length + binary_message

    pixels = image.load()

    data_index = 0

    for y in range(image.height):
        for x in range(image.width):

            r, g, b = pixels[x, y]

            if data_index < len(full_data):
                r = (r & ~1) | int(full_data[data_index])
                data_index += 1

            if data_index < len(full_data):
                g = (g & ~1) | int(full_data[data_index])
                data_index += 1

            if data_index < len(full_data):
                b = (b & ~1) | int(full_data[data_index])
                data_index += 1

            pixels[x, y] = (r, g, b)

            if data_index >= len(full_data):
                image.save(output_path)
                return