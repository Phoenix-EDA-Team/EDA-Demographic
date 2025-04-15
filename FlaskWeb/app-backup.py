# app.py
from flask import Flask, render_template, jsonify

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

# @app.route('/hypothesis')
# def hypothesis():
#     return render_template('3hypothesis.html')

@app.route('/hypothesis/<int:num>')
def hypothesis(num):
    # 각 가설별 HTML 블록 (글 내용 및 이미지 포함, 실제로는 파일에서 읽거나 DB에서 불러올 수도 있음)
    hypothesis_blocks = {
        1: '''
<strong>가설 :수도권으로의 인구 유입이 지방 인구 감소를 가속화한다</strong> <br>
<img src="../static/img/graph/수도권-비수도권 순이동률 비교 (2012-2022).png" class="img-fluid">
<hr>
''',
        2: '''
<strong>가설 :대도시의 자연증가율 보다 소도시의 자연증가율이 낮을것이다.</strong> <br>
<img src="../static/img/graph/가설2-2.도시.png" class="img-fluid">  
<img src="../static/img/graph/가설2-2.지방.png" class="img-fluid">
또한 자연 증가율 비교에 따르면,
수도권과 광역시에 비해 지방 소도시의 인구 감소 폭이 훨씬 더 크며,
이미 다수의 소도시에서는 자연 증가율이 마이너스 상태에 도달했다.
<hr>
''',
        3: '''
<strong>가설 :지방의 낮은 혼인율이 인구 감소를 가속화한다.</strong> <br>
<img src="../static/img/graph/가설1-년도별 수도권 vs 지방 출산율-결혼률 비교.png" class="img-fluid">
<img src="../static/img/graph/가설1-년도별 대도시 vs 소도시 출산율-결혼률 비교.png" class="img-fluid">
하지만 출산율과 혼인율 그래프에서는
수도권과 비수도권, 대도시와 소도시 모두가 같은 흐름으로 감소하고 있으며,
낙폭에는 차이가 있지만 감소 방향은 전국적으로 일관되게 나타나고 있다.
<br><br>
결론 : 다시 말해, 지방 공동화는 저출산의 주된 원인이라기보다,
인구 구조 붕괴를 더 빠르게 가속화시키는 지역적 촉매제이며,
저출산 문제 자체는 전국이 함께 겪고 있는 구조적 인구 위기라고 할 수 있다.
<hr>
''',
        4: '''
<strong>가설1 :</strong>결혼율 감소가 출산률 하락의 주요 원인일것이다. <br>
<img src="../static/img/graph/가설1-결혼률과 출생률 상관관계분석.png" class="img-fluid">
<img src="../static/img/graph/가설1-시간에따른 결혼률과 출산률 추이.png" class="img-fluid">
결혼율과 출산율은 같은 비율로 함께 하락하고 있으며,약 49.8%의 상관관계가 확인되었다.<br>
이는 결혼율 감소가 출산율 감소로 이어지는 구조적 연결 고리로 작용하고 있음을 의미한다.
<hr>
''',
        5: '''
<strong>가설2 :</strong>개인소득의 증가는 자연증가율을 증가시킬 것이다. <br>
<img src="../static/img/graph/가설2-지역별 경제 수준과 출산율의 관계.png" class="img-fluid">
1인당 개인소득이 약 16,000 이상인 시점부터 출산율이 회복되는 경향이 나타났다.<br>
이는 단순한 지원이 아닌, 출산이 가능한 경제적 안정 수준이 중요하다는 점을 시사한다.
<hr>
''',
        6: '''
<strong>가설3 :</strong>수도권의 높은 생활비가 출산 기피로 이어진다 <br>
<img src="../static/img/graph/가설3-출산율표.png" class="img-fluid">
<img src="../static/img/graph/가설3-물가지수그래프.png" class="img-fluid">
수도권과 비수도권 모두 유사한 물가 상승과 출산율 하락을 보여,
지역 간 생활비 격차가 출산율 저하의 결정적 원인은 아님이 드러났다.
<hr>
''',
        7: '''
<strong>가설4 :</strong>20~30대의 높은 실업률이 결혼율 감소에 주요 원인일 것이다 <br>
<img src="../static/img/graph/가설4-20대 결혼율VS실업율 상관관계Heatmap2.png" class="img-fluid">
<img src="../static/img/graph/가설4-30대 결혼율VS실업율 상관관계Heatmap1.png" class="img-fluid">
<img src="../static/img/graph/가설4-20~30대 혼인율VS실업률.png" class="img-fluid">
20대 여성 실업률과 혼인율 간 일부 음의 상관관계가 있었지만, 전체적으로 명확한 인과관계는 없었고 <br>
30대 남성의 경우에도 일시적 패턴에 불과했다.
<br><br>
<img src="../static/img/graph/혼인적령기인구_vs_혼인율_추이.png" class="img-fluid">
가장 구조적인 문제는 혼인 자체가 가능한 인구가 줄어들고 있다는 사실이다.<br>
20~34세 인구는 2001년 약 1,240만 명에서 2024년 약 935만 명으로 급감했고,<br>
이는 과거 출산율 하락이 현재의 혼인 가능 인구 감소로 이어진 구조적 결과다.<br>
이러한 흐름은 단순한 개인의 선택이 아닌, 인구구조적 악순환의 연속이며,<br>
결혼율과 출산율이 함께 감소하는 것은 이미 예견된 수순이었다.<br>
'''
    }
    return jsonify({'html': hypothesis_blocks.get(num, '해당 가설이 없습니다.')})




@app.route('/visualization')
def visualization():
    return render_template('4visualization.html')

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