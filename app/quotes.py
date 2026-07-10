import random

quotes = [
    {"quote": "The only way to do great work is to love what you do.", "author": "Steve Jobs"},
    {"quote": "Believe you can and you're halfway there.", "author": "Theodore Roosevelt"},
    {"quote": "It does not matter how slowly you go as long as you do not stop.", "author": "Confucius"},
    {"quote": "Act as if what you do makes a difference. It does.", "author": "William James"},
    {"quote": "Success is not final, failure is not fatal: it is the courage to continue that counts.", "author": "Winston Churchill"},
    {"quote": "Hard work beats talent when talent doesn't work hard.", "author": "Tim Notke"},
    {"quote": "Dream big and dare to fail.", "author": "Norman Vaughan"},
    {"quote": "What you get by achieving your goals is not as important as what you become by achieving your goals.", "author": "Zig Ziglar"},
]

def get_random_quote():
    return random.choice(quotes)