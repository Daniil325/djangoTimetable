from django.db import models
from slugify import slugify


class Faculty(models.Model):
    name = models.CharField("Факультет", max_length=255)
    slug = models.SlugField(max_length=255, allow_unicode=True)

    class Meta:
        verbose_name = "Факультет"
        verbose_name_plural = 'Факультеты'
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Department(models.Model):
    name = models.CharField("Кафедра", max_length=255)
    slug = models.SlugField(max_length=255, allow_unicode=True)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, verbose_name="Факультет",
                                related_name='faculty_content_type')

    class Meta:
        verbose_name = "Кафедра"
        verbose_name_plural = 'Кафедры'
        ordering = ['name']

    def __str__(self):
        return f"{self.name}, {self.faculty.name}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class Teacher(models.Model):
    name = models.CharField("ФИО", max_length=255)
    slug = models.SlugField(max_length=255, allow_unicode=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name='Кафедра',
                                   related_name='departments')

    class Meta:
        verbose_name = "Преподаватель"
        verbose_name_plural = 'Преподаватели'
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class Group(models.Model):
    name = models.CharField("Группа", max_length=255)
    slug = models.SlugField(max_length=255, allow_unicode=True)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, verbose_name="Факультет", related_name='faculties')

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = 'Группы'
        ordering = ['name']

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField("Предмет", max_length=255)
    slug = models.SlugField(max_length=255, allow_unicode=True)

    class Meta:
        verbose_name = "Предмет"
        verbose_name_plural = 'Предметы'
        ordering = ['name']

    def __str__(self):
        return self.name


class Audience(models.Model):
    name = models.CharField("Аудитория", max_length=255)
    slug = models.SlugField(max_length=255, allow_unicode=True)

    class Meta:
        verbose_name = "Аудитория"
        verbose_name_plural = 'Аудитории'
        unique_together = ['name']

    def __str__(self):
        return self.name


class TypeClass(models.Model):
    name = models.CharField("Вид занятия", max_length=255)
    slug = models.SlugField(max_length=255, allow_unicode=True)

    class Meta:
        verbose_name = "Вид занятия"
        verbose_name_plural = 'Виды занятий'

    def __str__(self):
        return self.name


class TimeClass(models.Model):
    name = models.CharField("Время занятия", max_length=255)
    slug = models.SlugField(max_length=255, allow_unicode=True)

    class Meta:
        verbose_name = "Время занятия"
        verbose_name_plural = 'Время занятий'

    def __str__(self):
        return self.name


class Employment(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name="Преподаватель",
                                related_name='teachers')
    group = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name="Группа", related_name='groups')
    audience = models.ForeignKey(Audience, on_delete=models.CASCADE, verbose_name="Аудитория", related_name='audiences')
    type_class = models.ForeignKey(TypeClass, on_delete=models.CASCADE, verbose_name="Вид занятия",
                                   related_name='types_classes')
    time_class = models.ForeignKey(TimeClass, on_delete=models.CASCADE, verbose_name="Время занятия",
                                   related_name='times_classes')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name="Предмет", related_name='subjects')
    date = models.DateField("Дата")
    num_week = models.IntegerField("Номер недели", null=True, blank=True)

    class Meta:
        verbose_name = "Занятие"
        verbose_name_plural = 'Занятия'
        unique_together = ['teacher', 'time_class', 'date']

    def save(self, *args, **kwargs):
        dt = self.date
        self.num_week = dt.isocalendar()[1]
        super().save(*args, **kwargs)