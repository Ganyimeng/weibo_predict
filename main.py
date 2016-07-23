# coding = utf-8
import pandas as pd
import numpy as np
columns = ['uid','mid','time','forward_count','comment_count','like_count','content']
train = pd.read_csv('..\weibo_train_data.txt',sep='\t',names=columns)

uids = list(set(train.uid.tolist()))

grouped = train.groupby('uid')
print 'the end'