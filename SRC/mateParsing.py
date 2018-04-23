import os

import marmot


def ConlluToConll2009(conllu2016Path):
    with open(conllu2016Path) as corpusFile:
        lines = corpusFile.readlines()
        Conll2009Text = ''

        for line in lines:
            if len(line) > 0 and line.endswith('\n'):
                line = line[:-1]
            if line.startswith('#'):
                continue
            if line == '':
                Conll2009Text += line + '\n'
                continue
            lineParts = line.split('\t')
            if '-' in lineParts[0]:
                continue
            if len(lineParts) != 10 or '-' in lineParts[0]:
                print 'Error: not-well formatted line: file: ', str(os.path.basename(conllu2016Path)), ', line:', line
                continue

            Conll2009Text += lineParts[0] + '\t' + lineParts[1] + '\t' + lineParts[2] + '\t' + lineParts[2] + '\t' + \
                             lineParts[3] + '\t' + lineParts[3] + '\t' + lineParts[5] \
                             + '\t' + lineParts[5] + '\t' + lineParts[6] + '\t' + lineParts[6] + '\t' + lineParts[
                                 7] + '\t' + lineParts[7] + '\t_\t' + lineParts[8] + '\t' + lineParts[8] + '\t_'

            idx = 0
            while idx < 14:
                Conll2009Text += '\t_'
                idx += 1
            Conll2009Text += '\n'
        mateFile = open(conllu2016Path + '.conllu2009', 'w+')
        mateFile.write(Conll2009Text)


def conllu2009Toconllu(autoDep2009, conllFile, autoPos2016, desConll2016Path):
    with open(autoPos2016, 'r') as autoPos2016File:
        autoPOSLines = autoPos2016File.readlines()
        with open(autoDep2009, 'r') as autoDepFile:
            lines9 = autoDepFile.readlines()
            with open(conllFile, 'r') as Conll2016File:
                lines2016 = Conll2016File.readlines()
            Conll2016Text = ''
            autoPosIdx, idx = 0, 0
            for line in lines2016:
                if len(line) > 0 and line.endswith('\n'):
                    line = line[:-1]
                if line.startswith('#'): #or (line.split('\t') and '-' in line.split('\t')[0])
                    autoPosIdx += 1
                    Conll2016Text += line + '\n'
                    continue
                if not line.strip():
                    idx += 1
                    autoPosIdx += 1
                    Conll2016Text += line + '\n'
                    continue
                lineParts16 = line.split('\t')
                if lineParts16[0].find('-') != -1:
                    Conll2016Text += line + '\n'
                    continue
                lineParts09 = lines9[idx].split('\t')
                autoPOSLineParts = autoPOSLines[autoPosIdx].split('\t')
                line16 = '{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\t{9}\n'.format(
                    lineParts16[0],lineParts16[1],lineParts16[2],autoPOSLineParts[3],autoPOSLineParts[4],
                    lineParts16[5],lineParts09[9],lineParts09[11],lineParts16[8],lineParts16[9])
                idx += 1
                autoPosIdx += 1
                # line = ''
                # for linePart in lineParts16:
                #     line += linePart + '\t'
                # line = line[:-1] + '\n'
                Conll2016Text += line16

    mateFile = open(desConll2016Path , 'w+')
    mateFile.write(Conll2016Text)


def jackknife(foldNum, langName):
    corpusPath = '/Users/halsaied/PycharmProjects/TextAnnotation/sharedTask/' + langName + '/train.conllu.autoPOS.conllu2009'
    with open(corpusPath) as corpusFile:
        lines = corpusFile.readlines()
        foldSize = len(lines) / foldNum

        ResultPath = '/Users/halsaied/PycharmProjects/TextAnnotation/Mate/' + langName + '/Jackkniffing/'
        for i in xrange(0, foldNum):

            trainPath = os.path.join(ResultPath, str(i) + '.train.jck.txt')
            testPath = os.path.join(ResultPath, str(i) + '.test.jck.txt')

            startCuttingIdx = i * foldSize
            startCuttingiIdx = marmot.approximateCuttingIdx(startCuttingIdx, lines)
            endCuttingIdx = (i + 1) * foldSize
            endCuttingIdx = marmot.approximateCuttingIdx(endCuttingIdx, lines)

            testLines = lines[startCuttingiIdx: endCuttingIdx]
            if startCuttingIdx == 0:
                trainLines = lines[endCuttingIdx:]
            elif endCuttingIdx == len(lines) - 1:
                trainLines = lines[: startCuttingIdx]
            else:
                trainLines = lines[:startCuttingiIdx] + lines[endCuttingIdx:]

            createMateFile(trainLines, trainPath)
            createMateFile(testLines, testPath)


def createMateFile(lines, path):
    trainCorpus = ''
    for line in lines:
        trainCorpus += line

    marmotTrainFile = open(path, 'w+')
    marmotTrainFile.write(trainCorpus)


def createMateBatchJCK(foldNum, langList):
    batch = '#!/bin/bash\n'
    outPutPath = '/Users/halsaied/PycharmProjects/TextAnnotation/Mate/srl/lib/'
    for lang in langList.split(','):
        jackPath = '/Users/halsaied/PycharmProjects/TextAnnotation/Mate/{0}/Jackkniffing/'.format(lang)
        for f in xrange(0, foldNum):
            trainFile = os.path.join(jackPath, str(f) + '.train.jck.txt')
            modelFile = os.path.join(jackPath, str(f) + '.model.jck.txt')
            batch += 'java -cp anna-3.3.jar is2.parser.Parser -train ' + trainFile + ' -model ' + modelFile + '\n'
            testFile = os.path.join(jackPath, str(f) + '.test.jck.txt')
            outputFile = os.path.join(jackPath, str(f) + '.output.jck.txt')
            batch += 'java -cp anna-3.3.jar is2.parser.Parser -model ' + modelFile + ' -test ' + testFile + ' -out ' + outputFile + '\n'

        batchFile = open(outPutPath + '{0}.dep.jck.batch.sh'.format(lang), 'w+')
        batchFile.write(batch)

#
# def mergeConlluFiles(outfilesPath, outputFileName):
#     lines = ''
#     for subdir, dirs, files in os.walk(outfilesPath):
#         for file in files:
#             with open(os.path.join(outfilesPath, file)) as conlluFile:
#                 jckOutLines = conlluFile.readlines()
#                 jckOutLines = marmot.removeFinalEmptyLines(jckOutLines)
#                 for line in jckOutLines:
#                     lines += line
#     outFile = open(os.path.join(outfilesPath, outputFileName), 'w')
#     outFile.write(lines)


#ConlluToConll2009('/Users/halsaied/PycharmProjects/TextAnnotation/sharedtask/FR/train.conllu.autoPOS')
#jackknife(10, 'FR')
#createMateBatchJCK(10, 'FR')
# conllu2009Toconllu('/Users/halsaied/PycharmProjects/TextAnnotation/sharedtask/HU/train.conllu.autoPOS.conllu2009', '/Users/halsaied/PycharmProjects/TextAnnotation/sharedtask/HU/train.conllu.autoPOS')
# ConlluToConll2009('/Users/halsaied/PycharmProjects/TextAnnotation/sharedtask/HU/test.conllu.autoPOS')

#ConlluToConll2009('/Users/halsaied/PycharmProjects/TextAnnotation/sharedtask/FR/test.conllu.autoPOS')
# mergeConlluFiles('/Users/halsaied/PycharmProjects/TextAnnotation/mateTools/SPMRL/','spmrl.conllu')

#for filename in os.listdir('../MateJackkniffing/FR/'):
    #if filename.endswith('output.jck.txt'):
if __name__ == '__main__':
    conllu2009Toconllu('/Users/halsaied/PycharmProjects/TextAnnotation/Mate/Jackkniffing/FR/train.conll.2009.jck.autoDep.txt',
                   '/Users/halsaied/PycharmProjects/TextAnnotation/SharedTask/FR/train.conllu',
                       '/Users/halsaied/PycharmProjects/TextAnnotation/SharedTask/FR/train.conllu.autoPOS',
                    '/Users/halsaied/PycharmProjects/TextAnnotation/SharedTask/FR/train.conllu.autoPOS.autoDep')