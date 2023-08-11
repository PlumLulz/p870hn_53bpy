# ZyXEL_DDDD    
# Zyxel P-870HN-53b
import hashlib
import argparse
import math

def p870hn_53b(serial):

	pwd_length = 12

	junk = 'agnahaakeaksalmaltalvandanearmaskaspattbagbakbiebilbitblableblib'\
	'lyboabodbokbolbomborbrabrobrubudbuedaldamdegderdetdindisdraduedu'\
	'kdundypeggeieeikelgelvemueneengennertesseteettfeifemfilfinflofly'\
	'forfotfrafrifusfyrgengirglagregrogrygulhaihamhanhavheihelherhith'\
	'ivhoshovhuehukhunhushvaideildileinnionisejagjegjetjodjusjuvkaika'\
	'mkankarkleklikloknaknekokkorkrokrykulkunkurladlaglamlavletlimlin'\
	'livlomloslovluelunlurlutlydlynlyrlysmaimalmatmedmegmelmenmermilm'\
	'inmotmurmyemykmyrnamnednesnoknyenysoboobsoddodeoppordormoseospos'\
	'sostovnpaiparpekpenpepperpippopradrakramrarrasremrenrevrikrimrir'\
	'risrivromroprorrosrovrursagsaksalsausegseiselsensessilsinsivsjus'\
	'jyskiskoskysmisnesnusolsomsotspastistosumsussydsylsynsyvtaktalta'\
	'mtautidtietiltjatogtomtretuetunturukeullulvungurourtutevarvedveg'\
	'veivelvevvidvikvisvriyreyte'

	md5 = hashlib.md5()
	md5.update(serial.encode())

	p = ""
	summ = 0
	for b in md5.digest():
		d1 = hex(b)[2:].upper()
		if len(d1) == 1:
			d1 += d1
		p += d1
	summ = sum([ord(char) for char in p])
	i = summ % 265
	if summ & 1:
		s1 = hex(ord(junk[1 + i * 3 - 1]))[2:]
		s1 += hex(ord(junk[2 + i * 3 - 1]))[2:]
		s1 += hex(ord(junk[3 + i * 3 - 1]))[2:]
	else:
		s1 = hex(ord(junk[1 + i * 3 - 1]))[2:].upper()
		s1 += hex(ord(junk[2 + i * 3 - 1]))[2:].upper()
		s1 += hex(ord(junk[3 + i * 3 - 1]))[2:].upper()

	s2 = "%s%s%s%s%s%s%s" % (p[0], s1[0:2], p[1:3], s1[2:4], p[3:6], s1[4:6], p[6:])

	md52 = hashlib.md5()
	md52.update(s2.encode())
	hex_digest = ""
	for b in md52.digest():
		d2 = hex(b)[2:].upper()
		if len(d2) == 1:
			d2 += d2
		hex_digest += d2

	filler = "AD3EHKL6V5XY9PQRSTUGN2CJW4FM7ZL"
	
	hex_digest = hex_digest[14:26]

	bad_chars = '01'

	uo_count = 0
	badchar_positions = []
	for i in range(0, pwd_length):
		if hex_digest[i] in bad_chars:
			uo_count += 1
			badchar_positions.append(i)


	list_count = (31 ** uo_count)
	badchar_count = uo_count

	current_mod = 31
	for list_number in range(0, list_count):
		list_position = list_number
		key = hex_digest[0:pwd_length]
		for char_pos in reversed(range(0, badchar_count)):
			char_value = list_number % current_mod
			replacement = filler[char_value]
			key = "%s%s%s" % (key[:badchar_positions[char_pos]], replacement, key[badchar_positions[char_pos]+1:])
			list_number = math.floor(list_number / current_mod)
		print(key)


parser = argparse.ArgumentParser(description='Zyxel P870HN_53b Keygen')
parser.add_argument('serial', help='Serial Number')
args = parser.parse_args()

p870hn_53b(args.serial)