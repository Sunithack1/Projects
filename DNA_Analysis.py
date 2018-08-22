'''DNA analysis to catch a spy'''
sample = ['GTA','GGG','CAC']
def read_dna(dna_file):
  dna_data = ""
  with open(dna_file, "r") as f:
    for line in f:
      dna_data += line
  return dna_data
def dna_codons(dna): # create list of dna codons
  codons = [] #empty list to add codons
  for i in range(0, len(dna), 3): #iterating in increments of 3 through suspect's dna
    if (i + 3) < len(dna):
      codons.append(dna[i: (i+3)])
  return codons
def match_dna(dna):
  matches = 0
  for codon in dna:
    if codon in sample:
      matches += 1
  return matches 
def is_criminal(dna_sample):
  dna_data = read_dna(dna_sample)  
  codons = dna_codons(dna_data)
  num_matches = match_dna(codons)
  if num_matches >= 3:
    print "Number of codon matches is %s, Continue investigation" % num_matches
  else:
    print "Numbr of codon matches is %s, Free the suspect" % num_matches
is_criminal('suspect1.txt')
is_criminal('suspect2.txt')
is_criminal('suspect3.txt')