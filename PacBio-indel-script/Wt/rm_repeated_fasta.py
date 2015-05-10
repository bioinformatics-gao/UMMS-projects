from Bio import SeqIO
from Bio.SeqUtils.CheckSum import seguid

def remove_dup_seqs(records):
    """"SeqRecord iterator to removing duplicate sequences."""
    checksums = set()
    for record in records:
        checksum = seguid(record.seq)
        if checksum in checksums:
            print "Ignoring %s" % record.id
            continue
        checksums.add(checksum)
        yield record

#records = remove_dup_seqs(SeqIO.parse("Sg2.fasta", "fasta"))
#count = SeqIO.write(records, "Sg2_no_repeated_seq.fasta", "fasta")
#records = remove_dup_seqs(SeqIO.parse("Sg5.fasta", "fasta"))
#count = SeqIO.write(records, "Sg5_no_repeated_seq.fasta", "fasta")
records = remove_dup_seqs(SeqIO.parse("Wt.fasta", "fasta"))
count = SeqIO.write(records, "Wt_no_repeat.fasta", "fasta")
print "Saved %i records" % count

