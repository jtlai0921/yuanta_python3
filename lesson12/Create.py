import datetime

from sqlalchemy import create_engine, Column, Integer, ForeignKey, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

from lesson12.Dao import getSession, User

if __name__ == '__main__':
    session = getSession()

    user = User('user1')
    session.add(user)


    # 提交到資料庫中儲存:
    session.commit()

    # 關閉 session:
    session.close()