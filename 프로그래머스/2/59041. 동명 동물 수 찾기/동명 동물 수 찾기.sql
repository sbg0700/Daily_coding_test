-- 집계 함수의 결과에 조건을 걸면 HAVING
-- 일반 컬럼(행)에 조건을 걸면 WHERE
-- 집계 함수 + 일반 컬럼을 SELECT에 쓰면 GROUP BY 필수


SELECT name,count(name) as COUNT
from animal_ins
having count(name) >= 2
group by name
order by name asc;






