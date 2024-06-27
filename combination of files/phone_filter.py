import re

characteristics = {
    'screen': ['oled', 'lcd', 'touchscreen', 'resolution', 'crystal clear', 'dull', 'not responsive'],
    'battery': ['mah', 'long-lasting', 'fast-charging', 'drains fast', 'excellent battery life', 'short battery life'],
    'camera': ['megapixel', 'zoom', 'wide-angle', 'clarity', 'night photos', 'focus', 'flash', 'photo quality', 'features', 'blurry'],
    'performance': ['speed', 'responsive', 'sluggish', 'exceeded expectations', 'slow'],
    'price': ['affordable', 'expensive', 'worth the price', 'value for money'],
    'software': ['buggy', 'slow updates', 'features', 'updates'],
    'network': ['network issues'],
    'storage': ['storage', 'insufficient storage'],
    'charging': ['fast charging', 'slow charging'],
}


def is_phone_review(review):
    for characteristic, specs in characteristics.items():
        for spec in specs:
            if re.search(spec , review, re.I):
                return True
    return False

with open('translated.txt', 'r', encoding='utf-8') as input_file, open('mobile_filter.txt', 'w', encoding='utf-8') as output_file:
    for review in input_file:
        if is_phone_review(review):
            output_file.write(review)
        # else:
        #     output_file.write('Not a phone review: ' + review)