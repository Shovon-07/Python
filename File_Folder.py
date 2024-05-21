import os

def CreateFolder() :
  i = 1
  while i<=10 :
    os.mkdir(f"Shovon_{i}")
    i+=1

def DeleteFolder() :
  i = 1
  while i<=10 :
    os.rmdir(f"Shovon_{i}")
    i+=1

def CreateFile() :
  i = 1
  while i<=10 :
    open(f"Shovon_{i}.txt","x")
    i+=1

def DeleteFile() :
  i = 1
  while i<=10 :
    os.remove(f"Shovon_{i}.txt")
    i+=1