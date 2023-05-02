# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context

# from Bio import SeqIO, Entrez
# Entrez.email = "vatsenko@gmail.com"
# handle = Entrez.efetch(db="protein", id="YP_009724390", rettype="gb", retmode="text")
# for s in SeqIO.parse(handle, 'gb'):
#     print(s)

import nglview as nv

view = nv.show_structure_file('2rh1.pdb')
view