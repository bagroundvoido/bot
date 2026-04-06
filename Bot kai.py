import socket
import select
import requests
import threading
import re
import time
import struct
import urllib3
import random

#################################

RbGx = False
back = False
enc_client_id = None
inviteD = False
inviteD = False
back = False
invit_spam = False

#################################

SOCKS_VERSION = 5

#################################


def generate_random_color():
	color_list = [
    "[00FF00][b][c]",
    "[FFDD00][b][c]",
    "[3813F3][b][c]",
    "[FF0000][b][c]",
    "[0000FF][b][c]",
    "[FFA500][b][c]",
    "[DF07F8][b][c]",
    "[11EAFD][b][c]",
    "[DCE775][b][c]",
    "[A8E6CF][b][c]",
    "[7CB342][b][c]",
    "[FF0000][b][c]",
    "[FFB300][b][c]",
    "[90EE90][b][c]"
]
	random_color = random.choice(color_list)
	return  random_color
	
	
	
#################################


	
yout1 = b"\x06\x00\x00\x00{\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*o\x08\x81\x80\x83\xb6\x01\x1a)[18ffff]\xd8\xb5\xd8\xa7\xd8\xa6\xd8\xaf\xe3\x85\xa4\xd8\xa7\xd9\x84\xd8\xa8\xd9\x87\xd8\xa7\xd8\xa6\xd9\x85[18ffff]2\x02ME@N\xb0\x01\x13\xb8\x01\xdc)\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\tAO'-'TEAM\xf0\x01\x01\xf8\x01\xdc\x03\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x11\xd8\x02F"
yout2 = b'\x06\x00\x00\x00|\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*p\x08\xd6\xd1\xb9(\x1a![18ffff]\xef\xbc\xa8\xef\xbc\xac\xe3\x85\xa4Hassone.[18ffff]2\x02ME@G\xb0\x01\x13\xb8\x01\xcf\x1e\xd8\x01\xcc\xd6\xd0\xad\x03\xe0\x01\xed\xdc\x8d\xae\x03\xea\x01\x1d\xef\xbc\xb4\xef\xbc\xa8\xef\xbc\xa5\xe3\x85\xa4\xef\xbc\xa8\xef\xbc\xa5\xef\xbc\xac\xef\xbc\xac\xe0\xbf\x90\xc2\xb9\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x01'
yout3 = b'\x06\x00\x00\x00x\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*l\x08\xe9\xa7\xe9\x1b\x1a [18ffff]DS\xe3\x85\xa4WAJIHANO\xe3\x85\xa4[18ffff]2\x02ME@Q\xb0\x01\x14\xb8\x01\xca2\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x10.DICTATORS\xe3\x85\xa4\xe2\x88\x9a\xf0\x01\x01\xf8\x01\xc4\x02\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x0c\xd8\x02+'
yout4 = b'\x06\x00\x00\x00z\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*n\x08\xed\xd4\xa7\xa2\x02\x1a\x1f[18ffff]M8N\xe3\x85\xa4y\xe3\x85\xa4Fouad[18ffff]2\x02ME@O\xb0\x01\x13\xb8\x01\xa9#\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xdb\xdb\x8d\xae\x03\xea\x01\x0cGREAT\xe2\x80\xbfWALL\xf0\x01\x01\xf8\x01b\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\r\xd8\x023\xe0\x02\xc1\xb7\xf8\xb1\x03'
yout5 = b"\x06\x00\x00\x00\x84\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*x\x08\xb6\xc0\xf1\xcc\x01\x1a'[18ffff]\xd9\x85\xd9\x84\xd9\x83\xd8\xa9*\xd9\x84\xd9\x85\xd8\xb9\xd9\x88\xd9\x82\xd9\x8a\xd9\x86[18ffff]2\x02ME@G\xb0\x01\x05\xb8\x01\x82\x0b\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x15\xe9\xbf\x84\xef\xbc\xac\xef\xbc\xaf\xef\xbc\xb2\xef\xbc\xa4\xef\xbc\xb3\xe9\xbf\x84\xf0\x01\x01\xf8\x01>\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x05\xd8\x02\x0e"
yout6 = b'\x06\x00\x00\x00\x8e\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*\x81\x01\x08\xeb\x98\x88\x8e\x01\x1a"[18ffff]OP\xe3\x85\xa4BNL\xe3\x85\xa4\xe2\x9a\xa1\xe3\x85\xa4*[18ffff]2\x02ME@R\xb0\x01\x10\xb8\x01\xce\x16\xd8\x01\x84\xf0\xd2\xad\x03\xe0\x01\xa8\xdb\x8d\xae\x03\xea\x01\x1f\xe1\xb4\x8f\xe1\xb4\xa0\xe1\xb4\x87\xca\x80\xe3\x85\xa4\xe1\xb4\x98\xe1\xb4\x8f\xe1\xb4\xa1\xe1\xb4\x87\xca\x80\xe2\x9a\xa1\xf0\x01\x01\xf8\x01A\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x01\xe0\x02\xf3\x94\xf6\xb1\x03'
yout7 = b"\x06\x00\x00\x00\x8e\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*\x81\x01\x08\xb0\xa4\xdb\x80\x01\x1a'[18ffff]\xd9\x85\xd9\x83\xd8\xa7\xd9\x81\xd8\xad\xd8\xa9.\xe2\x84\x93\xca\x99\xe3\x80\xb5..[18ffff]2\x02ME@T\xb0\x01\x13\xb8\x01\xfc$\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xc1\xdb\x8d\xae\x03\xea\x01\x1d\xef\xbc\xad\xef\xbc\xa1\xef\xbc\xa6\xef\xbc\xa9\xef\xbc\xa1\xe3\x85\xa4\xe2\x8e\xb0\xe2\x84\x93\xca\x99\xe2\x8e\xb1\xf0\x01\x01\xf8\x01\xdb\x02\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x0f\xd8\x02>"
yout8 = b'\x06\x00\x00\x00y\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*m\x08\xfd\x8a\xde\xb4\x02\x1a\x1f[18ffff]ITZ\xe4\xb8\xb6MOHA\xe3\x85\xa42M[18ffff]2\x02ME@C\xb0\x01\n\xb8\x01\xdf\x0f\xd8\x01\xac\xd8\xd0\xad\x03\xe0\x01\xf2\xdc\x8d\xae\x03\xea\x01\x15\xe3\x80\x9dITZ\xe3\x80\x9e\xe1\xb5\x97\xe1\xb5\x89\xe1\xb5\x83\xe1\xb5\x90\xf8\x01\x02\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x0e\xd8\x026'
yout9 = b'\x06\x00\x00\x00w\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*k\x08\xc6\x99\xddp\x1a\x1b[18ffff]HEROSHIIMA1[18ffff]2\x02ME@I\xb0\x01\x01\xb8\x01\xe8\x07\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x1e\xef\xbc\xa8\xef\xbc\xa5\xef\xbc\xb2\xef\xbc\xaf\xef\xbc\xb3\xef\xbc\xa8\xef\xbc\xa9\xef\xbc\xad\xef\xbc\xa1\xef\xa3\xbf\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x01'
yout10 = b'\x06\x00\x00\x00p\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*d\x08\xde\x91\xb7Q\x1a\x1c[18ffff]SH\xe3\x85\xa4SHIMA|M[18ffff]2\x02ME@R\xb0\x01\x14\xb8\x01\xe7C\xd8\x01\xdd\xd6\xd0\xad\x03\xe0\x01\xca\xdb\x8d\xae\x03\xea\x01\tSH\xe3\x85\xa4Team\xf8\x014\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x11\xd8\x02G\xe0\x02\x89\xa0\xf8\xb1\x03'
yout11 = b'\x06\x00\x00\x00h\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*\\\x08\xa1\x9f\xb3\xf4\x01\x1a\x1b[18ffff]2JZ\xe3\x85\xa4POWER[18ffff]2\x02ME@M\xb0\x01\x13\xb8\x01\xa5(\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xec\xdb\x8d\xae\x03\xf0\x01\x01\xf8\x01\x9a\x01\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x0c\xd8\x02.\xe0\x02\xb2\xe9\xf7\xb1\x03'
yout12 = b'\x06\x00\x00\x00\x8f\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*\x82\x01\x08\xaa\xe5\xa4\xe3\x01\x1a-[18ffff]\xe3\x85\xa4\xd8\xb4\xd9\x83\xd8\xa7\xd9\x8e\xd9\x83\xd9\x80\xd9\x8a\xe3\x80\x8e\xe2\x85\xb5\xe1\xb4\x98\xe3\x80\x8f[18ffff]2\x02ME@Q\xb0\x01\x13\xb8\x01\xf2*\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xaf\xdb\x8d\xae\x03\xea\x01\x15\xe2\x80\xa2\xe3\x85\xa4\xe2\x93\x8b\xe2\x92\xbe\xe2\x93\x85\xe3\x85\xa4\xe2\x80\xa2\xf8\x01q\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x13\xd8\x02e\xe0\x02\xa0\xf1\xf7\xb1\x03'
yout14 = b'\x06\x00\x00\x00\x86\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*z\x08\xfd\x8b\xf4\xfa\x01\x1a$[18ffff]"\xd8\xaf\xd8\xb1\xd8\xa7\xd8\xba\xd9\x88\xd9\x86\xd9\x80\xd9\x88\xd9\x81"[18ffff]2\x02ME@F\xb0\x01\x13\xb8\x01\xec \xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x12\xe1\xb4\x98\xe1\xb4\x84\xe1\xb5\x80\xe1\xb5\x89\xe1\xb5\x83\xe1\xb5\x90\xf0\x01\x01\xf8\x01\xb0\x02\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x04\xd8\x02\t\xe0\x02\xf2\x94\xf6\xb1\x03'
yout15 = b'\x06\x00\x00\x00\x7f\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*s\x08\x90\xf6\x87\x15\x1a"[18ffff]V4\xe3\x85\xa4RIO\xe3\x85\xa46%\xe3\x85\xa4zt[18ffff]2\x02ME@M\xb0\x01\x13\xb8\x01\x95&\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb1\xdd\x8d\xae\x03\xea\x01\x0e\xe1\xb4\xa0\xe1\xb4\x80\xe1\xb4\x8d\xe1\xb4\x8f\xd1\x95\xf0\x01\x01\xf8\x01\xe2\x02\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x13\xd8\x02^\xe0\x02\x85\xff\xf5\xb1\x03'
yout16 = b'\x06\x00\x00\x00s\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*g\x08\xaa\x84\xc1r\x1a\x1f[18ffff]SA777RAWI\xe3\x85\xa4\xe3\x85\xa4[18ffff]2\x02ME@N\xb0\x01\x13\xb8\x01\xc8\x1b\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x0cSA7RAWI\xe3\x85\xa4TM\xf0\x01\x01\xf8\x01\xfe\x01\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\t\xd8\x02 '
yout17 = b'\x06\x00\x00\x00y\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*m\x08\xe7\xbf\xb6\x8f\x01\x1a\x1c[18ffff]SVG.NINJA\xe2\xbc\xbd[18ffff]2\x02ME@I\xb0\x01\x13\xb8\x01\x94\x1b\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\x85\xdb\x8d\xae\x03\xea\x01\x15\xe3\x85\xa4\xe3\x85\xa4\xe3\x85\xa4\xe3\x85\xa4???\xe3\x85\xa4\xe3\x85\xa4\xf0\x01\x01\xf8\x01o\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x10\xd8\x02?'
yout18 = b"\x06\x00\x00\x00\x9d\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*\x90\x01\x08\xa8\xe8\x91\xd7\x01\x1a.[18ffff]\xef\xbc\xa1\xef\xbc\xac\xef\xbc\x93\xef\xbc\xab\xef\xbc\xa5\xef\xbc\xa4\xe4\xba\x97\xef\xbc\xb9\xef\xbc\xb4\xe3\x85\xa4[18ffff]2\x02ME@N\xb0\x01\x13\xb8\x01\x97'\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x1e\xef\xbc\xa1\xef\xbc\xac\xef\xbc\x93\xef\xbc\xab\xef\xbc\xa5\xef\xbc\xa4\xe2\x80\xa2\xef\xbc\xb9\xef\xbc\xb4\xe2\x9c\x93\xf0\x01\x01\xf8\x01\xab\x02\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x10\xd8\x02@\xe0\x02\xe9\x80\xf8\xb1\x03"
yout19 = b'\x06\x00\x00\x00r\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*f\x08\x9b\x94\xaa\r\x1a\x1c[18ffff]FARAMAWY_1M.[18ffff]2\x02ME@I\xb0\x01\x01\xb8\x01\xe8\x07\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x12\xe2\x80\xa2\xe3\x85\xa4STRONG\xe3\x85\xa4\xe2\x80\xa2\xf0\x01\x01\xf8\x01X\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x01'
yout20 = b'\x06\x00\x00\x00p\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*d\x08\xde\x91\xb7Q\x1a\x1c[18ffff]SH\xe3\x85\xa4SHIMA|M[18ffff]2\x02ME@R\xb0\x01\x14\xb8\x01\xe7C\xd8\x01\xdd\xd6\xd0\xad\x03\xe0\x01\xca\xdb\x8d\xae\x03\xea\x01\tSH\xe3\x85\xa4Team\xf8\x014\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x11\xd8\x02G\xe0\x02\x89\xa0\xf8\xb1\x03'
yout21= b'\x06\x00\x00\x00h\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*\\\x08\xa1\x9f\xb3\xf4\x01\x1a\x1b[18ffff]2JZ\xe3\x85\xa4POWER[18ffff]2\x02ME@M\xb0\x01\x13\xb8\x01\xa5(\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xec\xdb\x8d\xae\x03\xf0\x01\x01\xf8\x01\x9a\x01\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x0c\xd8\x02.\xe0\x02\xb2\xe9\xf7\xb1\x03'
yout22 = b'\x06\x00\x00\x00\x8f\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*\x82\x01\x08\xaa\xe5\xa4\xe3\x01\x1a-[18ffff]\xe3\x85\xa4\xd8\xb4\xd9\x83\xd8\xa7\xd9\x8e\xd9\x83\xd9\x80\xd9\x8a\xe3\x80\x8e\xe2\x85\xb5\xe1\xb4\x98\xe3\x80\x8f[18ffff]2\x02ME@Q\xb0\x01\x13\xb8\x01\xf2*\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xaf\xdb\x8d\xae\x03\xea\x01\x15\xe2\x80\xa2\xe3\x85\xa4\xe2\x93\x8b\xe2\x92\xbe\xe2\x93\x85\xe3\x85\xa4\xe2\x80\xa2\xf8\x01q\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x13\xd8\x02e\xe0\x02\xa0\xf1\xf7\xb1\x03'
yout23 = b'\x06\x00\x00\x00\x86\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*z\x08\xfd\x8b\xf4\xfa\x01\x1a$[18ffff]"\xd8\xaf\xd8\xb1\xd8\xa7\xd8\xba\xd9\x88\xd9\x86\xd9\x80\xd9\x88\xd9\x81"[18ffff]2\x02ME@F\xb0\x01\x13\xb8\x01\xec \xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x12\xe1\xb4\x98\xe1\xb4\x84\xe1\xb5\x80\xe1\xb5\x89\xe1\xb5\x83\xe1\xb5\x90\xf0\x01\x01\xf8\x01\xb0\x02\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x04\xd8\x02\t\xe0\x02\xf2\x94\xf6\xb1\x03'
yout24 = b'\x06\x00\x00\x00s\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*g\x08\xaa\x84\xc1r\x1a\x1f[18ffff]SA777RAWI\xe3\x85\xa4\xe3\x85\xa4[18ffff]2\x02ME@N\xb0\x01\x13\xb8\x01\xc8\x1b\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x0cSA7RAWI\xe3\x85\xa4TM\xf0\x01\x01\xf8\x01\xfe\x01\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\t\xd8\x02 '
yout25 = b'\x06\x00\x00\x00y\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*m\x08\xe7\xbf\xb6\x8f\x01\x1a\x1c[18ffff]SVG.NINJA\xe2\xbc\xbd[18ffff]2\x02ME@I\xb0\x01\x13\xb8\x01\x94\x1b\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\x85\xdb\x8d\xae\x03\xea\x01\x15\xe3\x85\xa4\xe3\x85\xa4\xe3\x85\xa4\xe3\x85\xa4???\xe3\x85\xa4\xe3\x85\xa4\xf0\x01\x01\xf8\x01o\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x10\xd8\x02?'
yout26 = b"\x06\x00\x00\x00\x9d\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*\x90\x01\x08\xa8\xe8\x91\xd7\x01\x1a.[18ffff]\xef\xbc\xa1\xef\xbc\xac\xef\xbc\x93\xef\xbc\xab\xef\xbc\xa5\xef\xbc\xa4\xe4\xba\x97\xef\xbc\xb9\xef\xbc\xb4\xe3\x85\xa4[18ffff]2\x02ME@N\xb0\x01\x13\xb8\x01\x97'\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x1e\xef\xbc\xa1\xef\xbc\xac\xef\xbc\x93\xef\xbc\xab\xef\xbc\xa5\xef\xbc\xa4\xe2\x80\xa2\xef\xbc\xb9\xef\xbc\xb4\xe2\x9c\x93\xf0\x01\x01\xf8\x01\xab\x02\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x10\xd8\x02@\xe0\x02\xe9\x80\xf8\xb1\x03"
yout27 = b'\x06\x00\x00\x00r\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*f\x08\x9b\x94\xaa\r\x1a\x1c[18ffff]FARAMAWY_1M.[18ffff]2\x02ME@I\xb0\x01\x01\xb8\x01\xe8\x07\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x12\xe2\x80\xa2\xe3\x85\xa4STRONG\xe3\x85\xa4\xe2\x80\xa2\xf0\x01\x01\xf8\x01X\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x01'
yout28 = b"\x06\x00\x00\x00\x82\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*v\x08\xaa\xdd\xf1'\x1a\x1d[18ffff]BM\xe3\x85\xa4ABDOU_YT[18ffff]2\x02ME@G\xb0\x01\x13\xb8\x01\xd4$\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x1d\xe2\x80\xa2\xc9\xae\xe1\xb4\x87\xca\x9f\xca\x9f\xe1\xb4\x80\xca\x8d\xe1\xb4\x80\xd2\x93\xc9\xaa\xe1\xb4\x80\xc2\xb0\xf0\x01\x01\xf8\x01\x8e\x01\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x07\xd8\x02\x16"
yout29 = b'\x06\x00\x00\x00r\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*f\x08\x9a\xd6\xdcL\x1a-[18ffff]\xe1\xb4\x8d\xcd\xa1\xcd\x9co\xe3\x85\xa4\xef\xbc\xa8\xef\xbc\xa1\xef\xbc\xa6\xef\xbc\xa9\xef\xbc\xa4\xef\xbc\xa9[18ffff]2\x02ME@H\xb0\x01\x01\xb8\x01\xe8\x07\xea\x01\x15\xe1\xb4\x8d\xcd\xa1\xcd\x9co\xc9\xb4\xef\xbd\x93\xe1\xb4\x9b\xe1\xb4\x87\xca\x80\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x01'
yout30 = b'\x06\x00\x00\x00v\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*j\x08\xb6\x92\xa9\xc8\x01\x1a [18ffff]\xef\xbc\xaa\xef\xbc\xad\xef\xbc\xb2\xe3\x85\xa4200K[18ffff]2\x02ME@R\xb0\x01\x13\xb8\x01\xc3(\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\n3KASH-TEAM\xf8\x012\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x06\xd8\x02\x13\xe0\x02\x89\xa0\xf8\xb1\x03'
yout31 = b"\x06\x00\x00\x00\x92\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*\x85\x01\x08\xa2\xd3\xf4\x81\x07\x1a'[18ffff]\xd8\xb3\xd9\x80\xd9\x86\xd9\x80\xd8\xaf\xd8\xb1\xd9\x8a\xd9\x84\xd8\xa71M\xe3\x85\xa4[18ffff]2\x02ME@K\xb0\x01\x13\xb8\x01\xc1 \xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x1a\xef\xbc\xad\xef\xbc\xa6\xef\xbc\x95\xef\xbc\xb2\xef\xbc\xa8\xe3\x85\xa4\xe1\xb4\xa0\xc9\xaa\xe1\xb4\x98\xf0\x01\x01\xf8\x01\x8c\x01\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x0e\xd8\x024\xe0\x02\x87\xff\xf5\xb1\x03"
yout32 = b'\x06\x00\x00\x00|\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*p\x08\xe0\xe1\xdeu\x1a\x1a[18ffff]P1\xe3\x85\xa4Fahad[18ffff]2\x02ME@N\xb0\x01\x13\xb8\x01\xd0&\xd8\x01\xea\xd6\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x1a\xe3\x85\xa4\xef\xbc\xb0\xef\xbc\xa8\xef\xbc\xaf\xef\xbc\xa5\xef\xbc\xae\xef\xbc\xa9\xef\xbc\xb8\xc2\xb9\xf0\x01\x01\xf8\x01\x9e\x03\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x0b\xd8\x02*'
yout33 = b'\x06\x00\x00\x00\x82\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*v\x08\xc5\xcf\x94\x8b\x02\x1a\x18[18ffff]@EL9YSAR[18ffff]2\x02ME@P\xb0\x01\x13\xb8\x01\x86+\xd8\x01\xa2\xd7\xd0\xad\x03\xe0\x01\x89\xae\x8f\xae\x03\xea\x01\x1d-\xc9\xaa\xe1\xb4\x8d\xe1\xb4\x8d\xe1\xb4\x8f\xca\x80\xe1\xb4\x9b\xe1\xb4\x80\xca\x9fs\xe2\xac\x86\xef\xb8\x8f\xf8\x01j\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x14\xd8\x02\xe2\x02\xe0\x02\x9f\xf1\xf7\xb1\x03'
yout34 = b'\x06\x00\x00\x00x\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*l\x08\xa9\x81\xe6^\x1a\x1e[18ffff]STRONG\xe3\x85\xa4CRONA[18ffff]2\x02ME@J\xb0\x01\x13\xb8\x01\xd8$\xd8\x01\xd8\xd6\xd0\xad\x03\xe0\x01\x92\xdb\x8d\xae\x03\xea\x01\x12\xe2\x80\xa2\xe3\x85\xa4STRONG\xe3\x85\xa4\xe2\x80\xa2\xf0\x01\x01\xf8\x01q\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x14\xd8\x02\xbc\x01'
yout35 = b'\x06\x00\x00\x00\x7f\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*s\x08\xeb\x8d\x97\xec\x01\x1a&[18ffff]\xd8\xb9\xd9\x80\xd9\x85\xd9\x80\xd8\xaf\xd9\x86\xd9\x8a\xd9\x80\xd8\xaa\xd9\x80\xd9\x88[18ffff]2\x02ME@F\xb0\x01\x13\xb8\x01\xd3\x1a\xd8\x01\xaf\xd7\xd0\xad\x03\xe0\x01\xf4\xdc\x8d\xae\x03\xea\x01\rOSIRIS\xe3\x85\xa4MASR\xf8\x01o\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x13\xd8\x02\\\xe0\x02\xf4\x94\xf6\xb1\x03'
yout36 = b'\x06\x00\x00\x00\x7f\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*s\x08\xb4\xff\xa3\xef\x01\x1a\x1c[18ffff]ZAIN_YT_500K[18ffff]2\x02ME@K\xb0\x01\x13\xb8\x01\xa3#\xd8\x01\xa2\xd7\xd0\xad\x03\xe0\x01\xbb\xdb\x8d\xae\x03\xea\x01\x1b\xe1\xb6\xbb\xe1\xb5\x83\xe1\xb6\xa4\xe1\xb6\xb0\xe3\x85\xa4\xe1\xb5\x97\xe1\xb5\x89\xe1\xb5\x83\xe1\xb5\x90\xf0\x01\x01\xf8\x01\\\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x0b\xd8\x02('
yout37 = b'\x06\x00\x00\x00\x8f\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*\x82\x01\x08\x86\xa7\x9e\xa7\x0b\x1a([18ffff]\xe2\x80\x94\xcd\x9e\xcd\x9f\xcd\x9e\xe2\x98\x85\xef\xbc\xa2\xef\xbc\xac\xef\xbc\xb2\xef\xbc\xb8[18ffff]2\x02ME@d\xb0\x01\x13\xb8\x01\xe3\x1c\xe0\x01\xf2\x83\x90\xae\x03\xea\x01!\xe3\x85\xa4\xef\xbc\xa2\xef\xbc\xac\xef\xbc\xb2\xef\xbc\xb8\xe3\x85\xa4\xef\xbc\xb4\xef\xbc\xa5\xef\xbc\xa1\xef\xbc\xad\xe3\x85\xa4\xf8\x01u\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x13\xd8\x02Y\xe0\x02\xc1\xb7\xf8\xb1\x03'
yout38 = b'\x06\x00\x00\x00\x85\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*y\x08\xc3\xcf\xe5H\x1a([18ffff]\xe3\x85\xa4BEE\xe2\x9c\xbfSTO\xe3\x85\xa4\xe1\xb5\x80\xe1\xb4\xb5\xe1\xb4\xb7[18ffff]2\x02ME@Q\xb0\x01\x14\xb8\x01\xffP\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xc1\xdb\x8d\xae\x03\xea\x01\x15TIK\xe2\x9c\xbfTOK\xe1\xb5\x80\xe1\xb4\xb1\xe1\xb4\xac\xe1\xb4\xb9\xf0\x01\x01\xf8\x01\xc8\x02\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x13\xd8\x02q'
yout39 = b'\x06\x00\x00\x00\x94\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*\x87\x01\x08\x97\xd5\x9a.\x1a%[18ffff]\xd8\xb9\xd9\x86\xd9\x83\xd9\x88\xd8\xb4\xe1\xb4\x80\xc9\xb4\xe1\xb4\x8b\xe3\x85\xa4[18ffff]2\x02ME@P\xb0\x01\x13\xb8\x01\xe8(\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x1f\xe1\xb4\x80\xc9\xb4\xe1\xb4\x8b\xe1\xb4\x9c\xea\x9c\xb1\xca\x9c\xe3\x85\xa4\xe1\xb4\x9b\xe1\xb4\x87\xe1\xb4\x80\xe1\xb4\x8d\xf0\x01\x01\xf8\x01\xb6\x03\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\n\xd8\x02"\xe0\x02\xf2\x94\xf6\xb1\x03'
yout40 = b'\x06\x00\x00\x00\x8a\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*~\x08\xf7\xdf\xda\\\x1a/[18ffff]\xef\xbc\xa1\xef\xbc\xac\xef\xbc\xa8\xef\xbc\xaf\xef\xbc\xad\xef\xbc\xb3\xef\xbc\xa9_\xef\xbc\xb9\xef\xbc\xb4\xe2\x9c\x93[18ffff]2\x02ME@P\xb0\x01\x13\xb8\x01\xb9*\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xc1\xdb\x8d\xae\x03\xea\x01\x0cALHOMSI~TEAM\xf0\x01\x01\xf8\x01\x8e\x0e\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x13\xd8\x02S\xe0\x02\xc3\xb7\xf8\xb1\x03'
yout41 = b'\x06\x00\x00\x00\x86\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*z\x08\xb5\xdd\xec\x8e\x01\x1a%[18ffff]\xd8\xa7\xd9\x88\xd9\x81\xe3\x80\x80\xd9\x85\xd9\x86\xd9\x83\xe3\x85\xa4\xe2\x9c\x93[18ffff]2\x02ME@K\xb0\x01\x13\xb8\x01\xdd#\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x18\xef\xbc\xaf\xef\xbc\xa6\xe3\x85\xa4\xef\xbc\xb4\xef\xbc\xa5\xef\xbc\xa1\xef\xbc\xad\xe3\x85\xa4\xf0\x01\x01\xf8\x01\xe8\x02\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x13\xd8\x02Q'
yout42 = b'\x06\x00\x00\x00\x8b\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*\x7f\x08\x81\xf4\xba\xf8\x01\x1a%[18ffff]\xef\xbc\xa7\xef\xbc\xa2\xe3\x85\xa4\xef\xbc\xae\xef\xbc\xaf\xef\xbc\x91\xe3\x81\x95[18ffff]2\x02ME@N\xb0\x01\x0c\xb8\x01\xbd\x11\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb1\xdd\x8d\xae\x03\xea\x01\x1a\xef\xbc\xa7\xef\xbc\xb2\xef\xbc\xa5\xef\xbc\xa1\xef\xbc\xb4__\xef\xbc\xa2\xef\xbc\xaf\xef\xbc\xb9\xf8\x018\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x0c\xd8\x02-\xe0\x02\x85\xff\xf5\xb1\x03'
yout43 = b'\x06\x00\x00\x00o\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*c\x08\xfb\x9d\xb9\xae\x06\x1a\x1c[18ffff]BT\xe3\x85\xa4BadroTV[18ffff]2\x02ME@@\xb0\x01\x13\xb8\x01\xe7\x1c\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\x91\xdb\x8d\xae\x03\xea\x01\nBadro_TV_F\xf0\x01\x01\xf8\x01\x91\x1a\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\n\xd8\x02!'
yout44 = b"\x06\x00\x00\x00s\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*g\x08\xc4\xe5\xe1>\x1a'[18ffff]\xd8\xb5\xd8\xa7\xd8\xa6\xd8\xaf~\xd8\xa7\xd9\x84\xd8\xba\xd9\x86\xd8\xa7\xd8\xa6\xd9\x85[18ffff]2\x02ME@J\xb0\x01\x14\xb8\x01\xceP\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x03Z7F\xf0\x01\x01\xf8\x01\xd0\x19\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x14\xd8\x02\x9c\x01"
yout45 = b'\x06\x00\x00\x00\x85\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*y\x08\xfd\xa4\xa6i\x1a$[18ffff]\xd8\xb2\xd9\x8a\xd9\x80\xd8\xb1\xc9\xb4\xcc\xb67\xcc\xb6\xca\x80\xe3\x85\xa4[18ffff]2\x02ME@M\xb0\x01\x13\xb8\x01\xe1(\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x19\xc2\xb7\xe3\x85\xa4\xe3\x85\xa4N\xe3\x85\xa47\xe3\x85\xa4R\xe3\x85\xa4\xe3\x85\xa4\xc2\xb7\xf0\x01\x01\xf8\x01\x8f\t\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x13\xd8\x02k'
yout46 = b'\x06\x00\x00\x00y\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*m\x08\xcc\xb9\xcc\xd4\x06\x1a"[18ffff]\xd8\xa8\xd9\x88\xd8\xad\xd8\xa7\xd9\x83\xd9\x80\xd9\x80\xd9\x80\xd9\x85[18ffff]2\x02ME@9\xb0\x01\x07\xb8\x01\xca\x0c\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x11*\xef\xbc\x97\xef\xbc\xaf\xef\xbc\xab\xef\xbc\xa1\xef\xbc\xad*\xf0\x01\x01\xf8\x01\xad\x05\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x01'
yout47 = b'\x06\x00\x00\x00e\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*Y\x08\xe8\xbd\xc9b\x1a [18ffff]\xe3\x80\x8cvip\xe3\x80\x8dDR999FF[18ffff]2\x02ME@Q\xb0\x01\x10\xb8\x01\x94\x16\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xf0\x01\x01\xf8\x01\xa0\x04\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x0c\xd8\x02+'
yout48 = b'\x06\x00\x00\x00\x82\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*v\x08\x86\xb7\x84\xf1\x01\x1a&[18ffff]\xd8\xa2\xd9\x86\xd9\x8a\xd9\x80\xd9\x80\xd9\x84\xd8\xa7\xce\x92\xe2\x92\x91\xe3\x85\xa4[18ffff]2\x02ME@Q\xb0\x01\x13\xb8\x01\x82)\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x13\xce\x92\xe2\x92\x91\xe3\x85\xa4MAFIA\xe3\x85\xa4\xef\xa3\xbf\xf0\x01\x01\xf8\x01\x95\x04\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x13\xd8\x02W'
yout49 = b'\x06\x00\x00\x00u\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*i\x08\xb4\xbe\xde\x83\x02\x1a [18ffff]SPONGEBOB!\xe3\x85\xa4\xe4\xba\x97[18ffff]2\x02ME@N\xb0\x01\x14\xb8\x01\x842\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\x96\xdb\x8d\xae\x03\xea\x01\x0cALHOMSI~TEAM\xf0\x01\x01\xf8\x01\xbd\x03\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x13\xd8\x02{'
yout50 = b'\x06\x00\x00\x00u\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*i\x08\xb4\xbe\xde\x83\x02\x1a [18ffff]SPONGEBOB!\xe3\x85\xa4\xe4\xba\x97[18ffff]2\x02ME@N\xb0\x01\x14\xb8\x01\x842\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\x96\xdb\x8d\xae\x03\xea\x01\x0cALHOMSI~TEAM\xf0\x01\x01\xf8\x01\xbd\x03\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x13\xd8\x02{'
yout51 = b'\x06\x00\x00\x00z\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x028c8d99a21bn\x08\xed\xd4\xa7\xa2\x02\x1a\x1f[18ffff]M8N\xe3\x85\xa4y\xe3\x85\xa4Fouad[18ffff]2\x02ME@O\xb0\x01\x13\xb8\x01\xa9#\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xdb\xdb\x8d\xae\x03\xea\x01\x0cGREAT\xe2\x80\xbfWALL\xf0\x01\x01\xf8\x01b\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\r\xd8\x023\xe0\x02\xc1\xb7\xf8\xb1\x03'
yout_list = [yout1,yout2,yout3,yout4,yout5,yout6,yout7,yout8,yout9,yout10,yout11,yout12,yout14,yout15,yout16,yout17,yout18,yout19,yout20,yout21,yout22,yout23,yout24,yout25,yout26,yout27,yout28,yout29,yout30,yout31,yout32,yout33,yout34,yout35,yout36,yout37,yout38,yout39,yout40,yout41,yout42,yout43,yout44,yout45,yout46,yout47,yout48,yout49,yout50,yout51]

                      
               
#################################


def GT500_msg(mess, data, clin):
    data = data[12:22]
    api_url = f"https://long-message-gt-500-karm.vercel.app/PaCKet-Msg-Gt-500?Id={data}&Msg={mess}&Key=GT-500-QF"
    try:
        response = requests.get(api_url)
        response.raise_for_status() 
        packet = response.text
        clin.send(bytes.fromhex(packet.strip('"')))
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"    
                        

#################################

                                
class Proxy:
    def __init__(self):
        self.username = "1"
        self.password = "1"
        self.last_check_time = 0
        self.comand = True
        self.yout_list = yout_list
        self.RbGx = False
         
              
#################################

        
    def spam__invite(self, data, remote):
        global invit_spam
        while invit_spam:
            try:
                for _ in range(5):
                    remote.send(data)
                    time.sleep(0.04)
                time.sleep(0.2)
            except:
                pass
            
                                
#################################

    def fake_friend(self, client, id: str):
        if len(id) == 8:
            packet = '060000007708d4d7faba1d100620022a6b08cec2f1051a1b5b3030464630305d2b2b2020202047504c00005b3030464630305d32024d454049b00101b801e807d801d4d8d0ad03e001b2dd8dae03ea011eefbca8efbca5efbcb2efbcafefbcb3efbca8efbca9efbcadefbca1efa3bf8002fd98a8dd03900201d00201'
            packet = re.sub(r'cec2f105', id, packet)
            client.send(bytes.fromhex(packet))
        elif len(id) == 10:
            packet = '060000006f08d4d7faba1d100620022a6308fb9db9ae061a1c5b3030464630305d2b2be385a447504c000020205b3030464630305d32024d454040b00113b801e71cd801d4d8d0ad03e00191db8dae03ea010a5a45522d49534b494e47f00101f801911a8002fd98a8dd03900201d0020ad80221'
            packet = re.sub(r'fb9db9ae06', id, packet)
            client.send(bytes.fromhex(packet))
        else:
            print(id)
            

    def Encrypt_ID(self, id):
        try:
            number = int(id)
            encoded_bytes = []
            while True:
                byte = number & 0x7F   
                number >>= 7
                if number:
                    byte |= 0x80     
                encoded_bytes.append(byte)
                if not number:
                    break

            return ''.join(f'{b:02x}' for b in encoded_bytes)

        except Exception as e:
            print("فشل التشفير:", e)
            return None
      


#################################


    def handle_client(self, connection):
        version, nmethods = connection.recv(2)
        methods = self.get_available_methods(nmethods, connection)
        if 2 not in set(methods):
            connection.close()
            return
        connection.sendall(bytes([SOCKS_VERSION, 2]))
        if not self.verify_credentials(connection):
            return
        version, cmd, _, address_type = connection.recv(4)
        if address_type == 1:
            address = socket.inet_ntoa(connection.recv(4))
        elif address_type == 3:
            domain_length = connection.recv(1)[0]
            address = connection.recv(domain_length)
            address = socket.gethostbyname(address)
        port = int.from_bytes(connection.recv(2), 'big', signed=False)
        try:
            if cmd == 1:
                remote = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                remote.connect((address, port))
                bind_address = remote.getsockname()
            else:
                connection.close()
                return
            addr = int.from_bytes(socket.inet_aton(bind_address[0]), 'big', signed=False)
            port = bind_address[1]
            reply = b''.join([
                SOCKS_VERSION.to_bytes(1, 'big'),
                int(0).to_bytes(1, 'big'),
                int(0).to_bytes(1, 'big'),
                int(1).to_bytes(1, 'big'),
                addr.to_bytes(4, 'big'),
                port.to_bytes(2, 'big')
            ])
        except Exception as e:
            reply = self.generate_failed_reply(address_type, 5)
        connection.sendall(reply)
        if reply[1] == 0 and cmd == 1:
            self.exchange_loop(connection, remote)
        connection.close()
       
#################################
    def msg_help(self):
        ent_packet = f"1200000F2F08{self.EncryptedPlayerid}101220022AA21E08{self.EncryptedPlayerid}10{self.EncryptedPlayerid}22FA1C0A5B625D5B635D5B4646303030305D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D0A0A5B625D5B635D5B4646464646465D2D2057656C636F6D6520546F205242475820426F54205B4646303030305DE29DA40A0A5B625D5B635D5B4646464646465D2D205468652076657273696F6E203A205B322E315D207C7C2047543530300A0A5B625D5B635D5B4646303030305D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D0A0A0A5B625D5B635D5B4646464630305D2D20426F742020417661696C61626C652020636F6D6D616E6473203A0A0A0A5B625D5B635D5B4646464646465D2D204F70656E2061207465616D206F66203A0A5B625D5B635D5B3030464630305D20203D3E202FF09F8D8635730A5B625D5B635D5B3030464630305D20203D3E202FF09F8D8636730A0A20200A5B625D5B635D5B4646464646465D2D20372079656172206261646765203A0A5B625D5B635D5B3030464630305D20203D3E202FF09F8D8637790A0A20200A5B625D5B635D5B4646464646465D2D20362079656172206261646765203A0A5B625D5B635D5B3030464630305D20203D3E202FF09F8D8636790A0A202020200A5B625D5B635D5B4646464646465D2D2046616B6520667269656E64203A0A5B625D5B635D5B3030464630305D20203D3E202FF09F8D866964205B69645D0A0A202020200A5B625D5B635D5B4646464646465D2D2041646420596F755475626572203A0A5B625D5B635D5B3030464630305D20203D3E202FF09F8D8679740A0A202020200A5B625D5B635D5B4646464646465D2D205370616D206D656D62657273686970207265717565737473203A0A5B625D5B635D5B3030464630305D20203D3E202FF09F8D86696E760A0A202020200A5B625D5B635D5B4646464646465D2D2053707920496E20746865207371756164203A200A5B625D5B635D5B3030464630305D20203D3E202FF09F8D867370790A0A20200A5B625D5B635D5B4646464646465D2D2053707920496E2074686520726F6F6D203A200A5B625D5B635D5B3030464630305D20203D3E202FF09F8D86737079726F6F6D0A0A20202020202020200A5B625D5B635D5B4646464646465D2D2046616B652031306B204469616D6F6E64203A200A5B625D5B635D5B3030464630305D20203D3E202FF09F8D86646D0A0A0A5B625D5B635D5B4646464646465D2D2046616B652035356B20676F6C64203A200A5B625D5B635D5B3030464630305D20203D3E202FF09F8D86676F6C640A0A202020200A5B625D5B635D5B4646464646465D2D20556E6C6F636B20616C6C20736B696E203A200A5B625D5B635D5B3030464630305D20203D3E202FF09F8D86736B696E0A0A0A5B625D5B635D5B4646464646465D2D205375706572204D6F6465203A200A5B625D5B635D5B3030464630305D20203D3E202FF09F8D8673757065720A0A0A5B625D5B635D5B4646464646465D2D20456E7472616E63652064616E636573203A200A5B625D5B635D5B3030464630305D20203D3E202FF09F8D86656E74646E630A0A20200A5B625D5B635D5B4646464630305D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D0A200A2020200A5B625D5B635D5B4646464646465D2D20466F6C6C6F77206D65206F6E2054656C656772616D206163636F756E7420203A2040526267786465760A0A5B625D5B635D5B4646464646465D2D2054686520676F616C206973203A203230303020666F6C6C6F7765727320536F20666F6C6C6F77206D65206F6E206D79206368616E6E656C0A0A20202020200A5B625D5B635D5B4646464630305D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D0A00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000200A28A083CABD064A250A0B4F5554E385A4414C56494E10E7B290AE0320D20128C1B7F8B103420737526164616121520261726A640A5E68747470733A2F2F6C68332E676F6F676C6575736572636F6E74656E742E636F6D2F612F414367386F634A614D4363556F6C4355397148576C6C2D79506E76516D3354782D304630304D30596A633350437737326F7A44503D7339362D63100118017200"

        if self.sock1200:
            self.sock1200.send(bytes.fromhex(ent_packet))
        else:
            print("[!] sock0500 not assigned.")    


                 
#############################


 
    def gen_squad5(self, id):
        ent_packet = f"05000001ff08{id}1005203a2af20308{id}12024d451801200432f70208{id}1209424c52585f4d6f642b1a024d4520d78aa5b40628023085cbd1303832421880c38566fa96e660c19de061d998a36180a89763aab9ce64480150c90158e80792010801090a12191a1e209801c901c00101e801018802039202029603aa0208080110e43218807daa0207080f10e4322001aa0205080210e432aa0205081810e432aa0205081a10e432aa0205081c10e432aa0205082010e432aa0205082210e432aa0205082110e432aa0205081710e432aa0205082310e432aa0205082b10e432aa0205083110e432aa0205083910e432aa0205083d10e432aa0205084110e432aa0205084910e432aa0205084d10e432aa0205081b10e432aa0205083410e432aa0205082810e432aa0205082910e432c2022812041a0201041a0508501201631a060851120265661a0f0848120b0104050607f1a802f4a8022200ea0204100118018a03009203009803b7919db30ba20319c2b27854e19687e197a95fe191ade192aae197a95945e19687e20301523a011a403e50056801721e313732303237323231313638373535353930315f736f3278687a61366e347801820103303b30880180e0aecdacceba8e19a20100b00114ea010449444332fa011e313732303237323231313638373535383330335f71356f79736b3934716d"
        if self.sock0500:
            self.sock0500.send(bytes.fromhex(ent_packet))
        else:
            print("[!] sock0500 not assigned.")


            
 

###############################
###############################


            
    
    
    def skinaaaat(self, idd):
    
        skins = [
    "c091e660","c191e660","c291e660","c391e660","c491e660","c591e660","c691e660","c791e660","c891e660","c991e660","ca91e660","cb91e660","cc91e660","cd91e660","ce91e660","cf91e660","d091e660","d191e660","d291e660","d391e660","d491e660","d591e660","d691e660","d791e660","d891e660","d991e660","da91e660","db91e660","dc91e660","dd91e660","de91e660","df91e660","e091e660","e191e660","e291e660","e391e660","e491e660","e591e660","e691e660","e791e660","e891e660","e991e660","ea91e660","eb91e660","ec91e660","ed91e660","ee91e660","ef91e660","f091e660","f191e660","f291e660","f391e660","f491e660","f591e660","f691e660","f791e660","f891e660","f991e660","fa91e660","fb91e660","fc91e660","fd91e660","fe91e660","ff91e660","8092e660","8192e660","8292e660","8392e660","8492e660","8592e660","8692e660","8792e660","8892e660","8992e660","8a92e660","8b92e660","8c92e660","8d92e660","8e92e660","8f92e660","9092e660","9192e660","9292e660","9392e660","9492e660","9592e660","9692e660","9792e660","9892e660","9992e660","9a92e660","9b92e660","9c92e660","9d92e660","9e92e660","9f92e660","a092e660","a192e660","a292e660","a392e660","a492e660","a592e660","a692e660","a792e660","a892e660","a992e660","aa92e660","ab92e660","ac92e660","ad92e660","ae92e660","af92e660","b092e660","b192e660","b292e660","b392e660","b492e660","b592e660","b692e660","b792e660","b892e660","b992e660","ba92e660","bb92e660","bc92e660","bd92e660","be92e660","bf92e660","c092e660","c192e660","c292e660","c392e660","c492e660","c592e660","c692e660","c792e660","c892e660","c992e660","ca92e660","cb92e660","cc92e660","cd92e660","ce92e660","cf92e660","d092e660","d192e660","d292e660","d392e660","d492e660","d592e660","d692e660","d792e660","d892e660","d992e660","da92e660","db92e660","dc92e660","dd92e660","de92e660","df92e660","e092e660","e192e660","e292e660","e592e660","e692e660","e792e660","e892e660","ea92e660","ec92e660","ed92e660","ee92e660","ef92e660","f092e660","f192e660","f292e660","f392e660","f492e660","f592e660","f692e660","f792e660","f892e660","f992e660","fa92e660","fb92e660","fc92e660","fd92e660","fe92e660","ff92e660","8093e660","8193e660","8293e660","8393e660","8493e660","8593e660","8693e660","8793e660","8893e660","8993e660","8a93e660","8b93e660","8c93e660","8d93e660","8e93e660","8f93e660","9093e660","9193e660","9293e660","9393e660","9493e660","9593e660","9693e660","9793e660","9893e660","9993e660","9a93e660","9b93e660","9c93e660","9d93e660","9e93e660","9f93e660","a093e660","a193e660","a293e660","a393e660","a493e660","a593e660","a693e660","a793e660","a893e660","a993e660","ac93e660","ad93e660","ae93e660","af93e660","b193e660","b293e660","b393e660","b493e660","b593e660","b693e660","b793e660","b893e660","b993e660","ba93e660","bb93e660","bc93e660","bd93e660","be93e660","bf93e660","c093e660","c193e660","c293e660","c393e660","c493e660","c593e660","c693e660","c793e660","c893e660","c993e660","ca93e660","cb93e660","cc93e660","cd93e660","ce93e660","cf93e660","d093e660","d193e660","d293e660","d393e660","d493e660","d593e660","d693e660","d793e660","d893e660","d993e660","da93e660","db93e660","dc93e660","dd93e660","de93e660","df93e660","e093e660","e193e660","e293e660","e393e660","e493e660","e593e660","e693e660","e793e660","e893e660","e993e660","ea93e660","eb93e660","ec93e660","ed93e660","ee93e660","ef93e660","f093e660","f193e660","f293e660","f393e660","f493e660","f593e660","f693e660","f793e660","f893e660","f993e660","fa93e660","fb93e660","fc93e660","fd93e660","fe93e660","ff93e660","8094e660","8194e660","8294e660","8394e660","8494e660","8594e660","8694e660","8794e660","8894e660","8994e660","8a94e660","8b94e660","8c94e660","8d94e660","8e94e660","8f94e660","9094e660","9194e660","9294e660","9394e660","9494e660","9594e660","9694e660","9794e660","9894e660","9994e660","9a94e660","9b94e660","9c94e660","9d94e660","9e94e660","9f94e660","a094e660","a194e660","a294e660","a394e660","a494e660","a594e660","a694e660","a794e660","a894e660","a994e660","aa94e660","ab94e660","ac94e660","ad94e660","ae94e660","af94e660","b094e660","b194e660","b294e660","b394e660","b494e660","b594e660","b694e660","b794e660","b894e660","b994e660","ba94e660","bb94e660","bc94e660","bd94e660","be94e660","bf94e660","c094e660","c194e660","c294e660","c394e660","c494e660","c594e660","c694e660","c794e660","c894e660","c994e660","ca94e660","cb94e660","cc94e660","cd94e660","ce94e660","cf94e660","d094e660","d194e660","d294e660","d394e660","d494e660","d594e660","d694e660","d794e660","d994e660","da94e660","db94e660","dc94e660","dd94e660","de94e660","df94e660","e094e660","e194e660","e294e660","e394e660","e494e660","e594e660","e694e660","e794e660","e894e660","e994e660","ea94e660","eb94e660","ec94e660","ed94e660","ee94e660","ef94e660","f094e660","f194e660","f294e660","f394e660","f494e660","f594e660","f694e660","f794e660","f894e660","f994e660","fa94e660","fb94e660","fc94e660","fd94e660","fe94e660","ff94e660","8095e660","8195e660","8295e660","8395e660","8495e660","8595e660","8695e660","8795e660","8895e660","8995e660","8a95e660","8b95e660","8c95e660","8d95e660","8e95e660","9095e660","9195e660","9295e660","9395e660","9495e660","9595e660","9695e660","9795e660","9895e660","9995e660","9a95e660","9b95e660","9c95e660","9d95e660","9e95e660","9f95e660","a095e660","a195e660","a295e660","a395e660","a495e660","a595e660","a695e660","a795e660","a895e660","a995e660","aa95e660","ab95e660","ac95e660","ad95e660","ae95e660","af95e660","b095e660","b195e660","b295e660","b395e660","b495e660","b595e660","b695e660","b795e660","b895e660","b995e660","ba95e660","bb95e660","bc95e660","bd95e660","be95e660","bf95e660","c095e660","c195e660","c295e660","c395e660","c495e660","c595e660","c695e660","c795e660","c895e660","c995e660","ca95e660","cb95e660","cc95e660","cd95e660","ce95e660","cf95e660","d095e660","d195e660","d295e660","d395e660","d495e660","d595e660","d695e660","d795e660","d895e660","d995e660","da95e660","db95e660","dc95e660","dd95e660","de95e660","df95e660","e095e660","e195e660","e295e660","e395e660","e495e660","e595e660","e695e660","e795e660","e895e660","e995e660","ea95e660","eb95e660","ec95e660","ed95e660","ee95e660","ef95e660","f095e660","f195e660","f295e660","f395e660","f495e660","f595e660","f695e660","f795e660","f895e660","f995e660","fa95e660","fb95e660","fc95e660","fd95e660","fe95e660","ff95e660","8096e660","8196e660","8296e660","8396e660","8496e660","8596e660","8696e660","8796e660","8896e660","8996e660","8a96e660","8b96e660","8c96e660","8d96e660","8e96e660","8f96e660","9096e660","9196e660","9296e660","9396e660","9496e660","9596e660","9696e660","9796e660","9896e660","9996e660","9a96e660","9b96e660","9c96e660","9d96e660","9e96e660","9f96e660","a096e660","a196e660","a296e660","a396e660","a496e660","a596e660","a696e660","a796e660","a896e660","a996e660","aa96e660","ab96e660","ac96e660","ad96e660","ae96e660","af96e660","b096e660","b196e660","b296e660","b396e660","b496e660","b596e660","b696e660","b796e660","b896e660","b996e660","ba96e660","bb96e660","bc96e660","bd96e660","be96e660","bf96e660","c096e660","c196e660","c296e660","c396e660","c496e660","c596e660","c696e660","c796e660","c896e660","c996e660","ca96e660","cb96e660","cc96e660","cd96e660","ce96e660","cf96e660","d096e660","d196e660","d296e660","d396e660","d496e660","d596e660","d696e660","d796e660","d896e660","d996e660","da96e660","db96e660","dc96e660","dd96e660","de96e660","df96e660","e096e660","e196e660","e296e660","e396e660","e496e660","e596e660","e696e660","e796e660","e896e660","e996e660","ea96e660","eb96e660","ec96e660","ed96e660","ee96e660","ef96e660","f096e660","f196e660","f296e660","f396e660","f496e660","f596e660","f696e660","f796e660","f896e660","f996e660","fa96e660","fb96e660","fc96e660","fd96e660","fe96e660","ff96e660","8097e660","8197e660","8297e660","8397e660","8497e660","8597e660","8697e660","8797e660","8897e660","8997e660","8a97e660","8b97e660","8c97e660","8d97e660","8e97e660","8f97e660","9097e660","9197e660","9297e660","9397e660","9497e660","9597e660","9697e660","9797e660","9897e660","9997e660","9a97e660","9b97e660","9c97e660","9d97e660","9e97e660","9f97e660","a097e660","a197e660","a297e660","a397e660","a497e660","a597e660","a697e660","a797e660","a897e660","a997e660","aa97e660","ab97e660","ac97e660","ad97e660","ae97e660","af97e660","b097e660","b197e660","b297e660","b397e660","b497e660","b597e660","b697e660","b797e660","b897e660","b997e660","ba97e660","bb97e660","bc97e660","bd97e660","be97e660","bf97e660","c097e660","c197e660","c297e660","c397e660","c497e660","c597e660","c697e660","c797e660","c897e660","c997e660","ca97e660","cb97e660","cc97e660","cd97e660","ce97e660","cf97e660","d097e660","d197e660","d297e660","d397e660","d497e660","d597e660","d697e660","d797e660","d897e660","d997e660","da97e660","db97e660","dc97e660","dd97e660","de97e660","df97e660","e097e660","e197e660","e297e660","e397e660","e497e660","e597e660","e697e660","e797e660","e897e660","e997e660","ea97e660","eb97e660","ec97e660","ed97e660","ee97e660","ef97e660","f097e660","f197e660","f297e660","f397e660","f497e660","f597e660","f697e660","fa97e660","fb97e660","fc97e660","fd97e660","fe97e660","ff97e660","8098e660","8198e660","8298e660","8398e660","8498e660","8598e660","8698e660","8798e660","8898e660","8998e660","8a98e660","8b98e660","8c98e660","8d98e660","8e98e660","8f98e660","9098e660","9198e660","9298e660","9398e660","9498e660","9598e660","9698e660","9798e660","9898e660","9998e660","9a98e660","9b98e660","9c98e660","9d98e660","9e98e660","9f98e660","a098e660","a198e660","a298e660","a398e660","a498e660","a598e660","a698e660","a798e660","a898e660","a998e660","aa98e660","ab98e660","ac98e660","ad98e660","ae98e660","af98e660","b098e660","b198e660","b298e660","b398e660","b498e660","b598e660","b698e660","b798e660","b898e660","b998e660","ba98e660","bb98e660","bc98e660","bd98e660","be98e660","bf98e660","c098e660","c198e660","c298e660","c398e660","c498e660","c598e660","c698e660","c798e660","c898e660","c998e660","ca98e660","cb98e660","cc98e660","cd98e660","ce98e660","cf98e660","d098e660","d198e660","d298e660","d398e660","d498e660","d598e660","d698e660","d798e660","d898e660","d998e660","da98e660","db98e660","dc98e660","dd98e660","de98e660","df98e660","e098e660","e198e660","e298e660","e398e660","e498e660","e598e660","e698e660","e798e660","e898e660","e998e660","ea98e660","eb98e660","ec98e660","ed98e660","ee98e660","ef98e660","f098e660","f198e660","f298e660","f398e660","f498e660","f598e660","f698e660","f798e660","f898e660","f998e660","fa98e660","fb98e660","fc98e660","fd98e660","fe98e660","ff98e660","8099e660","8199e660","8299e660","8399e660","8499e660","8599e660","8699e660","8799e660","8899e660","8999e660","8a99e660","8b99e660","8c99e660","8d99e660","8e99e660","8f99e660","9099e660","9199e660","9299e660","9399e660","9499e660","9599e660","9699e660","9799e660","9899e660","9999e660","9a99e660","9b99e660","9c99e660","9d99e660","9e99e660","9f99e660","a099e660","a199e660","a299e660","a399e660","a499e660","a599e660","a699e660","a799e660","a899e660","a999e660","aa99e660","ab99e660","ac99e660","ad99e660","ae99e660","af99e660","b199e660","b299e660","b399e660","b499e660","b599e660","b699e660","b799e660","b899e660","b999e660","ba99e660","bb99e660","bc99e660","bd99e660","be99e660","bf99e660","c099e660","c199e660","c299e660","c399e660","c499e660","c599e660","c699e660","c799e660","c899e660","c999e660","ca99e660","cb99e660","cc99e660","cd99e660","ce99e660","cf99e660","d099e660","d199e660","d299e660","d399e660","d499e660","d599e660","d699e660","d799e660","d899e660","d999e660","da99e660","db99e660","dc99e660","dd99e660","de99e660","df99e660","e099e660","e199e660","e299e660","e399e660","e499e660","e599e660","e699e660","e799e660","e899e660","e999e660","ea99e660","eb99e660","ec99e660","ed99e660","ee99e660","ef99e660","f099e660","f199e660","f299e660","f399e660","f499e660","f599e660","f699e660","f799e660","f899e660","f999e660","fa99e660","fb99e660","fc99e660","fd99e660","fe99e660","ff99e660","809ae660","819ae660","829ae660","839ae660","849ae660","859ae660","869ae660","879ae660","889ae660","899ae660","8a9ae660","8b9ae660","8c9ae660","8d9ae660","8e9ae660","8f9ae660","909ae660","919ae660","929ae660","939ae660","949ae660","959ae660","969ae660","979ae660","989ae660","999ae660","9a9ae660","9b9ae660","9c9ae660","9d9ae660","9e9ae660","9f9ae660","a09ae660","a19ae660","a29ae660","a39ae660","a49ae660","a59ae660","a69ae660","a79ae660","a89ae660","a99ae660","aa9ae660","ab9ae660","ac9ae660","ad9ae660","ae9ae660","af9ae660","b09ae660","b19ae660","b29ae660","b39ae660","b49ae660","b59ae660","b69ae660","b79ae660","b89ae660","b99ae660","ba9ae660","bb9ae660","bc9ae660","bd9ae660","be9ae660","bf9ae660","c09ae660","c19ae660","c29ae660","c39ae660","c49ae660","c59ae660","c69ae660","c79ae660","c89ae660","c99ae660","ca9ae660","cb9ae660","cc9ae660","cd9ae660","ce9ae660","cf9ae660","d09ae660","d19ae660","d29ae660","d39ae660","d49ae660","d59ae660","d69ae660","d79ae660","d89ae660","d99ae660","da9ae660","db9ae660","dc9ae660","dd9ae660","de9ae660","df9ae660","e09ae660","e19ae660","e29ae660","e39ae660","e49ae660","e59ae660","e69ae660","e79ae660","e89ae660","e99ae660","ea9ae660","eb9ae660","ec9ae660","ed9ae660","ee9ae660","ef9ae660","f09ae660","f19ae660","f49ae660","f59ae660","f69ae660","f79ae660","f89ae660","f99ae660","fa9ae660","fb9ae660","fc9ae660","fd9ae660","fe9ae660","ff9ae660","829be660","839be660","849be660","859be660","869be660","879be660","889be660","899be660","8a9be660","8b9be660","8c9be660","8d9be660","8e9be660","8f9be660","909be660","919be660","929be660","939be660","949be660","959be660","969be660","979be660","989be660","999be660","9a9be660","9b9be660","9c9be660","9d9be660","9e9be660","9f9be660","a09be660","a19be660","a29be660","a39be660","a49be660","a59be660","a69be660","a79be660","a89be660","a99be660","aa9be660","ab9be660","ac9be660","ad9be660","ae9be660","af9be660","b09be660","b19be660","b29be660","b39be660","b49be660","b59be660","b69be660","b79be660","b89be660","b99be660","ba9be660","bb9be660","bc9be660","bd9be660","be9be660","bf9be660","c09be660","c19be660","c29be660","c39be660","c49be660","c59be660","c69be660","c79be660","c89be660","c99be660","ca9be660","cb9be660","cc9be660","cd9be660","ce9be660","cf9be660","d09be660","d19be660","d29be660","d39be660","d49be660","d59be660","d69be660","d79be660","d89be660","d99be660","da9be660","db9be660","dc9be660","dd9be660","de9be660","df9be660","e09be660","e19be660","e29be660","e39be660","e49be660","e59be660","e69be660","e79be660","e89be660","e99be660","ea9be660","eb9be660","ec9be660","ed9be660","ee9be660","ef9be660","f09be660","f19be660","f29be660","f39be660","f49be660","f59be660","f69be660","f79be660","f89be660","f99be660","fa9be660","fb9be660","fc9be660","fd9be660","fe9be660","ff9be660","809ce660","819ce660","829ce660","839ce660","849ce660","859ce660","869ce660","879ce660","889ce660","8a9ce660","8b9ce660","8c9ce660","8d9ce660","8e9ce660","8f9ce660","909ce660","a993e860","aa93e860","ab93e860","ac93e860","ad93e860","ae93e860","af93e860","b093e860","b193e860","b293e860","b393e860","b493e860","b593e860","b693e860","b793e860","b893e860","b993e860","ba93e860","bb93e860","bc93e860","bd93e860","be93e860","bf93e860","c093e860","c193e860","c293e860","c393e860","c493e860","c593e860","c693e860","c793e860","c893e860","c993e860","ca93e860","cb93e860","cc93e860","cd93e860","ce93e860","cf93e860","d193e860","d293e860","d393e860","d493e860","d593e860","d693e860","d793e860","d893e860","d993e860","da93e860","db93e860","dc93e860","dd93e860","de93e860","df93e860","e093e860","e193e860","e293e860","e393e860","e493e860","e593e860","e693e860","e793e860","e893e860","e993e860","ea93e860","eb93e860","ec93e860","ed93e860","919be860","929be860","939be860","959be860","969be860","979be860","989be860","999be860","9a9be860","9b9be860","9d9be860","9e9be860","9f9be860","a09be860","a19be860","a29be860","a39be860","a49be860","a59be860","a69be860","a79be860","a89be860","a99be860","aa9be860","ab9be860","ac9be860","ad9be860","ae9be860","af9be860","b09be860","b19be860","b29be860","b39be860","b49be860","b59be860","b69be860","b79be860","b89be860","b99be860","ba9be860","bb9be860","bc9be860","bd9be860","be9be860","bf9be860","c09be860","c19be860","c29be860","c39be860","c49be860","c59be860","c69be860","c79be860","c89be860","c99be860","ca9be860","f9a2e860","faa2e860","fba2e860","fca2e860","fda2e860","fea2e860","ffa2e860","80a3e860","81a3e860","82a3e860","83a3e860","84a3e860","85a3e860","86a3e860","87a3e860","88a3e860","89a3e860","8aa3e860","8ba3e860","8ca3e860","8da3e860","8ea3e860","8fa3e860","90a3e860","91a3e860","92a3e860","93a3e860","94a3e860","95a3e860","96a3e860","97a3e860","98a3e860","99a3e860","9aa3e860","9ba3e860","9ca3e860","9da3e860","9ea3e860","9fa3e860","a0a3e860","a1a3e860","a2a3e860","a3a3e860","a4a3e860","a5a3e860","a6a3e860","a7a3e860","a8a3e860","a9a3e860","aaa3e860","aba3e860","aca3e860","ada3e860","aea3e860","afa3e860","b0a3e860","b1a3e860","b2a3e860","b3a3e860","b4a3e860","b5a3e860","e0aae860","e1aae860","e2aae860","e3aae860","e4aae860","e5aae860","e6aae860","e7aae860","e8aae860","e9aae860","eaaae860","ebaae860","ecaae860","edaae860","eeaae860","efaae860","f0aae860","f1aae860","f2aae860","f3aae860","f4aae860","f5aae860","f6aae860","f7aae860","f8aae860","f9aae860","faaae860","fbaae860","fcaae860","fdaae860","feaae860","ffaae860","80abe860","81abe860","82abe860","83abe860","84abe860","85abe860","86abe860","87abe860","88abe860","89abe860","8aabe860","8babe860","8cabe860","8dabe860","8eabe860","8fabe860","90abe860","91abe860","92abe860","95abe860","c8b2e860","c9b2e860","cab2e860","cbb2e860","ceb2e860","cfb2e860","d0b2e860","d1b2e860","d2b2e860","d3b2e860","d4b2e860","d5b2e860","d6b2e860","d7b2e860","d8b2e860","d9b2e860","dab2e860","dbb2e860","dcb2e860","ddb2e860","deb2e860","dfb2e860","e1b2e860","e2b2e860","e3b2e860","e4b2e860","e5b2e860","e6b2e860","e7b2e860","e8b2e860","e9b2e860","eab2e860","ebb2e860","ecb2e860","edb2e860","eeb2e860","efb2e860","f0b2e860","f1b2e860","f3b2e860","f6b2e860","f7b2e860","f8b2e860","f9b2e860","fab2e860","fbb2e860","fcb2e860","fdb2e860","feb2e860","ffb2e860","80b3e860","81b3e860","82b3e860","83b3e860","84b3e860","85b3e860","86b3e860","adbae860","aebae860","afbae860","b0bae860","b1bae860","b2bae860","b3bae860","b4bae860","b5bae860","b6bae860","b7bae860","b8bae860","b9bae860","babae860","bbbae860","bcbae860","bdbae860","bebae860","bfbae860","c0bae860","c1bae860","c2bae860","c3bae860","c4bae860","c5bae860","c6bae860","c7bae860","c8bae860","c9bae860","cdbae860","cebae860","cfbae860","d0bae860","d1bae860","d2bae860","d3bae860","d5bae860","d6bae860","d7bae860","d8bae860","d9bae860","dabae860","dcbae860","ddbae860","debae860","dfbae860","e0bae860","e1bae860","e2bae860","e3bae860","e4bae860","e8bae860","e9bae860","eabae860","ebbae860","ecbae860","edbae860","eebae860","efbae860","f0bae860","f1bae860","98c2e860","99c2e860","9ac2e860","9bc2e860","9cc2e860","9dc2e860","9ec2e860","9fc2e860","a0c2e860","a1c2e860","a2c2e860","a3c2e860","a4c2e860","a5c2e860","a6c2e860","a7c2e860","a8c2e860","a9c2e860","aac2e860","abc2e860","acc2e860","adc2e860","aec2e860","afc2e860","b0c2e860","b1c2e860","b2c2e860","b3c2e860","b4c2e860","b5c2e860","b6c2e860","b7c2e860","b8c2e860","b9c2e860","bec2e860","bfc2e860","c0c2e860","c1c2e860","c2c2e860","c3c2e860","c4c2e860","c5c2e860","c6c2e860","c7c2e860","c8c2e860","c9c2e860","cac2e860","cbc2e860","ccc2e860","cdc2e860","cec2e860","cfc2e860","d0c2e860","d1c2e860","80cae860","81cae860","82cae860","83cae860","84cae860","85cae860","86cae860","87cae860","88cae860","89cae860","8acae860","8bcae860","8ccae860","8dcae860","8ecae860","8fcae860","90cae860","91cae860","92cae860","93cae860","94cae860","95cae860","96cae860","97cae860","98cae860","99cae860","9acae860","9bcae860","9ccae860","9dcae860","9ecae860","9fcae860","a0cae860","a1cae860","a2cae860","a3cae860","a4cae860","a5cae860","a6cae860","a7cae860","a8cae860","a9cae860","aacae860","abcae860","accae860","adcae860","e8d1e860","e9d1e860","ead1e860","ebd1e860","ecd1e860","edd1e860","eed1e860","efd1e860","f0d1e860","f1d1e860","f2d1e860","f3d1e860","f4d1e860","f5d1e860","f6d1e860","f7d1e860","f8d1e860","f9d1e860","fad1e860","fbd1e860","fcd1e860","fdd1e860","fed1e860","ffd1e860","80d2e860","81d2e860","82d2e860","83d2e860","84d2e860","85d2e860","86d2e860","87d2e860","88d2e860","89d2e860","8ad2e860","8bd2e860","8cd2e860","8dd2e860","8ed2e860","8fd2e860","90d2e860","91d2e860","92d2e860","93d2e860","94d2e860","95d2e860","96d2e860","d0d9e860","d1d9e860","d2d9e860","d3d9e860","d4d9e860","d5d9e860","d6d9e860","d7d9e860","d8d9e860","d9d9e860","dad9e860","dbd9e860","dcd9e860","ddd9e860","ded9e860","dfd9e860","e0d9e860","e1d9e860","e2d9e860","e3d9e860","e4d9e860","e5d9e860","e6d9e860","e7d9e860","e8d9e860","e9d9e860","ead9e860","ebd9e860","ecd9e860","edd9e860","eed9e860","efd9e860","f0d9e860","f1d9e860","f2d9e860","b8e1e860","b9e1e860","bae1e860","bbe1e860","bce1e860","bde1e860","bee1e860","bfe1e860","c0e1e860","c1e1e860","c2e1e860","c3e1e860","c4e1e860","c5e1e860","c6e1e860","c7e1e860","c8e1e860","c9e1e860","cae1e860","cbe1e860","cce1e860","cde1e860","cee1e860","cfe1e860","d0e1e860","d1e1e860","d2e1e860","d3e1e860","d4e1e860","d5e1e860","d6e1e860","d7e1e860","d8e1e860","d9e1e860","dae1e860","dbe1e860","dce1e860","dde1e860","dee1e860","dfe1e860","e0e1e860","e1e1e860","e2e1e860","a0e9e860","a1e9e860","a2e9e860","a3e9e860","a4e9e860","a5e9e860","a6e9e860","a7e9e860","a8e9e860","a9e9e860","aae9e860","abe9e860","ace9e860","ade9e860","aee9e860","afe9e860","b0e9e860","b1e9e860","b2e9e860","b3e9e860","b4e9e860","b5e9e860","b6e9e860","b7e9e860","b8e9e860","b9e9e860","bae9e860","bbe9e860","bce9e860","bde9e860","bee9e860","88f1e860","89f1e860","8af1e860","8bf1e860","8cf1e860","8df1e860","8ef1e860","8ff1e860","90f1e860","91f1e860","92f1e860","93f1e860","94f1e860","95f1e860","96f1e860","97f1e860","98f1e860","99f1e860","9af1e860","9bf1e860","9cf1e860","9df1e860","9ef1e860","9ff1e860","a0f1e860","a1f1e860","a2f1e860","a3f1e860","a4f1e860","a5f1e860","a6f1e860","a7f1e860","a8f1e860","a9f1e860","aaf1e860","abf1e860","acf1e860","adf1e860","aef1e860","aff1e860","f0f8e860","f1f8e860","f2f8e860","f3f8e860","f4f8e860","f5f8e860","f6f8e860","f7f8e860","f8f8e860","f9f8e860","faf8e860","fbf8e860","fcf8e860","fdf8e860","fef8e860","fff8e860","80f9e860","81f9e860","82f9e860","83f9e860","84f9e860","85f9e860","86f9e860","87f9e860","88f9e860","89f9e860","8af9e860","8bf9e860","8cf9e860","8df9e860","8ef9e860","8ff9e860","90f9e860","91f9e860","92f9e860","94f9e860","95f9e860","96f9e860","97f9e860","98f9e860","99f9e860","9af9e860","9bf9e860","9cf9e860","9df9e860","9ef9e860","9ff9e860","a0f9e860","a1f9e860","a2f9e860","a3f9e860","a4f9e860","a5f9e860","a6f9e860","a7f9e860","a8f9e860","a9f9e860","aaf9e860","abf9e860","acf9e860","adf9e860","aef9e860","aff9e860","b0f9e860","b1f9e860","d880e960","d980e960","da80e960","db80e960","dc80e960","dd80e960","de80e960","df80e960","e080e960","e180e960","e280e960","e380e960","e480e960","e580e960","e680e960","e780e960","e880e960","e980e960","ea80e960","eb80e960","ec80e960","ee80e960","ef80e960","f080e960","f180e960","f280e960","f380e960","f480e960","f580e960","f680e960","f780e960","f880e960","f980e960","fa80e960","fb80e960","fc80e960","c088e960","c188e960","c288e960","c388e960","c488e960","c588e960","c688e960","c788e960","c888e960","c988e960","ca88e960","cb88e960","cc88e960","cd88e960","ce88e960","cf88e960","d088e960","d188e960","d288e960","d388e960","d488e960","d588e960","d688e960","d788e960","d888e960","d988e960","da88e960","db88e960","dc88e960","dd88e960","de88e960","df88e960","e088e960","e188e960","e288e960","e388e960","e488e960","e588e960","e688e960","e788e960","e888e960","e988e960","ea88e960","eb88e960","ec88e960","a890e960","a990e960","aa90e960","ab90e960","ac90e960","ad90e960","ae90e960","af90e960","b090e960","b190e960","b290e960","b390e960","b490e960","b590e960","b690e960","b790e960","b890e960","b990e960","ba90e960","bb90e960","bc90e960","bd90e960","be90e960","bf90e960","c090e960","c190e960","c290e960","c390e960","c490e960","c590e960","c690e960","c790e960","c890e960","c990e960","ca90e960","cb90e960","cc90e960","cd90e960","ce90e960","cf90e960","d090e960","d190e960","d290e960","d390e960","d490e960","d590e960","d690e960","9098e960","9198e960","9298e960","9398e960","9498e960","9598e960","9698e960","9798e960","9898e960","9998e960","9a98e960","9b98e960","9c98e960","9d98e960","9e98e960","9f98e960","a098e960","a198e960","a298e960","a398e960","a498e960","a598e960","a698e960","a798e960","a898e960","a998e960","aa98e960","ab98e960","ac98e960","ad98e960","ae98e960","af98e960","b098e960","b198e960","b298e960","b398e960","b498e960","b598e960","b698e960","b798e960","b898e960","b998e960","ea98e960","eb98e960","ec98e960","ed98e960","ee98e960","ef98e960","f098e960","f198e960","8096a361","8196a361","8296a361","8396a361","8496a361","8596a361","8696a361","8796a361","8896a361","8996a361","8a96a361","8b96a361","8c96a361","8d96a361","8e96a361","8f96a361","9096a361","9196a361","9296a361","9396a361","9496a361","9596a361","9696a361","9796a361","9896a361","9996a361","9a96a361","9b96a361","9c96a361","9d96a361","9e96a361","9f96a361","a096a361","a196a361","a296a361","a396a361","a496a361","a596a361","a696a361","a796a361","a896a361","a996a361","aa96a361","ab96a361","ac96a361","ad96a361","ae96a361","af96a361","b096a361","b196a361","b296a361","b396a361","b496a361","b596a361","b696a361","b796a361","b896a361","b996a361","ba96a361","bb96a361","bc96a361","bd96a361","be96a361","bf96a361","c096a361","c196a361","c296a361","c396a361","c496a361","c596a361","c696a361","c796a361","c896a361","c996a361","ca96a361","cb96a361","cc96a361","cd96a361","ce96a361","cf96a361","d096a361","d196a361","d296a361","d396a361","d496a361","d596a361","d696a361","d796a361","d896a361","d996a361","da96a361","db96a361","dc96a361","dd96a361","de96a361","df96a361","e096a361","e196a361","e396a361","e496a361","e596a361","e696a361","e796a361","e896a361","e996a361","ea96a361","eb96a361","ec96a361","ed96a361","ee96a361","ef96a361","f096a361","f196a361","f296a361","f396a361","f496a361","f596a361","f696a361","f796a361","f896a361","f996a361","fa96a361","fb96a361","fc96a361","fd96a361","fe96a361","ff96a361","8097a361","8197a361","8297a361","8397a361","8497a361","8597a361","8697a361","8797a361","8897a361","8997a361","8a97a361","8b97a361","8c97a361","8d97a361","8e97a361","8f97a361","9097a361","9197a361","9297a361","9397a361","9497a361","9597a361","9697a361","9797a361","9897a361","9997a361","9a97a361","9b97a361","9c97a361","9d97a361","9e97a361","9f97a361","a097a361","a197a361","a297a361","a397a361","a497a361","a597a361","a697a361","a797a361","a897a361","a997a361","aa97a361","ab97a361","ac97a361","ad97a361","ae97a361","af97a361","b097a361","b197a361","b297a361","b397a361","b497a361","b597a361","b697a361","b797a361","b897a361","b997a361","ba97a361","bb97a361","bc97a361","bd97a361","be97a361","bf97a361","c097a361","c197a361","c297a361","c397a361","c497a361","c597a361","c697a361","c797a361","c897a361","c997a361","ca97a361","cb97a361","cc97a361","cd97a361","ce97a361","cf97a361","d097a361","d197a361","d297a361","d397a361","d497a361","d597a361","d697a361","d797a361","d897a361","d997a361","da97a361","db97a361","dc97a361","dd97a361","de97a361","df97a361","e097a361","e197a361","e297a361","e397a361","e497a361","e597a361","e697a361","e797a361","e897a361","e997a361","ea97a361","eb97a361","ec97a361","ed97a361","ee97a361","ef97a361","f097a361","f197a361","f297a361","f397a361","f497a361","f597a361","f697a361","f797a361","f897a361","f997a361","fa97a361","fb97a361","fc97a361","fd97a361","fe97a361","ff97a361","8098a361","8198a361","8298a361","8398a361","8498a361","8598a361","8698a361","8798a361","8898a361","8998a361","8a98a361","8b98a361","8c98a361","8d98a361","8e98a361","8f98a361","9098a361","9198a361","9298a361","9398a361","9498a361","9598a361","9698a361","9798a361","9898a361","9998a361","9a98a361","9b98a361","9c98a361","9d98a361","9e98a361","9f98a361","a098a361","a198a361","a298a361","a398a361","a498a361","a598a361","a698a361","a798a361","a898a361","a998a361","aa98a361","ab98a361","ac98a361","ad98a361","ae98a361","af98a361","b098a361","b198a361","b298a361","b398a361","b498a361","b598a361","b698a361","b798a361","b898a361","b998a361","ba98a361","bb98a361","bc98a361","bd98a361","be98a361","bf98a361","c098a361","c198a361","c298a361","c398a361","c498a361","c598a361","c698a361","c798a361","c898a361","c998a361","ca98a361","cb98a361","cc98a361","cd98a361","ce98a361","cf98a361","d098a361","d198a361","d298a361","d398a361","d498a361","d598a361","d698a361","d798a361","d898a361","d998a361","da98a361","db98a361","dc98a361","dd98a361","de98a361","df98a361","e098a361","e198a361","e298a361","e398a361","e498a361","e598a361","e698a361","e798a361","e898a361","e998a361","ea98a361","eb98a361","ec98a361","ed98a361","ee98a361","ef98a361","f098a361","f198a361","f298a361","f398a361","f498a361","f698a361","f798a361","f898a361","f998a361","fa98a361","fb98a361","fc98a361","fd98a361","fe98a361","ff98a361","8099a361","8199a361","8299a361","8399a361","8499a361","8599a361","8699a361","8799a361","8899a361","8999a361","8a99a361","8b99a361","8c99a361","8d99a361","8e99a361","8f99a361","9099a361","9199a361","9299a361","9399a361","9499a361","9599a361","9699a361","9799a361","9899a361","9999a361","9a99a361","9b99a361","9c99a361","9d99a361","9e99a361","9f99a361","a099a361","a199a361","a299a361","a399a361","a499a361","a599a361","a699a361","a799a361","a899a361","a999a361","aa99a361","ab99a361","ac99a361","ad99a361","ae99a361","af99a361","b099a361","b199a361","b299a361","b399a361","b499a361","b599a361","b699a361","b799a361","b899a361","b999a361","ba99a361","bb99a361","bc99a361","bd99a361","be99a361","bf99a361","c099a361","c199a361","c299a361","c399a361","c499a361","c599a361","c699a361","c799a361","c899a361","c999a361","ca99a361","cb99a361","cc99a361","cd99a361","ce99a361","cf99a361","d099a361","d199a361","d299a361","d399a361","d499a361","d599a361","d699a361","d799a361","d899a361","d999a361","da99a361","db99a361","dc99a361","dd99a361","de99a361","df99a361","e099a361","e199a361","e299a361","e399a361","e499a361","e599a361","e699a361","e799a361","e899a361","e999a361","ea99a361","eb99a361","ec99a361","ed99a361","ee99a361","ef99a361","f099a361","f199a361","f299a361","f399a361","f499a361","f599a361","f699a361","f799a361","f899a361","f999a361","fa99a361","fb99a361","fc99a361","fd99a361","fe99a361","ff99a361","809aa361","819aa361","829aa361","839aa361","849aa361","859aa361","869aa361","879aa361","889aa361","899aa361","8a9aa361","8b9aa361","8c9aa361","8d9aa361","8e9aa361","8f9aa361","909aa361","919aa361","929aa361","939aa361","949aa361","959aa361","969aa361","979aa361","989aa361","999aa361","9a9aa361","9b9aa361","9c9aa361","9d9aa361","9e9aa361","9f9aa361","a09aa361","a19aa361","a29aa361","a39aa361","a49aa361","a59aa361","a69aa361","a79aa361","a89aa361","a99aa361","aa9aa361","ab9aa361","ac9aa361","ad9aa361","ae9aa361","af9aa361","b09aa361","b19aa361","b29aa361","b39aa361","b49aa361","b59aa361","b69aa361","b79aa361","b89aa361","b99aa361","ba9aa361","bb9aa361","bc9aa361","bd9aa361","be9aa361","bf9aa361","c09aa361","c19aa361","c29aa361","c39aa361","c49aa361","c59aa361","c69aa361","c79aa361","c89aa361","c99aa361","ca9aa361","cb9aa361","cc9aa361","cd9aa361","ce9aa361","cf9aa361","d09aa361","d19aa361","d29aa361","d39aa361","d49aa361","d59aa361","d69aa361","d79aa361","d89aa361","d99aa361","da9aa361","db9aa361","dc9aa361","dd9aa361","de9aa361","df9aa361","e09aa361","e19aa361","e29aa361","e39aa361","e49aa361","e59aa361","e69aa361","e79aa361","e89aa361","e99aa361","ea9aa361","eb9aa361","ec9aa361","ed9aa361","ee9aa361","ef9aa361","f09aa361","f19aa361","f29aa361","f39aa361","f49aa361","f59aa361","f69aa361","f79aa361","f89aa361","f99aa361","fa9aa361","fb9aa361","fc9aa361","fd9aa361","fe9aa361","ff9aa361","809ba361","819ba361","829ba361","839ba361","849ba361","859ba361","869ba361","879ba361","889ba361","899ba361","8a9ba361","8b9ba361","8c9ba361","8d9ba361","8e9ba361","8f9ba361","909ba361","919ba361","929ba361","939ba361","949ba361","959ba361","969ba361","979ba361","989ba361","999ba361","9a9ba361","9b9ba361","9c9ba361","9d9ba361","9e9ba361","9f9ba361","a09ba361","a19ba361","a29ba361","a39ba361","a49ba361","a59ba361","a69ba361","a79ba361","a89ba361","a99ba361","ab9ba361","ac9ba361","ad9ba361","ae9ba361","af9ba361","b09ba361","b19ba361","b49ba361","b59ba361","b69ba361","b79ba361","b89ba361","b99ba361","ba9ba361","bb9ba361","bc9ba361","bd9ba361","be9ba361","bf9ba361","c09ba361","c19ba361","c29ba361","c39ba361","c49ba361","c59ba361","c69ba361","c79ba361","c89ba361","c99ba361","ca9ba361","cb9ba361","cc9ba361","cd9ba361","ce9ba361","cf9ba361","d09ba361","d19ba361","d29ba361","d39ba361","d49ba361","d59ba361","d69ba361","d79ba361","d89ba361","d99ba361","da9ba361","db9ba361","dc9ba361","dd9ba361","de9ba361","df9ba361","e09ba361","e19ba361","e29ba361","e39ba361","e49ba361","e59ba361","e69ba361","e79ba361","e89ba361","e99ba361","ea9ba361","eb9ba361","ec9ba361","ed9ba361","ee9ba361","ef9ba361","f09ba361","f19ba361","f29ba361","f39ba361","f49ba361","f59ba361","f69ba361","f79ba361","f89ba361","f99ba361","fa9ba361","fb9ba361","fc9ba361","fd9ba361","fe9ba361","ff9ba361","809ca361","819ca361","829ca361","839ca361","849ca361","859ca361","869ca361","879ca361","889ca361","899ca361","8a9ca361","8b9ca361","8c9ca361","8d9ca361","8e9ca361","8f9ca361","909ca361","919ca361","929ca361","939ca361","949ca361","959ca361","969ca361","979ca361","989ca361","999ca361","9a9ca361","9b9ca361","9c9ca361","9d9ca361","9e9ca361","9f9ca361","a09ca361","a19ca361","a29ca361","a39ca361","a49ca361","a59ca361","a69ca361","a79ca361","a89ca361","a99ca361","aa9ca361","ab9ca361","ac9ca361","ad9ca361","ae9ca361","af9ca361","b09ca361","b19ca361","b29ca361","b39ca361","b49ca361","b59ca361","b69ca361","b79ca361","b89ca361","b99ca361","ba9ca361","bb9ca361","bc9ca361","bd9ca361","be9ca361","bf9ca361","c09ca361","c19ca361","c29ca361","c39ca361","c49ca361","c59ca361","c89ca361","c99ca361","ca9ca361","cb9ca361","cc9ca361","cd9ca361","ce9ca361","cf9ca361","d09ca361","d19ca361","d29ca361","d39ca361","d69ca361","d79ca361","d89ca361","d99ca361","da9ca361","db9ca361","dc9ca361","dd9ca361","de9ca361","df9ca361","e09ca361","e19ca361","e29ca361","e39ca361","e49ca361","e59ca361","e69ca361","e79ca361","e89ca361","e99ca361","ea9ca361","eb9ca361","ec9ca361","ed9ca361","ee9ca361","ef9ca361","f09ca361","f19ca361","f29ca361","f39ca361","f49ca361","f59ca361","f69ca361","f79ca361","f89ca361","f99ca361","fa9ca361","fb9ca361","fc9ca361","fd9ca361","fe9ca361","ff9ca361","809da361","819da361","829da361","839da361","849da361","859da361","869da361","879da361","889da361","899da361","8a9da361","8b9da361","8c9da361","8d9da361","8e9da361","8f9da361","909da361","919da361","929da361","939da361","949da361","959da361","969da361","979da361","989da361","999da361","9a9da361","9b9da361","9c9da361","9d9da361","9e9da361","9f9da361","a09da361","a19da361","a29da361","a39da361","a49da361","a59da361","a69da361","a79da361","a89da361","a99da361","aa9da361","ab9da361","ac9da361","ad9da361","ae9da361","af9da361","b09da361","b19da361","b29da361","b39da361","b49da361","b59da361","b69da361","b79da361","b89da361","b99da361","ba9da361","bb9da361","bc9da361","bd9da361","be9da361","bf9da361","c09da361","c19da361","c29da361","c39da361","c49da361","c59da361","c69da361","c79da361","c99da361","ca9da361","cb9da361","cc9da361","e997a561","ea97a561","eb97a561","ec97a561","ed97a561","ee97a561","ef97a561","f097a561","f197a561","f297a561","f397a561","f497a561","f597a561","f697a561","f797a561","f897a561","f997a561","fa97a561","fb97a561","fc97a561","fd97a561","fe97a561","ff97a561","8098a561","8198a561","8298a561","8398a561","8498a561","8598a561","8698a561","8898a561","8998a561","8a98a561","8b98a561","8c98a561","8e98a561","8f98a561","9098a561","9198a561","9298a561","9398a561","9498a561","9598a561","9698a561","9798a561","9898a561","d19fa561","d29fa561","d49fa561","d59fa561","d69fa561","d79fa561","d89fa561","d99fa561","da9fa561","db9fa561","dc9fa561","dd9fa561","de9fa561","df9fa561","e09fa561","e19fa561","e29fa561","e39fa561","e49fa561","e59fa561","e69fa561","e79fa561","e89fa561","e99fa561","ea9fa561","eb9fa561","ec9fa561","ed9fa561","ee9fa561","ef9fa561","f09fa561","f19fa561","f29fa561","f39fa561","f49fa561","f59fa561","f69fa561","f79fa561","f89fa561","f99fa561","fa9fa561","fb9fa561","fc9fa561","fd9fa561","fe9fa561","ff9fa561","80a0a561","81a0a561","82a0a561","b9a7a561","baa7a561","bba7a561","bca7a561","bda7a561","bea7a561","bfa7a561","c0a7a561","c1a7a561","c2a7a561","c3a7a561","c4a7a561","c5a7a561","c6a7a561","c7a7a561","c8a7a561","c9a7a561","caa7a561","cba7a561","cca7a561","cda7a561","cea7a561","cfa7a561","d0a7a561","d1a7a561","d2a7a561","d3a7a561","d4a7a561","d5a7a561","d6a7a561","d7a7a561","d8a7a561","d9a7a561","daa7a561","dba7a561","dca7a561","dda7a561","dea7a561","dfa7a561","e0a7a561","e1a7a561","e2a7a561","e3a7a561","e4a7a561","e5a7a561","e6a7a561","e7a7a561","e8a7a561","a0afa561","a1afa561","a2afa561","a3afa561","a4afa561","a5afa561","a6afa561","a7afa561","a8afa561","a9afa561","aaafa561","abafa561","acafa561","adafa561","aeafa561","afafa561","b0afa561","b1afa561","b2afa561","b3afa561","b4afa561","b5afa561","b6afa561","b7afa561","b8afa561","b9afa561","baafa561","bbafa561","bcafa561","bdafa561","beafa561","bfafa561","c0afa561","c1afa561","c2afa561","c3afa561","c4afa561","c5afa561","c6afa561","c7afa561","c8afa561","c9afa561","ccafa561","88b7a561","89b7a561","8ab7a561","8bb7a561","8eb7a561","8fb7a561","90b7a561","91b7a561","92b7a561","93b7a561","94b7a561","95b7a561","96b7a561","97b7a561","98b7a561","99b7a561","9ab7a561","9bb7a561","9cb7a561","9db7a561","9eb7a561","9fb7a561","a1b7a561","a2b7a561","a3b7a561","a4b7a561","a5b7a561","a6b7a561","a7b7a561","a8b7a561","a9b7a561","aab7a561","abb7a561","acb7a561","adb7a561","aeb7a561","afb7a561","b0b7a561","b1b7a561","b2b7a561","b3b7a561","b4b7a561","b5b7a561","b6b7a561","b7b7a561","b8b7a561","b9b7a561","bab7a561","bbb7a561","bcb7a561","bdb7a561","beb7a561","8eb8a561","8fb8a561","edbea561","eebea561","efbea561","f0bea561","f1bea561","f2bea561","f3bea561","f4bea561","f5bea561","f6bea561","f7bea561","f8bea561","f9bea561","fabea561","fbbea561","fcbea561","fdbea561","febea561","ffbea561","80bfa561","81bfa561","82bfa561","83bfa561","84bfa561","85bfa561","87bfa561","8bbfa561","8cbfa561","8dbfa561","8fbfa561","90bfa561","92bfa561","93bfa561","94bfa561","95bfa561","97bfa561","98bfa561","99bfa561","9abfa561","9bbfa561","9cbfa561","9dbfa561","9ebfa561","a5bfa561","a6bfa561","a7bfa561","a8bfa561","a9bfa561","aabfa561","abbfa561","acbfa561","adbfa561","aebfa561","d8c6a561","d9c6a561","dac6a561","dbc6a561","dcc6a561","ddc6a561","dec6a561","dfc6a561","e0c6a561","e1c6a561","e2c6a561","e3c6a561","e4c6a561","e5c6a561","e6c6a561","e7c6a561","e8c6a561","e9c6a561","eac6a561","ebc6a561","ecc6a561","edc6a561","eec6a561","efc6a561","f0c6a561","f1c6a561","f2c6a561","f3c6a561","f4c6a561","f5c6a561","f6c6a561","f7c6a561","f8c6a561","f9c6a561","fec6a561","ffc6a561","80c7a561","81c7a561","82c7a561","83c7a561","84c7a561","85c7a561","86c7a561","87c7a561","88c7a561","89c7a561","8ac7a561","8bc7a561","8cc7a561","c0cea561","c1cea561","c2cea561","c3cea561","c4cea561","c5cea561","c6cea561","c7cea561","c8cea561","c9cea561","cacea561","cbcea561","cccea561","cdcea561","cecea561","cfcea561","d0cea561","d1cea561","d2cea561","d3cea561","d4cea561","d5cea561","d6cea561","d7cea561","d8cea561","d9cea561","dacea561","dbcea561","dccea561","ddcea561","decea561","dfcea561","e0cea561","e1cea561","e2cea561","e3cea561","e4cea561","e5cea561","e6cea561","e7cea561","e8cea561","e9cea561","eacea561","ebcea561","a8d6a561","a9d6a561","aad6a561","abd6a561","acd6a561","add6a561","aed6a561","afd6a561","b0d6a561","b1d6a561","b2d6a561","b3d6a561","b4d6a561","b5d6a561","b6d6a561","b7d6a561","b8d6a561","b9d6a561","bad6a561","bbd6a561","bcd6a561","bdd6a561","bed6a561","bfd6a561","c0d6a561","c1d6a561","c2d6a561","c3d6a561","c4d6a561","c5d6a561","c6d6a561","c7d6a561","c8d6a561","c9d6a561","cad6a561","cbd6a561","ccd6a561","cdd6a561","90dea561","91dea561","92dea561","93dea561","94dea561","95dea561","96dea561","97dea561","98dea561","99dea561","9adea561","9bdea561","9cdea561","9ddea561","9edea561","9fdea561","a0dea561","a1dea561","a2dea561","a3dea561","a4dea561","a5dea561","a6dea561","a7dea561","a8dea561","a9dea561","aadea561","abdea561","acdea561","addea561","aedea561","afdea561","f8e5a561","f9e5a561","fae5a561","fbe5a561","fce5a561","fde5a561","fee5a561","ffe5a561","80e6a561","81e6a561","82e6a561","83e6a561","84e6a561","85e6a561","86e6a561","87e6a561","88e6a561","89e6a561","8ae6a561","8be6a561","8ce6a561","8de6a561","8ee6a561","8fe6a561","90e6a561","91e6a561","92e6a561","93e6a561","94e6a561","95e6a561","96e6a561","97e6a561","98e6a561","99e6a561","9ae6a561","9be6a561","9ce6a561","9de6a561","9ee6a561","e0eda561","e1eda561","e2eda561","e3eda561","e4eda561","e5eda561","e6eda561","e7eda561","e8eda561","e9eda561","eaeda561","ebeda561","eceda561","ededa561","eeeda561","efeda561","f0eda561","f1eda561","f2eda561","f3eda561","f4eda561","f5eda561","f6eda561","f7eda561","f8eda561","f9eda561","faeda561","fbeda561","fceda561","c8f5a561","c9f5a561","caf5a561","cbf5a561","ccf5a561","cdf5a561","cef5a561","cff5a561","d0f5a561","d1f5a561","d2f5a561","d3f5a561","d4f5a561","d5f5a561","d6f5a561","d7f5a561","d8f5a561","d9f5a561","daf5a561","dbf5a561","dcf5a561","ddf5a561","def5a561","dff5a561","e0f5a561","e1f5a561","e2f5a561","e3f5a561","e4f5a561","b0fda561","b1fda561","b2fda561","b3fda561","b4fda561","b5fda561","b6fda561","b7fda561","b8fda561","b9fda561","bafda561","bbfda561","bcfda561","bdfda561","befda561","bffda561","c0fda561","c1fda561","c2fda561","c3fda561","c4fda561","c5fda561","c6fda561","c7fda561","c8fda561","c9fda561","cafda561","cbfda561","ccfda561","cdfda561","cefda561","cffda561","d0fda561","d1fda561","d2fda561","d3fda561","d4fda561","d5fda561","9885a661","9985a661","9a85a661","9b85a661","9c85a661","9d85a661","9e85a661","9f85a661","a085a661","a185a661","a285a661","a385a661","a485a661","a585a661","a685a661","a785a661","a885a661","a985a661","aa85a661","ab85a661","ac85a661","ae85a661","af85a661","b085a661","b185a661","b285a661","b385a661","b485a661","b585a661","b685a661","b785a661","808da661","818da661","828da661","838da661","848da661","858da661","868da661","878da661","888da661","898da661","8a8da661","8b8da661","8c8da661","8d8da661","8e8da661","8f8da661","908da661","918da661","928da661","938da661","948da661","958da661","968da661","978da661","988da661","998da661","9a8da661","9b8da661","9c8da661","9d8da661","9e8da661","9f8da661","a08da661","a18da661","a28da661","a38da661","a48da661","e894a661","e994a661","ea94a661","eb94a661","ec94a661","ed94a661","ee94a661","ef94a661","f094a661","f194a661","f294a661","f394a661","f494a661","f594a661","f694a661","f794a661","f894a661","f994a661","fa94a661","fb94a661","fc94a661","fd94a661","fe94a661","ff94a661","8095a661","8195a661","8295a661","8395a661","8495a661","8595a661","8695a661","8795a661","8895a661","d09ca661","d19ca661","d29ca661","d39ca661","d49ca661","d59ca661","d69ca661","d79ca661","d89ca661","d99ca661","da9ca661","db9ca661","dc9ca661","dd9ca661","de9ca661","df9ca661","e09ca661","e19ca661","e29ca661","e39ca661","e49ca661","e59ca661","e69ca661","e79ca661","e89ca661","e99ca661","ea9ca661","eb9ca661","ec9ca661","ed9ca661","ee9ca661","ef9ca661","f09ca661","f19ca661","f29ca661","aa9da661","ab9da661","ac9da661","ad9da661","ae9da661","af9da661","c09ae061","c19ae061","c29ae061","c39ae061","c49ae061","c59ae061","c69ae061","c79ae061","c89ae061","c99ae061","ca9ae061","cb9ae061","cc9ae061","cd9ae061","ce9ae061","cf9ae061","d09ae061","d19ae061","d29ae061","d39ae061","d49ae061","d59ae061","d69ae061","d79ae061","d89ae061","d99ae061","da9ae061","db9ae061","dc9ae061","dd9ae061","de9ae061","df9ae061","e09ae061","e19ae061","e29ae061","e39ae061","e49ae061","e59ae061","e69ae061","e79ae061","e89ae061","e99ae061","ea9ae061","eb9ae061","ec9ae061","ed9ae061","ee9ae061","ef9ae061","f09ae061","f19ae061","f29ae061","f39ae061","f49ae061","f59ae061","f69ae061","f79ae061","f89ae061","f99ae061","fa9ae061","fb9ae061","fc9ae061","fd9ae061","fe9ae061","ff9ae061","809be061","819be061","829be061","839be061","849be061","859be061","869be061","879be061","889be061","899be061","8a9be061","8b9be061","8d9be061","919be061","929be061","939be061","949be061","959be061","969be061","979be061","989be061","999be061","9a9be061","9b9be061","9c9be061","9d9be061","9e9be061","9f9be061","a19be061","a29be061","a39be061","a49be061","a59be061","a69be061","a79be061","a89be061","a99be061","aa9be061","ab9be061","ac9be061","ad9be061","ae9be061","af9be061","b09be061","b19be061","b29be061","b39be061","b49be061","b59be061","b69be061","b79be061","b89be061","b99be061","ba9be061","bb9be061","bc9be061","bd9be061","be9be061","bf9be061","c09be061","c19be061","c29be061","c39be061","c49be061","c59be061","c69be061","c79be061","c89be061","c99be061","ca9be061","cb9be061","cc9be061","cd9be061","ce9be061","cf9be061","d09be061","d19be061","d29be061","d39be061","d49be061","d59be061","d69be061","d79be061","d89be061","d99be061","da9be061","db9be061","dc9be061","dd9be061","de9be061","df9be061","e09be061","e19be061","e29be061","e39be061","e49be061","e59be061","e69be061","e79be061","e89be061","e99be061","ea9be061","eb9be061","ec9be061","ed9be061","ee9be061","ef9be061","f09be061","f19be061","f29be061","f39be061","f49be061","f59be061","f69be061","f79be061","f89be061","f99be061","fa9be061","fb9be061","fc9be061","fd9be061","fe9be061","ff9be061","809ce061","819ce061","829ce061","839ce061","849ce061","859ce061","869ce061","879ce061","889ce061","899ce061","8a9ce061","8b9ce061","8c9ce061","8d9ce061","8e9ce061","8f9ce061","909ce061","919ce061","929ce061","939ce061","949ce061","959ce061","969ce061","979ce061","989ce061","999ce061","9a9ce061","9b9ce061","9c9ce061","9d9ce061","9e9ce061","9f9ce061","a09ce061","a19ce061","a29ce061","a39ce061","a49ce061","a59ce061","a69ce061","a79ce061","a89ce061","a99ce061","aa9ce061","ab9ce061","ac9ce061","ad9ce061","ae9ce061","af9ce061","b09ce061","b19ce061","b29ce061","b39ce061","b49ce061","b59ce061","b69ce061","b79ce061","b89ce061","b99ce061","ba9ce061","bb9ce061","bc9ce061","bd9ce061","be9ce061","bf9ce061","c09ce061","c19ce061","c29ce061","c39ce061","c49ce061","c59ce061","c69ce061","c79ce061","c89ce061","c99ce061","ca9ce061","cb9ce061","cc9ce061","cd9ce061","ce9ce061","cf9ce061","d09ce061","d19ce061","d29ce061","d39ce061","d49ce061","d59ce061","d69ce061","d79ce061","d89ce061","d99ce061","da9ce061","db9ce061","dc9ce061","dd9ce061","de9ce061","df9ce061","e09ce061","e19ce061","e29ce061","e39ce061","e49ce061","e59ce061","e69ce061","e79ce061","e89ce061","e99ce061","ea9ce061","eb9ce061","ec9ce061","ed9ce061","ee9ce061","ef9ce061","f09ce061","f19ce061","f29ce061","f39ce061","f49ce061","f59ce061","f69ce061","f79ce061","f89ce061","f99ce061","fa9ce061","fb9ce061","fc9ce061","fd9ce061","fe9ce061","ff9ce061","809de061","819de061","829de061","839de061","849de061","869de061","879de061","889de061","899de061","8a9de061","8b9de061","8c9de061","8d9de061","8e9de061","8f9de061","909de061","919de061","929de061","939de061","949de061","959de061","969de061","979de061","989de061","999de061","9a9de061","9b9de061","9c9de061","9d9de061","9e9de061","9f9de061","a09de061","a19de061","a29de061","a39de061","a49de061","a59de061","a69de061","a79de061","a89de061","a99de061","aa9de061","ab9de061","ac9de061","ad9de061","ae9de061","af9de061","b09de061","b19de061","b29de061","b39de061","b49de061","b59de061","b69de061","b79de061","b89de061","b99de061","ba9de061","bb9de061","bc9de061","bd9de061","be9de061","bf9de061","c09de061","c19de061","c29de061","c39de061","c49de061","c59de061","c69de061","c79de061","c89de061","c99de061","ca9de061","cb9de061","cc9de061","cd9de061","ce9de061","cf9de061","d09de061","d19de061","d29de061","d39de061","d49de061","d59de061","d69de061","d79de061","d89de061","d99de061","da9de061","db9de061","dc9de061","dd9de061","de9de061","df9de061","e09de061","e19de061","e29de061","e39de061","e49de061","e59de061","e69de061","e79de061","e89de061","e99de061","ea9de061","eb9de061","ec9de061","ed9de061","ee9de061","ef9de061","f09de061","f19de061","f29de061","f39de061","f49de061","f59de061","f69de061","f79de061","f89de061","f99de061","fa9de061","fb9de061","fc9de061","fd9de061","fe9de061","ff9de061","809ee061","819ee061","829ee061","839ee061","849ee061","859ee061","869ee061","879ee061","889ee061","899ee061","8a9ee061","8b9ee061","8c9ee061","8d9ee061","8e9ee061","8f9ee061","909ee061","919ee061","929ee061","939ee061","949ee061","959ee061","969ee061","979ee061","989ee061","999ee061","9a9ee061","9b9ee061","9c9ee061","9d9ee061","9e9ee061","9f9ee061","a09ee061","a19ee061","a29ee061","a39ee061","a49ee061","a59ee061","a69ee061","a79ee061","a89ee061","a99ee061","aa9ee061","ab9ee061","ac9ee061","ad9ee061","ae9ee061","af9ee061","b09ee061","b19ee061","b29ee061","b39ee061","b49ee061","b59ee061","b69ee061","b79ee061","b89ee061","b99ee061","ba9ee061","bb9ee061","bc9ee061","bd9ee061","be9ee061","bf9ee061","c09ee061","c19ee061","c29ee061","c39ee061","c49ee061","c59ee061","c69ee061","c79ee061","c89ee061","c99ee061","ca9ee061","cb9ee061","cc9ee061","cd9ee061","ce9ee061","cf9ee061","d09ee061","d19ee061","d29ee061","d39ee061","d49ee061","d59ee061","d69ee061","d79ee061","d89ee061","d99ee061","da9ee061","db9ee061","dc9ee061","dd9ee061","de9ee061","df9ee061","e09ee061","e19ee061","e29ee061","e39ee061","e49ee061","e59ee061","e69ee061","e79ee061","e89ee061","e99ee061","ea9ee061","eb9ee061","ec9ee061","ed9ee061","ee9ee061","ef9ee061","f09ee061","f19ee061","f29ee061","f39ee061","f49ee061","f59ee061","f69ee061","f79ee061","f89ee061","f99ee061","fa9ee061","fb9ee061","fc9ee061","fd9ee061","fe9ee061","ff9ee061","809fe061","819fe061","829fe061","839fe061","849fe061","859fe061","869fe061","879fe061","889fe061","899fe061","8a9fe061","8b9fe061","8c9fe061","8d9fe061","8e9fe061","8f9fe061","909fe061","919fe061","929fe061","939fe061","949fe061","959fe061","969fe061","979fe061","989fe061","999fe061","9a9fe061","9b9fe061","9c9fe061","9d9fe061","9e9fe061","9f9fe061","a09fe061","a19fe061","a29fe061","a39fe061","a49fe061","a59fe061","a69fe061","a79fe061","a89fe061","a99fe061","aa9fe061","ab9fe061","ac9fe061","ad9fe061","ae9fe061","b09fe061","b19fe061","b29fe061","b39fe061","b49fe061","b59fe061","b69fe061","b79fe061","b89fe061","b99fe061","ba9fe061","bb9fe061","bc9fe061","bd9fe061","be9fe061","bf9fe061","c09fe061","c19fe061","c29fe061","c39fe061","c49fe061","c59fe061","c69fe061","c79fe061","c89fe061","c99fe061","ca9fe061","cb9fe061","cc9fe061","cd9fe061","ce9fe061","cf9fe061","d09fe061","d19fe061","d29fe061","d39fe061","d49fe061","d59fe061","d69fe061","d79fe061","d89fe061","d99fe061","da9fe061","db9fe061","dc9fe061","dd9fe061","de9fe061","df9fe061","e09fe061","e19fe061","e29fe061","e39fe061","e49fe061","e59fe061","e69fe061","e79fe061","e89fe061","e99fe061","ea9fe061","eb9fe061","ec9fe061","ed9fe061","ee9fe061","ef9fe061","f09fe061","f19fe061","f29fe061","f39fe061","f49fe061","f59fe061","f69fe061","f79fe061","f89fe061","f99fe061","fa9fe061","fb9fe061","fc9fe061","fd9fe061","fe9fe061","ff9fe061","80a0e061","81a0e061","82a0e061","83a0e061","84a0e061","85a0e061","86a0e061","87a0e061","88a0e061","89a0e061","8aa0e061","8ba0e061","8ca0e061","8da0e061","8ea0e061","8fa0e061","90a0e061","91a0e061","92a0e061","93a0e061","94a0e061","95a0e061","96a0e061","97a0e061","98a0e061","99a0e061","9aa0e061","9ba0e061","9ca0e061","9da0e061","9ea0e061","9fa0e061","a0a0e061","a1a0e061","a2a0e061","a3a0e061","a4a0e061","a5a0e061","a6a0e061","a7a0e061","a8a0e061","a9a0e061","aaa0e061","aba0e061","aca0e061","ada0e061","aea0e061","afa0e061","b0a0e061","b1a0e061","b2a0e061","b3a0e061","b4a0e061","b5a0e061","b6a0e061","b7a0e061","b8a0e061","b9a0e061","baa0e061","bba0e061","bca0e061","bda0e061","c0a0e061","c1a0e061","c2a0e061","c3a0e061","c4a0e061","c5a0e061","c6a0e061","c7a0e061","c8a0e061","c9a0e061","cca0e061","cda0e061","cea0e061","cfa0e061","d0a0e061","d1a0e061","d2a0e061","d3a0e061","d4a0e061","d5a0e061","d6a0e061","d7a0e061","d8a0e061","d9a0e061","daa0e061","dba0e061","dca0e061","dda0e061","dea0e061","dfa0e061","e0a0e061","e1a0e061","e2a0e061","e3a0e061","e4a0e061","e5a0e061","e6a0e061","e7a0e061","e8a0e061","e9a0e061","eaa0e061","eba0e061","eca0e061","eda0e061","eea0e061","efa0e061","f0a0e061","f1a0e061","f2a0e061","f3a0e061","f4a0e061","f5a0e061","f6a0e061","f7a0e061","f8a0e061","f9a0e061","faa0e061","fba0e061","fca0e061","fda0e061","fea0e061","ffa0e061","80a1e061","81a1e061","82a1e061","83a1e061","84a1e061","85a1e061","86a1e061","87a1e061","88a1e061","89a1e061","8aa1e061","8ba1e061","8ca1e061","8da1e061","8ea1e061","8fa1e061","90a1e061","91a1e061","92a1e061","93a1e061","94a1e061","95a1e061","96a1e061","97a1e061","98a1e061","99a1e061","9aa1e061","9ba1e061","9ca1e061","9da1e061","9ea1e061","9fa1e061","a0a1e061","a1a1e061","a2a1e061","a3a1e061","a4a1e061","a5a1e061","a6a1e061","a7a1e061","a8a1e061","a9a1e061","aaa1e061","aba1e061","aca1e061","ada1e061","aea1e061","afa1e061","b0a1e061","b1a1e061","b2a1e061","b3a1e061","b4a1e061","b6a1e061","b7a1e061","b8a1e061","b9a1e061","a99ce261","aa9ce261","ab9ce261","ac9ce261","ad9ce261","ae9ce261","af9ce261","b09ce261","b19ce261","b29ce261","b39ce261","b49ce261","b59ce261","b69ce261","b79ce261","b89ce261","b99ce261","ba9ce261","bb9ce261","bc9ce261","bd9ce261","be9ce261","bf9ce261","c09ce261","c19ce261","c29ce261","c39ce261","c49ce261","c69ce261","c79ce261","c89ce261","c99ce261","ca9ce261","cb9ce261","cd9ce261","ce9ce261","cf9ce261","d09ce261","d19ce261","d29ce261","d39ce261","d49ce261","d59ce261","d69ce261","d79ce261","d89ce261","d99ce261","da9ce261","db9ce261","dc9ce261","91a4e261","92a4e261","94a4e261","95a4e261","96a4e261","97a4e261","98a4e261","99a4e261","9aa4e261","9ba4e261","9ca4e261","9da4e261","9ea4e261","9fa4e261","a0a4e261","a1a4e261","a2a4e261","a3a4e261","a4a4e261","a5a4e261","a6a4e261","a7a4e261","a8a4e261","a9a4e261","aaa4e261","aba4e261","aca4e261","ada4e261","aea4e261","afa4e261","b0a4e261","b1a4e261","b2a4e261","b3a4e261","b4a4e261","b5a4e261","b6a4e261","b7a4e261","b8a4e261","b9a4e261","baa4e261","bba4e261","bca4e261","bda4e261","bea4e261","bfa4e261","c0a4e261","c1a4e261","c2a4e261","f9abe261","faabe261","fbabe261","fcabe261","fdabe261","feabe261","ffabe261","80ace261","81ace261","82ace261","83ace261","84ace261","85ace261","86ace261","87ace261","88ace261","89ace261","8aace261","8bace261","8cace261","8dace261","8eace261","8face261","90ace261","91ace261","92ace261","93ace261","94ace261","95ace261","96ace261","97ace261","98ace261","99ace261","9aace261","9bace261","9cace261","9dace261","9eace261","9face261","a0ace261","a1ace261","a2ace261","a3ace261","a4ace261","a5ace261","a7ace261","a8ace261","e0b3e261","e1b3e261","e2b3e261","e3b3e261","e4b3e261","e5b3e261","e6b3e261","e7b3e261","e8b3e261","e9b3e261","eab3e261","ebb3e261","ecb3e261","edb3e261","eeb3e261","efb3e261","f0b3e261","f1b3e261","f2b3e261","f3b3e261","f4b3e261","f5b3e261","f6b3e261","f7b3e261","f8b3e261","f9b3e261","fab3e261","fbb3e261","fcb3e261","fdb3e261","feb3e261","ffb3e261","80b4e261","81b4e261","82b4e261","83b4e261","84b4e261","85b4e261","86b4e261","87b4e261","88b4e261","89b4e261","8ab4e261","c8bbe261","c9bbe261","cabbe261","cbbbe261","cebbe261","cfbbe261","d0bbe261","d1bbe261","d2bbe261","d3bbe261","d4bbe261","d5bbe261","d6bbe261","d7bbe261","d8bbe261","d9bbe261","dabbe261","dbbbe261","dcbbe261","ddbbe261","debbe261","dfbbe261","e1bbe261","e2bbe261","e3bbe261","e4bbe261","e6bbe261","e7bbe261","e8bbe261","eabbe261","ebbbe261","eebbe261","efbbe261","f0bbe261","f1bbe261","f2bbe261","f3bbe261","f4bbe261","f5bbe261","f6bbe261","f7bbe261","f8bbe261","f9bbe261","fabbe261","fbbbe261","fcbbe261","fdbbe261","febbe261","d3bce261","b0c3e261","b1c3e261","b2c3e261","b3c3e261","b4c3e261","b5c3e261","b6c3e261","b7c3e261","b8c3e261","b9c3e261","bac3e261","bbc3e261","bcc3e261","bdc3e261","bec3e261","bfc3e261","c0c3e261","c1c3e261","c2c3e261","c3c3e261","c4c3e261","c5c3e261","c6c3e261","c7c3e261","cbc3e261","ccc3e261","cdc3e261","cec3e261","d0c3e261","d2c3e261","d3c3e261","d4c3e261","d5c3e261","d7c3e261","d8c3e261","d9c3e261","dac3e261","dbc3e261","dcc3e261","ddc3e261","dec3e261","e6c3e261","e7c3e261","e8c3e261","e9c3e261","eac3e261","ebc3e261","ecc3e261","edc3e261","eec3e261","efc3e261","98cbe261","99cbe261","9acbe261","9bcbe261","9ccbe261","9dcbe261","9ecbe261","9fcbe261","a0cbe261","a1cbe261","a2cbe261","a3cbe261","a4cbe261","a5cbe261","a6cbe261","a7cbe261","a8cbe261","a9cbe261","aacbe261","abcbe261","accbe261","adcbe261","aecbe261","afcbe261","b0cbe261","b1cbe261","b2cbe261","b3cbe261","b4cbe261","b5cbe261","b6cbe261","b7cbe261","b8cbe261","b9cbe261","bacbe261","bbcbe261","bccbe261","bdcbe261","becbe261","bfcbe261","c0cbe261","c1cbe261","c2cbe261","c3cbe261","c4cbe261","c5cbe261","c6cbe261","80d3e261","81d3e261","82d3e261","83d3e261","84d3e261","85d3e261","86d3e261","87d3e261","88d3e261","89d3e261","8ad3e261","8bd3e261","8cd3e261","8dd3e261","8ed3e261","8fd3e261","90d3e261","91d3e261","92d3e261","93d3e261","94d3e261","95d3e261","96d3e261","97d3e261","98d3e261","99d3e261","9ad3e261","9bd3e261","9cd3e261","9dd3e261","9ed3e261","9fd3e261","a0d3e261","a1d3e261","a2d3e261","a3d3e261","a4d3e261","a5d3e261","a6d3e261","e8dae261","e9dae261","eadae261","ebdae261","ecdae261","eddae261","eedae261","efdae261","f0dae261","f1dae261","f2dae261","f3dae261","f4dae261","f5dae261","f6dae261","f7dae261","f8dae261","f9dae261","fadae261","fbdae261","fcdae261","fddae261","fedae261","ffdae261","80dbe261","81dbe261","82dbe261","83dbe261","84dbe261","85dbe261","86dbe261","87dbe261","88dbe261","89dbe261","8adbe261","8bdbe261","8cdbe261","8ddbe261","8edbe261","8fdbe261","d0e2e261","d1e2e261","d2e2e261","d3e2e261","d4e2e261","d5e2e261","d6e2e261","d7e2e261","d8e2e261","d9e2e261","dae2e261","dbe2e261","dce2e261","dde2e261","dee2e261","dfe2e261","e0e2e261","e1e2e261","e2e2e261","e3e2e261","e4e2e261","e5e2e261","e6e2e261","e7e2e261","e8e2e261","e9e2e261","eae2e261","ebe2e261","ece2e261","b8eae261","b9eae261","baeae261","bbeae261","bceae261","bdeae261","beeae261","bfeae261","c0eae261","c1eae261","c2eae261","c3eae261","c4eae261","c5eae261","c6eae261","c7eae261","c8eae261","c9eae261","caeae261","cbeae261","cceae261","cdeae261","ceeae261","cfeae261","d0eae261","d1eae261","d2eae261","d3eae261","d4eae261","d5eae261","d6eae261","d7eae261","d8eae261","d9eae261","daeae261","dbeae261","dceae261","ddeae261","deeae261","a0f2e261","a1f2e261","a2f2e261","a3f2e261","a4f2e261","a5f2e261","a6f2e261","a7f2e261","a8f2e261","a9f2e261","aaf2e261","abf2e261","acf2e261","adf2e261","aef2e261","aff2e261","b0f2e261","b1f2e261","b2f2e261","b3f2e261","b4f2e261","b5f2e261","b6f2e261","b7f2e261","b8f2e261","b9f2e261","baf2e261","bbf2e261","bcf2e261","bdf2e261","88fae261","89fae261","8afae261","8bfae261","8cfae261","8dfae261","8efae261","8ffae261","90fae261","91fae261","92fae261","93fae261","94fae261","95fae261","96fae261","97fae261","98fae261","99fae261","9afae261","9bfae261","9cfae261","9dfae261","9efae261","9ffae261","a0fae261","a1fae261","a2fae261","f081e361","f181e361","f281e361","f381e361","f481e361","f581e361","f681e361","f781e361","f881e361","f981e361","fa81e361","fb81e361","fc81e361","fd81e361","fe81e361","ff81e361","8082e361","8182e361","8282e361","8382e361","8482e361","8582e361","8682e361","8782e361","8882e361","8982e361","8a82e361","8b82e361","8c82e361","8d82e361","8e82e361","8f82e361","9082e361","9182e361","d889e361","d989e361","da89e361","db89e361","dc89e361","dd89e361","de89e361","df89e361","e089e361","e189e361","e289e361","e389e361","e489e361","e589e361","e689e361","e789e361","e889e361","e989e361","ea89e361","eb89e361","ed89e361","ee89e361","ef89e361","f089e361","f189e361","f289e361","f389e361","f489e361","f589e361","f689e361","c091e361","c191e361","c291e361","c391e361","c491e361","c591e361","c691e361","c791e361","c891e361","c991e361","ca91e361","cb91e361","cc91e361","cd91e361","ce91e361","cf91e361","d091e361","d191e361","d291e361","d391e361","d491e361","d591e361","d691e361","d791e361","d891e361","d991e361","da91e361","db91e361","dc91e361","dd91e361","de91e361","df91e361","e091e361","e191e361","e291e361","e391e361","e491e361","e591e361","e691e361","a899e361","a999e361","aa99e361","ab99e361","ac99e361","ad99e361","ae99e361","af99e361","b099e361","b199e361","b299e361","b399e361","b499e361","b599e361","b699e361","b799e361","b899e361","b999e361","ba99e361","bb99e361","bc99e361","bd99e361","be99e361","bf99e361","c099e361","c199e361","c299e361","c399e361","c499e361","c599e361","c699e361","c799e361","c899e361","c999e361","ca99e361","cb99e361","cc99e361","cd99e361","90a1e361","91a1e361","92a1e361","93a1e361","94a1e361","95a1e361","96a1e361","97a1e361","98a1e361","99a1e361","9aa1e361","9ba1e361","9ca1e361","9da1e361","9ea1e361","9fa1e361","a0a1e361","a1a1e361","a2a1e361","a3a1e361","a4a1e361","a5a1e361","a6a1e361","a7a1e361","a8a1e361","a9a1e361","aaa1e361","aba1e361","aca1e361","ada1e361","aea1e361","afa1e361","b0a1e361","eaa1e361","eba1e361","eca1e361","eda1e361","eea1e361","efa1e361","80a89763","c0b5ce64","c1b5ce64","c3b5ce64","c4b5ce64","c5b5ce64","c6b5ce64","c7b5ce64","c8b5ce64","c9b5ce64","cab5ce64","cbb5ce64","ccb5ce64","cfb5ce64","d0b5ce64","d1b5ce64","d2b5ce64","d4b5ce64","d6b5ce64","d7b5ce64","d8b5ce64","d9b5ce64","dab5ce64","dbb5ce64","dcb5ce64","ddb5ce64","deb5ce64","dfb5ce64","e0b5ce64","e1b5ce64","e2b5ce64","e3b5ce64","e4b5ce64","e5b5ce64","e6b5ce64","e7b5ce64","e8b5ce64","e9b5ce64","eab5ce64","ebb5ce64","ecb5ce64","edb5ce64","eeb5ce64","efb5ce64","f0b5ce64","f1b5ce64","f2b5ce64","f3b5ce64","f4b5ce64","f7b5ce64","f8b5ce64","f9b5ce64","fab5ce64","fbb5ce64","fcb5ce64","fdb5ce64","feb5ce64","ffb5ce64","80b6ce64","81b6ce64","82b6ce64","83b6ce64","84b6ce64","85b6ce64","86b6ce64","87b6ce64","88b6ce64","89b6ce64","8ab6ce64","8bb6ce64","8cb6ce64","8db6ce64","8eb6ce64","8fb6ce64","90b6ce64","91b6ce64","93b6ce64","94b6ce64","95b6ce64","96b6ce64","97b6ce64","98b6ce64","99b6ce64","9ab6ce64","9bb6ce64","9cb6ce64","9db6ce64","9eb6ce64","9fb6ce64","a0b6ce64","a1b6ce64","a2b6ce64","a3b6ce64","a4b6ce64","a5b6ce64","a6b6ce64","a7b6ce64","a8b6ce64","a9b6ce64","aab6ce64","abb6ce64","acb6ce64","adb6ce64","aeb6ce64","afb6ce64","b0b6ce64","b1b6ce64","b2b6ce64","b3b6ce64","b4b6ce64","b5b6ce64","b6b6ce64","b7b6ce64","b8b6ce64","b9b6ce64","bab6ce64","bbb6ce64","bcb6ce64","bdb6ce64","beb6ce64","bfb6ce64","c0b6ce64","c1b6ce64","c2b6ce64","c3b6ce64","c4b6ce64","c5b6ce64","c6b6ce64","c7b6ce64","c8b6ce64","c9b6ce64","cab6ce64","cbb6ce64","ccb6ce64","cdb6ce64","ceb6ce64","cfb6ce64","d0b6ce64","d1b6ce64","d2b6ce64","d4b6ce64","d5b6ce64","d6b6ce64","d7b6ce64","d8b6ce64","d9b6ce64","dab6ce64","dbb6ce64","dcb6ce64","deb6ce64","dfb6ce64","e0b6ce64","e1b6ce64","e2b6ce64","e3b6ce64","e4b6ce64","e5b6ce64","e6b6ce64","e7b6ce64","e8b6ce64","e9b6ce64","eab6ce64","ebb6ce64","ecb6ce64","edb6ce64","eeb6ce64","efb6ce64","f0b6ce64","f1b6ce64","f2b6ce64","f3b6ce64","f4b6ce64","f5b6ce64","f6b6ce64","f7b6ce64","f8b6ce64","f9b6ce64","fab6ce64","fbb6ce64","fcb6ce64","fdb6ce64","feb6ce64","ffb6ce64","80b7ce64","81b7ce64","82b7ce64","83b7ce64","84b7ce64","85b7ce64","86b7ce64","87b7ce64","88b7ce64","89b7ce64","8ab7ce64","8bb7ce64","8cb7ce64","8db7ce64","8eb7ce64","8fb7ce64","90b7ce64","91b7ce64","92b7ce64","93b7ce64","94b7ce64","95b7ce64","96b7ce64","97b7ce64","98b7ce64","99b7ce64","9ab7ce64","9bb7ce64","9cb7ce64","9db7ce64","9eb7ce64","9fb7ce64","a1b7ce64","a2b7ce64","a3b7ce64","a4b7ce64","a5b7ce64","a6b7ce64","a7b7ce64","a8b7ce64","a9b7ce64","aab7ce64","abb7ce64","acb7ce64","adb7ce64","aeb7ce64","afb7ce64","b0b7ce64","b1b7ce64","b2b7ce64","b3b7ce64","b4b7ce64","b5b7ce64","b6b7ce64","b7b7ce64","b8b7ce64","b9b7ce64","bab7ce64","bbb7ce64","bcb7ce64","bdb7ce64","beb7ce64","bfb7ce64","c0b7ce64","c1b7ce64","c2b7ce64","c3b7ce64","c4b7ce64","c5b7ce64","c6b7ce64","c7b7ce64","c8b7ce64","c9b7ce64","cab7ce64","cbb7ce64","ccb7ce64","cdb7ce64","ceb7ce64","cfb7ce64","d0b7ce64","d1b7ce64","d2b7ce64","d3b7ce64","d4b7ce64","d5b7ce64","d6b7ce64","d7b7ce64","d8b7ce64","d9b7ce64","dab7ce64","dbb7ce64","dcb7ce64","ddb7ce64","deb7ce64","dfb7ce64","e0b7ce64","e1b7ce64","e2b7ce64","e3b7ce64","e4b7ce64","e5b7ce64","e6b7ce64","e7b7ce64","e8b7ce64","e9b7ce64","eab7ce64","ebb7ce64","ecb7ce64","edb7ce64","eeb7ce64","efb7ce64","f0b7ce64","f1b7ce64","f2b7ce64","f3b7ce64","f4b7ce64","f5b7ce64","f6b7ce64","f7b7ce64","f8b7ce64","f9b7ce64","fab7ce64","fbb7ce64","fcb7ce64","fdb7ce64","feb7ce64","ffb7ce64","80b8ce64","81b8ce64","82b8ce64","83b8ce64","84b8ce64","85b8ce64","86b8ce64","87b8ce64","88b8ce64","89b8ce64","8ab8ce64","8bb8ce64","8cb8ce64","8db8ce64","8eb8ce64","8fb8ce64","90b8ce64","91b8ce64","92b8ce64","93b8ce64","94b8ce64","95b8ce64","96b8ce64","97b8ce64","98b8ce64","99b8ce64","9ab8ce64","9bb8ce64","9cb8ce64","9db8ce64","9eb8ce64","a0b8ce64","a1b8ce64","a4b8ce64","a5b8ce64","a8b8ce64","a9b8ce64","abb8ce64","acb8ce64","adb8ce64","aeb8ce64","afb8ce64","b0b8ce64","b1b8ce64","b2b8ce64","b3b8ce64","b4b8ce64","b5b8ce64","b6b8ce64","b7b8ce64","b8b8ce64","b9b8ce64","bab8ce64","bbb8ce64","bcb8ce64","bdb8ce64","beb8ce64","bfb8ce64","c0b8ce64","c1b8ce64","c2b8ce64","c3b8ce64","c4b8ce64","c5b8ce64","c7b8ce64","c8b8ce64","c9b8ce64","cab8ce64","cbb8ce64","ccb8ce64","cdb8ce64","ceb8ce64","cfb8ce64","d0b8ce64","d1b8ce64","d2b8ce64","d3b8ce64","d4b8ce64","d5b8ce64","d6b8ce64","d7b8ce64","d8b8ce64","d9b8ce64","dab8ce64","dbb8ce64","dcb8ce64","ddb8ce64","deb8ce64","dfb8ce64","e0b8ce64","e1b8ce64","e2b8ce64","e3b8ce64","e4b8ce64","e5b8ce64","e6b8ce64","e7b8ce64","e8b8ce64","e9b8ce64","eab8ce64","ebb8ce64","ecb8ce64","edb8ce64","eeb8ce64","efb8ce64","f0b8ce64","f1b8ce64","f2b8ce64","f3b8ce64","f4b8ce64","f5b8ce64","f6b8ce64","f7b8ce64","f8b8ce64","f9b8ce64","fab8ce64","fbb8ce64","fcb8ce64","fdb8ce64","feb8ce64","ffb8ce64","81b9ce64","82b9ce64","83b9ce64","84b9ce64","85b9ce64","86b9ce64","87b9ce64","88b9ce64","89b9ce64","8ab9ce64","8bb9ce64","8cb9ce64","8db9ce64","8eb9ce64","8fb9ce64","90b9ce64","91b9ce64","92b9ce64","93b9ce64","95b9ce64","96b9ce64","97b9ce64","98b9ce64","99b9ce64","9ab9ce64","9bb9ce64","9cb9ce64","9db9ce64","9eb9ce64","9fb9ce64","a0b9ce64","a1b9ce64","a2b9ce64","a3b9ce64","a4b9ce64","a5b9ce64","a6b9ce64","a7b9ce64","a8b9ce64","a9b9ce64","aab9ce64","abb9ce64","acb9ce64","adb9ce64","aeb9ce64","afb9ce64","b0b9ce64","b1b9ce64","b2b9ce64","b3b9ce64","b4b9ce64","b5b9ce64","b6b9ce64","b7b9ce64","b8b9ce64","b9b9ce64","bab9ce64","bbb9ce64","bcb9ce64","bdb9ce64","beb9ce64","bfb9ce64","c0b9ce64","c1b9ce64","c2b9ce64","c3b9ce64","c4b9ce64","c5b9ce64","c6b9ce64","c7b9ce64","c8b9ce64","c9b9ce64","cab9ce64","cbb9ce64","ccb9ce64","cdb9ce64","ceb9ce64","cfb9ce64","d0b9ce64","d1b9ce64","d2b9ce64","d3b9ce64","d4b9ce64","d5b9ce64","d6b9ce64","d7b9ce64","d8b9ce64","d9b9ce64","dab9ce64","dbb9ce64","dcb9ce64","ddb9ce64","dfb9ce64","e0b9ce64","e1b9ce64","e2b9ce64","e3b9ce64","e4b9ce64","e5b9ce64","e6b9ce64","e7b9ce64","e8b9ce64","e9b9ce64","eab9ce64","ebb9ce64","ecb9ce64","edb9ce64","eeb9ce64","efb9ce64","f0b9ce64","f1b9ce64","f2b9ce64","f3b9ce64","f4b9ce64","f5b9ce64","f6b9ce64","f7b9ce64","f8b9ce64","f9b9ce64","fab9ce64","fbb9ce64","fcb9ce64","fdb9ce64","feb9ce64","ffb9ce64","80bace64","81bace64","82bace64","83bace64","84bace64","85bace64","86bace64","87bace64","88bace64","89bace64","8abace64","8bbace64","8cbace64","8dbace64","8ebace64","8fbace64","90bace64","91bace64","92bace64","93bace64","94bace64","95bace64","96bace64","97bace64","98bace64","99bace64","9abace64","9bbace64","9cbace64","9dbace64","9ebace64","9fbace64","a0bace64","a1bace64","a2bace64","a3bace64","a4bace64","a5bace64","a6bace64","a7bace64","a8bace64","a9bace64","aabace64","abbace64","acbace64","adbace64","aebace64","afbace64","b0bace64","b1bace64","b2bace64","b3bace64","b4bace64","b5bace64","b6bace64","b7bace64","b8bace64","b9bace64","babace64","bbbace64","bcbace64","bdbace64","bebace64","bfbace64","c0bace64","c1bace64","c2bace64","c3bace64","c4bace64","c5bace64","c6bace64","c7bace64","c8bace64","c9bace64","cabace64","cbbace64","ccbace64","cdbace64","cebace64","cfbace64","d0bace64","d1bace64","d2bace64","d3bace64","d4bace64","d5bace64","d6bace64","d7bace64","d8bace64","d9bace64","dabace64","dbbace64","dcbace64","ddbace64","debace64","dfbace64","e0bace64","e1bace64","e2bace64","e3bace64","e4bace64","e6bace64","e8bace64","e9bace64","eabace64","ebbace64","ecbace64","edbace64","eebace64","efbace64","f0bace64","f1bace64","f2bace64","f3bace64","f4bace64","f5bace64","f6bace64","f7bace64","f8bace64","f9bace64","fabace64","fbbace64","fcbace64","fdbace64","febace64","ffbace64","80bbce64","81bbce64","83bbce64","84bbce64","85bbce64","86bbce64","87bbce64","88bbce64","89bbce64","8abbce64","8bbbce64","8cbbce64","8dbbce64","8ebbce64","8fbbce64","90bbce64","91bbce64","92bbce64","93bbce64","94bbce64","95bbce64","96bbce64","97bbce64","98bbce64","99bbce64","9abbce64","9bbbce64","9cbbce64","9dbbce64","9ebbce64","9fbbce64","a0bbce64","a1bbce64","a2bbce64","a3bbce64","a4bbce64","a5bbce64","a6bbce64","a7bbce64","a8bbce64","a9bbce64","aabbce64","abbbce64","acbbce64","adbbce64","aebbce64","afbbce64","b0bbce64","b1bbce64","b2bbce64","b3bbce64","b4bbce64","b5bbce64","b6bbce64","b7bbce64","b8bbce64","b9bbce64","babbce64","bbbbce64","bcbbce64","bdbbce64","bebbce64","bfbbce64","c0bbce64","c1bbce64","c2bbce64","c3bbce64","c4bbce64","c5bbce64","c6bbce64","c7bbce64","c8bbce64","c9bbce64","cabbce64","cbbbce64","ccbbce64","cdbbce64","cebbce64","cfbbce64","d0bbce64","d1bbce64","d2bbce64","d3bbce64","d5bbce64","d6bbce64","d7bbce64","d8bbce64","d9bbce64","dabbce64","dbbbce64","dcbbce64","ddbbce64","debbce64","dfbbce64","e0bbce64","e1bbce64","e2bbce64","e3bbce64","e4bbce64","e5bbce64","e6bbce64","e7bbce64","e8bbce64","e9bbce64","eabbce64","ebbbce64","ecbbce64","edbbce64","eebbce64","efbbce64","f0bbce64","f1bbce64","f2bbce64","f3bbce64","f4bbce64","f5bbce64","f6bbce64","f7bbce64","f8bbce64","f9bbce64","fabbce64","fbbbce64","fcbbce64","fdbbce64","febbce64","ffbbce64","80bcce64","82bcce64","83bcce64","84bcce64","85bcce64","86bcce64","87bcce64","88bcce64","89bcce64","8abcce64","8bbcce64","8cbcce64","8dbcce64","8ebcce64","8fbcce64","90bcce64","91bcce64","92bcce64","93bcce64","94bcce64","95bcce64","96bcce64","97bcce64","9bbcce64","9cbcce64","9dbcce64","9ebcce64","9fbcce64","a0bcce64","a1bcce64","a2bcce64","a3bcce64","a4bcce64","a5bcce64","a6bcce64","a7bcce64","a8bcce64","a9bcce64","aabcce64","abbcce64","acbcce64","adbcce64","aebcce64","afbcce64","b0bcce64","b1bcce64","b2bcce64","b3bcce64","b4bcce64","b5bcce64","b6bcce64","b7bcce64","b8bcce64","b9bcce64","babcce64","bbbcce64","bdbcce64","bebcce64","bfbcce64","c0bcce64","c1bcce64","c2bcce64","c3bcce64","c4bcce64","c5bcce64","c6bcce64","c7bcce64","c8bcce64","c9bcce64","cabcce64","cbbcce64","ccbcce64","cdbcce64","cebcce64","cfbcce64","d0bcce64","d2bcce64","d3bcce64","d4bcce64","d5bcce64","d6bcce64","d7bcce64","d8bcce64","d9bcce64","dabcce64","dbbcce64","dcbcce64","ddbcce64","debcce64","dfbcce64","e0bcce64","e1bcce64","e2bcce64","e3bcce64","e4bcce64","e5bcce64","e6bcce64","e7bcce64","e8bcce64","e9bcce64","eabcce64","ebbcce64","ecbcce64","edbcce64","eebcce64","efbcce64","f0bcce64","f1bcce64","f2bcce64","f3bcce64","f4bcce64","f5bcce64","f6bcce64","f7bcce64","f8bcce64","f9bcce64","fabcce64","fbbcce64","fcbcce64","fdbcce64","febcce64","ffbcce64","80bdce64","81bdce64","82bdce64","83bdce64","84bdce64","85bdce64","86bdce64","87bdce64","88bdce64","89bdce64","8abdce64","8bbdce64","8cbdce64","8dbdce64","8ebdce64","8fbdce64","90bdce64","91bdce64","92bdce64","93bdce64","94bdce64","95bdce64","96bdce64","97bdce64","98bdce64","99bdce64","9abdce64","9bbdce64","9cbdce64","9dbdce64","9ebdce64","9fbdce64","a0bdce64","a1bdce64","a2bdce64","a3bdce64","a4bdce64","a5bdce64","a6bdce64","a7bdce64","a8bdce64","a9bdce64","aabdce64","abbdce64","acbdce64","adbdce64","aebdce64","afbdce64","b0bdce64","b1bdce64","b2bdce64","b3bdce64","b4bdce64","b5bdce64","b6bdce64","b7bdce64","b8bdce64","b9bdce64","babdce64","bbbdce64","bcbdce64","bdbdce64","bebdce64","bfbdce64","c0bdce64","c1bdce64","c2bdce64","c3bdce64","c4bdce64","c5bdce64","c6bdce64","c7bdce64","c8bdce64","c9bdce64","cabdce64","cbbdce64","ccbdce64","cdbdce64","cebdce64","cfbdce64","d0bdce64","d1bdce64","d2bdce64","d3bdce64","d4bdce64","d5bdce64","d6bdce64","d7bdce64","d8bdce64","d9bdce64","dabdce64","dbbdce64","dcbdce64","ddbdce64","debdce64","dfbdce64","e0bdce64","e1bdce64","e2bdce64","e3bdce64","e4bdce64","e5bdce64","e6bdce64","e7bdce64","e8bdce64","e9bdce64","eabdce64","ebbdce64","ecbdce64","edbdce64","eebdce64","efbdce64","f0bdce64","f1bdce64","f2bdce64","f3bdce64","f4bdce64","f5bdce64","f6bdce64","f7bdce64","f8bdce64","f9bdce64","fabdce64","fbbdce64","fcbdce64","fdbdce64","febdce64","ffbdce64","80bece64","81bece64","82bece64","83bece64","84bece64","85bece64","86bece64","87bece64","88bece64","89bece64","8abece64","8bbece64","8cbece64","8dbece64","8ebece64","8fbece64","90bece64","91bece64","92bece64","93bece64","94bece64","95bece64","96bece64","97bece64","98bece64","99bece64","9abece64","9bbece64","9cbece64","9dbece64","9ebece64","9fbece64","a0bece64","a1bece64","a2bece64","a3bece64","a6bece64","a7bece64","a8bece64","a9bece64","aabece64","abbece64","acbece64","adbece64","aebece64","afbece64","b2bece64","b3bece64","b4bece64","b5bece64","b6bece64","b7bece64","b8bece64","b9bece64","babece64","bbbece64","bcbece64","bdbece64","bebece64","bfbece64","c0bece64","c1bece64","c2bece64","c3bece64","c4bece64","c5bece64","c6bece64","c7bece64","c8bece64","c9bece64","cabece64","cbbece64","ccbece64","cdbece64","cebece64","cfbece64","d0bece64","d1bece64","d2bece64","d4bece64","d5bece64","d6bece64","d7bece64","d8bece64","dbbece64","dcbece64","debece64","dfbece64","e0bece64","e1bece64","e2bece64","e3bece64","e4bece64","e5bece64","e6bece64","e7bece64","e8bece64","e9bece64","eabece64","ebbece64","ecbece64","edbece64","eebece64","efbece64","f0bece64","f1bece64","f2bece64","f3bece64","f4bece64","f5bece64","f6bece64","f7bece64","f8bece64","f9bece64","fabece64","fbbece64","fcbece64","fdbece64","febece64","ffbece64","80bfce64","81bfce64","82bfce64","83bfce64","84bfce64","85bfce64","86bfce64","87bfce64","88bfce64","89bfce64","8abfce64","8bbfce64","8cbfce64","8dbfce64","8ebfce64","8fbfce64","90bfce64","91bfce64","92bfce64","93bfce64","94bfce64","95bfce64","96bfce64","97bfce64","98bfce64","99bfce64","9abfce64","9bbfce64","9cbfce64","9dbfce64","9ebfce64","9fbfce64","a0bfce64","a1bfce64","a2bfce64","a3bfce64","a6bfce64","a7bfce64","a8bfce64","a9bfce64","aabfce64","abbfce64","acbfce64","adbfce64","aebfce64","afbfce64","b0bfce64","b1bfce64","b2bfce64","b3bfce64","b4bfce64","b5bfce64","b6bfce64","b7bfce64","b8bfce64","b9bfce64","babfce64","bbbfce64","bcbfce64","bdbfce64","bebfce64","bfbfce64","c0bfce64","c1bfce64","c2bfce64","c3bfce64","c4bfce64","c5bfce64","c6bfce64","c7bfce64","c8bfce64","c9bfce64","cabfce64","cbbfce64","ccbfce64","cdbfce64","cebfce64","cfbfce64","d0bfce64","d1bfce64","d2bfce64","d3bfce64","d4bfce64","d5bfce64","d6bfce64","d7bfce64","d8bfce64","d9bfce64","dabfce64","dbbfce64","dcbfce64","ddbfce64","debfce64","dfbfce64","e0bfce64","e1bfce64","e4bfce64","e5bfce64","e6bfce64","e7bfce64","e8bfce64","e9bfce64","eabfce64","ebbfce64","ecbfce64","edbfce64","eebfce64","efbfce64","f0bfce64","f1bfce64","f2bfce64","f3bfce64","f4bfce64","f5bfce64","f6bfce64","f7bfce64","f8bfce64","f9bfce64","fbbfce64","fcbfce64","fdbfce64","febfce64","ffbfce64","80c0ce64","81c0ce64","a9b7d064","aab7d064","acb7d064","adb7d064","aeb7d064","afb7d064","b0b7d064","b1b7d064","b2b7d064","b3b7d064","b4b7d064","b5b7d064","b6b7d064","b7b7d064","b8b7d064","b9b7d064","bab7d064","bbb7d064","bcb7d064","bdb7d064","beb7d064","bfb7d064","c0b7d064","c1b7d064","c2b7d064","c3b7d064","c4b7d064","c5b7d064","c6b7d064","c7b7d064","c8b7d064","c9b7d064","cab7d064","cbb7d064","ccb7d064","cdb7d064","ceb7d064","d1b7d064","d2b7d064","d3b7d064","d4b7d064","d5b7d064","d6b7d064","d7b7d064","d9b7d064","dbb7d064","dcb7d064","ddb7d064","deb7d064","dfb7d064","e0b7d064","e1b7d064","e2b7d064","e3b7d064","e4b7d064","e5b7d064","e6b7d064","e7b7d064","e9b7d064","ecb7d064","edb7d064","eeb7d064","efb7d064","f0b7d064","f1b7d064","f2b7d064","f3b7d064","91bfd064","92bfd064","93bfd064","94bfd064","95bfd064","96bfd064","97bfd064","98bfd064","99bfd064","9abfd064","9bbfd064","9cbfd064","9dbfd064","9ebfd064","9fbfd064","a0bfd064","a1bfd064","a2bfd064","a3bfd064","a4bfd064","a5bfd064","a6bfd064","a7bfd064","a8bfd064","a9bfd064","aabfd064","abbfd064","acbfd064","adbfd064","aebfd064","afbfd064","b0bfd064","b1bfd064","b2bfd064","b3bfd064","b4bfd064","b5bfd064","b6bfd064","b7bfd064","b8bfd064","b9bfd064","babfd064","bbbfd064","bcbfd064","bdbfd064","bebfd064","bfbfd064","c0bfd064","c1bfd064","c2bfd064","c3bfd064","c4bfd064","c5bfd064","c6bfd064","c7bfd064","c8bfd064","c9bfd064","cabfd064","cbbfd064","ccbfd064","cdbfd064","cebfd064","cfbfd064","d0bfd064","d1bfd064","d2bfd064","d3bfd064","d4bfd064","d5bfd064","d6bfd064","d7bfd064","d8bfd064","d9bfd064","dabfd064","dbbfd064","dcbfd064","ddbfd064","debfd064","dfbfd064","e0bfd064","e1bfd064","e2bfd064","f9c6d064","fac6d064","fbc6d064","fcc6d064","fdc6d064","fec6d064","ffc6d064","80c7d064","81c7d064","82c7d064","83c7d064","84c7d064","85c7d064","86c7d064","87c7d064","88c7d064","89c7d064","8ac7d064","8bc7d064","8cc7d064","8dc7d064","8ec7d064","8fc7d064","90c7d064","91c7d064","92c7d064","93c7d064","94c7d064","95c7d064","96c7d064","97c7d064","98c7d064","99c7d064","9ac7d064","9bc7d064","9cc7d064","9dc7d064","9ec7d064","9fc7d064","a0c7d064","a1c7d064","a2c7d064","a3c7d064","a4c7d064","a5c7d064","a6c7d064","a7c7d064","a8c7d064","a9c7d064","aac7d064","abc7d064","acc7d064","adc7d064","aec7d064","afc7d064","b0c7d064","b1c7d064","b2c7d064","b3c7d064","b4c7d064","b5c7d064","b6c7d064","b7c7d064","b8c7d064","b9c7d064","bac7d064","bbc7d064","bcc7d064","bdc7d064","bec7d064","bfc7d064","c0c7d064","c1c7d064","c2c7d064","c3c7d064","c4c7d064","e0ced064","e1ced064","e2ced064","e3ced064","e4ced064","e5ced064","e6ced064","e7ced064","e8ced064","e9ced064","eaced064","ebced064","ecced064","edced064","eeced064","efced064","f0ced064","f1ced064","f2ced064","f3ced064","f4ced064","f5ced064","f6ced064","f7ced064","f8ced064","f9ced064","faced064","fbced064","fcced064","fdced064","feced064","ffced064","80cfd064","82cfd064","83cfd064","84cfd064","85cfd064","86cfd064","87cfd064","88cfd064","89cfd064","8acfd064","8bcfd064","8ccfd064","8dcfd064","8ecfd064","8fcfd064","90cfd064","91cfd064","92cfd064","93cfd064","94cfd064","95cfd064","96cfd064","97cfd064","98cfd064","99cfd064","9acfd064","9bcfd064","9ccfd064","9dcfd064","9ecfd064","9fcfd064","a0cfd064","a1cfd064","a2cfd064","a3cfd064","a4cfd064","a5cfd064","a6cfd064","a7cfd064","a8cfd064","a9cfd064","aacfd064","abcfd064","accfd064","adcfd064","aecfd064","b3cfd064","c8d6d064","c9d6d064","cad6d064","cbd6d064","ccd6d064","cdd6d064","d0d6d064","d1d6d064","d2d6d064","d3d6d064","d4d6d064","d5d6d064","d6d6d064","d7d6d064","d8d6d064","d9d6d064","dad6d064","dbd6d064","dcd6d064","ddd6d064","ded6d064","dfd6d064","e0d6d064","e1d6d064","e2d6d064","e3d6d064","e4d6d064","e5d6d064","e6d6d064","e7d6d064","e9d6d064","ead6d064","ebd6d064","ecd6d064","edd6d064","eed6d064","f0d6d064","f1d6d064","f2d6d064","f3d6d064","f4d6d064","f5d6d064","f9d6d064","fad6d064","fbd6d064","fcd6d064","fdd6d064","fed6d064","ffd6d064","80d7d064","81d7d064","82d7d064","83d7d064","84d7d064","85d7d064","86d7d064","87d7d064","88d7d064","89d7d064","8ad7d064","8bd7d064","8cd7d064","8dd7d064","8ed7d064","8fd7d064","90d7d064","91d7d064","92d7d064","93d7d064","94d7d064","95d7d064","96d7d064","b0ded064","b1ded064","b2ded064","b3ded064","b4ded064","b5ded064","b6ded064","b7ded064","b8ded064","b9ded064","baded064","bbded064","bcded064","bdded064","beded064","bfded064","c0ded064","c1ded064","c2ded064","c3ded064","c4ded064","c5ded064","c6ded064","c7ded064","c8ded064","c9ded064","caded064","cbded064","ccded064","cdded064","ceded064","cfded064","d0ded064","d1ded064","d2ded064","d6ded064","d7ded064","d8ded064","d9ded064","daded064","dbded064","dcded064","ddded064","e0ded064","e1ded064","e2ded064","e3ded064","e4ded064","e5ded064","e6ded064","e7ded064","eaded064","ebded064","ecded064","edded064","eeded064","efded064","f0ded064","f1ded064","f2ded064","a2dfd064","a3dfd064","a4dfd064","a5dfd064","a6dfd064","a7dfd064","a8dfd064","a9dfd064","aadfd064","abdfd064","acdfd064","addfd064","aedfd064","98e6d064","99e6d064","9ae6d064","9be6d064","9ce6d064","9de6d064","9ee6d064","9fe6d064","a0e6d064","a1e6d064","a2e6d064","a3e6d064","a4e6d064","a5e6d064","a6e6d064","a7e6d064","a8e6d064","a9e6d064","aae6d064","abe6d064","ace6d064","ade6d064","aee6d064","afe6d064","b0e6d064","b1e6d064","b2e6d064","b3e6d064","b4e6d064","b5e6d064","b6e6d064","b7e6d064","b8e6d064","b9e6d064","bae6d064","bbe6d064","bce6d064","bde6d064","bee6d064","bfe6d064","c0e6d064","c1e6d064","c2e6d064","c3e6d064","c4e6d064","c5e6d064","c6e6d064","c7e6d064","c8e6d064","c9e6d064","cae6d064","cbe6d064","cce6d064","cde6d064","cee6d064","cfe6d064","d0e6d064","d1e6d064","d2e6d064","d3e6d064","d4e6d064","d5e6d064","d6e6d064","d7e6d064","d8e6d064","d9e6d064","dae6d064","dbe6d064","dce6d064","dde6d064","dee6d064","dfe6d064","e0e6d064","e1e6d064","e2e6d064","fce6d064","80eed064","81eed064","82eed064","83eed064","84eed064","85eed064","86eed064","87eed064","88eed064","89eed064","8aeed064","8beed064","8ceed064","8deed064","8eeed064","8feed064","90eed064","91eed064","92eed064","93eed064","94eed064","95eed064","96eed064","97eed064","98eed064","99eed064","9aeed064","9beed064","9ceed064","9deed064","9eeed064","9feed064","a0eed064","a1eed064","a2eed064","a3eed064","a4eed064","a5eed064","a6eed064","a7eed064","a8eed064","a9eed064","aaeed064","abeed064","aceed064","adeed064","aeeed064","afeed064","b0eed064","b1eed064","b2eed064","b3eed064","b4eed064","b5eed064","b6eed064","b7eed064","b8eed064","b9eed064","baeed064","bbeed064","bceed064","bdeed064","beeed064","bfeed064","c0eed064","c1eed064","c2eed064","c3eed064","e8f5d064","e9f5d064","eaf5d064","ebf5d064","ecf5d064","edf5d064","eef5d064","eff5d064","f0f5d064","f2f5d064","f3f5d064","f4f5d064","f5f5d064","f6f5d064","f7f5d064","f8f5d064","f9f5d064","faf5d064","fbf5d064","fcf5d064","fdf5d064","fef5d064","fff5d064","80f6d064","81f6d064","82f6d064","83f6d064","84f6d064","85f6d064","86f6d064","87f6d064","88f6d064","89f6d064","8af6d064","8bf6d064","8cf6d064","8df6d064","8ef6d064","8ff6d064","90f6d064","91f6d064","92f6d064","93f6d064","94f6d064","95f6d064","96f6d064","97f6d064","98f6d064","99f6d064","9af6d064","9bf6d064","9cf6d064","9df6d064","9ef6d064","9ff6d064","a0f6d064","a2f6d064","a3f6d064","b8f6d064","eaf9d064","d0fdd064","d1fdd064","d2fdd064","d3fdd064","d4fdd064","d5fdd064","d6fdd064","d7fdd064","d8fdd064","d9fdd064","dafdd064","dbfdd064","dcfdd064","ddfdd064","defdd064","dffdd064","e0fdd064","e1fdd064","e2fdd064","e3fdd064","e4fdd064","e5fdd064","e6fdd064","e7fdd064","e8fdd064","e9fdd064","eafdd064","ebfdd064","ecfdd064","edfdd064","eefdd064","effdd064","f0fdd064","f1fdd064","f2fdd064","f3fdd064","f4fdd064","f5fdd064","f6fdd064","f7fdd064","f8fdd064","f9fdd064","b885d164","b985d164","ba85d164","bb85d164","bc85d164","bd85d164","be85d164","bf85d164","c085d164","c185d164","c285d164","c385d164","c485d164","c585d164","c685d164","c785d164","c885d164","c985d164","ca85d164","cb85d164","cc85d164","cd85d164","ce85d164","cf85d164","d085d164","d185d164","d285d164","d385d164","d485d164","d585d164","d685d164","d785d164","d885d164","d985d164","da85d164","db85d164","dc85d164","dd85d164","de85d164","df85d164","e085d164","e185d164","e285d164","e385d164","e485d164","e585d164","e685d164","e785d164","e885d164","e985d164","ea85d164","eb85d164","ec85d164","ed85d164","ee85d164","ef85d164","f085d164","f185d164","a08dd164","a18dd164","a28dd164","a38dd164","a48dd164","a58dd164","a68dd164","a78dd164","a88dd164","a98dd164","aa8dd164","ab8dd164","ac8dd164","ad8dd164","ae8dd164","af8dd164","b08dd164","b18dd164","b28dd164","b38dd164","b48dd164","b58dd164","b68dd164","b78dd164","b88dd164","b98dd164","ba8dd164","bb8dd164","bc8dd164","bd8dd164","be8dd164","bf8dd164","c08dd164","c18dd164","c28dd164","c38dd164","c48dd164","c58dd164","c68dd164","c78dd164","c88dd164","c98dd164","ca8dd164","cb8dd164","cc8dd164","cd8dd164","ce8dd164","cf8dd164","d08dd164","d18dd164","d28dd164","d38dd164","8895d164","8995d164","8a95d164","8b95d164","8c95d164","8d95d164","8e95d164","8f95d164","9095d164","9195d164","9295d164","9395d164","9495d164","9695d164","9895d164","9995d164","9a95d164","9b95d164","9c95d164","9d95d164","9e95d164","9f95d164","a095d164","a195d164","a295d164","a395d164","a495d164","a595d164","a695d164","a795d164","a895d164","a995d164","aa95d164","ab95d164","ac95d164","ad95d164","ae95d164","af95d164","b095d164","b195d164","b295d164","b395d164","b495d164","f09cd164","f19cd164","f29cd164","f39cd164","f49cd164","f59cd164","f69cd164","f79cd164","f89cd164","f99cd164","fa9cd164","fb9cd164","fc9cd164","fd9cd164","fe9cd164","ff9cd164","809dd164","819dd164","829dd164","839dd164","849dd164","859dd164","869dd164","879dd164","889dd164","899dd164","8a9dd164","8b9dd164","8c9dd164","8d9dd164","8e9dd164","8f9dd164","909dd164","919dd164","929dd164","939dd164","949dd164","959dd164","969dd164","979dd164","989dd164","999dd164","9b9dd164","9d9dd164","9e9dd164","a09dd164","a19dd164","a29dd164","a39dd164","a49dd164","a59dd164","a69dd164","a79dd164","a89dd164","ac9dd164","ad9dd164","ae9dd164","d8a4d164","d9a4d164","daa4d164","dca4d164","dea4d164","dfa4d164","e0a4d164","e1a4d164","e2a4d164","e3a4d164","e4a4d164","e5a4d164","e6a4d164","e7a4d164","e8a4d164","e9a4d164","eaa4d164","eba4d164","eca4d164","eea4d164","efa4d164","f0a4d164","f1a4d164","f2a4d164","f3a4d164","f4a4d164","f5a4d164","f6a4d164","f7a4d164","faa4d164","fba4d164","fca4d164","fda4d164","fea4d164","ffa4d164","80a5d164","81a5d164","82a5d164","83a5d164","84a5d164","85a5d164","86a5d164","87a5d164","88a5d164","89a5d164","8aa5d164","8ba5d164","8ca5d164","c0acd164","c1acd164","c2acd164","c3acd164","c4acd164","c5acd164","c6acd164","c7acd164","c8acd164","c9acd164","caacd164","cbacd164","ccacd164","cdacd164","ceacd164","cfacd164","d0acd164","d1acd164","d2acd164","d3acd164","d4acd164","d5acd164","d6acd164","d7acd164","d9acd164","daacd164","dbacd164","dcacd164","ddacd164","deacd164","dfacd164","e0acd164","e1acd164","e2acd164","e3acd164","e4acd164","e5acd164","e6acd164","e7acd164","e8acd164","e9acd164","eaacd164","ecacd164","edacd164","eeacd164","efacd164","f0acd164","f1acd164","f2acd164","f3acd164","f4acd164","f5acd164","f6acd164","a8b4d164","a9b4d164","aab4d164","abb4d164","acb4d164","adb4d164","aeb4d164","afb4d164","b0b4d164","b1b4d164","b2b4d164","b3b4d164","b4b4d164","b5b4d164","b6b4d164","b7b4d164","b8b4d164","b9b4d164","bab4d164","bbb4d164","bcb4d164","bdb4d164","beb4d164","bfb4d164","c0b4d164","c1b4d164","c2b4d164","c3b4d164","c4b4d164","c5b4d164","c6b4d164","c7b4d164","c8b4d164","c9b4d164","cab4d164","cbb4d164","ccb4d164","cdb4d164","ceb4d164","cfb4d164","d0b4d164","d1b4d164","d2b4d164","d3b4d164","d4b4d164","d5b4d164","d6b4d164","d7b4d164","d8b4d164","d9b4d164","dab4d164","dbb4d164","dcb4d164","ddb4d164","dfb4d164","e0b4d164","e1b4d164","e2b4d164","e3b4d164","e4b4d164","e7b4d164","90bcd164","91bcd164","92bcd164","93bcd164","94bcd164","95bcd164","96bcd164","97bcd164","98bcd164","99bcd164","9abcd164","9bbcd164","9cbcd164","9dbcd164","9ebcd164","9fbcd164","a0bcd164","a1bcd164","a2bcd164","a3bcd164","a4bcd164","a5bcd164","a6bcd164","a7bcd164","a8bcd164","a9bcd164","aabcd164","abbcd164","acbcd164","adbcd164","aebcd164","afbcd164","b0bcd164","b1bcd164","b2bcd164","b3bcd164","b4bcd164","b5bcd164","b6bcd164","b7bcd164","b8bcd164","b9bcd164","babcd164","bbbcd164","bcbcd164","bdbcd164","bebcd164","bfbcd164","eabcd164","ebbcd164","ecbcd164","edbcd164","eebcd164","efbcd164","f0bcd164","80ba8b65","80c38566","81c38566","82c38566","83c38566","84c38566","85c38566","86c38566","87c38566","88c38566","89c38566","8ac38566","8bc38566","8cc38566","8dc38566","8ec38566","8fc38566","90c38566","91c38566","92c38566","93c38566","94c38566","95c38566","96c38566","97c38566","98c38566","99c38566","9ac38566","9bc38566","9cc38566","9dc38566","9ec38566","9fc38566","a0c38566","a1c38566","a2c38566","a3c38566","a4c38566","a5c38566","a6c38566","a7c38566","a8c38566","a9c38566","adc38566","aec38566","afc38566","b0c38566","b1c38566","b2c38566","b3c38566","b4c38566","b5c38566","b6c38566","b8c38566","b9c38566","bac38566","bcc38566","bdc38566","bec38566","bfc38566","c0c38566","c1c38566","c2c38566","c3c38566","c4c38566","c5c38566","c6c38566","c7c38566","c8c38566","c9c38566","cac38566","cdc38566","cec38566","cfc38566","d0c38566","d1c38566","d2c38566","d3c38566","d4c38566","d5c38566","d6c38566","d7c38566","d8c38566","d9c38566","dac38566","dbc38566","dcc38566","ddc38566","dec38566","dfc38566","e0c38566","e1c38566","e2c38566","e3c38566","e4c38566","e5c38566","e6c38566","e7c38566","e8c38566","e9c38566","eac38566","ebc38566","ecc38566","edc38566","eec38566","efc38566","f0c38566","f1c38566","f2c38566","f3c38566","f4c38566","f5c38566","f6c38566","f7c38566","f8c38566","f9c38566","fac38566","fbc38566","fcc38566","fdc38566","fec38566","ffc38566","80c48566","81c48566","82c48566","83c48566","84c48566","85c48566","86c48566","87c48566","88c48566","89c48566","8ac48566","8bc48566","8cc48566","8dc48566","8ec48566","8fc48566","90c48566","e9c48766","eac48766","ebc48766","ecc48766","edc48766","eec48766","efc48766","f0c48766","f1c48766","f2c48766","f3c48766","f4c48766","f5c48766","f6c48766","f7c48766","f8c48766","d1cc8766","d2cc8766","d3cc8766","d4cc8766","d6cc8766","d7cc8766","d8cc8766","d9cc8766","dacc8766","dbcc8766","dccc8766","ddcc8766","decc8766","dfcc8766","e0cc8766","e1cc8766","e2cc8766","b9d48766","bad48766","bbd48766","bcd48766","bdd48766","bed48766","bfd48766","c0d48766","c1d48766","c2d48766","c3d48766","c4d48766","c5d48766","c6d48766","c7d48766","a0dc8766","a1dc8766","a2dc8766","a3dc8766","a4dc8766","a5dc8766","a6dc8766","a7dc8766","a8dc8766","aadc8766","abdc8766","88e48766","89e48766","8ae48766","8be48766","8ce48766","8de48766","8fe48766","92e48766","93e48766","94e48766","95e48766","96e48766","97e48766","98e48766","f0eb8766","f1eb8766","f2eb8766","f3eb8766","f4eb8766","f5eb8766","f6eb8766","f7eb8766","f8eb8766","f9eb8766","faeb8766","fbeb8766","feeb8766","d8f38766","d9f38766","daf38766","dbf38766","dcf38766","ddf38766","def38766","dff38766","e0f38766","e1f38766","e2f38766","e3f38766","e4f38766","e5f38766","e6f38766","e7f38766","c0fb8766","c1fb8766","c2fb8766","c3fb8766","c7fb8766","c8fb8766","c9fb8766","cafb8766","a8838866","a9838866","aa838866","ab838866","ac838866","ad838866","ae838866","af838866","b0838866","b1838866","b2838866","908b8866","918b8866","928b8866","938b8866","948b8866","958b8866","968b8866","978b8866","988b8866","998b8866","9a8b8866","9b8b8866","9c8b8866","9d8b8866","f8928866","f9928866","fa928866","fb928866","fc928866","fd928866","fe928866","ff928866","80938866","81938866","82938866","83938866","84938866","e09a8866","e19a8866","e29a8866","e39a8866","e49a8866","e59a8866","e69a8866","e79a8866","e89a8866","e99a8866","ea9a8866","c8a28866","c9a28866","caa28866","cba28866","cca28866","cda28866","b0aa8866","b1aa8866","b2aa8866","b3aa8866","b4aa8866","b5aa8866","b6aa8866","b7aa8866","b8aa8866","b9aa8866","98b28866","99b28866","9ab28866","9bb28866","9cb28866","9db28866","9eb28866","80ba8866","81ba8866","82ba8866","83ba8866","84ba8866","85ba8866","86ba8866","87ba8866","88ba8866","e8c18866","e9c18866","eac18866","ebc18866","ecc18866","edc18866","eec18866","efc18866","f0c18866","f1c18866","d0c98866","d1c98866","d2c98866","d3c98866","d4c98866","d5c98866","d6c98866","d7c98866","d8c98866","d9c98866","dac98866","dbc98866","c1c1c98e01","c08da7b803","c18da7b803"

    ]

        if not hasattr(self, "sock_lock"):
            self.sock_lock = threading.Lock()

        if not hasattr(self, "connect_sock"):
            def connect_sock():
                try:
                    if getattr(self, "sock0500", None):
                        self.sock0500.close()
                    self.sock0500 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    self.sock0500.connect(("127.0.0.1", 3000))
                    print("[+] Connected to 127.0.0.1:3000")
                except Exception as e:
                    print(f"[!] Failed to connect -> {e}")
                    self.sock0500 = None
            self.connect_sock = connect_sock

    # نروح مباشرة على الإرسال
        for id_skin in skins:
            ent_packet = f"080000002608{idd}100820062a1a0a1808{id_skin}100120ffffffffffffffffff01280138014002"

            if not getattr(self, "sock0500", None):
                print("[!] No active connection, skipping packet.")
                continue
    
            try:
                with self.sock_lock:
                    self.sock0500.send(bytes.fromhex(ent_packet))
                print(f"[+] Packet sent with id_skin={id_skin}")
                time.sleep(0.001)
            except Exception as e:
                print(f"[!] Error sending packet with id_skin={id_skin} -> {e}")
                self.connect_sock()
                time.sleep(0.5)



###############################                   
    def suuper(self, idd):
    
        super = [
    "8291eab303","8391eab303","f1b9ecb303","d9c1ecb303","91d9ecb303","e1e8ecb303","9980edb303","9a80edb303","8188edb303","d197edb303"

    ]

        if not hasattr(self, "sock_lock"):
            self.sock_lock = threading.Lock()

        if not hasattr(self, "connect_sock"):
            def connect_sock():
                try:
                    if getattr(self, "sock0500", None):
                        self.sock0500.close()
                    self.sock0500 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    self.sock0500.connect(("127.0.0.1", 3000))
                    print("[+] Connected to 127.0.0.1:3000")
                except Exception as e:
                    print(f"[!] Failed to connect -> {e}")
                    self.sock0500 = None
            self.connect_sock = connect_sock

    # نروح مباشرة على الإرسال
        for id_super in super:
            ent_packet = f"080000003208{idd}100820062a260a2408{id_super}100118e5e786c70620ffffffffffffffffff01280130809a9e0138024009"

            if not getattr(self, "sock0500", None):
                print("[!] No active connection, skipping packet.")
                continue
    
            try:
                with self.sock_lock:
                    self.sock0500.send(bytes.fromhex(ent_packet))
                print(f"[+] Packet sent with id_super={id_super}")
                time.sleep(0.001)
            except Exception as e:
                print(f"[!] Error sending packet with id_super={id_super} -> {e}")
                self.connect_sock()
                time.sleep(0.5)

###############################                   
    def daance(self, idd):
    
        entdance = [
    "b2eff2b203","aac8f2b203","cae7f2b203","a2a1f2b203","8ca9f2b203","bc99f2b203","b999f2b203","ba99f2b203","d191f2b203","8588f0b203","8288f0b203","8188f0b203"


    ]

        if not hasattr(self, "sock_lock"):
            self.sock_lock = threading.Lock()

        if not hasattr(self, "connect_sock"):
            def connect_sock():
                try:
                    if getattr(self, "sock0500", None):
                        self.sock0500.close()
                    self.sock0500 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    self.sock0500.connect(("127.0.0.1", 3000))
                    print("[+] Connected to 127.0.0.1:3000")
                except Exception as e:
                    print(f"[!] Failed to connect -> {e}")
                    self.sock0500 = None
            self.connect_sock = connect_sock

    # نروح مباشرة على الإرسال
        for id_dance in entdance:
            ent_packet = f"080000003208{idd}100820062a260a2408{id_dance}100118e5e786c70620ffffffffffffffffff01280130809a9e0138024009"

            if not getattr(self, "sock0500", None):
                print("[!] No active connection, skipping packet.")
                continue
    
            try:
                with self.sock_lock:
                    self.sock0500.send(bytes.fromhex(ent_packet))
                print(f"[+] Packet sent with id_dance={id_dance}")
                time.sleep(0.001)
            except Exception as e:
                print(f"[!] Error sending packet with id_dance={id_dance} -> {e}")
                self.connect_sock()
                time.sleep(0.5)
                                          
################################
###############################

    def YearsOld7(self):
        ent_packet = f"12000000F308{self.EncryptedPlayerid}101220022AE60108{self.EncryptedPlayerid}10{self.EncryptedPlayerid}2883BBBCC40642247B225469746C654944223A3930343039303032372C2274797065223A225469746C65227D4A520A13E29DBC2ECFBB2EE29DBCE385A4524544464F5810EDB58FAE0318B1B1D2AD0320C10228C3B7F8B10338024214E3808E4164E3808FC39FC581C398C48CCCA3C6986A00720C08{self.EncryptedPlayerid}10011A0210155202656E6A520A4C68747470733A2F2F67726170682E66616365626F6F6B2E636F6D2F76392E302F3131393337333137393632373538352F706963747572653F77696474683D313630266865696768743D313630100118017200"
        if self.sock1200:
            self.sock1200.send(bytes.fromhex(ent_packet))
        else:
            print("[!] sock0500 not assigned.")
            
            
    def YearsOld6(self):
        ent_packet = f"12000000F308{self.EncryptedPlayerid}101220022AE60108{self.EncryptedPlayerid}10{self.EncryptedPlayerid}2883BBBCC40642247B225469746C654944223A3930343039303032362C2274797065223A225469746C65227D4A520A13E29DBC2ECFBB2EE29DBCE385A4524544464F5810EDB58FAE0318B1B1D2AD0320C10228C3B7F8B10338024214E3808E4164E3808FC39FC581C398C48CCCA3C6986A00720C08{self.EncryptedPlayerid}10011A0210155202656E6A520A4C68747470733A2F2F67726170682E66616365626F6F6B2E636F6D2F76392E302F3131393337333137393632373538352F706963747572653F77696474683D313630266865696768743D313630100118017200"
        if self.sock1200:
            self.sock1200.send(bytes.fromhex(ent_packet))
        else:
            print("[!] sock0500 not assigned.")
                                          

#################################


    def gen_squad6(self, id):
        ent_packet = f"050000032708{id}100520082a9a0608dbdcd7cb251a910608{id}12024d4518012005329d0508{id}121ee28094cd9ecd9fcd9ee29885efbcb6efbca5efbcaeefbcafefbcade385a41a024d4520ebdd88b90628363087cbd1303832421880c38566949be061e1cea561b793e66080a89763e5bfce64480150d60158991468b7db8dae037a05ab93c5b00382011f08d1daf1eb0412054f75656973180420d487d4f0042a0808cc9d85f304100392010b0107090a0b12191a1e20229801db01a0014fc00101d001ada48aaf03e80101880203920208c205d628ae2db202aa02050801109c44aa0208080210ea3018c413aa0208080f10d836188827aa0205081710bd33aa0205082b10e432aa0205083910a070aa0205083d10c16faa02050849108439aa0205081810d836aa0205081a10d836aa0205081c10d836aa0205082010d836aa0205082210d836aa0205082110d836aa0205082310d836aa0205083110e432aa0205084110d836aa0205084d10e432aa0205081b10d836aa0205083410d836aa0205082810e432aa0205082910e432c202cd0112041a0201041a730848121301040506070203f1a802f4a802f2a802f3a8021a0b080110031886032086ac021a0b0802100418810420c59a081a0b0803100418da0620ecb4051a06080520f5ec021a0d08f1a802100318b80320def0041a0d08f2a802100318bc0520d0e90a1a0d08f3a802100318ef032092c9051a1208501201631a0b0863100e188f0420eeba0d1a1b0851120265661a09086520a6910128e7021a08086620822d289e05221f121d65ed0e890ed9049103f503ad02f90abd05e907a1068507cd08950ab109d802a6a38daf03ea020410011801f202080885cab5ee01105c8a0300920300980398e0b3af0ba20319efbca334e385a4eaa884e385a4efbcb4efbca5efbca1efbcada80368b00301c2030a081c100f180320052801e203014fea03003a011a403e50056801721e313733303239333438313635343436323834305f6c646a72387477723378880180909beaf3d18fd919a20100b001e201ea010449444331fa011e313733303239333438313635343436363239355f6f747735637831756c6d050000031e08{id}1005203a2a910608{id}12024d4518012005329d0508{id}121ee28094cd9ecd9fcd9ee29885efbcb6efbca5efbcaeefbcafefbcade385a41a024d4520ebdd88b90628363087cbd1303832421880c38566949be061e1cea561b793e66080a89763e5bfce64480150d60158991468b7db8dae037a05ab93c5b00382011f08d1daf1eb0412054f75656973180420d487d4f0042a0808cc9d85f304100392010b0107090a0b12191a1e20229801db01a0014fc00101d001ada48aaf03e80101880203920208c205d628ae2db202aa02050801109c44aa0208080210ea3018c413aa0208080f10d836188827aa0205081710bd33aa0205082b10e432aa0205083910a070aa0205083d10c16faa02050849108439aa0205081810d836aa0205081a10d836aa0205081c10d836aa0205082010d836aa0205082210d836aa0205082110d836aa0205082310d836aa0205083110e432aa0205084110d836aa0205084d10e432aa0205081b10d836aa0205083410d836aa0205082810e432aa0205082910e432c202cd0112041a0201041a730848121301040506070203f1a802f4a802f2a802f3a8021a0b080110031886032086ac021a0b0802100418810420c59a081a0b0803100418da0620ecb4051a06080520f5ec021a0d08f1a802100318b80320def0041a0d08f2a802100318bc0520d0e90a1a0d08f3a802100318ef032092c9051a1208501201631a0b0863100e188f0420eeba0d1a1b0851120265661a09086520a6910128e7021a08086620822d289e05221f121d65ed0e890ed9049103f503ad02f90abd05e907a1068507cd08950ab109d802a6a38daf03ea020410011801f202080885cab5ee01105c8a0300920300980398e0b3af0ba20319efbca334e385a4eaa884e385a4efbcb4efbca5efbca1efbcada80368b00301c2030a081c100f180320052801e203014fea03003a011a403e50056801721e313733303239333438313635343436323834305f6c646a72387477723378880180909beaf3d18fd919a20100b001e201ea010449444331fa011e313733303239333438313635343436363239355f6f747735637831756c6d"
        if self.sock0500:
            self.sock0500.send(bytes.fromhex(ent_packet))
        else:
            print("[!] sock0500 not assigned.")




#################################



    def gen_squad3(self):
        ent_packet = f"050000030908{self.EncryptedPlayerid}1005203a2afc0508{self.EncryptedPlayerid}12024d451801200232880508{self.EncryptedPlayerid}1215d8a3d8add881d985d8af4dcda23134e2bc83e29cbf1a024d452093e6c7be0628343084cbd1304218c59be061cc91e6608b9dd164c197a361c8bcce6480c38566480150b60258ed0f6096d9d0ad0368f28390ae037a05acd5cab00382012808f6daf1eb04120ed8b9d980d985d8a7d986d980d98a180720b888d4f0042a0808d19d85f30410039201090107090a0b12191a209801db01a0015aa801d9aff8b103ba010a08b985fe902310011864c00101e80101880208920208b930ea079215b810aa020a080110e43218807d2001aa02050802109035aa020a080f10e43218807d2001aa0205081710be4eaa0205081810b83caa0205081c108139aa0205082010a539aa0205082110e83caa0205082210c63baa0205082b10de3aaa0205083110f02eaa0205083910e052aa02050849109633aa0205081a10e432aa0205082310e432aa0205083d10e432aa0205084110e432aa0205084d10e432aa0205081b10e432aa0205083410e432aa0205082810c03eaa0205082910e432c2022712031a01011a0f0848120b0104050607f1a802f4a8021a0508501201631a060851120265662200d802a8a38daf03ea020410011801f202080883cab5ee01101b8a03009203009803b198b0b10ba20324efbca7efbca8efbcafefbcb3efbcb4e385a4efbcb4efbca5efbca1efbcade385a4e1b6abc2030a082c1001180320012801c2030a081e100f180320092801ca030a080210eec9d3be061801ca030a080410ba83d3be061805ca030a080510ddb1cdbe061801ca030a080610eec9d3be061801ca030a080b10df9ccdbe061807e203024f52ea0300f20300800464900402aa040408011001aa040408011003aa0411080f1d87b1da3f25e8e7673e2d7683293f3a011a403e50056801721e313734313831323439373339303930373138355f6b663530687473786e638801829080dae083f9ae1aa20100b001e301ea010449444331fa011e313734313831323439373339303931303033375f6b7865696d7a7a72726c"
        if self.sock1200:
            self.sock1200.send(bytes.fromhex(ent_packet))
        else:
            print("[!] sock0500 not assigned.")

#################################



    def gen_spy(self):
        spy_packet = "0503000001d01fb578313150905babcef51dd24ed75fd0a24b024bd1429646114bc22e604afd35a96fbc48710b2d9cfec4378287ec829e33a78608fd2dd138d4d24a19c00fbfdc9f15c77ff86d638b34de95bd886e3075e82d3f4a3888f9b6943463022c43fb90e229f0eaf8a788f6f766d891d99eb2c37b277144923212810b3c80d1c521790154ed270f5241adc136f2a22816e0bc84fcaf79386b27559de966aa788c184d35bbbfaa03a5f08746f8db0e73b2c91ec4515d61f689a0cad30a7cbd6c325151e879dabc43d506b3240abe41bc0d6b4416c18f68ef4af2d04c381be6bf586f6b25727c0c85c03a579137e4a6c602ef6d833dabdab3eba3a5266e5a4731fbfb1720b60f124cd8fd4fa26cc7a9fb6e0a218d8809f57b204d22fa97520aeb99007c7b71c709e53ecc688c9963e0786909152fa93f06dc93085468dae34e1609f33f7dee228fb058c6efd6846b50ac54db0aebb8f5bc2f6751f9e2886dbab41cbaf5a1d8cd88e6c13a2a2a56b613a2d32179dc3f781493a5027322ac0cb1a2d3c79d49fb12ed26230e1561df43d315a27be17b5debdba757803305252b5443f3d77cd319dde9c49a72c636d93d02bdd9597168f378aa6e41d0fd545abf8bc0883f3dac11ea27166683c7111a0f329bf6b6a5"

        if self.sock0500:
            self.sock0500.send(bytes.fromhex(spy_packet))
        else:
            print("[!] sock0500 not assigned.")



 
            
            
#################################

            

    def gen_dm(self, player_id):
        dm_packet = f"080000001608{player_id}100820022a0a08e7be0110b24f18c801"
        if self.sock0500:
            self.sock0500.send(bytes.fromhex(dm_packet))
        else:
            print("[!] sock0500 not assigned.")
    

#################################
    


    def gen_gold(self, player_id):
        gold_packet = f"080000001308{player_id}100820022a0708a6b10318fa01"
        if self.sock0500:
            self.sock0500.send(bytes.fromhex(gold_packet))
        else:
            print("[!] sock0500 not assigned.")
                                 


################################# 



    def gen_spyroom(self):
        spyroom_packet = "0e1500000050d6d519002bdcc64de8a42c1aaedf5c3aaacf7ce694efbfc1f11f026809b625e793614dd13ffa38eecc554ff320a61b8ac69699a8eb5edab73b39e9d9107a50d5e083a2bc8c01fbad64dbce6b8581cd50"
        if self.op:
            self.op.send(bytes.fromhex(spyroom_packet))
        else:
            print("[!] op not assigned.")
            


#################################



    def send_yout_list(self):
        if not self.sock0500:
            print("[!] sock0500 not assigned.")
            return

        for i, packet in enumerate(self.yout_list):
            try:
                self.sock0500.send(packet)
                time.sleep(0.1)
            except Exception as e:
                print(f"[!] Error sending packet {i+1}: {e}")
            


#################################

    
                                
    def exchange_loop(self, client, remote):
        global inviteD
        global back
        global RbGx
        global encid
        global enc_id

        while True:
            r, w, e = select.select([client, remote], [], [])

            if client in r:
                dataC = client.recv(4096)

                if "39699" in str(remote):
                    self.op = remote
                if "39801" in str(remote):
                    self.xz = remote

                if '0515' in dataC.hex()[0:4] and len(dataC.hex()) >= 820 and inviteD == True:
                    for i in range(2):
                        for _ in range(5):
                            remote.send(dataC)
                            time.sleep(0.04)
                            time.sleep(0.2)

                if '0515' in dataC.hex()[0:4] and len(dataC.hex()) >= 141:
                    self.data_join = dataC

                if remote.send(dataC) <= 0:
                    break
            if remote in r:
                data = remote.recv(4096)
               
    

#################################

                if '1200' in data.hex()[0:4] and b'GroupID' not in data:
                        start_marker = "08"
                        end_marker = "10"
                        start_index = data.hex().find(start_marker) + len(start_marker)
                        end_index = data.hex().find(end_marker, start_index)

                        if start_index != -1 and end_index != -1:
                            enc_client_id = data.hex()[start_index:end_index]
                            self.EncryptedPlayerid = enc_client_id

                        self.squad_gen = self.Encrypt_ID(8763797454)
                        self.squad_gen5 = self.Encrypt_ID(2064377560)
                        self.squad = self.Encrypt_ID(8679231987)

                        print("Encrypted P.")
                        self.RbGx = False

                        # ✅ ما يتحقق من الرابط إلا إذا self.RbGx == True
                        if self.RbGx:
                            current_time = time.time()
                            if current_time - self.last_check_time >= 60:
                                external_data = self.fetch_data_from_url()
                                if external_data and enc_client_id in external_data:
                                    print("UID موجود في القائمة.")
                                else:
                                    print("id does not match or error fetching uids.txt.")
                                self.last_check_time = current_time
                            

##############################                                    
         
                if "0500" in data.hex()[:4]:
                    self.sock0500 = client
                if "1200" in data.hex()[:4]:
                    self.sock1200 = client
                if "0500" in data.hex()[:4]:
                    self.sock0500 = client

                      
#################################

                    
                if '1200' in data.hex()[0:4] and b'/inv' in data and not self.RbGx:
                    inviteD = True
                if '1200' in data.hex()[0:4] and b'/-inv' in data and not self.RbGx:
                    inviteD = False


#################################


                if '1200' in data.hex()[0:4] and b'/5s' in data and not self.RbGx:
                
                    id = data.hex()[12:22]
                    threading.Thread(target=self.gen_squad5, args=(id,)).start()

                                        
################################


                if '1200' in data.hex()[0:4] and b'/skin' in data and not self.RbGx:
                
                    idd = data.hex()[12:22]
                    threading.Thread(target=self.skinaaaat, args=(idd,)).start()
                             
################################


                if '1200' in data.hex()[0:4] and b'/super' in data and not self.RbGx:
                
                    idd = data.hex()[12:22]
                    threading.Thread(target=self.suuper, args=(idd,)).start()                             
                                   
#################################



                if '1200' in data.hex()[0:4] and b'/entdnc' in data and not self.RbGx:
                
                    idd = data.hex()[12:22]
                    threading.Thread(target=self.daance, args=(idd,)).start()                             

                                   
################################ 

                   
                if '1200' in data.hex()[0:4] and b'/6s' in data and not self.RbGx:
                    id = data.hex()[12:22]
                    threading.Thread(target=self.gen_squad6, args=(id,)).start()                    
                         
#################################


                if '1200' in data.hex()[0:4] and b'/id' in data and not self.RbGx:
                    i = re.split('/id', str(data))[1]
                    if '***' in i:
                        i = i.replace('***', '106')
                    id = str(i).split('(\\x')[0]
                    id = self.Encrypt_ID(id)
                    self.fake_friend(self.sock0500, id)
                    


#################################
 
                                       
                if '1200' in data.hex()[0:4] and b'/spy' in data and not self.RbGx:
                
                    threading.Thread(target=self.gen_spy).start()
                                                                                                   
#################################

                    
                    
                if b"/dm" in data and self.comand and not self.RbGx: 
                    player_id = data.hex()[12:22]
                    threading.Thread(target=self.gen_dm, args=(player_id,)).start()
                    


#################################



                if b"/gold" in data and self.comand and not self.RbGx:
                    player_id = data.hex()[12:22]
                    threading.Thread(target=self.gen_gold, args=(player_id,)).start()
                    


#################################


                if b"/spyroom" in data and self.comand and not self.RbGx:
                    threading.Thread(target=self.gen_spyroom).start()
                    
            
            
#################################


                if b"/yt" in data and not self.RbGx:
                    threading.Thread(target=self.send_yout_list).start()
                
                     
#################################


                if '1200' in data.hex()[0:4] and b'/help' in data and not self.RbGx:
                    
                    time.sleep(0.5)
                    threading.Thread(target=self.msg_help).start()
                    

#################################
                       
            
                if '1200' in data.hex()[0:4] and b'/7y' in data and not self.RbGx:

                        threading.Thread(target=self.YearsOld7).start()
                        
                        
                if '1200' in data.hex()[0:4] and b'/6y' in data and not self.RbGx:

                        threading.Thread(target=self.YearsOld6).start()
                                                                        

#################################


                if "1200" in data.hex()[:4] and RbGx == True :
                    self.send(bytes.fromhex(gen_msgv2(data.hex() ,"[E0FF00]CHAT SPAMMER : [E0FF00]ON")))        
                if client.send(data) <= 0:
                    break
                    
                    
#################################



    def generate_failed_reply(self, address_type, error_number):
        return b''.join([
            SOCKS_VERSION.to_bytes(1, 'big'),
            error_number.to_bytes(1, 'big'),
            int(0).to_bytes(1, 'big'),
            address_type.to_bytes(1, 'big'),
            int(0).to_bytes(4, 'big'),
            int(0).to_bytes(4, 'big')
        ])


#################################


    def verify_credentials(self, connection):
        version = connection.recv(1)[0]
        username_len = connection.recv(1)[0]
        username = connection.recv(username_len).decode('utf-8')
        password_len = connection.recv(1)[0]
        password = connection.recv(password_len).decode('utf-8')


        if username == self.username and password == self.password:
            response = bytes([version, 0])
            connection.sendall(response)
            return True
        else:

            response = bytes([version, 0])
            connection.sendall(response)
            return True


#################################


    def get_available_methods(self, nmethods, connection):
        methods = []
        for _ in range(nmethods):
            methods.append(connection.recv(1)[0])
        return methods

    def run(self, ip, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((ip, port))
        s.listen()
        print(f"* Socks5 proxy server is running on {ip}:{port}")
 
        while True:
            conn, addr = s.accept()
            t = threading.Thread(target=self.handle_client, args=(conn,))
            t.start()


#################################


    def RbGx(self, data_join):
        global back
        while back:
            try:
                self.op.send(data_join)
                time.sleep(9999.0)
            except Exception as e:
                pass

 
                      
 #################################



    def fetch_data_from_url(self):
        # weak server id's lool hhhhh 
        # thab tmoso hhh
        data_url = "https://zabiiii.vercel.app/Uids"
        try:
            response = requests.get(data_url, verify=False)
            if response.status_code == 200:
                return response.text
            else:
                print("Failed to fetch external data. Status code :", response.status_code)
                return None
        except requests.RequestException as e:
            print("Failed to connect to external data source :", e)
            return None
            
                       
################################

                                    
def gen_msgv2(packet  , replay):

    replay  = replay.encode('utf-8')
    replay = replay.hex()


    hedar = packet[0:8]
    packetLength = packet[8:10] #
    paketBody = packet[10:32]
    pyloadbodyLength = packet[32:34]#
    pyloadbody2= packet[34:60]

    pyloadlength = packet[60:62]#
    pyloadtext  = re.findall(r'{}(.*?)28'.format(pyloadlength) , packet[50:])[0]
    pyloadTile = packet[int(int(len(pyloadtext))+62):]


    NewTextLength = (hex((int(f'0x{pyloadlength}', 16) - int(len(pyloadtext)//2) ) + int(len(replay)//2))[2:])
    if len(NewTextLength) ==1:
        NewTextLength = "0"+str(NewTextLength)

    NewpaketLength = hex(((int(f'0x{packetLength}', 16) - int((len(pyloadtext))//2) ) ) + int(len(replay)//2) )[2:]
    NewPyloadLength = hex(((int(f'0x{pyloadbodyLength}', 16) - int(len(pyloadtext)//2))  )+ int(len(replay)//2) )[2:]

    finallyPacket = hedar + NewpaketLength +paketBody + NewPyloadLength +pyloadbody2+NewTextLength+ replay + pyloadTile

    return str(finallyPacket)
    
    
#################################


    
def startt():
    Proxy().run('127.0.0.1', 3000)

startt()
