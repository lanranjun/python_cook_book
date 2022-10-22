# encoding: utf-8
from operator import methodcaller


def avg(data):
    return sum(data) / len(data)


def drop_first_last(grades):
    first, *middle, last = grades
    return avg(middle)


record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')

name, email, *phone_numbers = record

print(phone_numbers)

*trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]
print(trailing)

records = [
    ('do_foo', 1, 2),
    ('do_bar', 'hello'),
    ('do_foo', 3, 4)
]


def do_foo(x, y):
    print("foo", x, y)


def do_bar(s):
    print("bar", s)


for tag, *args in records:
    locals().get(tag)(*args)

line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(":")
print(uname, homedir, sh)

record = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_, (*_, year) = record
print(name, year)


def sum_iter(items):
    head, *tail = items
    return head + sum_iter(tail) if tail else head


items = [1, 10, 7, 4, 5, 9]
print(sum(items))
