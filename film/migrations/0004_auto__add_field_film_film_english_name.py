# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Film.film_english_name'
        db.add_column('film', 'film_english_name',
                      self.gf('django.db.models.fields.CharField')(max_length=300, default=''),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Film.film_english_name'
        db.delete_column('film', 'film_english_name')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80', 'unique': 'True'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'symmetrical': 'False', 'to': "orm['auth.Permission']"})
        },
        'auth.permission': {
            'Meta': {'unique_together': "(('content_type', 'codename'),)", 'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'user_set'", 'symmetrical': 'False', 'to': "orm['auth.Group']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'user_set'", 'symmetrical': 'False', 'to': "orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '30', 'unique': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'ordering': "('name',)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'film.aboutcreatedusers': {
            'Meta': {'db_table': "'about_created_users'", 'object_name': 'AboutCreatedUsers'},
            'film_actors': ('django.db.models.fields.TextField', [], {'default': "'-'"}),
            'film_compozitor': ('django.db.models.fields.CharField', [], {'max_length': '256', 'default': "'-'"}),
            'film_id': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['film.Film']"}),
            'film_montaj': ('django.db.models.fields.CharField', [], {'max_length': '256', 'default': "'-'"}),
            'film_produsser': ('django.db.models.fields.CharField', [], {'max_length': '256', 'default': "'-'"}),
            'film_rejisser': ('django.db.models.fields.CharField', [], {'max_length': '256', 'default': "'-'"}),
            'film_scenarii': ('django.db.models.fields.CharField', [], {'max_length': '256', 'default': "'-'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'film.film': {
            'Meta': {'db_table': "'film'", 'object_name': 'Film'},
            'film_award': ('django.db.models.fields.TextField', [], {'blank': 'True', 'default': "'-'"}),
            'film_country': ('django.db.models.fields.CharField', [], {'max_length': '200', 'default': "'-'"}),
            'film_date_public': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 9, 5, 0, 0)'}),
            'film_english_name': ('django.db.models.fields.CharField', [], {'max_length': '300', 'default': "''"}),
            'film_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True', 'default': "'/media/filmImg/default.jpg'"}),
            'film_is_moderator': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'film_jenres': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'film'", 'symmetrical': 'False', 'to': "orm['film.Jenre']"}),
            'film_like': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True', 'default': '0'}),
            'film_money_create': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'default': '0'}),
            'film_name': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'film_sided_id': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'film_sided_site': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'film_status': ('django.db.models.fields.related.ForeignKey', [], {'default': '2', 'to': "orm['film.Status']"}),
            'film_text': ('django.db.models.fields.TextField', [], {}),
            'film_user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'film'", 'to': "orm['auth.User']"}),
            'film_year': ('django.db.models.fields.IntegerField', [], {'default': '2014'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'film.film_comment': {
            'Meta': {'db_table': "'film_comment'", 'object_name': 'Film_comment'},
            'film_comment_date': ('django.db.models.fields.DateTimeField', [], {}),
            'film_comment_link': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['film.Film']"}),
            'film_comment_text': ('django.db.models.fields.TextField', [], {}),
            'film_comment_user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'film.jenre': {
            'Meta': {'object_name': 'Jenre'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jenre_name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'jenre_title': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        'film.status': {
            'Meta': {'object_name': 'Status'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'status_film_name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['film']