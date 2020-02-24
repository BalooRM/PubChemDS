# parse smiles in CID-SMILES download from PubChem
import pysmiles as ps
import subprocess
import sys

def countatoms(smiles, element):
    # accept a smiles string and an element symbol and count nodes that match the element
    atomcount = 0
    mol = ps.read_smiles(smiles)
    for tupnode in mol.nodes(data='element'):   # each node is a tuple [(0,'C'), (1,'C'), etc.]
        #print (tupnode)
        if (tupnode[1] == element):
            atomcount += 1
    return atomcount

# read CIDs PubChem CID-PMID
pmid_cid = []
mycmd = 'head -1000 .\\Download\\CID-PMID'
(out, err) = subprocess.Popen(mycmd, stdout=subprocess.PIPE, shell=True).communicate()
myrows = str(out.decode("utf-8")).split("\n")
for myrow in myrows:
    #print(myrow)
    myfields = myrow.split("\t")
    if (len(myfields) > 1):
        cid = myfields[0]  # first column contains CID
        if not cid in pmid_cid:
            pmid_cid.append(int(cid))

#print (pmid_cid)

# read CIDs with HSDB content from .\HSDB\HSDB_CIDs.txt - CID in column [1]
hsdb_cid = []
mycmd = 'grep "^CID" .\\HSDB\\HSDB_CIDs.txt'
(out, err) = subprocess.Popen(mycmd, stdout=subprocess.PIPE, shell=True).communicate()
myrows = str(out.decode("utf-8")).split("\n")
for myrow in myrows:
    #print(myrow)
    myfields = myrow.split("\t")
    if (len(myfields) > 1):
        cid = myfields[1]
        hsdb_cid.append(int(cid))


# grab content from PubChem CID-SMILES file
# omit representations of molecular hydrogen as [HH] - 48,812 rows
print ("CID", "HSDB", "C", "N", "O", "SMILES", sep="\t")
for i in range(len(pmid_cid)):
    #mycmd = "grep -v HH Download\\CID-SMILES"
    mycmd = 'grep -P "^' + str(pmid_cid[i]) + '\\t" -m 1 Download\\CID-SMILES | grep -v HH'
    #print (mycmd)
    (out, err) = subprocess.Popen(mycmd, stdout=subprocess.PIPE, shell=True).communicate()
    myrows = str(out.decode("utf-8")).split("\n")
    for myrow in myrows:
        #print(myrow)
        hsdb = "no"
        myfields = myrow.split("\t")
        if (len(myfields) > 1):
            cid = int(myfields[0])
            print ("cid = ", str(cid))
            if cid in hsdb_cid:
                hsdb = "hsdb"
            smiles = myfields[1]   # we may need to test for valid SMILES before trying to compute
            C = countatoms(smiles, 'C')
            N = countatoms(smiles, 'N')
            O = countatoms(smiles, 'O')
            if ((C > 4) & (N + O > 1)):
                #print ("CID", "HSDB", "C", "N", "O", "SMILES", sep="\t")
                print (str(cid), hsdb, C, N, O, smiles, sep="\t")
                # print out number of matching PMIDs
                mycmd = 'grep -c -P "^' + str(pmid_cid[i]) + '\\t" Download\\CID-PMID'
                (out, err) = subprocess.Popen(mycmd, stdout=subprocess.PIPE, shell=True).communicate()
                #print (out)
                myrows = str(out.decode("utf-8")).split("\n")
                for myrow in myrows:
                    print(myrow)
                # print out first n (e.g., 20) matching PMIDs
                mycmd = 'grep -P "^' + str(pmid_cid[i]) + '\\t" -m 20 Download\\CID-PMID'
                (out, err) = subprocess.Popen(mycmd, stdout=subprocess.PIPE, shell=True).communicate()
                #print (out)
                myrows = str(out.decode("utf-8")).split("\n")
                for myrow in myrows:
                    print(myrow)

    
# docno = 7915
# smiles = "CC(C)OC(=O)C"
# print (smiles)

# cid = 31239
# #hsdb_cid.append(cid)
# smiles = "CCCCCCCCCCCCCCCC[N+]1=CC=CC=C1.[Cl-]"
# print (smiles)
# C = countatoms(smiles, 'C')
# N = countatoms(smiles, 'N')
# O = countatoms(smiles, 'O')
# hsdb = 0
# if cid in hsdb_cid:
#     print (str(cid), " is in hsdb")
#     hsdb = 1
# else:
#     print (str(cid), " is not in hsdb")
# if ((C > 4) & ((N + O) > 1)):
#     #print ("CID", "HSDB", "C", "N", "O", "SMILES", sep="\t")
#     print (cid, hsdb, C, N, O, smiles, sep="\t")
# sys.exit()
