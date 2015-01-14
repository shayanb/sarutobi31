#SaruTobi31 - Play SaruTobi 24/7
![Saritubi](https://raw.githubusercontent.com/shayanb/sarutobi31/master/misc/sarutobi.png)


As the new update of [SaruTobi] is now more secure and prevents this type of attack, I'm releasing the code.

>"SaruTobi is literally Japanese for 'Monkey Fly', and this is pretty much the premise of the game. The user ... flings him across an 8-bit jungle collecting floating bitcoin along the way."
-[Christian Moss]

##What is SariTubi31
Before version 1.31, you could simulate game play and get bitcoin rewards without playing the game, hence without generating revenue for the developer.

##How
On the first run sarutobi31 will generate required bitcoin addresses and on the second run forward it will simulate the game play
- __genwallet.key__ holds the private keys and can be imported in MultiBit or Blockchain.info 
- __pubkeys.txt__ holds the public keys and is for the use of the script

##result
```
...
laravel_session=COOKIE
3
Donation Address: 3MXxfNZoifLYdS8wJTpvfeDNPt9ZWuMAaN Distance: 5946 Passphrase: XXX
{
    "thestatus": "sent",
    "amount": "0.0001"
}
laravel_session=COOKIE2
4
Donation Address: 3MXxfNZoifLYdS8wJTpvfeDNPt9ZWuMAaN Distance: 5418 Passphrase: XXX
{
    "thestatus": "sent",
    "amount": "0.0001"
}
...
```
##Am I rich?
I donated back half of what I earned from this script to Sarutobi, and will keep the rest to tip people in reddit like I usually do.

However the concern I have regarding this type of games is to overpollute the blockchain... Other than having too many dust transactions, when I was trying to send a transaction of 0.1 BTC from these addresses (Gathered by 1000 tips of 0.0001 BTC), MultiBit was not able to broadcast the transaction and had to rebuild it's blockchain database many times to show the right balance.

[SaruTobi]:https://itunes.apple.com/us/app/sarutobi/id932194840?mt=8&uo=4&at=1l3vuQn
[Christian Moss]:http://www.mandelduck.com/sarutobi/

##Why 31?

[![31](http://img.youtube.com/vi/Rk1z25gVZRA/0.jpg)](https://www.youtube.com/watch?v=Rk1z25gVZRA)

##Disclaimer
I'm not responsible for anything, anywhere, anytime
