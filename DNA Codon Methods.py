from typing import List, TextIO


def startCodons(DNAseq):
    DNAseq = DNAseq.upper()
    startCodon = 'ATG'
    start_indices = [i for i in range(len(DNAseq)) if DNAseq[i:i + 3] == startCodon]
    num_starts = len(start_indices)
    return start_indices


def stopCodons(DNAseq_in, Sloc):
    DNAseq = DNAseq_in.upper()
    stopCodons = ['TGA', 'TAG', 'TAA']
    stop_indices = [i for i in range(Sloc, len(DNAseq), 3) if DNAseq[i:i + 3] in stopCodons]
    num_stops = len(stop_indices)
    return stop_indices


def compSeq(DNAseq_in):
    DNAseq = DNAseq_in.upper()
    complement = ""
    for i in range(len(DNAseq) - 1, -1, -1):
        if DNAseq[i] == 'A':
            nuc = 'T'
        elif DNAseq[i] == 'T':
            nuc = 'A'
        elif DNAseq[i] == 'C':
            nuc = 'G'
        else:
            nuc = 'C'
        complement += nuc
    return complement


def findORF(DNAseq: str, min_length: int):
    # get the index of start codons
    lstarts = startCodons(DNAseq)
    # from each start codon, find all the stop codons
    found = 0
    for i in range(len(lstarts)):
        lstops = stopCodons(DNAseq, lstarts[i])
        # find the length of the string with those stop codons
        # and compare it to the required length
        for j in range(len(lstops)):
            lORF = ((lstops[j] + 2) - lstarts[i])
            if lORF > min_length:
                print("In the 5'-3' strand, an ORF starts at {} and ends at {}".format(lstarts[i], (lstops[j] + 2)))
                found = 1
            if found == 1:
                break
    if found == 0:
        print("No ORFs were found in the 5'-3' strand")


# repeat the process with the 3'-5' strand
# strand = compSeq(DNAseq)
# startCodons(strand)
# found = 0
#     for i in range(len(startList)):
#             stopCodons(strand,startList[i])
#         for j in range(len(stop_indices)):
#             lORF = ((stop_indices[j] + 2) - startList[i])
#         if lORF > length:
#             print "In the 3'-5' strand, an ORF starts at", startList[i], "and ends at", (stop_indices[j] + 2)
#             found = 1
#         if found == 1:
#             break
# if found == 0:
#     print "No ORFs were found in the 3'-5' strand"


if __name__ == "__main__":
    # to read from a file
    '''
    DNAfile = open('C:\_dev\PycharmProjects\pythonPractice\DNA input\DNA input 1', 'r')
    DNAseq = (DNAfile.readline()).replace(' ', '')
    DNAfile.close()
    '''
    # raw input
    DNAseq = 'CATATTTCATTACTTAAAGTGAATCAATCTTTACCAAACTTCCATGAAGACACTATTAGAATGTTAACTTTAAGAATGTTTTTAAAGTTTGGTGAAAAGTTAAGAAACAAAAAAGTTATGATACGAAATGTAAAAATAACCCAAAAATGATTACCTAAAATAATAGGACCAGTTCAGAAAATTTTAAAATAATTATCATTTATTATTATTAAATAACAGATTTTGATGTTATTTAGTTGTCGGATAGCTTAACTTAAATTAGTGAACTAATGCGTACACATTTTTTTTTGCAGAAACGCTAATGCGAGAATATTACGGCACTCGCTTCAGGGTTTTGAGCTCCCTTTGCACTGAGAGACGAAATAGTGGTGAGTACCTTCGTCTATGGGTATAAAAGCGCGTCACAACGCTGGATCGCTTACACTGTGTTCTAAGCCGTTGCCTAGAACACTTCACACGATCAATTAGCTCGTGTATTTTTGGGTGCACTACTTCAAGCGCTTAATTGAAGGAATTCCAACGATGGGCCGTAGTGCACACTCCACACAACAACAGCGTTTAGATATCAAACGTTTGTGAATACATA'

    # perform functions

    # start_indices = startCodons(DNAseq)
    # print(start_indices)
    # stop_indices = [stopCodons(DNAseq, start_i) for start_i in start_indices]
    # print(stop_indices)
    print('ORF List:')
    min_ORF_len = 50
    findORF(DNAseq, min_ORF_len)
    print('\nComplement Sequence:')
    print(compSeq(DNAseq))
