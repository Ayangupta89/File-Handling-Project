from pathlib import Path
import os
def createfile():
    try:
        name = input("enter your file name: ")
        path = Path(name)
        if not path.exists():
            with open(path,"w") as fs:
                data = input("enter what you want to add in your file: ")
                fs.write(data)
                print("file created sucessfully")
        else:
            print("error name already exists")
    except Exception as err:
        print(f"an error accured as {err}")



def readfile():
    try:
        name = input("enter file name: ")
        path = Path(name)
        if path.exists():
         with open(path,"r") as fs:
            content = fs.read()
            print(f"your file content is \n {content}")
        else:
            print("error no such file found")
    except Exception as err:
        print(f"an error is accured as {err}")
        

def updatefile():
    try:
        name = input("enter file name: ")
        path = Path(name)

        if path.exists():
         print("operations")
         print("1. renaming the file")
         print("2. appending the file")
         print("3. overwriting the file")

         choice = int(input("enter your option: "))

         if choice ==1:
             newname = input("enter new name")
             new_path = Path(newname)
             if not new_path.exists():
                 path.rename(new_path)
                 print("renamed sucessfully")

             else:
                 print("file already exists")    

         elif choice == 2:
             with open(path,"a") as fs:
                 data =input("what do you want to append : ") 
                 fs.write("\n"+data)
                 print("sucrssfully appended")

        elif choice == 3:
            with open(path,"w") as fs:
                data = input("what do you want to overwrite")
                fs.write("\n"+data)
                print("sucessfully overwiitten")
    except Exception as err:
        print(f"an error exists as {err}")




            

def deletefile():
try:
        name = input("enter your file name")
        path = Path(name)

        if path.exists():
            path.unlink()
            print("file deleted sucessfully")

        else:
            print("error no such file found")
except Exception as err:
    print{f"an error accured as {err}"}

print("press 1 for creating a file")
print("press 2 for reading a file")
print("press 3 for update a file")
print("press 4 for deleting a file")

a = int(input("\nenter your response: "))

if a == 1:
    createfile()
if a == 2:
    readfile()
if a == 3:
    updatefile()
if a == 4:
    deletefile()

