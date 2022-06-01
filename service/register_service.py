from models.login_dto import Login
from models.user_info_dto import User
from repo.login_dao import insert_user, select_user_by_id
from repo.user_info_dao import insert_user_info
from repo.pr_dao import insert_pr
from models.pr_dto import PR

def validate_registration(input):
    login_dto = Login(0, input.get("username"), input.get("password"))
    info_dto = User(0, 0, input.get("first_name"), input.get("last_name"))

    return login_dto.validate_login() and info_dto.validate_user_info()

def create_login(input):
    user_id = insert_user(input.get("username"), input.get("password"))

    if user_id is not None:
        return user_id

def create_user_info(user_id, input):
    login_dto = select_user_by_id(user_id)
    info_id = insert_user_info(login_dto, input.get("first_name"), input.get("last_name"))

    if info_id is not None:
        return info_id
 
#add user to the PR table
def create_user_pr(user_id):
    pr_dto = PR(0, user_id, None, None, None, None, None, None, None)
    print(pr_dto)
    return_id = insert_pr(user_id, pr_dto)
    print(return_id)
    