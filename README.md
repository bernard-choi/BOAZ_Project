## BOAZ_Project
#### 감정기반 이모지추천 시스템(김지연 이명아 이혜원 최연식)

#####
![](https://user-images.githubusercontent.com/36406676/54875373-417c0b80-4e41-11e9-88ca-fcf5c6548176.png)

Presentation
---
- BOAZ 9th Conference : [너의 기분이모지?](https://www.youtube.com/watch?v=PElfNl7bH-w&t=235s)
- BOAZ Slideshare : [너의 기분이모지?_PPT](https://www.slideshare.net/BOAZbigdata/9-boaz-emoji)

Did List
---
- [18.08.10] 자연어처리 팀 결성. 주제선정회의

- [18.08.16] cs224n 스터디 구성. 아이디어 추가

- [18.08.23] 주제 아이디어 추가.

- [18.08.30] 아이디어 확정.(이모지 추천 시스템)

- [18.09.06] SemEval-2018 Multilingual Emoji Prediction toy data로 실습

- [18.09.13] SemEval-2018 Multilingual Emoji Prediction toy data로 실습

- [18.09.20] 데이터수집 시작 (API&Twitterscraper) 및 역할 분배

- [18.09.27] 데이터수집 및 전반적인 전처리 구상 & 감정분석 관련 논문정리

- [18.10.04] BILSTM with attention 공부

- [18.10.11] TextCNN & Fasttext 논문 리뷰

- [18.11.01] 전처리 진행중. Imbalanced date에 대한 처리 방법 논의

- [18.11.08] 워드임베딩 방법 논의. 

- [18.11.15] Soynlp, Konlpy 한국어 전처리 활용방안 공부. 데이터 전처리 진행

- [18.11.22] Fasttext로 모델링 완료. 

- [18.11.29] Deepmoji 싸이트 참고 ui 구상. (Pyqt활용예정)

- [18.12.06] Bilstm with attention 모델 구현 완료

- [18.12.20] Emojitracker 기반 추천할 이모지들 최종 결정. 전처리 다시 새로함.

- [18.12.27] Pyqt시연. 컨퍼런스 리허설 피드백 수렴

- [19.01.13] Fasttext와 Bilstm with attention모델 비교 정리.

To Do List
---
[19.01.13]

- 데이터 전처리 추가 예정(네이버 맞춤법 검사기)

- Pyqt에 칼라 이미지 삽입(현재 유니코드로 대응시킴)

- 데이터 임베딩(fasttext, Lookuptable, word2vec, glove) 다르게 해서 결과값 비교

강의
---
- CS224n
  - [lecture](https://www.youtube.com/playlist?list=PL3FW7Lu3i5Jsnh1rnUwq_TcylNr7EkRe6)
  - [syllabu](http://web.stanford.edu/class/cs224n/syllabus.html)
- CS231n
  - [lecture](https://www.youtube.com/playlist?list=PL3FW7Lu3i5JvHM8ljYj-zLfQRF3EO8sYv)
  - [syllabus](http://cs231n.stanford.edu/2017/syllabus.html)

Data Crawling
---
- [twitterscraper](https://github.com/taspinar/twitterscraper)

Data Preprocessing
---
1. customized KoNLPy
    - [luvit github](https://github.com/lovit/customized_konlpy)

2. Soynlp
    - [luvit github](https://github.com/lovit/soynlp)

3. 트위터 한국어 처리기 (twitter-korean-text)
    - [twitterkoreantext github](https://github.com/twitter/twitter-korean-text)

4. Pycon2017 koreanNLP (konlpy,soynlp 정리 ppt)
    - [slideshare](https://www.slideshare.net/kimhyunjoonglovit/pycon2017-koreannlp)

5. 형태소 분석기 성능 비교 ratsgo’s blog
    - [ratsgo's blog](https://ratsgo.github.io/from%20frequency%20to%20semantics/2017/05/10/postag/)

6. Naver 맞춤법검사기
    - [youtube](https://www.youtube.com/watch?v=RZqRkoSaoYA)

7. resampling
    - [kaggle link](https://www.kaggle.com/rafjaa/resampling-strategies-for-imbalanced-datasets)
    - [slide share](https://www.slideshare.net/PyData/python-resampling-65637486)

NLP Model
---

1. CNN
    - Ratsgo’s blog CNN으로 문장분류하기
     : [ratsgo's blog](https://ratsgo.github.io/natural%20language%20processing/2017/03/19/CNN/)
    - CNN in keras with pretrained word2vec 
     : [kaggle link](https://www.kaggle.com/marijakekic/cnn-in-keras-with-pretrained-word2vec-weights)
    - CNN-text-classification 설명
     : [CNN text classification](http://docs.likejazz.com/cnn-text-classification-tf/)
    - implementing CNN for Text classification in tensorflow 설명 
     : [CNN in tensorflow](http://www.wildml.com/2015/12/implementing-a-cnn-for-text-classification-in-tensorflow/)
    - pytorch text-Cnn
     : [kaggle link](https://www.kaggle.com/ziliwang/pytorch-text-cnn)
    - Cnn text classification with word2vec
     : [gihub link](https://github.com/juanmangh/CNN-text-classification-with-Word2Vec/blob/master/CNN-text-classification-model-using-word2vec_Presentation.pdf)

2. FastText
    - facebook’s fastText algorithm
     : [kaggle link](https://www.kaggle.com/heesoo37/facebook-s-fasttext-algorithm)

3. Bilstm / LSTM
    - Emoji Prediction with BILSTM & LSTM model
     : [github link](https://github.com/neonrights/emoji_predictor/blob/master/Emoji_Prediction_BILSTM_LSTM_model3.ipynb)
    - attention base bilstm
     : [github link](https://github.com/SeoSangwoo/Attention-Based-BiLSTM-relation-extraction)
    - ratsgo’s blog bi-Lstm hegemony
     : [ratsgo's blog](https://ratsgo.github.io/natural%20language%20processing/2017/10/22/manning/)
    - ratsgo’s blog rnn과 lstm 설명 
     : [ratsgo's blog](https://ratsgo.github.io/natural%20language%20processing/2017/03/09/rnnlstm/)
    - sentimental analysis bilstm을 이용한 영화 리뷰 감성분석
     : [github link])https://github.com/MSWon/Sentimental-Analysis)
    - pytorch bilstm  
     : [kaggle link](https://www.kaggle.com/ziliwang/baseline-pytorch-bilstm)

4. text classification model 총괄 (CNN & RNN & Bilstm)
    - cnn/rnn text classification 관련 자료 
     : [github link](https://github.com/dongjun-Lee/text-classification-models-tf)
    - deeplearning 4 text classification (cNN, bilstm)
     : [kaggle link](https://www.kaggle.com/kakiac/deep-learning-4-text-classification-cnn-bi-lstm)
5. word rembedding
   - bag of words
     : [BOW](https://khanrc.tistory.com/entry/kaggle-Bag-of-Words-Meet-Bags-of-Popcorn-1-Part-1)
    - word2vec (skip-gram)
     : [W2V_skipgram](https://towardsdatascience.com/word2vec-skip-gram-model-part-2-implementation-in-tf-7efdf6f58a27)

pyqt
---
- [pyqt 강의 영상](https://www.youtube.com/watch?v=LYu5x339USM) 
- [pyqt tutorial](https://opentutorials.org/module/544)

Deepmoji / Emoji 관련 사이트
---
- [Deepmoji site](https://deepmoji.mit.edu/)
- [emojitacker](http://emojitracker.com/)  

관련논문/깃헙
---
- [Paper](http://aclweb.org/anthology/S18-1003)
- [Mit github](https://github.com/bfelbo/DeepMoji)







