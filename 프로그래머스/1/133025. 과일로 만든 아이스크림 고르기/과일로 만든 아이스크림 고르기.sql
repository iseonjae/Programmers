-- 코드를 입력하세요
SELECT fh.FLAVOR 
FROM FIRST_HALF AS fh
JOIN ICECREAM_INFO as ii
on fh.flavor = ii.flavor
where fh.total_order > 3000
 and ii.ingredient_type = 'fruit_based'
order by fh.total_order desc;