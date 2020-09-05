from tkinter import *
from tkinter.ttk import *
import numpy as np
class GradePrediction:
  def __init__(self,student):
   
    #student information inputs
    #get the info of student's gender(choose)
    self.gender_label=Label(student,text="1.Student's gender")
    self.gender_label.grid(row=1,column=1,sticky=W)
    self.gender_choices = ["Female", "Male"]
    self.gender_combobox = Combobox(student,
                              values=self.gender_choices,
                              font=("Arial", 10))
    self.gender_combobox.set('Male')
    self.gender_combobox.grid(row=1, column=2,)    
    
    #get the info of times the student participate on discussion groups(entry)
    self.discussion_label=Label(student,text="2.How many times the student participate on discussion groups (numeric:0-100)?")
    self.discussion_label.grid(row=2,column=1,sticky=W)
    self.discussion_entry = Entry(student,width=12)
    self.discussion_entry.grid(row=2,column=2)
    
    #get the info of who's responsible for student?(choose)
    self.relation_label=Label(student,text="3.Who's responsible for student?")
    self.relation_label.grid(row=3,column=1,sticky=W)
    self.responsible_choices = ["Father", "Mum"]
    self.responsible_combobox = Combobox(student,
                              value=self.responsible_choices,
                              font=("Arial", 10))
    self.responsible_combobox.set('Mum')
    self.responsible_combobox.grid(row=3, column=2) 
    
    #get the info of times the student raises his/her hand on classroom(entry)
    self.raisedhands_label=Label(student,text="4.How many times the student raises his/her hand on classroom(numeric:0-100)?")
    self.raisedhands_label.grid(row=4,column=1,sticky=W)
    self.raisedhands_entry = Entry(student,width=12)
    self.raisedhands_entry.grid(row=4,column=2)    
    
    #get the info of the  times the student visits a course content?
    self.VisITedResources_label=Label(student,text="5.How many times the student visits a course content(numeric:0-100)?")
    self.VisITedResources_label.grid(row=5,column=1,sticky=W)
    self.VisITedResources_entry = Entry(student,width=12)
    self.VisITedResources_entry.grid(row=5,column=2)    
    
    #get the info of times the student checks the new announcements
    self.AnnouncementsView_label=Label(student,text="6.How many times the student checks the new announcements(numeric:0-100)?")
    self.AnnouncementsView_label.grid(row=6,column=1,sticky=W) 
    self.AnnouncementsView_entry = Entry(student,width=12)
    self.AnnouncementsView_entry.grid(row=6,column=2)    
    
    #get the info of if parent answered the surveys which are provided from school or not 
    self.ParentAnsweringSurvey_label=Label(student,text="7.Parent answered the surveys which are provided from school or not.")
    self.ParentAnsweringSurvey_label.grid(row=7,column=1,sticky=W)
    self.survey_choices = ["Yes", "No"]
    self.survey_combobox = Combobox(student,
                              value=self.survey_choices,
                              font=("Arial", 10))
    self.survey_combobox.set('Yes')
    self.survey_combobox.grid(row=7, column=2)    
    
    #get the info of the Degree of parent satisfaction from school.
    self.ParentschoolSatisfaction_label=Label(student,text="8.The Degree of parent satisfaction from school.")
    self.ParentschoolSatisfaction_label.grid(row=8,column=1,sticky=W)
    self.satisfaction_choices = ["Good", "Bad"]
    self.satisfaction_combobox = Combobox(student,
                              value=self.satisfaction_choices,
                              font=("Arial", 10))
    self.satisfaction_combobox.set('Good')
    self.satisfaction_combobox.grid(row=8, column=2)   
    
    #get the info of the number of absence days for each student
    self.StudentAbsenceDays_label=Label(student,text="9.The number of absence days for each student.")
    self.StudentAbsenceDays_label.grid(row=9,column=1,sticky=W)
    self.absence_choices = ["above-7", "under-7"]
    self.absence_combobox = Combobox(student,
                              value=self.absence_choices,
                              font=("Arial", 10))
    self.absence_combobox.set('above-7')
    self.absence_combobox.grid(row=9, column=2)
    
    #submit and quit function
    self.submit_button = Button(student,text='Submit',command=self.generategrade)
    self.submit_button.grid(row=10,column=1,padx=3, pady=10)  
    self.quit_button = Button(student,text='Quit',command=student.withdraw)
    self.quit_button.grid(row=10,column=2,padx=3, pady=10)    
    
    #the ouput
    self.prediction_label=Label(student,text='As predicted, your grade level might be ...',font=("Arial", 18))
    self.prediction_label.grid(row=11,column=1,columnspan=3, pady=10)
    
  def generategrade(self):
    '''use the model to predict a student's grade'''
    
    gender=self.gender_combobox.get()
    if self.gender_combobox.get() == 'Female':
      gender = 1
    elif self.gender_combobox.get() == 'Male':
      gender = 0
      
    Discussion = float(self.discussion_entry.get())
    raisedhands = float(self.raisedhands_entry.get())
    Relation=self.responsible_combobox.get()
    if self.responsible_combobox.get() == "Father":
      Relation = 0
    elif self.responsible_combobox.get() ==  "Mum":
      Relation = 1
      
    VisITedResources=float(self.VisITedResources_entry.get())
      
    AnnouncementsView=float(self.AnnouncementsView_entry.get())
      
    ParentAnsweringSurvey = self.survey_combobox.get()
    if self.survey_combobox.get() == "Yes":
      ParentAnsweringSurvey = 0
    elif self.survey_combobox.get() =="No":
      ParentAnsweringSurvey = 1
  
    ParentschoolSatisfaction=self.satisfaction_combobox.get()
    if self.satisfaction_combobox.get()=='Good':
      ParentschoolSatisfaction=0
    elif self.satisfaction_combobox.get()=='Bad':
      ParentschoolSatisfaction=1
      
    StudentAbsenceDays=self.absence_combobox.get()
    if self.absence_combobox.get()=='under-7':
      StudentAbsenceDays=0
    elif self.absence_combobox.get()=='above-7':
      StudentAbsenceDays=1
    
    
    facts = [gender, Discussion, Relation, raisedhands, VisITedResources, AnnouncementsView, ParentAnsweringSurvey, 
                ParentschoolSatisfaction, StudentAbsenceDays]    
    
    model_coef = [0.08651352, 0.00727865, -0.55704206, 0.01842747, -0.01123074,0.01458594
    ,-0.57467457, 0.61160851,-0.12445824]
    model_intercept = 4.720395792757541  

    res = -1
    for i in range(0, len(model_coef)):
      res += model_coef[i] * facts[i]
      grade = res + model_intercept
    if grade <= 0:
      grade = 0
    self.prediction_label['text'] = 'As predicted, your grade level might be G-'+ str(int(grade))+'.'
            
def main():
    window = Tk()
     #give the program a title
    header = Label(window,text='Student Grades Prediction Program',font=("Arial", 18))
    header.grid(row=0, column=0,columnspan=3, pady=10)    
    gui = GradePrediction(window)
    window.mainloop()
main()
