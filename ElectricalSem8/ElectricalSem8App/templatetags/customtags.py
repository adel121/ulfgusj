from django import template
import datetime
import string

register = template.Library()


def fixVideo(video):
	if "embed" in video.Youtube:
		return ""
	else:
		video.Youtube = "https://youtube.com/embed/"+video.Youtube[17:]
		video.Drive="https://drive.google.com/uc?export=download&id="+video.Drive.split('/')[5]
		video.save()
		return ""

def fixDoc(document):
	if "uc?export=download&id=" in document.Drive:
		return ""
	else:
		document.Drive="https://drive.google.com/uc?export=download&id="+document.Drive.split('/')[5]
		document.save()
		return ""


register.filter('fixVideo',fixVideo)
register.filter('fixDoc',fixDoc)