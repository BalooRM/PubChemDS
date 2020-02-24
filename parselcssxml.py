from xml.etree import ElementTree as ET

#root = ET.parse('./Download/CID-LCSS.xml').getroot()
root = ET.parse('./Download/short2.xml').getroot()
print (root.tag)
for myrec in root:
    #print (myrec.tag, myrec.text, sep="\t")
#for myrec in root.iter('Record'):
    for child in myrec:
        found = 0
        #print (child.tag)
        if (child.tag == 'RecordNumber'):
            if (int(child.text) == 5816):
                found = 1
                print (child.tag, child.text, sep="\t")
        if (found == 1):
            ET.dump(myrec)
