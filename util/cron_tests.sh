#!/bin/sh
rm -fR $HOME/tested_spike_prev
mv $HOME/tested_spike $HOME/tested_spike_prev
mkdir $HOME/tested_spike
cd $HOME/tested_spike
/usr/local/bin/hg clone ssh://hg@bitbucket.org/delsuc/spike
python -m spike.Tests -m madelsuc@unistra.fr -m lionel.chiron@gmail.com -D /Volumes/biak_1ToHD/rdc/DATA_test 