from ..models import Classroom, Forum, Post, Exam


def create_new_classroom(lesson, grade, class_num, teacher, description=None):
    if description:
        classroom = Classroom(lesson=lesson, grade=grade, class_num=class_num, teacher=teacher)
    else:
        classroom = Classroom(lesson=lesson, grade=grade, class_num=class_num, teacher=teacher, description=description)
    classroom.save()


def add_student_to_classroom(classroom, student):
    student.classrooms_as_student.add(classroom)


def create_forum(title, classroom, description=None):
    if description:
        forum = Forum(title=title, classroom=classroom)
    else:
        forum = Forum(title=title, classroom=classroom, description=description)
    forum.save()


def create_post(content, author, forum):
    post = Post(content=content, author=author, forum=forum)
    # todo check some consistency to see if author is a member of the forum
    post.save()


def create_exam(title, exam_file, classroom, description=None):
    if description:
        exam = Exam(title=title, exam_file=exam_file, classroom=classroom, description=description)
    else:
        exam = Exam(title=title, exam_file=exam_file, classroom=classroom)
    exam.save()


# todo implement condition in which user is a teacher of admin. For now we assume user to be a student
def get_classrooms(user):
    return user.classrooms_as_student.all()


def get_forums(classroom):
    return classroom.forum_set.all()


def get_exams(classroom):
    return classroom.exam_set.all()


def get_posts(forum):
    return sorted(forum.posts_set.all(), key=lambda x: x.date_posted())

