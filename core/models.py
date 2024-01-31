from django.db import models


class About(models.Model):
    short_description = models.TextField(verbose_name="Descrição Breve")
    description = models.TextField(verbose_name="Descrição Completa")
    image = models.ImageField(upload_to="About", blank=True, null=True)

    class Meta:
        verbose_name = "Sobre mim"
        verbose_name_plural = "Sobre mim"

    def __str__(self):
        return self.short_description


class trajetoria_pessoal(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nome")
    description = models.TextField(verbose_name="Descrição")
    image = models.ImageField(upload_to="trajetoria_pessoal", blank=True, null=True)

    class Meta:
        verbose_name = "Trajetória Pessoal"
        verbose_name_plural = "Trajetória Pessoal"

    def __str__(self):
        return self.name


class trajetoria_profissional(models.Model):
    title = models.CharField(max_length=100, verbose_name="Título")
    description = models.TextField(verbose_name="Descrição")
    image = models.ImageField(upload_to="works", blank=True, null=True)
    link = models.URLField(
        verbose_name="Link", blank=True, null=True
    )  # Adicione este campo

    class Meta:
        verbose_name = "Trajetória Profissional"
        verbose_name_plural = "Trajetória Profissional"

    def __str__(self):
        return self.title


class Certificate(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    pdf_file = models.FileField(upload_to="certificados/")

    class Meta:
        verbose_name = "Certificados"
        verbose_name_plural = "Certificados"

    def __str__(self):
        return self.title
