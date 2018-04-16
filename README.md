# TextAnnotation
Couple of scripts used to generate automatique annotation for golden annotated CoNLL files using Jackknifing, Marmot parser for POS tags and Mate parser for syntactic annotations



### Dependencies

1- Convert the current conllu train file into conllu 2009

2- extract the mate model based of the train file

3- predict the dep of test file.

4- integrate the predictions.

5- divide the train file into 10 folds of train and tests.

6- creat a batsh to train a model, predict the test

7- merge all resulting folds

8- integrate them with train file.