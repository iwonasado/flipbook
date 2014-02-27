from django.db import models
from django.utils.translation import ugettext_lazy as _
from cms.models import CMSPlugin, Page
from os.path import basename
from django.contrib.auth.models import User
import os

def get_image_path(instance, filename):
    return os.path.join('flipbook', str(instance.usuario.username),str(instance.titulo),'img', filename)

class FlipBook(models.Model):
    # parent = models.ForeignKey('self', blank=True, null=True)
    usuario = models.ForeignKey(User)
    titulo = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    subTitulo = models.CharField(max_length=255,blank=True, null=True)
    texto = models.TextField(_("Texto"),max_length=140,blank=True, null=True, help_text=_("max 140 caracteres"))
    image = models.ImageField(_("Capa"), upload_to=get_image_path,blank=True, null=True)
    logo = models.ImageField(_("Logo"), upload_to=get_image_path,blank=True, null=True)
    demo = models.BooleanField(help_text=_("Demonstration"))

    def __unicode__(self):
        return self.titulo     

def get_image_path_2(instance, filename):
    return os.path.join('flipbook', str(instance.gallery.usuario.username),str(instance.gallery.titulo),'img', filename)  
    
class FlipBookPage(models.Model):
    gallery = models.ForeignKey(FlipBook)
    image = models.ImageField(_("Imagem"), upload_to=get_image_path_2)
    alt = models.CharField(_("Descricao"), max_length=255, blank=True, null=True, help_text=_("Descricao Textual da Imagem"))
    longdesc = models.CharField(_("Discricao Longa"), max_length=255, blank=True, null=True, help_text=_("Descricao Textual adicional da Imagem"))
    zoom = models.BooleanField(help_text=_("Zoom"))
    numero = models.IntegerField(_("Numero da Pagina"))
    def __unicode__(self):
        if self.alt:
            return self.alt[:40]
        elif self.image:
            # added if, because it raised attribute error when file wasn't defined
            try:
                return u"%s" % basename(self.image.path)
            except:
                pass
        return "<empty>"

class FlipBookPlugin(CMSPlugin):
	flipbook = models.ForeignKey(FlipBook)
