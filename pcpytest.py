import pubchempy as pcp
import re

for compound in pcp.get_compounds('benzophenone', 'name'):
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
    #print ('Synonyms:\n', compound.synonyms)
