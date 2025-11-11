## The goal of this code is to use DNA to store bytes. 
## One DNA nucleotide can code for two bytes. 
## While the computer traditionnal byte-computer is using base-2 system, 
## that would mean the DNA computer operates in base-4. 

DNA_conversion = {
  "00" : 'A', # Adénine
  "01" : 'T', # Thymine
  "10" : 'C', # Cytosine
  "11" : 'G' # Guanine
}

def BytesToDNA(number):
  bin_string = bin(number)[2:]  # remove '0b' that indicates it's a binary number
  array = []
  pair_length = 2

  if len(bin_string) % pair_length != 0:
    raise ValueError("error, bytes chain length must be even. otherwise orphan byte in conversion will fail to be translated into DNA nucleotid")
  
  for i in range(0, len(bin_string), 2):
    bytes_pair = bin_string[i:i+2]
    if bytes_pair in DNA_conversion:
      nucleotide = DNA_conversion[bytes_pair]
      array.append(nucleotide)
  return ''.join(array)

number = 0b1000110101010001  # binary number
dna = BytesToDNA(number)
print("DNA:", dna)
