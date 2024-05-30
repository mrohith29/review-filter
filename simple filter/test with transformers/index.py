from transformers import pipeline

def is_phone_review(review, classifier):
    result = classifier(
        review,
        candidate_labels = ["mobile phone"]
    )
    print(f"Review: {review[:50]}...") 
    print(f"Score: {result['scores'][0]}")  
    if result['scores'][0] >= 0.5:
        return True
    else:
        return False

classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

with open('input.txt', 'r') as input_file, open('output.txt', 'w') as output_file:
    for review in input_file:
        if is_phone_review(review, classifier):
            output_file.write(review)

# output

# Review: The OLED screen on this phone is amazing.
# ...
# Score: 0.9951146245002747
# Review: The battery life is long-lasting and the fast-char...
# Score: 0.7749876976013184
# Review: The 12-megapixel camera takes stunning photos.
# ...
# Score: 0.6318285465240479
# Review: I love the touchscreen on this phone.
# ...
# Score: 0.9929348230361938
# Review: The LCD screen is bright and clear.
# ...
# Score: 0.6869888305664062
# Review: The 5000 mAh battery lasts all day.
# ...
# Score: 0.8266293406486511
# Review: The wide-angle camera is great for landscape photo...
# Score: 0.15717633068561554
# Review: This laptop has a great keyboard.
# ...
# Score: 0.00023294826678466052
# Review: The sound quality on these headphones is excellent...
# Score: 0.005417752545326948
# Review: This smartwatch has a great battery life....
# Score: 8.699587488081306e-05