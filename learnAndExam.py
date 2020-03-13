# -*- coding: utf-8 -*-
import yaml
import random
import time
import requests

serverUrl = 'https://weiban.mycourse.cn/pharos'

requests.head('https://g.alicdn.com/wt/log/web.js')     # 测试网络
with open('questionBanks.yaml', 'r', encoding='UTF-8') as questionsFile:
    questions = yaml.safe_load(questionsFile)
with open('configTemplate.yaml', 'r', encoding='UTF-8') as configFile:
    config = yaml.safe_load(configFile)
data = {
    'userProjectId': input('userProjectId(/login.do | /getStudyTask.do 响应参数): '),
    'userId': input('userId(/login.do 响应参数): '),
    'token': input('token(/login.do 响应参数): '),
    'tenantCode': config['tenantCode'],
    'chooseType': '3',
}

option = input('键入 回车 以 刷课+测试，键入 空格、回车 以 仅刷课\n')

listCourseRequest = requests.post(serverUrl + '/usercourse/listCourse.do', data=data)
categories = listCourseRequest.json()['data']
for categoryIndex, category in enumerate(categories, 1):
    for courseIndex, course in enumerate(category['courseList'], 1):
        print(categoryIndex, '/', len(categories), '\t', courseIndex, '/', category['totalNum'], '\t',
              course['resourceName'], sep='', end='\t\t', flush=True)
        if course['finished'] == 2:
            data['courseId'] = course['resourceId']
            requests.post(serverUrl + '/usercourse/study.do', data=data)
            print('正在学习，等待0-1s', end='\t', flush=True)
            time.sleep(random.random())
            requests.get(serverUrl + '/usercourse/finish.do',
                         params={
                             'callback': 'jQuery1234567822223333456_1577808000000',
                             'userCourseId': course['userCourseId'],
                             'tenantCode': data['tenantCode'],
                             '_': '1577808000000',
                         })
            print('完成，等待0-1s')
            time.sleep(random.random())
        else:
            print('已完成')


if option == '':
    data['userExamPlanId'] = requests.post(serverUrl + '/exam/listPlan.do', data=data).json()['data'][0]['id']
    requests.post(serverUrl + '/exam/preparePaper.do', data=data)
    startPaperRequestJSON = requests.post(serverUrl + '/exam/startPaper.do', data=data).json()
    noAnswer = False
    for questionIndex, question in enumerate(startPaperRequestJSON['data'], 1):
        print(questionIndex, '/', len(startPaperRequestJSON['data']), sep='', end='\t', flush=True)
        if question['id'] not in questions:
            print('@@@@@@@@@@无答案@@@@@@@@@@', end='\t', flush=True)
            noAnswer = True
            continue
        data['questionId'] = question['id']
        data['useTime'] = '1'
        answers = []
        answersContent = []
        for answer in questions[question['id']]['optionList']:
            answers.append(answer['id'])
            answersContent.append(answer['content'])
        data['answerIds'] = ','.join(answers)
        requests.post(serverUrl + '/exam/recordQuestion.do', data=data)
        print(question['title'], answersContent, sep='\t')
    if noAnswer:
        print('未提交测试')
    else:
        requests.post(serverUrl + '/exam/submitPaper.do', data=data)
