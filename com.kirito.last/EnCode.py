import hashlib
import base64


def file_base64(file):
    while True:
        lines = file.readline()
        if not lines:
            break
            pass
        line = lines.strip()
        str1 = line.encode(encoding='utf-8')
        str2 = base64.b64encode(str1).decode()
        print(str2)
        hash1 = "19990909"
        sha1 = hashlib.md5(str2.encode(encoding='utf-8'))
        sha1.update(hash1.encode("utf-8"))
        osv = sha1.hexdigest()
        print(osv)
        with open('res/sercert.txt', 'a+') as file2:
            file2.write(osv+"\n")


if __name__ == '__main__':
    file = open('res/test.txt', mode='r', buffering=1, encoding='utf-8')
    file_base64(file)
