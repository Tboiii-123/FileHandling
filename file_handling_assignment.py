try:
    with open('my_file.txt','w') as handler:
        handler.writelines(["I am lawal hussein","\nI am a student of PLP community","\nI am 19 years old"])
        print("Executed successfully....")
except FileNotFoundError:
    print("File Not found")
finally:
    print("Done\n")

try:
    with open('my_file.txt','r') as handlerread:
        view =handlerread.read()
        print(view)
        print("File viewed successfully.... ")
except FileExistsError:
    print("File is'nt founded for reading")
finally:
    print("Done\n")


try:
    with open('my_file.txt','a') as handlerappend:
        append =handlerappend.write("\nThis is an appended text")
        print("appended successfully.....")

except FileNotFoundError:
    print("File not founded for appending")

finally:
    print("Done ")
