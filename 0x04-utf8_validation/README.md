# Start of solving the utf-8 validation problem

**Write a method that determines if a given data set represents a valid UTF-8 encoding.**
- Prototype: `def validUTF8(data)`
- Return: `True` if data is a valid UTF-8 encoding, else return `False`
- A character in UTF-8 can be 1 to 4 bytes long
- The data set can contain multiple characters
- The data will be represented by a list of integers
- Each integer represents 1 byte of data, therefore you only need to handle the 8 least significant bits of each integer

```bash
tommy@ubuntu:~/0x04-utf8_validation$ ./0-main.py
True
True
False
tommy@ubuntu:~/0x04-utf8_validation$
```
