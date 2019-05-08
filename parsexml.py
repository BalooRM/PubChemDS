from xml.etree import ElementTree as ET
import pubchempy as pcp
import re
import time

# parse XML of HSDB database export to extract key information
# > perl ~/Github/MyTools/srchor.pl "DOC\>" DOCNO NameOfSubstance /
#   CASRegistryNumber "unii\>" < hsdb.xml.20190428 > hsdb.txt
# 
# <DOC>
#   <DOCNO>12</DOCNO>
#   <NameOfSubstance>STRONTIUM SULFIDE</NameOfSubstance>
#   <CASRegistryNumber>1314-96-1</CASRegistryNumber>
#   <unii>06I13IA27T</unii>
# </DOC>

print ('Localtime =', time.asctime( time.localtime(time.time()) ))
root = ET.parse('./HSDB/hsdb.txt').getroot()

for mydoc in root.iter('DOC'):
    print ('Localtime =', time.asctime( time.localtime(time.time()) ))
    print ('--------DOC--------')
    lookupval = ''
    for child in mydoc:
        print (child.tag, child.text)
        if (child.tag == 'CASRegistryNumber'):
            lookupval = child.text
    if (lookupval != ''):
        for compound in pcp.get_compounds(lookupval, 'name'):
            print ('CID\t', compound.cid)
            print ('Formula\t', compound.molecular_formula)
            print ('Mol Wt\t', compound.molecular_weight)
            print ('Charge\t', compound.charge)
            print ('XLogP\t', compound.xlogp)
            print ('IUPAC Name\t', compound.iupac_name)
            print ('InChI\t', compound.inchi)
            print ('InChI Key\t', compound.inchikey)
            print ('Fingerprint\t', compound.fingerprint)
            print ('Isomeric SMILES\t', compound.isomeric_smiles)
            print ('Canonical SMILES\t', compound.canonical_smiles)
            for mysyn in compound.synonyms:
                m = re.search('^CAS', mysyn)
                if m != None:
                    print ('CASRN\t', mysyn)
                    m = re.search('^UNII', mysyn)
                if m != None:
                    print ('UNII\t', mysyn)
# print completion time
print ('Localtime =', time.asctime( time.localtime(time.time()) ))
