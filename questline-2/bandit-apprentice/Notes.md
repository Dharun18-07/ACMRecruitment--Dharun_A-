**Bandit Level 0:**

command:ssh bandit0@bandit.labs.overthewire.org -p 2220
password:bandit0

**Bandit Level 0 → Level 1:**

commands:ls 
         cat readme
password:ZjLjTmM6FvvyRnrb2rfNWOZOTa6ip5If

**Bandit Level 1 → Level 2**

commands:ssh bandit1@bandit.labs.overthewire.org -p 2220
         ls
         cat ./-
password:263JGJPfgU6LtdEvgfWU1XP5yac29mFx

**Bandit Level 2 → Level 3**

commands:ssh bandit2@bandit.labs.overthewire.org -p 2220
         ls
         cat ./--spaces\ in\ this\ filename--
password:MNk8KNH3Usiio41PRUEoDFPqfxLPlSmx

**Bandit Level 3 → Level 4**

commands: ssh bandit3@bandit.labs.overthewire.org -p 2220
          ls
          cd inhere
          ls -a
          cat ...Hiding-From-You
password:2WmrDFRmJIq3IPxneAaMGhap0pFhF3NJ

**Bandit Level 4 → Level 5**

commands: ssh bandit4@bandit.labs.overthewire.org -p 2220
          ls
          cd inhere
          ls
          file ./*
          cat ./-file07
password:4oQYVPkxZOOEOO5pTW81FB8j8lxXGUQw





 
    
