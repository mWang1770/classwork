## pwd
  - print working directory
  - prints where we currently are in the file system
  - Mac: /Users/username
  - Linux:/home/username

## ls
  - shows all the files in the file system you are currently in

## cd
  - change directory
  - how to use: cd name_of_file
  - if use pwd now, displays: /Users/username/name_of_file
    -shows that you are inside the file now
      
## Hidden Files
  - can be seen by doing: ls-a
     - lists every file, including hidden files

## Long Listing
  - If you want to see more info about your files
  - use ls-l
  - lists the long forms of the files
  - tells you more infor like permissions, user, group owners, sizes and date info

## Long Listing of Hidden Files 
  - use ls-la
      -lists long forms of all files, including hidden ones
      
## RELATIVE PATHS
  - . (one dot)
    - current directory
  - .. (two dots)
    - parent directory
    - if you want to go from a file back to file systems, use cd ..
      - e.g. /Users/username/name_of_file/doc
      - if you want are currently in doc, but want to move back to name_of_file, then use cd ..
      - once you move, you can see all the other files in name_of_file

## Reaching Files Within Files Using One Command Line
  - /cd name_of_file/doc/
    - ^ that will take you directly to doc, without writing a command line to open name_of_file
  - it can also move backwards: cd .. / .. /
    - e.g. /Users/username/name_of_file/doc
    - if you were in doc, it would move to name_of_file and then to username in one command line

## cd+enter or cd~
  - takes you back to the home directory
    - if you pwd after writin gthis command, it will show: /Users/username
  - this can be used as a launching point to reach files
    - e.g.: cd~/name_of_file/
        - ^ goes back to the file and then heads to name_of_file
