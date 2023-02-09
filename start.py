class Student:
  def __init__(self, name):
    
    name=str(input("Enter your name:"))
    self.name = name
  def printname(self):
    print(self.name)

class Units(Student):
    def __init__(self, name,Maths, Eng ,Kisw ,Sci ,Cre ):
      super().__init__(name)
      self.Maths = Maths
      self.Eng = Eng
      self.Kisw = Kisw
      self.Sci = Sci
      self.Cre = Cre
    def Unitnames(self):
      print(self.name,self.Maths,self.Maths,self.Eng,self.Kisw,self.Sci,self.Cre)


class Marks(Units):
    def __init__(self,name, Maths, Eng ,Kisw ,Sci ,Cre , MathsMarks, EngMarks ,KiswMarks ,SciMarks ,CreMarks ):
      super().__init__(name,Maths, Eng ,Kisw ,Sci ,Cre)
      
      MathsMarks=int(input("Enter your Marks for Maths:"))
      MathsMarks=int(input("Enter your Marks for Eng:"))
      MathsMarks=int(input("Enter your Marks for Kisw:"))
      MathsMarks=int(input("Enter your Marks for Sci:"))
      MathsMarks=int(input("Enter your Marks for Cre:"))
      self.MathsMarks = MathsMarks
      self.EngMarks = EngMarks
      self.KiswMarks = KiswMarks
      self.SciMarks = SciMarks
      self.CreMarks = CreMarks
    def UnitsMarks(self):
      print( self.MathsMarks , self.EngMarks , self.KiswMarks , self.SciMarks ,self.CreMarks )


class Average(Marks):
  def __init__(self,name, Maths, Eng ,Kisw ,Sci ,Cre , MathsMarks, EngMarks ,KiswMarks ,SciMarks ,CreMarks,total ,mean):
     super().__init__(name, Maths, Eng ,Kisw ,Sci ,Cre ,MathsMarks, EngMarks ,KiswMarks ,SciMarks ,CreMarks )
     
     
     total=(self.MathsMarks+ self.EngMarks +self.KiswMarks +self.SciMarks +self.CreMarks)
     self.total=total
     mean=(self.total/5)
     self.mean = mean
  def printmean(self):
    print("your average is:" + self.mean +"having a total of :"+ self.total)

class Grade(Average):
  def __init__(self,name, Maths, Eng ,Kisw ,Sci ,Cre , MathsMarks, EngMarks ,KiswMarks ,SciMarks ,CreMarks,total ,mean,Grade):
     super().__init__(name, Maths, Eng ,Kisw ,Sci ,Cre ,MathsMarks, EngMarks ,KiswMarks ,SciMarks ,CreMarks,total,mean )
     self.Grade = Grade
     if self.mean <40:
        self.Grade="E therefore you have failed"
     elif self.mean >=40 and self.mean <50:
        self.Grade="D therefore you have pass"
     elif self.mean >=50 and self.mean <60:
        self.Grade="C is fair"
     elif    self.mean >=60 and self.mean <70:
        self.Grade="B congratulation you passed"
     elif   self.mean >=70 and self.mean <=100:
        self.Grade="A excellent work"
     else:
        self.Grade="N/A"
     
  def printGrade(self):
    
    print( "Hello" + " " + self.name +" "  + "Your total marks is" + " "+self.total+ " " + "you have   points" + " " +self.mean+ " " + "scoring grade" + " " + self.Grade)


final=Grade("name", "Maths", "Eng" ,"Kisw" ,"Sci" ,"Cre" ,"MathsMarks", "EngMarks" ,"KiswMarks" ,"SciMarks" ,"CreMarks","total ","mean","Grade")
final.printGrade()


