#!/usr/bin/python

from pwn import *


exe = context.binary = ELF('./bof')


#host = args.HOST or 'localhost'
#port = int(args.PORT or 1337)

host = "buffer-overflow.ctfcompetition.com"
port = 1337

gdbscript = '''
break *0x{exe.symbols.main.x}
continue
'''

# Execute the target binary locally
def local(argv=[], *a, **kw):
    if args.GDB:
        return gdb.debug([exe.path] + argv, gdbscript=gdbscript, *a, **kw)
    else:
        return process([exe.path] + argv, *a, **kw)

# Connect to the remote process
def remote(argv=[], *a, **kw):
    io = connect(host,port)
    if args.GDB:
        gdb.attach(io,gdbscript=gdbscript)
    return io


start = local if args.LOCAL else remote



io = start()

io.interactive()
