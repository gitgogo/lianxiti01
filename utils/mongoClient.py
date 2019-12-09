#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:finup
# datetime:2019-12-03 11:51
# software: PyCharm

from pymongo import MongoClient, ASCENDING, DESCENDING

client = MongoClient('mongodb://localhost:27017/')
# client = pymongo.MongoClient(host='localhost', port=27017)
db = client.admin
db.authenticate("test", "123456")
db = client.test
collection = db.test
student1 = {
    'id': '20170101',
    'name': 'Jordan',
    'age': 20,
    'gender': 'male'
}
student2 = {
    'id': '20170202',
    'name': 'Mike',
    'age': 21,
    'gender': 'male'
}
# 插入数据
# result = collection.insert_one(student)
# result = collection.insert_many([student1, student2])
# print(result)

# 查询
# result = collection.find_one({'name': 'Jordan'})
# print(f'查询结果1: {result}')

# results = collection.find().sort('name', pymongo.ASCENDING)  # 排序
#
# results = collection.find_one({'age': {'$gt': 20}})  # age >20
# # $lt 小于；$gte 大于等于；$lte 小于等于；$ne 不等于；$in $nin
# print(f'查询结果2: {results}')

# 更新
condition = {'name': 'Mike'}
student = collection.find_one(condition)
print(f'student:{student}')
student['age'] = 55
result = collection.update_one(condition, {'$set': student})
student_post = collection.find_one(condition)
print(student_post)

# 删除
result2 = collection.delete_one({'name': 'Kevin'})
print(result2)
