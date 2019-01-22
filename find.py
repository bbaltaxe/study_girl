import argparse
import pandas as pd

def getargs():
 
    #commandline handling
    parser = argparse.ArgumentParser(description='Returns all lines of a file which contain a specified word')
    parser.add_argument('-f', dest='filename', type=str , required=True,
            help='path to file to search')
    parser.add_argument('-w', dest='word', type=str, required=True,
            help='What word to find')

    args = parser.parse_args()

    return args

if __name__ == "__main__": 
    args = getargs()
    df = pd.read_csv(args.filename,header=None,names=('time','comment'))
    ndf = pd.DataFrame(columns=('time','comment'))
   
    args.word = ' ' + args.word.lower() + ' '


    for i,c in enumerate(df['comment']):
        c = c.lower()
        if args.word in c:
            ndf = ndf.append(df.iloc[i],ignore_index=True)
        
    print(ndf)
    ndf.to_csv('out.csv',index=False,header=False)
