#! /usr/bin/env python
import khmer

filename = '1m.fa'
fp = open('stats.txt', 'w')

primes = [50000021,
          50000047,
          50000059,
          50000063,
          50000101,
          50000131,
          50000141,
          50000161,
          50000201,
          50000207,
          50000221,
          50000231,
          50000233,
          50000239,
          50000243,
          50000257,
          50000273,
          50000309,
          50000311,
          50000329,
          50000341,
          50000347]

primes = [100000007,
          100000037,
          100000039,
          100000049,
          100000073,
          100000081,
          100000123,
          100000127,
          100000193,
          100000213,
          100000217,
          100000223,
          100000231,
          100000237,
          100000259,
          100000267,
          100000279,
          100000357,
          100000379]

primes = [75000007,
          75000017,
          75000031,
          75000047,
          75000071,
          75000083,
          75000097,
          75000103,
          75000113,
          75000143,
          75000157,
          75000169,
          75000173,
          75000179,
          75000181,
          75000187,
          75000197,
          75000227,
          75000241]

###

this_filename = filename
readmask = None

for n, prime in enumerate(primes):
    ht_small = khmer.new_hashtable(15, prime)

    if not readmask:
        x = ht_small.consume_fasta_build_readmask(this_filename)
        total_reads, n_consumed, readmask = x
    else:
        total_reads, n_consumed = ht_small.consume_fasta(this_filename, 0, 0,
                                                         readmask)
        
    print '%d: ate %d k-mers of %d reads' % (n, n_consumed, total_reads)

    print 'filtering...'
    minmax = ht_small.fasta_file_to_minmax(this_filename, total_reads)
    readmask = ht_small.filter_fasta_file_max(this_filename, minmax,
                                              5, readmask)

    n_seq_kept = readmask.n_kept()

    print '%d: kept %d of %d (%.1f%%)' % (n, n_seq_kept, total_reads, n_seq_kept/float(total_reads)*100)

    fp.write('%d %d %d\n' % (n, n_seq_kept, ht_small.n_occupied()))
    fp.flush()

###
