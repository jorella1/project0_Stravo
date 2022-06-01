from distutils.dep_util import newer_pairwise
from flask import render_template, redirect, url_for
from repo.login_dao import select_user_by_username
from repo.pr_dao import update_pr
from service.pace_calculator import hms_to_seconds,secs_to_time

def get_pr_page(user):
    return render_template("pr.html", username=user)

def add_new_pr(user, pr_input):
    print(pr_input)
    new_pr = secs_to_time(hms_to_seconds(int(pr_input["timeH"]),int(pr_input["timeM"]),int(pr_input["timeS"])))

    distance = pr_input["distance"]
    user_id = select_user_by_username(user)
    if(distance == '13'):
        update_pr(user_id.user_id, ("half_pr", new_pr))
    if(distance == '26'):
        update_pr(user_id.user_id, ("full_pr", new_pr))
    if(distance == '31'):
        update_pr(user_id.user_id, ("fiftyk_pr", new_pr))
    if(distance == '50'):
        update_pr(user_id.user_id, ("fiftym_pr", new_pr))
    if(distance == '62'):
        update_pr(user_id.user_id, ("hundredk_pr", new_pr))
    if(distance == '100'):
        update_pr(user_id.user_id, ("hundredm_pr", new_pr))

    return redirect(url_for('account_page', user=user))


