import caesar


#===== examples =====#

ciphertext1 = 'JVTIVK JRCRU IVTZGV'
#             'secret salad recipe'
ciphertext2 = 'LQKP OG CV GKIJV DA VJG BQQ'
#             'join me at eight by the zoo'
ciphertext3 = 'FRZDUGV GLH PDQB WLPHV EHIRUH WKHLU GHDWKV; WKH YDOLDQW QHYHU WDVWH RI GHDWK EXW RQFH.'
#             'cowards die many times before their deaths; the valiant never taste of death but once.'
ciphertext4 = 'Z. VKDNHVSHDUH, MXOLXV FDHVDU'
#             'w. shakespeare, julius caesar'
ciphertext5 = 'BUUBDL BU EBXO'
#              'attack at dawn'
ciphertext6 = 'KYV MVIP NFIU “JVTIVTP” ZJ IVGLXEREK ZE R WIVV REU FGVE JFTZVKP; REU NV RIV RJ R GVFGCV ZEYVIVEKCP REU YZJKFIZTRCCP FGGFJVU KF JVTIVK JFTZVKZVJ, KF JVTIVK FRKYJ REU KF JVTIVK GIFTVVUZEXJ. NV UVTZUVU CFEX RXF KYRK KYV UREXVIJ FW VOTVJJZMV REU LENRIIREKVU TFETVRCDVEK FW GVIKZEVEK WRTKJ WRI FLKNVZXYVU KYV UREXVIJ NYZTY RIV TZKVU KF ALJKZWP ZK. AFYE W BVEEVUP'
#             'the very word “secrecy” is repugnant in a free and open society; and we are as a people inherently and historically opposed to secret societies, to secret oaths and to secret proceedings. we decided long ago that the dangers of excessive and unwarranted concealment of pertinent facts far outweighed the dangers which are cited to justify it. john f kennedy'


print('\n', caesar.salad(ciphertext1))
print('\n', caesar.salad(ciphertext3))
print('\n', caesar.salad(ciphertext4))			# salad() auto picks decipher method based on strlen
print('\n', caesar.guessSalad(ciphertext4, 1))	# loopupSalad() does not do well with names and pronouns
print('\n', caesar.lookupSalad(ciphertext5))
print('\n', caesar.guessSalad(ciphertext6, 1))