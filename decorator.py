import mysql.connector


def db_conn(funct):
    def inner_func(*args,**kwargs):
        conn = mysql.connector.connect(
            host='',
            user='',
            password='',
            database=''

        )
        cursor = conn.cursor()

        result = funct(cursor, *args, **kwargs)

        conn.commit()
        cursor.close()
        conn.close()

        return result

    return inner_func
