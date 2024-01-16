# SUF


**suf.py** is a simple script to search for a valid user by means of an id_rsa file. 

## **``Download``**

```bash
git clone https://github.com/0x-noname/suf.git
cd suf
chmod +x suf.py
```

### To view help options.

```bash
./suf.py --help
```
![](/suf_help.png)

### Launch script with another dictionary.

```bash
suf.py -t 192.168.1.89 -k id_rsa -t name.txt
```
![](/suf_with_dict.png)

### You can launch the script without the ``-w`` flag. 
```bash
suf.py -t 192.168.1.89 -k id_rsa
```

![](/suf_ok.png)

### For launch the script without the ``-w`` flag you need to have seclists installed.

```bash 
sudo apt install seclists
```

### You can change the default dictionary ``suf.py`` uses by changing the path in this line of code:

```bash
parser.add_argument('-w', '--wordlist', help="Path to user list file", default='/usr/share/seclists/Usernames/Names/names.txt', required=False)
```

for

```bash
parser.add_argument('-w', '--wordlist', help="Path to user list file", default='/Your/dictionary.txt', required=False)
```


![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2F0x-noname%2Fsuf&countColor=%23bd4658)
