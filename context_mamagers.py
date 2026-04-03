import json

# with open("myJson.json","r") as f:
#     data=json.load(f) 
#     print(data)


class ManagedFile:
    def __init__(self,filename):
        self.filename=filename

    def __enter__(self):
        print("enteringgg.....")
        self.file=open(self.filename,'w')
        return self.file
        

    def __exit__(self, exc_type, exc, tb):
        if self.file:
            self.file.close()
        if exc_type is not None:
            print("exception is handeled")
            
        print("exception: ",exc_type,exc)
        return True


with ManagedFile("myJson.json") as f:
    print("do some stufff")
    data={"a":"hello"}
    json.dump(data,f)
    f.somemthod()

print("continuing")



from contextlib import contextmanager

@contextmanager
def managed_file(filename,mode):
    f=open(filename,mode)

    try:
        yield f
    finally:
        f.close()


with managed_file("myJson.json","r") as f:
    data=json.load(f)
    print(data)