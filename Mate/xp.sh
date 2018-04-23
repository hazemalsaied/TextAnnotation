#!/bin/bash
cd MateParser
java -cp anna-3.3.jar is2.parser.Parser -train Jackkniffing/1.train.jck.txt -model Jackkniffing/1.model.jck.txt
java -cp anna-3.3.jar is2.parser.Parser -model Jackkniffing/1.model.jck.txt -test Jackkniffing/1.test.jck.txt -out Jackkniffing/1.output.jck.txt
java -cp anna-3.3.jar is2.parser.Parser -train Jackkniffing/2.train.jck.txt -model Jackkniffing/2.model.jck.txt
java -cp anna-3.3.jar is2.parser.Parser -model Jackkniffing/2.model.jck.txt -test Jackkniffing/2.test.jck.txt -out Jackkniffing/2.output.jck.txt
java -cp anna-3.3.jar is2.parser.Parser -train Jackkniffing/3.train.jck.txt -model Jackkniffing/3.model.jck.txt
java -cp anna-3.3.jar is2.parser.Parser -model Jackkniffing/3.model.jck.txt -test Jackkniffing/3.test.jck.txt -out Jackkniffing/3.output.jck.txt
java -cp anna-3.3.jar is2.parser.Parser -train Jackkniffing/4.train.jck.txt -model Jackkniffing/4.model.jck.txt
java -cp anna-3.3.jar is2.parser.Parser -model Jackkniffing/4.model.jck.txt -test Jackkniffing/4.test.jck.txt -out Jackkniffing/4.output.jck.txt
java -cp anna-3.3.jar is2.parser.Parser -train Jackkniffing/5.train.jck.txt -model Jackkniffing/5.model.jck.txt
java -cp anna-3.3.jar is2.parser.Parser -model Jackkniffing/5.model.jck.txt -test Jackkniffing/5.test.jck.txt -out Jackkniffing/5.output.jck.txt
java -cp anna-3.3.jar is2.parser.Parser -train Jackkniffing/6.train.jck.txt -model Jackkniffing/6.model.jck.txt
java -cp anna-3.3.jar is2.parser.Parser -model Jackkniffing/6.model.jck.txt -test Jackkniffing/6.test.jck.txt -out Jackkniffing/6.output.jck.txt
java -cp anna-3.3.jar is2.parser.Parser -train Jackkniffing/7.train.jck.txt -model Jackkniffing/7.model.jck.txt
java -cp anna-3.3.jar is2.parser.Parser -model Jackkniffing/7.model.jck.txt -test Jackkniffing/7.test.jck.txt -out Jackkniffing/7.output.jck.txt
java -cp anna-3.3.jar is2.parser.Parser -train Jackkniffing/8.train.jck.txt -model Jackkniffing/8.model.jck.txt
java -cp anna-3.3.jar is2.parser.Parser -model Jackkniffing/8.model.jck.txt -test Jackkniffing/8.test.jck.txt -out Jackkniffing/8.output.jck.txt
java -cp anna-3.3.jar is2.parser.Parser -train Jackkniffing/9.train.jck.txt -model Jackkniffing/9.model.jck.txt
java -cp anna-3.3.jar is2.parser.Parser -model Jackkniffing/9.model.jck.txt -test Jackkniffing/9.test.jck.txt -out Jackkniffing/9.output.jck.txt
java -cp anna-3.3.jar is2.parser.Parser -train Jackkniffing/train.conllu.autoPOS.conllu2009 -model Jackkniffing/model.txt
java -cp anna-3.3.jar is2.parser.Parser -model Jackkniffing/model.txt -test Jackkniffing/test.conllu.autoPOS.conllu2009 -out Jackkniffing/output.txt