<p align="center">
  <img src="https://user-images.githubusercontent.com/101402577/201824633-9be36a69-1ab7-462f-a157-2a2e8163ff8c.png" style="width:15em; height: 15em;">
</p>

# PyLua
A fun way to use python for roblox game development.

## Getting Started
Clone the github repo.

```bash
git clone https://github.com/ItsNotAlexy/PyBlox
```
Next, Create a python file with your code thats written in python.

```py
#This is an example.

def Hello_Word():
  return "Hello World!"

Hello_World()
```

After that, Config the file input by going to startup.py and putting your file that has the code inside of the read function.
```py
with open('hello_world.py', "r") as f:
    pycode = f.read()
```

Next, You can change the directory on where the file should go to. For default it will go to the `Replicated Storage`
```py
with open("src/server/init.server.lua", "a") as f:
    f.write(complier.translate(pycode))
    f.close()
    print('Done.')
```
<br>

## Deploying Your Code
You need to deploy your code into the `Roblox Studio` via Rojo.

Inside of VSCode, Install the Rojo Extension.
<br>
![image](https://user-images.githubusercontent.com/101402577/201830390-4469beca-63b3-48d6-bb0f-7dc9abdd25f0.png)

Next do `ctrl` + `shift` + `p` and search Rojo.
<br>
![image](https://user-images.githubusercontent.com/101402577/201830832-5402a37e-557f-42cc-ad20-ccd21edbe3e2.png)

After that, Install the Rojo Roblox Studio plugin.
<br>
![image](https://user-images.githubusercontent.com/101402577/201830916-6d3f74b6-128c-4d4f-9abb-a19045f00e11.png)


After downloading the Rojo Roblox Studio plugin, You need to serve your code and changes. By pressing on the Rojo button.
<br>
![image](https://user-images.githubusercontent.com/101402577/201830037-15e9b248-588e-4a59-b677-18a57f69d2bf.png)

Go to Roblox Studio, And press the Rojo Plugin. Click connect and your code is now deployed!

