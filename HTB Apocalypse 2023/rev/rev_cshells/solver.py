t= [0x2C ,0x4A ,0xB7 ,0x99 ,0xA3 ,0xE5 ,0x70 ,0x78 ,0x93 ,0x6E ,0x97 ,0xD9 ,0x47 ,0x6D ,0x38 ,0xBD ,0xFF ,0xBB ,0x85 ,0x99 ,0x6F ,0xE1 ,0x4A ,0xAB ,0x74 ,0xC3 ,0x7B ,0xA8 ,0xB2 ,0x9F ,0xD7 ,0xEC ,0xEB ,0xCD ,0x63 ,0xB2 ,0x39 ,0x23 ,0xE1 ,0x84 ,0x92 ,0x96 ,0x09 ,0xC6 ,0x99 ,0xF2 ,0x58 ,0xFA ,0xCB ,0x6F ,0x6F ,0x5E ,0x1F ,0xBE ,0x2B ,0x13 ,0x8E ,0xA5 ,0xA9 ,0x99 ,0x93 ,0xAB ,0x8F ,0x70 ,0x1C ,0xC0 ,0xC4 ,0x3E ,0xA6 ,0xFE ,0x93 ,0x35 ,0x90 ,0xC3 ,0xC9 ,0x10 ,0xE9 ,0x00 ,0x00 ,0x00 ,0x00 ,0x00 ,0x00 ,0x00 ,0x00 ,0x00 ,0x00 ,0x00 ,0x00 ,0x00 ,0x00 ,0x00 ,0x00 ,0x00 ,0x00 ,0x00]

m2=[0x64 ,0x1E ,0xF5 ,0xE2 ,0xC0 ,0x97 ,0x44 ,0x1B ,0xF8 ,0x5F ,0xF9 ,0xBE ,0x18 ,0x5D ,0x48 ,0x8E ,0x91 ,0xE4 ,0xF6 ,0xF1 ,0x5C ,0x8D ,0x26 ,0x9E ,0x2B ,0xA1 ,0x02 ,0xF7 ,0xC6 ,0xF7 ,0xE4 ,0xB3 ,0x98 ,0xFE ,0x57 ,0xED ,0x4A ,0x4B ,0xD1 ,0xF6 ,0xA1 ,0xEB ,0x09 ,0xC6 ,0x99 ,0xF2 ,0x58 ,0xFA ,0xCB ,0x6F ,0x6F ,0x5E ,0x1F ,0xBE ,0x2B ,0x13 ,0x8E ,0xA5 ,0xA9 ,0x99 ,0x93 ,0xAB ,0x8F ,0x70 ,0x1C ,0xC0 ,0xC4 ,0x3E ,0xA6 ,0xFE ,0x93 ,0x35 ,0x90 ,0xC3 ,0xC9 ,0x10]

x=""
for i in range(len(m2)):
    x=x+chr(m2[i]^t[i])

print(x)
