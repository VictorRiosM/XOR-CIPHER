#!/usr/bin/python2
from sys import argv
import random
from shutil import copy2

def xorCipher(message, keySize, keyOwner, line):
   f = open(keyOwner+'Key.txt', 'r+')
   if line == 0: f.seek(0)
   else: f.seek(line*(keySize + 1))
   key = f.readline()
   if line == 0: f.seek(0)
   else: f.seek(line*(keySize + 1))
   for c in xrange(len(key)-1):
      f.write(chr(32))
   f.close()
   cipher = ''
   for i in xrange(len(message)):
      cipher += chr(ord(message[i]) ^ ord(key[i%keySize]))
   return cipher

def keyCreation(numberKeys, keySize):
   f = open("AliceKey.txt", "w")
   for i in xrange(numberKeys):
      for j  in xrange(keySize):
         c = chr(random.randint(32, 126))
         f.write(c)
      f.write("\n")
   f.write("\n")
   f.close()
   copy2('AliceKey.txt', 'BobKey.txt')

def main():
   try:
      numberKeys = int(argv[1])
      keySize = int(argv[2])
   except:
      numberKeys = input("Number of keys to generate: ")
      keySize = input("Size of the key (# of characters): ")
   print numberKeys
   print keySize
   keyCreation(numberKeys, keySize);
   for i in xrange(numberKeys):
      print i
      sender = ''
      while True:
         sender = raw_input("Who sends the message? Alice : a -- Bob : b -> ")
         if sender == 'a' or sender == 'b': break
      if sender == 'a': 
         sender = 'Alice'
         receiver = 'Bob'
      if sender == 'b':
         sender = 'Bob'
         receiver = 'Alice'
      message = raw_input("Enter the message: ")
      encrypted = xorCipher(message, keySize, sender, i)
      print sender + " sends this encrypted message: " + encrypted
      decrypted = xorCipher(encrypted, keySize, receiver, i)
      print receiver + " receives this decrypted message: " + decrypted

main()
