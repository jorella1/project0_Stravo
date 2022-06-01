from flask import render_template
from service.account_service import get_prs, delete_all
#get all the info for the account page -> return the template with PRs and info
def get_account_page(user):

    pr_info = get_prs(user)

    return render_template("account.html", username=user, pr_info=pr_info)

def delete_user_account(user):
    delete_all(user)
    return render_template("deleted.html")
