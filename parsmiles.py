# parse smiles in CID-SMILES download from PubChem
import pysmiles as ps
import subprocess

def countatoms(smiles, element):
    # accept a smiles string and an element symbol and count nodes that match the element
    atomcount = 0
    mol = ps.read_smiles(smiles)
    for tupnode in mol.nodes(data='element'):   # each node is a tuple [(0,'C'), (1,'C'), etc.]
        #print (tupnode)
        if (tupnode[1] == element):
            atomcount += 1
    return atomcount

mycmd = "head Download\\CID-SMILES"
(out, err) = subprocess.Popen(mycmd, stdout=subprocess.PIPE, shell=True).communicate()

myrows = str(out.decode("utf-8")).split("\n")
for myrow in myrows:
    print(myrow)
    myfields = myrow.split("\t")
    docno = myfields[0]
    smiles = myfields[1]
    C = countatoms(smiles, 'C')
    N = countatoms(smiles, 'N')
    O = countatoms(smiles, 'O')
    if ((C > 4) & (N + O > 1)):
        print ("DOCNO", "C", "N", "O", "SMILES", sep="\t")
        print (docno, C, N, O, smiles, sep="\t")
    
# docno = 7915
# smiles = "CC(C)OC(=O)C"
# print (smiles)
