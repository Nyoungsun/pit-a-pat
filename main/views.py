from django.shortcuts import render
from papers.models import Rolling_paper

def main(request):

    paper = None
    paper_list = []
    err_msg = ""

    # 세션에서 메세지 가져오고 세션에 저장된 내용 초기화
    if 'err_msg' in request.session :
        err_msg = request.session['err_msg']
        request.session['err_msg'] = ""
    
    # 전체 롤링페이퍼 중, 마지막으로 만들어진 롤링페이퍼를 보여주는 경우
    if True :
        paper = Rolling_paper.objects.all().order_by("-paper_number").values()
    
    # 본인의 롤링페이퍼를 보여주는 경우
    else :
        paper = Rolling_paper.objects.filter(nickname=request.user.username).order_by("-paper_number").values()
    

    # 내림차순 정렬, 순서대로 9개 선택
    i = 0
    for dic in paper :
        paper_list.append(dic)
        i += 1
    
    context = {
        "papers" : paper_list,
        "err_msg" : err_msg,
    }

    return render(request, 'main/main.html', context)
