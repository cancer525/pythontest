from django.db import connection

def user_contacts(request):
    user = request.GET['username']
    sql = "SELECT * FROM user_contacts WHERE username = %s;"
    cursor = connection.cursor()
    cursor.execute(sql, [user]) # 1
    cursor.execute(sql, user) # 2
    # ... do something with the results

user_contacts();
