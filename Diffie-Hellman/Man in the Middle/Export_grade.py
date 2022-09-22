'''
The issue here is that Alice is basically asking Bob how long should be the prime number p
that will be used in Diffie-Hellman exchange. Among the choises there is DH64 (Diffie-Hellman using 64 bits prime), but the Discrete logarithm problem 
with number this small is solvable using your computer, so is not safe at all. Obviously Bob will never choose this option, unless it's the only option available!
So we can take the Alice's first message {"supported": ["DH1536", "DH1024", "DH512", "DH256", "DH128", "DH64"]} and remove the safe (or safe-ish) options. 
We'll send this to Bob instead: {"supported": ["DH64"]}.Now Bob is forced to choose DH64.
'''