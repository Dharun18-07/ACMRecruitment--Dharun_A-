Bandit Level 0:
command:ssh bandit0@bandit.labs.overthewire.org -p 2220
password:bandit0

Bandit Level 0 → Level 1:
commands:ls 
         cat readme
password:ZjLjTmM6FvvyRnrb2rfNWOZOTa6ip5If

Bandit Level 1 → Level 2
commands:ssh bandit1@bandit.labs.overthewire.org -p 2220
         ls
         cat ./-
password:263JGJPfgU6LtdEvgfWU1XP5yac29mFx

Bandit Level 2 → Level 3
commands:ssh bandit2@bandit.labs.overthewire.org -p 2220
         ls
         cat ./--spaces\ in\ this\ filename--
password:MNk8KNH3Usiio41PRUEoDFPqfxLPlSmx

Bandit Level 3 → Level 4
commands: ssh bandit3@bandit.labs.overthewire.org -p 2220
          ls
          cd inhere
          ls -a
          cat ...Hiding-From-You
password:2WmrDFRmJIq3IPxneAaMGhap0pFhF3NJ

Bandit Level 4 → Level 5
commands: ssh bandit4@bandit.labs.overthewire.org -p 2220
          ls
          cd inhere
          ls
          file ./*
          cat ./-file07
password:4oQYVPkxZOOEOO5pTW81FB8j8lxXGUQw

Bandit Level 5 → Level 6
commands:  ssh bandit5@bandit.labs.overthewire.org -p 2220
           ls
           find inhere/ -type f -size 1033c ! -executable
           cat inhere/maybehere07/.file2
password:HWasnPhtq9AVKe0dmk45nxy20cvUa6EG

Bandit Level 6 → Level 7
commands: ssh bandit6@bandit.labs.overthewire.org -p 2220
          find / -user bandit7 -group bandit6 -size 33c 2>/dev/null
          cat /var/lib/dpkg/info/bandit7.password
password:morbNTDkSW6jIlUc0ymOdMaLnOlFVAaj

Bandit Level 7 → Level 8
commands:ssh bandit7@bandit.labs.overthewire.org -p 2220
         ls
         grep millionth data.txt
password:dfwvzFQi4mU0wfNbFOe9RoWskMLg7eEc

Bandit Level 8 → Level 9
commands:ssh bandit8@bandit.labs.overthewire.org -p 2220
         ls
         sort data.txt | uniq -u
password:4CKMh1JI91bUIZZPXDqGanal4xvAg0JM

Bandit Level 9 → Level 10
commands:ssh bandit9@bandit.labs.overthewire.org -p 2220
         ls
         strings data.txt | grep ==
password:FGUW5ilLVJrxX9kMYMmlN4MgbpfMiqey

Bandit Level 10 → Level 11
commands:ssh bandit10@bandit.labs.overthewire.org -p 2220
         ls
         base64 -d data.txt
password:dtR173fZKb0RRsDFSGsg2RWnpNVj3qRr
          



 
    
