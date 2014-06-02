#! /usr/bin/env python
#
# This file is part of khmer, http://github.com/ged-lab/khmer/, and is
# Copyright (C) Michigan State University, 2009-2014. It is licensed under
# the three-clause BSD license; see doc/LICENSE.txt. Contact: ctb@msu.edu
#

import khmer
import subprocess

def main():
    # nbm_fa = object from normalize_by_median
    input_file = "ultralight.fastq"
<<<<<<< HEAD
    nbm_cmd = ['python', 'normalize-by-median.py', '-k', input_file]

    nbm_fa = subprocess.call(nbm_cmd, shell=False)
    # nbm_ht = object from load_graph(nbm_fa)
'''
    nbm_load_graph_cmd = ['python', 'load_graph.py', nbm_fa]
    nbm_ht = subprocess.Popen(nbm_load_graph_cmd, stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE)
=======
    nbm_cmd = ['python', 'normalize_by_median.py', '-k', input_file]

    nbm_fa = subprocess.Popen(nbm_cmd, stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE)

    # nbm_ht = object from load_graph(nbm_fa)
    nbm_load_graph_cmd = ['python', 'load_graph.py', nbm_fa]
    nbm_ht = subprocess.Popen(nbm_load_graph_cmd, stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE)


>>>>>>> d07a5d58685d140a0cece1117a5bc24cd30c800c
    for fprate in range(10,51,5):
        for rec in range(100000,500000000,1000000):
            fp = 0.01 * fprate
            
            # making object from optimize_diginorm.py (opt) to 
            # compare to nbm using count_overlap
            # opt_fa = object from normalize_by_median(foo.fa)
            opt_cmd = ['python', 'implement_norm.py', '-k', 
                    '--false-positive', str(fp), input_file]
            opt_fa = subprocess.Popen(opt_cmd, stdout=subprocess.PIPE, 
                    stderr=subprocess.PIPE)

            # opt_ht = object from load_graph(opt_fa)
            opt_load_graph_cmd = ['python', 'load_graph.py', '-k', opt_fa]
            opt_ht = subprocess.Popen(nbm_load_graph_cmd, 
                    stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            # nbm_count = count_overlap(opt_ht, nbm_fa)
            opt_cmd = ['python', 'count-overlap.py', '-k']
            opt_fa = subprocess.Popen(opt_cmd, stdout=subprocess.PIPE, 
                    stderr=subprocess.PIPE)

            # opt_count = count_overlap(nbm_ht, opt_fa)

        try:
            p = subprocess.Popen(cmd, stdout=subprocess.PIPE, 
                    stderr=subprocess.PIPE)
        except OSError:
            return traceback.format_exc()
        (out, err) = p.communicate()
        print out, err 
<<<<<<< HEAD
'''
=======
>>>>>>> d07a5d58685d140a0cece1117a5bc24cd30c800c

if __name__ == '__main__':
    main()
