import pubchempy as pcp
import sys
import re

usage = ("Usage: \n"
         " > python lkupcas.py \"search term\"")
         
myargs = sys.argv
if len(myargs) == 1:
    sys.exit (usage)

mycid = myargs[1]  # ignore argv 0 = script name
print (mycid)
    
if (1 == 1):
    compound = pcp.Compound.from_cid(mycid)
    myfound = 0
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
            myfound = 1
            print ('CASRN\t', mysyn)
        m = re.search('^UNII', mysyn)
        if m != None:
            print ('UNII\t', mysyn)
        m = re.search('^HSDB', mysyn)
        if m != None:
            print ('HSDB\t', mysyn)
    # if the CASRN was not found with the CAS prefix, use the search value
    if myfound == 0:
        print ('CID\t', mycid)
    print ('Synonyms:\n', compound.synonyms)
