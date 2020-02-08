# Command line notes

Corey Schafer has a few very important videos related to the Command line. Check them out and take notes below.

## Linux/Mac Terminal Tutorial: Navigating your Filesystem
[Watch the Video](https://www.youtube.com/watch?v=j6vKLJxAKfw)

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


## Linux/Mac Terminal Tutorial: Create, Copy, Move, Rename and Delete Files and Directories
[Watch the Video](https://www.youtube.com/watch?v=eoejHvAPDFs)

## Creating Directories:
  - mkdir name
## Creating Files
  - touch name_of_file.txt
## Opening Files
  - open name_of_file.txt
## Copying Files
  - cp name_of_file.txt copy_of_name_of_file.txt
## Renaming Files
  - in order to rename, you must move to same directory
  - mv name_of_file new_name_of_file
## Moving Files
  - first need to create somewhere new for the file to go
  - so, create a subdirectory to move the file
    - e.g. mkdir name_of_subdir
  - once you've created the subdirectory:
    - mv name_of_file.txt name_of_subdir/
    -                                   ^ the slash is important to distinguish this from renaming
## Moving and Renaming in same command line
  - mv name_of_file.txt name_of_subdir/new_name_of_file.txt
  - you have to first move and then rename

## Deleting Files
  - rm name_of_file.txt
  - be careful with this command since if it's removed, it is essentially impossible to recover

## Copying Directories
  - first need to make new directory for it to go to
    - mkdir copy_of_name_of_directory
  - once you create a new location for it to move, copy that to the new location
    - mv-R name_of_directory/copy_of_name_of_directory
    -    ^ the -R is important because mv does not apply for directories, only files

## Renaming Directories
  - It is the same as renaming files
  - mv name_of_directory/new_name_of_directory
  
## Moving Directories
  - Same as moving files
  - mv name_of_directory/ new_name_of_directory/

## Moving and Renaming in same command line
  - mv name_of_directory/../new_name_of_directory
  
## Deleting Directories
  - rm-R name_of_directory
  - Special Cases:
    - Some directories do not delete properly using this command, so you can force deletion:
      - rm-rf new_name_of_directory

## Mac OS X Terminal Tutorial: Time-Saving Keyboard Shortcuts
[Watch the Video](https://www.youtube.com/watch?v=TXzrk3b9sKM)

- can use arrow keys to move around the code

## Ctrl + a
  - moves to beginning of the line

## Ctrl + e
  - moves to the end of the line
  
## Ctrl + u
  - deletes everything before the cursor
  
## Ctrl + k
  - deletes everything after cursor
  
## Tab
  - autocompletes

## Up Arrow
  - scrolls through past commands

## Down Arrow
  - goes down through the command  list until it reaches a new blank command line

## ! Command
  - goes through all past commands and reruns the first command with the letters you typed
    - e.g. ! fi
    - re-runs all past commands until it encounters and reruns the first command beginning with "fi"
    
## history
  - shows you all your past commands with a number assigned to each
  - can also use ! assigned number to find the related code
  
## Ctrl + r
  - reverse search
  - 'search': past command that the terminal is going to run
  
## Ctrl + l
  - clears screen, but doesn't clear the scroll back
  - if you scroll up, you can still find your past commands
  
## Option <- ->
  - moves one ward at a time
  
## Option + Click
  - the pointer turns into a bullseye kind of thing(?)
  - anywhere you click, it goes to 
  
## Cmnd + k
  - clears screen and scroll at the same time
  
    
