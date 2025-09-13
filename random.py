import string
import random2
n=1010
letters=string.ascii_letters+string.digits+string.punctuation
s=" ".join(random2.choice(letters)for i in range(n))
print(s)
    