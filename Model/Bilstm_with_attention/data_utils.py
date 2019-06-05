import os
import wget
import tarfile
import re
import collections
import pandas as pd
import pickle
import numpy as np
from itertools import chain
from konlpy.tag import Twitter

def tokenize(doc):  ## 리스트형테의 데이터 안에서 리뷰부분을 토크나이징해서 다시 리스트로 저장

    return ['/'.join(t) for t in pos_tagger.pos(doc, norm=True, stem=True)]

def random_row_sampling(df,n): ## 데이터 내에서 몇개 뽑아서 쓸건지. random_sampling해줌
    return df.ix[np.random.random_integers(0,len(df),n)]


def build_word_dict():
        total_balanced_data = pd.read_csv("total_balance_final.csv")
        total_balanced_data = total_balanced_data.reset_index().drop(['index','Unnamed: 0'],axis=1)


        pos_tagger = Twitter()

        total_tokens = [tokenize(row) for row in total_balanced_data['tweet']]
        total_labels = [int(row[9:]) for row in total_balanced_data['labels_text']]

        unlist_tokens = list(chain.from_iterable(total_tokens))



        words = list() ## word index를 주기 위해서 dictionary를 만든다 -> lookup table사용
        for word in unlist_tokens:
            words.append(word)

        word_counter = collections.Counter(words).most_common()
        word_dict = dict()
        word_dict["<pad>"] = 0
        word_dict["<unk>"] = 1
        word_dict["<eos>"] = 2
        for word,_ in word_counter:
            word_dict[word] = len(word_dict)

        return word_dict


def build_word_dataset(step, word_dict, document_max_len):

    total_balanced_data = pd.read_csv("total_balance_final.csv")
    sampled_data = random_row_sampling(total_balanced_data,3000000)
    train_data = sampled_data.iloc[:2500000,:]
    test_data = sampled_data.iloc[2500000:,:]

    train_data = train_data.reset_index().drop(['index','Unnamed: 0'],axis=1)
    test_data = test_data.reset_index().drop(['index','Unnamed: 0'],axis=1)

    train_tokens = [tokenize(row) for row in train_data['tweet']]
    train_labels = [int(row[9:]) for row in train_data['labels_text']]

    test_tokens = [tokenize(row) for row in test_data['tweet']]
    test_labels = [int(row[9:]) for row in test_data['labels_text']]

    if step == "train":
        df = train_tokens
        df_y = train_labels
    else:
        df = test_tokens
        df_y = test_labels

    # Shuffle dataframe

    x = list(map(lambda d: list(map(lambda w: word_dict.get(w, word_dict["<unk>"]), d)), df))
    x = list(map(lambda d: d[:50], x))
    x = list(map(lambda d: d + (50- len(d)) * [word_dict["<pad>"]], x))

    y = df_y

    return x, y




def batch_iter(inputs, outputs, batch_size, num_epochs):
    inputs = np.array(inputs)
    outputs = np.array(outputs)

    num_batches_per_epoch = (len(inputs) - 1) // batch_size + 1
    for epoch in range(num_epochs):
        for batch_num in range(num_batches_per_epoch):
            start_index = batch_num * batch_size
            end_index = min((batch_num + 1) * batch_size, len(inputs))
            yield inputs[start_index:end_index], outputs[start_index:end_index]
