# Approach
- First, I connected to the target server with `nc readme.ctfcompetition.com 1337`
- I was prompt with an interactive shell that has limited commands.
- After observing the usable commands from `../bin`, I found the command `lzop -c` to be useful in printing out the content of the `README.flag`.

# Flag
CTF{4ll_D474_5h4ll_B3_Fr33}


# Second Flag

## Background

* BusyBox is actaully a software suite that replaces more than 300 common commands, and it is commonly used in embedded system with limited resources. 

* In order to use the functionality provided by busybox, we cab call `/bin/busybox` from another place. And it turns out that we can manually link the loader `/lib/ld-musl-x86_64.so.1` with the executable `/bin/busybox` and then use `cat` or `chmod` on the files.

# Flag
CTF{Th3r3_1s_4lw4y5_4N07h3r_W4y}
