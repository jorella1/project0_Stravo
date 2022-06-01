from models.login_dto import Login
from repo.login_dao import delete_user, select_user
from repo.pr_dao import select_pr_by_id, delete_pr_info
from repo.login_dao import select_user_by_username
from repo.user_info_dao import delete_user_info

def get_prs(user):
    user_id = select_user_by_username(user)
    pr_dto = select_pr_by_id(user_id.user_id)
    #print(pr_dto)
    if pr_dto is not None:
        return pr_dto
    else:
        return None

def delete_all(user):
    user_id = select_user_by_username(user)
    delete_pr_info(user_id)
    delete_user_info(user_id)
    delete_user(user_id)

