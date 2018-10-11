import numpy as np
import sys
sys.path
sys.path.append('./midi')

import midi
from midi.utils import midiwrite

import sys
# print "This is the name of the script: ", sys.argv[0]
# print "Number of arguments: ", len(sys.argv)
# print "The arguments are: " , str(sys.argv)

if len(sys.argv)!=2:
    print 'song ID as arg'
else:
    print 'Song ID:',int(sys.argv[1])

    song_num = int(sys.argv[1])
    results_dir = 'Results'

    new_song = np.load('{}/input_song_{}.npz'.format(results_dir, song_num))
    new_song = new_song[new_song.files[0]]

    print(new_song.shape)
    midiwrite('{}/input_song_{}.mid'.format(results_dir, song_num), new_song.T, (32, 93), 0.25) 

    new_song = np.load('{}/output_song_{}.npz'.format(results_dir, song_num))
    new_song = new_song[new_song.files[0]]

    print(new_song.shape)
    midiwrite('{}/output_song_{}.mid'.format(results_dir, song_num), new_song.T, (32, 93), 0.25) 

    print '\n\nMiDi Generated...'
