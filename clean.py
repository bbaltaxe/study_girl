import argparse
import pandas as pd

def getargs():
 
    #commandline handling
    parser = argparse.ArgumentParser(description='gets rid of duplicates in a txt file')
    parser.add_argument('-f', dest='filename', type=str , required=True,
            help='path to file to clean')

    args = parser.parse_args()

    return args

if __name__ == "__main__": 
    args = getargs()
    df = pd.read_csv(args.filename,sep='Z "',header=None,names=('time','comment'))
    #remove last quote because we used the first in delim
    df['comment'] = df['comment'].map(lambda x: str(x)[:-1])
    print(df)
    lt = '0'

    for i,t in enumerate(df['time']):
        if t < lt:
            df = df.drop(i)
            print('{} < {}'.format(t,lt))
           #            print('{} is less than {}'.format(t,lt))
        else: 
            lt = t
        
    print(df)
    df.to_csv('try.csv',index=False,header=False)
