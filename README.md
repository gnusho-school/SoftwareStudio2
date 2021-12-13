# calendar-hyun-server

**BASE\_URL** = [http://server.calendarhyun.com:8000/](http://server.calendarhyun.com:8000/)

**Date Form** = &quot;0000-00-00&quot;

**Time Form** = &quot;00:00&quot; (24시간 기준 -\&gt; 오후 3시 = 15:00)

**1. USER**

| **Action + Contents** | **HTTP Method** | **URI** | **Header** | **Body** | **구현 여부** |
| --- | --- | --- | --- | --- | --- |
| User 추가 | POST | user/ | X | uid -\&gt; Firebase에서 받아온 값 | O |
| User 전체 정보 가져오기 | GET | user/ | X | X | O |
| User 한 명 정보 가져오기 | GET | user/\&lt;string: uid\&gt;/ | X | X | O |
| User 한 명 정보 수정 | PUT | user/\&lt;string: uid\&gt;/ | X | X | O |
| xUser 한 명 삭제 | DEL | user/\&lt;string: uid\&gt;/ | X | X | O |

**2. SCHEDULE**

| **Action + Contents** | **HTTP Method** | **URI** | **Header** | **Body** | **구현 여부** |
| --- | --- | --- | --- | --- | --- |
| 특정 기간 특정 유저의 스케줄 전부 가져오기 | GET | schedule/ | user -\&gt; user pkstart\_date -\&gt; date formend\_date -\&gt; date form | X | O |
| 일반 스케줄 추가 | POST | shortterm/ | X | title -\&gt; stringuser -\&gt; user pkdate -\&gt; date formstart\_time -\&gt;time form (없어도 생성)end\_time -\&gt; time form(없어도 생성) | O |
| 일반 스케줄 전체 가져오기 | GET | shortterm/ | user -\&gt; user pkstart\_date -\&gt; date formend\_date -\&gt; date form | X | O |
| 일반 스케줄 하나 가져오기 | GET | shortterm/\&lt;int: 스케줄 pk\&gt; | X | X | O |
| 일반 스케줄 하나 수정 | PUT | shortterm/\&lt;int: 스케줄 pk\&gt; | X | title -\&gt; stringuser -\&gt; user pkdate -\&gt; date formstatus -\&gt; char( &#39;D&#39; -\&gt; 해결한 스케줄 &#39;F&#39; -\&gt; 실패한 스케줄 &#39;O&#39; -\&gt; 진행중인 스케줄)start\_time -\&gt;time form (없어도 생성)end\_time -\&gt; time form(없어도 생성) | O |
| 일반 스케줄 하나 삭제 | DEL | shortterm/\&lt;int: 스케줄 pk\&gt; | X | X | O |
| 기간 스케줄 추가 | POST | longterm/ | X | title -\&gt; stringuser -\&gt; user pkdate -\&gt; date formstatus -\&gt; char( &#39;D&#39; -\&gt; 해결한 스케줄 &#39;F&#39; -\&gt; 실패한 스케줄 &#39;O&#39; -\&gt; 진행중인 스케줄)end\_date -\&gt; date form | O |
| 기간 스케줄 전체 가져오기 | GET | longterm/ | user -\&gt; user pkstart\_date -\&gt; date formend\_date -\&gt; date form | X | O |
| 기간 스케줄 하나 가져오기 | GET | longterm/\&lt;int: 스케줄 pk\&gt; | X | X | O |
| 기간 스케줄 하나 수정 | PUT | longterm/\&lt;int: 스케줄 pk\&gt; | X | title -\&gt; stringuser -\&gt; user pkdate -\&gt; date formstatus -\&gt; char( &#39;D&#39; -\&gt; 해결한 스케줄 &#39;F&#39; -\&gt; 실패한 스케줄 &#39;O&#39; -\&gt; 진행중인 스케줄)end\_date -\&gt; date form | O |
| 기간 스케줄 하나 삭제 | DEL | longterm/\&lt;int: 스케줄 pk\&gt; | X | X | O |
