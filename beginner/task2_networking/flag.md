CTF{4efcc72090af28fd33a2118985541f92e793477f}

found the flag by first running the program `init_sat` and entered the satellite name `Osmium`.
and found the link `https://docs.google.com/document/d/14eYPluD_pi3824GAFanS29tWdTcKxP_XUxx7e303-3E`

You can also use `strace -f -s 10000 -e trace=recv,read ./init_sat` to find the flag without using wireshark. `-f` is used to follow any process that is created by the current program, `-s` specify the maximum strsize to print, `-e trace` trace only the specified set of system calls. 
