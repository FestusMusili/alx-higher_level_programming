root@6963f7bb2ede:~/alx-higher_level_programming/0x03-python-data_structures# cat 1-element_at.py
#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return (None)
    if idx > len(my_list) - 1:
        return (None)
    return my_list[idx]
