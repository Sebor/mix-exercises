/*
Имеется таблица something:

something [ id, ..., date ]

Необходимо написать SQL-запрос, который удалит из данной таблицы все записи,
кроме 5ти записей, имеющих самую свежую дату (date).
*/

DELETE FROM something
WHERE date NOT IN (
    SELECT date FROM something
    ORDER BY date DESC
    LIMIT 5
)
