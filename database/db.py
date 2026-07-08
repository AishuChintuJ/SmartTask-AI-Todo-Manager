import sqlite3


def connect_db():

    return sqlite3.connect(
        "smarttask.db"
    )



# ================= USERS =================


def create_tables():

    conn = connect_db()

    cursor = conn.cursor()


    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            username TEXT,

            email TEXT UNIQUE,

            password TEXT

        )
        """
    )


    conn.commit()

    conn.close()





def register_user(username,email,password):

    try:

        conn=connect_db()

        cursor=conn.cursor()


        cursor.execute(
            """
            INSERT INTO users
            (username,email,password)
            VALUES(?,?,?)
            """,

            (
                username,
                email,
                password
            )
        )


        conn.commit()

        conn.close()


        return True


    except:


        return False





def login_user(email,password):


    conn=connect_db()

    cursor=conn.cursor()


    cursor.execute(

        """
        SELECT * FROM users
        WHERE email=? AND password=?
        """,

        (
            email,
            password
        )

    )


    user=cursor.fetchone()


    conn.close()


    return user




# ================= TASK TABLE =================


def create_task_table():


    conn=connect_db()

    cursor=conn.cursor()



    cursor.execute(

        """
        CREATE TABLE IF NOT EXISTS tasks(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            user_id INTEGER,

            title TEXT,

            category TEXT,

            priority TEXT,

            due_date TEXT,

            status TEXT

        )
        """

    )


    conn.commit()

    conn.close()





def add_task(
        user_id,
        title,
        category,
        priority,
        due_date
):


    conn=connect_db()

    cursor=conn.cursor()


    cursor.execute(

        """
        INSERT INTO tasks
        (
        user_id,
        title,
        category,
        priority,
        due_date,
        status
        )

        VALUES(?,?,?,?,?,?)
        """,

        (
            user_id,
            title,
            category,
            priority,
            due_date,
            "Pending"
        )

    )


    conn.commit()

    conn.close()





def get_tasks(user_id):


    conn=connect_db()

    cursor=conn.cursor()


    cursor.execute(

        """
        SELECT *
        FROM tasks
        WHERE user_id=?
        """,

        (
            user_id,
        )

    )


    tasks=cursor.fetchall()


    conn.close()


    return tasks






def update_task_status(
        task_id,
        status
):


    conn=connect_db()

    cursor=conn.cursor()


    cursor.execute(

        """
        UPDATE tasks

        SET status=?

        WHERE id=?
        """,

        (
            status,
            task_id
        )

    )


    conn.commit()


    conn.close()






# ================= DASHBOARD =================


def task_statistics(user_id):


    conn=connect_db()

    cursor=conn.cursor()



    # Total


    cursor.execute(

        """
        SELECT COUNT(*)

        FROM tasks

        WHERE user_id=?
        """,

        (
            user_id,
        )

    )


    total=cursor.fetchone()[0]





    # Completed


    cursor.execute(

        """
        SELECT COUNT(*)

        FROM tasks

        WHERE user_id=?

        AND status='Completed'
        """,

        (
            user_id,
        )

    )


    completed=cursor.fetchone()[0]





    # Pending


    cursor.execute(

        """
        SELECT COUNT(*)

        FROM tasks

        WHERE user_id=?

        AND status='Pending'
        """,

        (
            user_id,
        )

    )



    pending=cursor.fetchone()[0]


    conn.close()



    return (
        total,
        completed,
        pending
    )





# SEARCH


def search_task(user_id,keyword):


    conn=connect_db()

    cursor=conn.cursor()


    cursor.execute(

        """
        SELECT *

        FROM tasks

        WHERE user_id=?

        AND title LIKE ?
        """,

        (
            user_id,
            "%"+keyword+"%"
        )

    )


    data=cursor.fetchall()


    conn.close()


    return data





# FILTER


def filter_task(user_id,status):


    conn=connect_db()


    cursor=conn.cursor()



    cursor.execute(

        """
        SELECT *

        FROM tasks

        WHERE user_id=?

        AND status=?
        """,

        (
            user_id,
            status
        )

    )



    data=cursor.fetchall()


    conn.close()


    return data