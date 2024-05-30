import re

characteristics = {
    'screen': ['oled', 'lcd', 'touchscreen'],
    'battery': ['mah', 'long-lasting', 'fast-charging'],
    'camera': ['megapixel', 'zoom', 'wide-angle'],
}

def is_phone_review(review):
    for characteristic, specs in characteristics.items():
        for spec in specs:
            if re.search(spec , review, re.I):
                return True
    return False

with open('input.txt', 'r') as input_file, open('output.txt', 'w') as output_file:
    for review in input_file:
        if is_phone_review(review):
            output_file.write('Phone review: ' + review)
        else:
            output_file.write('Not a phone review: ' + review)