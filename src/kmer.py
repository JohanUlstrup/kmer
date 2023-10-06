"""Computing kmers of a string."""


def kmer(x: str, k: int) -> list[str]:
    """
    Computer all k-mers of x.

    >>> kmer('agtagtcg', 3)
    ['agt', 'gta', 'tag', 'agt', 'gtc', 'tcg']

    FIXME: do you want more tests here?
    """
    codons=[]
    for i in range(0,len(x)-(k-1)):
        
        codons.append(x[i:i+k])

    return codons
    ...

    
#print(kmer('agtagtcg', 3))

def unique_kmers(x: str, k: int) -> list[str]:
    """
    Computer all unique k-mers of x.

    FIXME: do you want more tests here?
    """
    unique_codons=[]
    codons = kmer(x,k)
    for i in codons:
        #print(i)

        if i not in unique_codons: 
            unique_codons.append(i)

   

    return unique_codons
    ...
#print (unique_kmers('agtagtcg', 3))



def count_kmers(x: str, k: int) -> dict[str, int]:
    """
    Computer all k-mers of x and count how often they appear.

    FIXME: do you want more tests here?
    """
    ...
    count_condons = {}
    codons = kmer(x,k)
    for i in codons:
        if i not in count_condons: 
            count_condons[i]=1
        else:
            count_condons[i]+=1
    
    return count_condons

print (count_kmers('agtagtcg', 3))

