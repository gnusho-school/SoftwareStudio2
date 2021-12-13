# calendar-hyun-server

**BASE\_URL** = [http://server.calendarhyun.com:8000/](http://server.calendarhyun.com:8000/)

**Date Form** = &quot;0000-00-00&quot;

**Time Form** = &quot;00:00&quot; (24시간 기준 -> 오후 3시 = 15:00)

**1. USER**

| **Action + Contents** | **HTTP Method** | **URI** | **Header** | **Body** | **구현 여부** |
| --- | --- | --- | --- | --- | --- |
| User 추가 | POST | user/ | X | uid -> Firebase에서 받아온 값 | O |
| User 전체 정보 가져오기 | GET | user/ | X | X | O |
| User 한 명 정보 가져오기 | GET | user/<string: uid>/ | X | X | O |
| User 한 명 정보 수정 | PUT | user/<string: uid>/ | X | X | O |
| xUser 한 명 삭제 | DEL | user/<string: uid>/ | X | X | O |

**2. SCHEDULE**

| **Action + Contents** | **HTTP Method** | **URI** | **Header** | **Body** | **구현 여부** |
| --- | --- | --- | --- | --- | --- |
| 특정 기간 특정 유저의 스케줄 전부 가져오기 | GET | schedule/ | user -> user pkstart\_date -> date formend\_date -> date form | X | O |
| 일반 스케줄 추가 | POST | shortterm/ | X | title -> stringuser -> user pkdate -> date formstart\_time ->time form (없어도 생성)end\_time -> time form(없어도 생성) | O |
| 일반 스케줄 전체 가져오기 | GET | shortterm/ | user -> user pkstart\_date -> date formend\_date -> date form | X | O |
| 일반 스케줄 하나 가져오기 | GET | shortterm/<int: 스케줄 pk>/ | X | X | O |
| 일반 스케줄 하나 수정 | PUT | shortterm/<int: 스케줄 pk>/ | X | title -> stringuser -> user pkdate -> date formstatus -> char( &#39;D&#39; -> 해결한 스케줄 &#39;F&#39; -> 실패한 스케줄 &#39;O&#39; -> 진행중인 스케줄)start\_time ->time form (없어도 생성)end\_time -> time form(없어도 생성) | O |
| 일반 스케줄 하나 삭제 | DEL | shortterm/<int: 스케줄 pk>/ | X | X | O |
| 기간 스케줄 추가 | POST | longterm/ | X | title -> stringuser -> user pkdate -> date formend\_date -> date form | O |
| 기간 스케줄 전체 가져오기 | GET | longterm/ | user -> user pkstart\_date -> date formend\_date -> date form | X | O |
| 기간 스케줄 하나 가져오기 | GET | longterm/<int: 스케줄 pk>/ | X | X | O |
| 기간 스케줄 하나 수정 | PUT | longterm/<int: 스케줄 pk>/ | X | title -> stringuser -> user pkdate -> date formstatus -> char( &#39;D&#39; -> 해결한 스케줄 &#39;F&#39; -> 실패한 스케줄 &#39;O&#39; -> 진행중인 스케줄)end\_date -> date form | O |
| 기간 스케줄 하나 삭제 | DEL | longterm/<int: 스케줄 pk>/ | X | X | O |
| 반복 스케줄 추가 | POST | repeat/ | X | title -> stringuser -> user pkstart\_date -> date formend\_date -> date formterm -> intstart\_time ->time form (없어도 생성)end\_time -> time form(없어도 생성) |
| 반복 스케줄 전체 가져오기 | GET | repeat/<int: repeat pk>/ | user -> user pkstart\_date -> date formend\_date -> date form | X |
| 반복 스케줄 하나 가져오기 | GET | repeat/<int: repeat pk>/ | user -> user pkstart\_date -> date formend\_date -> date form | X |
| 반복 스케줄 하나 삭제 | DEL | repeat/<int: repeat pk>/ | X | X |
