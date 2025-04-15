# app.py
from flask import Flask, render_template

app = Flask(__name__)

# 메인 페이지
@app.route('/')
def index():
    return render_template('main.html')

# 각 메뉴별 페이지 라우팅
@app.route('/scenario')
def scenario():
    return render_template('0scenario.html')

@app.route('/analysis_goal')
def analysis_goal():
    return render_template('1analysis_goal.html')

@app.route('/libraries')
def libraries():
    return render_template('2libraries.html')

@app.route('/hypothesis')
def hypothesis():
    return render_template('3hypothesis.html')
#=========================

# @app.route('/visualization')
# def visualization():
#     return render_template('4visualization.html')

@app.route('/visualization')
def visualization():
    return render_template('4visualization.html')

@app.route('/get_overcrowding_content')
def get_overcrowding_content():
    return render_template('4visualization-1.html')

@app.route('/get_lowbirth_content')
def get_lowbirth_content():
    return render_template('4visualization-2.html')


#=========================

@app.route('/conclusion')
def conclusion():
    return render_template('5conclusion.html')

@app.route('/references')
def references():
    return render_template('6references.html')

@app.route('/team')
def team():
    return render_template('7team.html')

if __name__ == '__main__':
    app.run(debug=True,port=5001)