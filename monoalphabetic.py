# number   = "0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25"
# alphabet = "A b c d e f G h i j  k  l  m  n  o  p  q  r  s  t  y  v  w  x  u  Z"
# key      = "z y x w v u t s r q  p  o  n  m  l  k  j  i  h  g  f  e  d  c  b  a"
class monoalphabet:
    def encryption(key,plaintext):
        en_text=""
        for i in plaintext:
            if i.isalpha():
                index=ord(i)-97
                en_text += key[index]
        return en_text
    def decryption(key,ciphertext):
        de_text=""
        for i in ciphertext:
            if i.isalpha():
                index=key.index(i)
                de_text += chr(index+97)
        return de_text

