text = "X-DSPAM-Confidence:    0.8475"
c=text.find(":")
ext=text[c+1:]
ext1=ext.strip()
print(float(ext1))