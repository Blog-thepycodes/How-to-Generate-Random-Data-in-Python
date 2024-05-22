import tkinter as tk
from tkinter import messagebox
import random
import os
import string
import secrets
 
 
def generate_randint():
   result = random.randint(1, 500)
   show_result("Random Integer", result)
 
 
def generate_randrange():
   result = random.randrange(0, 500, 5)
   show_result("Random Integer from Range", result)
 
 
def generate_choice():
   result = random.choice(["hello", "hi", "welcome", "bye", "see you"])
   show_result("Random Choice", result)
 
 
def generate_choices():
   result = random.choices(range(1000), k=5)
   show_result("Random Choices", result)
 
 
def generate_randfloat_0_1():
   result = random.random()
   show_result("Random Float (0.0 - 1.0)", result)
 
 
def generate_randfloat_5_10():
   result = random.uniform(5, 10)
   show_result("Random Float (5.0 - 10.0)", result)
 
 
def shuffle_list():
   l = list(range(10))
   random.shuffle(l)
   show_result("Shuffled List", l)
 
 
def generate_randstring():
   result = ''.join(random.sample(string.ascii_letters, 16))
   show_result("Random String (16 characters)", result)
 
 
def generate_randbytes_os():
   result = os.urandom(16)
   show_result("Cryptographic Random Bytes (os.urandom)", result)
 
 
def generate_randbytes_secrets():
   result = secrets.token_bytes(16)
   show_result("Cryptographic Random Bytes (secrets.token_bytes)", result)
 
 
def generate_randstring_crypto():
   result = secrets.token_urlsafe(16)
   show_result("Cryptographic Random String (secrets.token_urlsafe)", result)
 
 
def generate_randbits_crypto():
   result = secrets.randbits(16)
   show_result("Cryptographic Random Bits (16 bits)", result)
 
 
def show_result(title, result):
   messagebox.showinfo(title, f"{title}: {result}")
 
 
def main():
   root = tk.Tk()
   root.title("Random Generator - The Pycodes")
   root.geometry("500x500")
 
 
   buttons = [
       ("Generate Random Integer (1 to 500)", generate_randint),
       ("Generate Random Integer from Range (0 to 500 step 5)", generate_randrange),
       ("Generate Random Choice from List", generate_choice),
       ("Generate five Random Choices from 0 to 1000", generate_choices),
       ("Generate Random Float (0.0 - 1.0)", generate_randfloat_0_1),
       ("Generate Random Float (5.0 - 10.0)", generate_randfloat_5_10),
       ("Shuffle List (0 to 9)", shuffle_list),
       ("Generate Random String (16 characters)", generate_randstring),
       ("Generate Cryptographic Random Bytes (os.urandom)", generate_randbytes_os),
       ("Generate Cryptographic Random Bytes (secrets.token_bytes)", generate_randbytes_secrets),
       ("Generate Cryptographic Random String (secrets.token_urlsafe)", generate_randstring_crypto),
       ("Generate Cryptographic Random Bits (16 bits)", generate_randbits_crypto),
   ]
 
 
   for text, command in buttons:
       button = tk.Button(root, text=text, command=command)
       button.pack(pady=5)
 
 
   root.mainloop()
 
 
if __name__ == "__main__":
   main()
