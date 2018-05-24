
# Create 3 different user accounts
In [8]: u = User.objects.create(first_name="Harry", last_name="Potter", email="hp@gmail.com")
In [9]: u.save()
In [10]: u = User.objects.create(first_name="Ron", last_name="Weasley", email="rw@gmail.com")
In [11]: u.save()
In [12]: u = User.objects.create(first_name="Hermione", last_name="Granger", email="hg@gmail.com")
In [13]: u.save()

# Have the first user create/upload 2 books.
In [14]: u = User.objects.get(name="Harry")

In [16]: Book.objects.create(name="book 1", desc="akjhjkad", uploader=u)
Out[16]: <Blog object: Title: book 1, Description: akjhjkad>
In [17]: Book.objects.create(name="book 2", desc="aasdadasdhjkad", uploader=u)
Out[17]: <Blog object: Title: book 2, Description: aasdadasdhjkad>
In [17]: Book.objects.create(name="book 3", desc="aasdadasdhjkad", uploader=u)
Out[17]: <Blog object: Title: book 2, Description: aasdadasdhjkad>


# Have the second user create/upload 2 other books.
In [18]: u = User.objects.get(name="Ron")

In [20]: Book.objects.create(name="book 4", desc="as3441dasdakjhjkad", uploader=u)
Out[20]: <Blog object: Title: book 4, Description: as3441dasdakjhjkad>
In [21]: Book.objects.create(name="book 5", desc="as3441dasdakjhjkad", uploader=u)
Out[21]: <Blog object: Title: book 5, Description: as3441dasdakjhjkad>

# Have the third user create/upload 2 other books.
In [22]: u = User.objects.get(first_name="Hermione")
Out[23]: <Blog object: first_name:Hermione, last_name:Granger, email:hg@gmail.com>
In [24]: Book.objects.create(name="book 6", desc="as3441dasdakjhjkad", uploader=u)
Out[24]: <Blog object: Title: book 6, Description: as3441dasdakjhjkad>
In [25]: Book.objects.create(name="book 7", desc="as3441dasdakjhjkad", uploader=u)
Out[25]: <Blog object: Title: book 7, Description: as3441dasdakjhjkad>

# Have the first user like the last book and the first book
In [29]: u = User.objects.first()
In [30]: b_last = Book.objects.last()
In [31]: b_first = Book.objects.first()
In [35]: u.liked_books.add(b_first)
In [36]: u
Out[36]: <Blog object: first_name:Harry, last_name:Potter, email:hp@gmail.com>
In [37]: u.liked_books.add(b_last)
In [38]: u
Out[38]: <Blog object: first_name:Harry, last_name:Potter, email:hp@gmail.com>

# Have the second user like the first book and the third book
In [45]: b_first
Out[45]: <Blog object: Title: book 1, Description: akjhjkad>

In [46]: b_third
Out[46]: <Blog object: Title: book 3, Description: as3441dasdakjhjkad>
In [48]: u.liked_books.add(b_first, b_third)
In [49]: u
Out[49]: <Blog object: first_name:Ron, last_name:Weasley, email:rw@gmail.com>

# Have the third user like all books
In [54]: u.liked_books.add(*Book.objects.all())

# Display all users who like the first book
In [56]: u = User.objects.filter(liked_books=27)

In [57]: u
Out[57]: <QuerySet [<Blog object: first_name:Harry, last_name:Potter, email:hp@gmail.com>, <Blog object: first_name:Ron, last_name:Weasley, email:rw@gmail.com>, <Blog object: first_name:Hermione, last_name:Granger, email:hg@gmail.com>]>


# Display the user who uploaded the first book
In [58]: u = Book.objects.first().uploader_id
In [59]: u
Out[59]: 14
# Display all users who like the second book

In [61]: u = User.objects.filter(liked_books=28)

In [62]: u
Out[62]: <QuerySet [<Blog object: first_name:Hermione, last_name:Granger, email:hg@gmail.com>]>

# Display the user who uploaded the second book
In [64]: u = Book.objects.get(id=28).uploader_id

In [65]: u
Out[65]: 14