import requests

def help():
    print('''
    =========================================
    Hello, from the mcavatar community!
    Join our discord for help: https://discord.gg/6FSz8r3FpE
    Documenations coming soon...
    =========================================
    ''')

def uuid(username):
    link = f"https://api.mojang.com/users/profiles/minecraft/{username}"
    response = requests.get(link)
    uuid = response.json()['id']
    return uuid

def bust(uuid):
    link = f"https://minotar.net/bust/{uuid}"
    return link

def head(uuid):
    link=f"https://minotar.net/avatar/{uuid}"
    return link

def head3d(uuid):
    link=f"https://minotar.net/cube/{uuid}"
    return link

def body(uuid):
    link=f"https://minotar.net/body/{uuid}"
    return link

def skin(uuid):
    link=f"https://minotar.net/skin/{uuid}"
    return link

def dnskin(uuid):
    link=f"https://minotar.net/download/{uuid}"
    return link

def steve():
    link=f"https://minotar.net/avatar/MHF_Steve"
    return link

def alex():
    link=f"https://minotar.net/avatar/MHF_Alex"
    return link

def github():
    link=f"https://minotar.net/avatar/MHF_Github"
    return link
