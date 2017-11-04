from flask import Flask
from flask import request
from flask import render_template
from Reply_Classifier import *

app = Flask(__name__)
Reply_Set=[]
def mapToReply(a):
    print(a)
    if a==[1.]:
       print('hello')
       return("We will look into it ASAP", 'We are working on it','It will be up and running in')
    if a ==[2.]:
       return("Please come to the IT help desk.","You can change your password here:","The details are fine. Please try again.")
    if a ==[3.]:
       return("Please come to the IT help desk","No clicker is available at the moment.","	We'll send someone now. ")
    if a ==[4.]:
       return("We'll get it checked.","	We will send someone right now","We have fixed the problem.")
    if a ==[5.]:
       return("Please come to the IT help desk.","The ID card has been blocked.","We will let you know soon.")
    if a ==[6.]:
       return("The course has been added.","You cannot add this course.","Please come to the OAA office.")
    if a ==[7.]:
       return("The course has been dropped.","	You cannot drop any more courses.","Please come to the OAA office.")
    if a ==[8.]:
       return("Please check the timetable.","We'll check and let you know.","It has been resolved. Please check timetable.")
    if a ==[9.]:
       return("We'll be sending it out soon.","Please find it attached.","We'll check and let you know.")
    if a ==[10.]:
       return("It will be held on ","The dates haven't been finalised.","We'll check and let you know.")
    if a ==[11.]:
       return("The room has been booked.","The room is not available.","We'll check and let you know.")
    if a ==[12.]:
       return("The booking has been cancelled.","We cannot book another room at the moment","Done. Do you want to book another room ?")
    if a ==[13.]:
       return("We'll let you know soon.","Can you meet us at OSL office at: ","This timings are not suitable. Are you free anytime else?")
    if a ==[14.]:
       return("Please come to the reception and collect it.","We haven't received the bills from you yet.","We'll let you know once it's ready.")
@app.route('/')
def my_form():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def my_form_post():

    text = request.form['text']
    subject = request.form['subject']
    sub=subject
    Body = text
    Set_Classifier(sub,Body)
    rep = Reply_Classify(sub,Body)
    a = mapToReply(rep)
    reply1 = a[0]
    reply2 = a[1]
    reply3 = a[2]
    print(reply1,reply2,reply3)
    return render_template("new.html",freply1=reply1,freply2=reply2,freply3=reply3)

if __name__ == '__main__':
    app.debug = True
    app.run()
