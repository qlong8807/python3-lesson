#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

"""
pip3 install face_recognition
"""

__author__ = 'Jans'
__date__ = '2018/3/27 下午4:31'
__createby__ = 'PyCharm'


# 识别图片中的人脸
import face_recognition

trump_image = face_recognition.load_image_file("pic/trump.jpg");
trump_new_image = face_recognition.load_image_file("pic/trump_new.jpg");
trump_old_image = face_recognition.load_image_file("pic/trump_old.jpg");
trump_young_image = face_recognition.load_image_file("pic/trump_young.jpg");

encoding1 = face_recognition.face_encodings(trump_image)[0]
encoding2 = face_recognition.face_encodings(trump_old_image)[0]
encoding3 = face_recognition.face_encodings(trump_new_image)[0]
# encoding3 = face_recognition.face_encodings(trump_young_image)[0]

results = face_recognition.compare_faces([encoding1, encoding2], encoding3 )
labels = ['img', 'old']

print('results:'+str(results))

for i in range(0, len(results)):
    if results[i] == True:
        print('The person is:'+labels[i])