import psycopg2
from repo.connection import get_connection
from models.login_dto import Login
from models.pr_dto import PR
from psycopg2.extensions import AsIs

def select_pr_by_id(user_id):
    connection = get_connection()
    cursor = connection.cursor()

    qry = f"SELECT * FROM pr_table WHERE user_id = {user_id};"

    try:
        cursor.execute(qry)
        while True:
            record = cursor.fetchone()
            if record is None:
                break
            user_pr = PR(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8])
            return user_pr
    except(psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
 
def insert_pr(user_id, pr):
    connection = get_connection()
    cursor = connection.cursor()
    qry = "INSERT INTO pr_table VALUES (default, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING user_id;"

    try:
        cursor.execute(qry, (user_id, pr.half_pr, pr.full_pr, pr.fiftyk_pr, pr.fiftym_pr, pr.hundredk_pr, pr.hundredm_pr, pr.about_me))
        id = cursor.fetchone()[0]
        connection.commit()
        return id
    except(psycopg2.DatabaseError) as error:
        print(error)
        connection.rollback()
    finally:
        if connection is not None:
            connection.close()
#user_id and tuple of PR (distance column name, seconds)
def update_pr(user_id, pr):
    connection = get_connection()
    cursor = connection.cursor()
    qry = "UPDATE pr_table SET %s = %s where user_id = %s RETURNING user_id;"
    print(qry)
    try:
        cursor.execute(qry, (AsIs(pr[0]), pr[1], user_id))
        id = cursor.fetchone()[0]
        connection.commit()
        return id
    except(psycopg2.DatabaseError) as error:
        print(error)
        connection.rollback()
    finally:
        if connection is not None:
            connection.close()

def delete_pr_info(login_dto: Login):
    connection = get_connection()
    cursor = connection.cursor()

    qry = f"DELETE FROM pr_table WHERE user_id = {login_dto.user_id} RETURNING pr_id;"

    try:
        cursor.execute(qry)
        id = cursor.fetchone()[0]
        connection.commit()
        return id
    except(psycopg2.DatabaseError) as error:
        print(error)
        connection.rollback()
    finally:
        if connection is not None:
            connection.close()