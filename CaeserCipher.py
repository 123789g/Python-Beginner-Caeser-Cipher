#This function is just going to contain our work and we can call this to run over anything as long as we pass in the (string, and the key).
def caeserCipher(string, key):
  # Initializing a... cart of sorts. This will hold whatever we need and deliver it through the function.
  payload= ""
  
  # This is where the actual encryption happens. To start we are using i to hold our characters. For each character in the *string*, we added as a param in the function, do the following. This loop will keep going for each and every character in the string.
  for i in string: 
    
    # This is looking for spaces. If there is a space/whitespace, we're just going to iterate again by moving to the next character in the payload. Also without this small if, the returned encryption WONT HAVE SPACES! :scream: So think about this as a way to keep our weird characters.
    if i == ' ' and "." and "!" and ",":
      payload = payload + i
      
      # If the letter/character being delivered through this loop is uppercase then run this.
    elif  i.isupper():
      # We are iteraing using chr. This will take our SINGLE character and pass it through this formula to encrypt it. The key is whatever is passed in when the function is run. No matter what the key is, it needs to be within the range of our alphabet. We have to use ASCII to find our letters and the capital letters in ASCII is a range between 65 and 90. ¯\_(ツ)_/¯ so we'll use 65 to keep us around that range and %(modulous) to keep us from going past that ASCII limit.
      payload = payload + chr((ord(i) + key - 65) % 25 + 65)
      
      # If the letter/character being delivered through the loop isn't uppercase then it MUST be lowercase. So no matter what run this instead. Also. Lowercase letters are in the ASCII range of 97 - 122. So guess what. That's right we're changing that 65 to 97 and %ing to keep us in that range.
    else:
      payload = payload + chr((ord(i) + key - 97) % 25 + 97)
  
  return payload
#  Self explanatory. This gathers the user's input and stores it in variables. We'll pass these into the function we made at the start of this.
userString = input("What would you like to encrypt? ")
# We add an int in there to MAKE SURE the user actually puts in a number and not like "nine" or something :v
cipherKey = int(input("What's your key?(How far should the cipher shift?) "))

# Finally. Run the function on user Determined Values
print("Cipher Success! Text Encrypted To:", caeserCipher(userString, cipherKey))

