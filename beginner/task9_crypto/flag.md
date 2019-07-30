# Approach
- Looking at the `msg.txt`, it contains a `n` and a `e`, which hints to a RSA public key. This is verified by the message in the given `project_dc.pdf` file.

- After reviewing the pdf, I was able to find several hints:
1. A * P == B * Q
2. abs(A * P - B * Q) < 10000
3. 1 <= A , B <= 1000
- From the implementation of RSA, we know that `n = P * Q`. Further, we can rearrange the equation `1` to get that `P == sqrt(B * n / A)`. With `P`, we know `Q = n / P`

- Next, we simply need to set up a brute force mechanism to check the possible `A` and `B`, since there are only a million possibilities (1000^2). We used `gmpy2` in order to perform integer square root.

- Since we know the cipher text, `msg`, the public modulo, `n`, the public exponent, `e`, and recently found out `P` and `Q`, all we need to do is to find the modular multiplicative inverse of `e` and `phi(n)` to get the decryption key.

- After getting the decryption key, we apply it to the cipher text with along with the public modulo to get back the plain text using `pow` function. `pow` is optimized to perform modular exponentiation.

- After decoding the decrypted message, we were able to see the flag.

# Flag
CTF{017d72f0b513e89830bccf5a36306ad944085a47}

