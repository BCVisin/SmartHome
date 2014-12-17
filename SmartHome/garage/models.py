from django.db import models

class garage(models.Model):

	class Meta:
		permissions = (
			("view", "view"),
			("trigger", "trigger"),
		)
