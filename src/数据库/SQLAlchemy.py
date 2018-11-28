#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

"""
pip3 install sqlalchemy
"""

__author__ = 'Jans'
__date__ = '2018/1/25 下午1:48'
__createby__ = 'PyCharm'

from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()


# 定义User对象:
class User(Base):
    # 表的名字:
    __tablename__ = 'user'

    # 表的结构:
    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    age = Column(Integer)

    def __str__(self):
        return 'User-> id:%s,name:%s,age:%s' % (self.id, self.name, self.age)

    __repr__ = __str__


# 初始化数据库连接:
engine = create_engine('mysql+mysqlconnector://root:root1234@localhost:3306/test?charset=utf8')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)
# 创建session对象:
session = DBSession()
# 删除
session.query(User).filter(User.id == '5').delete()
session.commit()
# 创建新User对象:
new_user = User(id='5', name='Bob', age=25)
# 添加到session:
session.add(new_user)
# session.add_all([
#     User(id='a', name="alex1", age=15),
#     User(id='b', name="alex2", age=11)
# ])
# 提交即保存到数据库:
session.commit()
# 修改
# session.query(User).filter(User.id == 5).update({"name": "099"})
# session.query(User).filter(User.id == 6).update({User.name: User.name + "099"}, synchronize_session=False)
# session.query(User).filter(User.id > 8).update({"num": User.num + 1}, synchronize_session="evaluate")
session.commit()
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
user = session.query(User).filter(User.id == '5').one()
print(user)
ret = session.query(User).all()
print(ret)
ret = session.query(User.name, User.age).all()
print(ret)
ret = session.query(User).filter_by(name='Bob').all()
print(ret)
ret = ret = session.query(User).filter(User.name.like('alex%')).all()
print(ret)
ret = session.query(User).filter_by(name='alex1').first()
print(ret)
# 关闭session:
session.close()
