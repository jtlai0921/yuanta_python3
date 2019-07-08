from lesson12.Dao import getSession, User

if __name__ == '__main__':
    session = getSession()

    users = session.query(User)
    for user in users:
        print(user)

    # 關閉 session:
    session.close()
