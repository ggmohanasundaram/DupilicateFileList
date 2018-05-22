# DupilicateFileList

  # Rules to filter identical files
      1. The files have been considered as duplicate if they have same data
      2. The files with same name and different data didnt consider as duplicate
      
  # Implementation
      1. MD5 check sum has been used to find the files with same data
      2. This implementation is o(n)
      3. This script has been implemented in Python 3.5.2
      
  # How to run
   ../DuplicateFileList$ python redundantfilesMain.py <folder to scan>
  
  
