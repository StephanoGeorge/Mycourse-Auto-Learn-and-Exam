# -*- coding: utf-8 -*-
import yaml
import json
import os


def readQuestions(path):
    with open(path, 'r', encoding='UTF-8') as questionFile:
        questionsResponse = json.load(questionFile)
    for question in questionsResponse['data']['questions']:
        del question['sequence']
        del question['analysis']
        del question['isRight']
        newOptionList = []
        for index, option in enumerate(question['optionList'], 0):
            if option['isCorrect'] == 1:
                del option['sequence']
                del option['selected']
                del option['isCorrect']
                newOptionList.append(option)
        question['optionList'] = newOptionList
        questionList[question['id']] = question
        del questionList[question['id']]['id']


with open('questionBanks.yaml', 'r+', encoding='UTF-8') as questionSummaryFile:
    questionList = yaml.safe_load(questionSummaryFile)
    for file in os.listdir('QuestionBanks'):
        readQuestions('QuestionBanks/' + file)
    questionSummaryFile.seek(0, 0)
    yaml.safe_dump(questionList, questionSummaryFile, indent=4, allow_unicode=True)
