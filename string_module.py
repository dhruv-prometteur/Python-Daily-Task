import string
text="dhruv patel""\n"
print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.capwords(text))
print(type(string.digits))
print(string.hexdigits)
print(string.octdigits)
print(string.punctuation)
print(string.whitespace)



from string import Template
t=Template("my name is $name and i am $age year old")
print(t.substitute(name="Dhruv",age=23))
t=Template("hello $name . welcome to $place")
print(t.safe_substitute(name="Dhruv"))
r=t.get_identifiers()
print(r)