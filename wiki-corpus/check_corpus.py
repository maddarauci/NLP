'''
the artical i got this from can be found at [ https://www.kdnuggets.com/2017/11/building-wikipedia-text-corpus-nlp.html ]
given the enormouse size of the wiki dump files, its dificult to read the full files into memory
at one time.

this script then starts by reading 50 lines -- which equates to 50 full articals -- from the text file
and outputing them to the terminal, after which you can press a key to output another 50 or type 'stop'
to quit.
once you do that the will load the entire files into memory (this can be a problem).
this can be mitigated by varifying the text with batches of lines.
'''

import sys, time

def check_corpus(input_file):
  # read some lines from the corpus
  while(1):
    for lines in range(50):
      print(input_file.readline())
    user_input = input('>>> Type \'STOP'\ to quit or hit enter key for more <<<')
    if user_input == 'STOP':
      break

def load_corpus:
  # laods corpus from text file
  print('loading corpus...')
  time1 = time.time()
  corpus = input_file.read()
  time2 = time.time()
  total_time = time2-time1
  print('it took %0.3f seconds to load corpus' %total_time)
  return corpus

if __name__ == '__main__':
  if len(sys.argv) != 2:
    print('Usage: python check_corpus.py <corpus_file>')
    sys.exit(1)

  corpus_file = open(sys.argv[1], 'r')
  check_corpus(corpus_file)
  corpus = load_corpus(corpus_file)


# the corpus file must be specified at the cmd line to execute
# $ python check_corpus.py wiki_en.txt

#example out -->
#best loved patriotic songs harperresource external links mp and realaudio
#recordings available at the united states library of congress words sheet
#music midi file at the cyber hymnal america the beautiful park in colorado
#springs named for katharine lee bates words archival collection of america
#the beautiful lantern slides from the another free sheet music
#>>> Type 'STOP' to quit or hit Enter key for more <<<
