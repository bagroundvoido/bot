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
    "dc92e660", "b597a361", "929be061", "e8b6ce64", "efb7ce64"
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
