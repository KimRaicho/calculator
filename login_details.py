login_dict = {}
filename = 'login.txt'


def save_login_details():
    with open(filename, 'w') as f:
        for login in login_dict:
            f.write(login)
