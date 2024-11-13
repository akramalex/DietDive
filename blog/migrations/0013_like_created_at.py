from django.db import migrations, models
import django.utils.timezone

class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_remove_post_likes_alter_like_unique_together'),  # Corrected migration dependency
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, auto_now_add=True),
        ),
    ]