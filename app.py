from flask import Flask,render_template,request
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('marksheet.html')

def getPercent(m,t):
    p=int(m)/int(t)*100
    return p

def grade(p):
    
    if(p>95):
        g="S"
    elif(p>90):
        g="A+"
    elif(p>85):
        g="A"
    elif(p>80):
        g="B+"
    elif(p>75):
        g="B"
    elif(p>70):
        g="C+"
    elif(p>65):
        g="C"
    elif(p>60):
        g="D+"
    elif(p>55):
        g="D"
    elif(p<50):
        g="F"
    return g

@app.route('/result',methods=['GET','POST'])
def result():
    if(request.method=='POST'):
        getName=request.form['name']
        getRegNo=request.form['regno']
        getsem=request.form['semester']
        getcol=request.form['college']
        getsname1=request.form['s1']
        getsmark1=request.form['s1o']
        getstotal1=request.form['s1t']
        getsname2=request.form['s2']
        getsmark2=request.form['s2o']
        getstotal2=request.form['s2t']
        getsname3=request.form['s3']
        getsmark3=request.form['s3o']
        getstotal3=request.form['s3t']
        getsname4=request.form['s4']
        getsmark4=request.form['s4o']
        getstotal4=request.form['s4t']
       
        g1=grade(getPercent(getsmark1,getstotal1))
        g2=grade(getPercent(getsmark2,getstotal2))
        g3=grade(getPercent(getsmark3,getstotal3))
        g4=grade(getPercent(getsmark4,getstotal4))
        if(g1=="F" or g2=="F" or g3=="F" or g4=="F"):
            status="Failed"
        else:
            status="PASS"
        return render_template('result.html',inp1=getName,inp2=getRegNo,inp3=getsem,inp4=getcol,inp5=getsname1,inp6=getsmark1,inp7=getstotal1,inp8=getsname2,inp9=getsmark2,inp10=getstotal2,inp11=getsname3,inp12=getsmark3,inp13=getstotal3,inp14=getsname4,inp15=getsmark4,inp16=getstotal4,g1=g1,g2=g2,g3=g3,g4=g4,status=status)

if(__name__=='__main__'):
    app.run(debug=True)