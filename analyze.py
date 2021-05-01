import pickle
import random

with open('words.txt', 'rb') as f:
    words = pickle.load(f)

def get_random_word():
    return random.choice(words)

def sample(n):
    return random.sample(words, n)