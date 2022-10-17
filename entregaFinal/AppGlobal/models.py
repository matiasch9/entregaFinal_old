from django.db import models
from django.contrib.auth.models import User
from AppGlobal.choices import tipos
from django.db.models import Max

# Create your models here.
class Blog(models.Model):
   titulo = models.CharField(max_length=30)
   descripcion = models.CharField(max_length=80)
   body = models.TextField()
   publish_date = models.DateTimeField(auto_now_add=True)
   image = models.ImageField(upload_to='imagenes', null = True, blank = True)
   tipo = models.CharField(max_length=12, choices=tipos)
   author= models.ForeignKey(User, on_delete=models.CASCADE, default = '0')
   def __str__(self):
        return str(self.author) +  " Blog titulo: " + self.titulo
   
class Autores(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f"username:{self.username} - email:{email}"

class Avatar(models.Model):
    #vinculo con el usuario
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #subcarpeta Avatares de media
    image = models.ImageField(upload_to='avatares', null = True, blank = True)

# Create for DM.
class Message(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
	sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='from_user')
	recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='to_user')
	body = models.TextField(max_length=1000, blank=True, null=True)
	date = models.DateTimeField(auto_now_add=True)
	is_read = models.BooleanField(default=False)

	def send_message(from_user, to_user, body):
		sender_message = Message(
			user=from_user,
			sender=from_user,
			recipient=to_user,
			body=body,
			is_read=True)
		sender_message.save()

		recipient_message = Message(
			user=to_user,
			sender=from_user,
			body=body,
			recipient=from_user,)
		recipient_message.save()
		return sender_message

	def get_messages(user):
		messages = Message.objects.filter(user=user).values('recipient').annotate(last=Max('date')).order_by('-last')
		users = []
		for message in messages:
			users.append({
				'user': User.objects.get(pk=message['recipient']),
				'last': message['last'],
				'unread': Message.objects.filter(user=user, recipient__pk=message['recipient'], is_read=False).count()
				})
		return users