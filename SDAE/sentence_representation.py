import numpy

from desent import embedding

def main(job_id, params):
    print 'Anything printed here will end up in the output directory for job #%d' % job_id
    print params
    embedding(model=params['model'][0],
            dictionary = params['dictionary'][0],
            save=params['save'][0],
            sentences=params['sentences'][0]
            )

if __name__ == '__main__':
    main(0, {'model': ['/home/ep490/Desktop/SDAE models/model-en.npz'],
             'dictionary': ['/home/ep490/Desktop/sentences/en.txt.dict.pkl'],
             'save': ['/home/ep490/Desktop/SDAE models/en.txt'],
             'sentences': ['/home/ep490/Dropbox/Decoding Event Information from Distributed Representation of Sentences/sentiment/en.txt']})

# model: path/name.npz for your trained model
# dictionary: path/name.txt.dict.pkl for your dictionary
# save: path/name.txt for your output file with embeddings
# sentences: path/name.txt for your input file with one-per-line sentences
