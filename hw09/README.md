hw09 에서 해결하지 못했던 부분이 총 3가지가 존재합니다. <hr>
1. css 파일을 읽지 못하여 홈페이지 가장 윗 부분 파란색 배경색이 출력이 안되었던 점
2. js 파일을  읽지 못하여 현재 시간이 출력되지 않았던 점
3. 이미지 파일이 출력이 안되었던 점   <hr>
1~3가지 모두 파일 구조와 경로 참조 파트에서 문제가 있었던 것으로 파악됩니다.  <p>
이를 해결하기 위해서 1,2 번 문제의 경우, <p> src="{% static 'single_pages/js/what_time_is_it.js' %}" 였던 구조를 <p>
src="{% static 'js/what_time_is_it.js' %}"로 변경하였습니다. <p>
3번 문제의 경우, <p> static/siingle_pages/images 로 파일 구조를 하나 더 만들었고, <p>혹시나 있을 에러를 방지하기 위해
모든 이미지 파일을 .jpg로 바꿔주는 작업을 진행했습니다. <p> 또한 몇몇 이미지 파일은 width 설정이 되어 있지 않았던 것 같습니다. <p>
수정본 코드는 파일명 hw09_updated 로 GitHub 저장소에 올려두겠습니다.
 
