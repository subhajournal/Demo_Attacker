Please Follow the steps:

1. Extract the Zip File
2. Take a backup of the folders with name '1' & 'V4' as those are required for all these four
execution. Store the backup in completely different location.
3. The objective of the viruses are defined in the code and the corresponding outputs are shown 
in the .md file as well as in the ipynb file.
4. Permit the directory for any kind of permission, as if the permissions are auto granted, 
it will be caught by Antivirus as it will tends to change te registry structure which are not allowed.
5. Steps to execute:
   a. Place Folder '1' and the program files in a same folder, of you place these two in two seperate 
      folder, then you hav etochange the address of the directory in the program that is defined by 'dr'.
      Execute V1.py and see that the files are encrypted and 
   b. After execution of V1.py, copy the backup folder '1' to the program native directory that is where the 
      python files are stored and execute V2.py. It will streal the content of te file and store all those 
      content into another log file and after that all th files are made read-only so you cannot change the file
      contect further.
   c. After execution of V2.py, copy the backup folder '1' to the program native directory that is where the 
      python files are stored and execute V3.py. It will strael the files from the base directory and make the 
      files encrypted.
   d. After execution of V3.py, copy the backup folder '1' to the program native directory that is where the 
      python files are stored and execute V4.py. It will search and destroy the files with extentions 
      of programming file like .py or .c etc from the base directory and make the files encrypted with password.
      Which cannot be retrieved with decryption.