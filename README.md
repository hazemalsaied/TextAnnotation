# TextAnnotation
Couple of scripts used to generate automatique annotation for golden annotated CoNLL files using Jackknifing, Marmot parser for POS tags and Mate parser for syntactic annotations

# Ref:
        https://github.com/muelletm/cistern/blob/wiki/marmot.md

        http://cistern.cis.lmu.de/marmot/

## Marmot (FR as example)
### Train annotation:
1. python marmot.jackknife(10, 'FR')
2. python marmot.creatBatchForMarmotJCK(10, Language)
3. run the batch: Marmot/Jackkniffing/FR.postag.jck.batch.sh
4. python marmot.mergeJckOutFiles()
5. python marmot.integrateAutoPOS(jckMarmotFile, train file)

### Test annotation:
1. python marmot.getTrainModelCorpus()
2. python marmot.getTestModelCorpus()
3. run the batch : Marmot/FR.postag.batch.sh
4. python marmot.integrateAutoPOS(marmotTestFile, test file)


## Mate (FR as example)
### Train annotation:
1. python mate.ConlluToConll2009
2. python mate.jackknife
3. python marmot.creatBatch
4. run the batch: Mate/xp.sh
5. python marmot.mergeJckOutFiles
6. python marmot.conllu2009Toconllu

### Test annotation:
1. python mate.ConlluToConll2009
2. run the batch : Mate/xp.sh
3. python marmot.conllu2009Toconllu



### Dependencies

1- Convert the current conllu train file into conllu 2009

2- extract the mate model based of the train file

3- predict the dep of test file.

4- integrate the predictions.

5- divide the train file into 10 folds of train and tests.

6- creat a batsh to train a model, predict the test

7- merge all resulting folds

8- integrate them with train file.