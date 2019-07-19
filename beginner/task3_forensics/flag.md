# Background information
- File Allocation Table (FAT)
- New Technology File System (NTFS) to overcome the limitation the file size limit of FAT, with now the limitation to be 116 exabyte EB

# Approach
- Unzipping w/ 7zip or Mounting `family.ntfs` allows us to find `credentials.txt`. The file mentions that `I keep pictures of my credentials in extended attributes`, "extended attributes" hints that there exists an alternate data stream to the file and it is a picture. 
- After finding out the name of the alternate data stream `FILE0` with the windows command `dir /r`, I was able to open the image containing the flag with `mspaint credentials.txt:FILE0`

# Flag
CTF{congratsyoufoundmycreds}


