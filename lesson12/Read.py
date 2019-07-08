from lesson12.Dao import getSession, User

if __name__ == '__main__':
    session = getSession()

    for u in session.query(User):
        print(u)

    # 關閉 session:
    session.close()
