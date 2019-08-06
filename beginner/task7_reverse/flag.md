# Task 7 Reverse

## Approach 
* We were first given two files, one is full of emoji symbols, which looks like customized operations, and a python file which looks like an implementation of VM.
* First attempt at running the python file with the emoji file, I was able to see the beginning part of an URL `http://emoji-t0anaxn` before coming to a halt. 
* Since it is a VM, I inserted a debugging statement that prints out the content of the stack every time the function `step` is being called.
* This allow me to see what the virtual machine is doing in a dynamic fashion.
* Upon inspecting the debugging result, I found out that the list of value that is being pushed to the stack are the numerical value in the emoji.
* Further inspecting the output, I found out that those value are XOR-ed with what seems to be a sequence of prime values.
* After thought that I had secret sequence, I started to write python exploit to xor the stack values with a normal sequence of a list of prime numbers.
* However, I soon found out that the prime number only worked for the first 5 values. To fix the problem, I printed out the values that are being xor-ed in the python vm file.
* The secret sequence turns out to be symmetric prime numbers, palindrome primes. And after replaced the normal primes with a list of palindrome primes, I was able to get the first part of the URL. `http://emoji-t0anaxnr3nacpt4na.web.ctfco`
* After typing it in to a search engine, I was able to see the final website. I know that to get the full sequence, I have to xor the second and third stack, but a simple search led me to the webpage that contain the flag.

## Flag
CTF{Peace_from_Cauli!}

