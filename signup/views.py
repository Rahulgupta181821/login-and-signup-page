from django.shortcuts import render
import mysql.connector as sql
fn=''
ln=''
s=''
em=''
pwd=''


# Create your views here.
def signupaction(request):
    global fn,ln,s,em,pwd
    if request.method == 'POST':
        m = sql.connect(host="127.0.0.1",user='root',passwd="Rahul@#123",database='website')
        cursor = m.cursor()
        d = request.POST
        for key, value in d.items():
            if key=='first_name':
                fn=value
            if key=='last_name':
                ln=value
            if key=='sex':
                s=value
            if key=='email':
                em=value
            if key=='password':
                pwd=value
        c = "insert into users Values('{}','{}','{}','{}','{}')".format(fn,ln,s,em,pwd)
        cursor.execute(c)
        m.commit()
    return render(request,'signup_page.html')
            
            
            
        
         
    