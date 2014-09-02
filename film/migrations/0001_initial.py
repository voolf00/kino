# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Jenre'
        db.create_table('film_jenre', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('jenre_name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('jenre_title', self.gf('django.db.models.fields.CharField')(max_length=256)),
        ))
        db.send_create_signal('film', ['Jenre'])

        # Adding model 'Status'
        db.create_table('film_status', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('status_film_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal('film', ['Status'])

        # Adding model 'Film'
        db.create_table('film', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('film_name', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('film_created_users', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('film_text', self.gf('django.db.models.fields.TextField')()),
            ('film_year', self.gf('django.db.models.fields.IntegerField')(default=2014)),
            ('film_date_public', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 9, 2, 0, 0))),
            ('film_user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], related_name='film')),
            ('film_award', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('film_like', self.gf('django.db.models.fields.IntegerField')(null=True, default=0, blank=True)),
            ('film_sided_site', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('film_sided_id', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('film_country', self.gf('django.db.models.fields.CharField')(default='', max_length=200)),
            ('film_is_moderator', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('film_image', self.gf('django.db.models.fields.files.ImageField')(blank=True, default='/media/filmImg/default.jpg', max_length=100)),
        ))
        db.send_create_signal('film', ['Film'])

        # Adding model 'Film_comment'
        db.create_table('film_comment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('film_comment_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('film_comment_text', self.gf('django.db.models.fields.TextField')()),
            ('film_comment_link', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['film.Film'])),
            ('film_comment_user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal('film', ['Film_comment'])


    def backwards(self, orm):
        # Deleting model 'Jenre'
        db.delete_table('film_jenre')

        # Deleting model 'Status'
        db.delete_table('film_status')

        # Deleting model 'Film'
        db.delete_table('film')

        # Deleting model 'Film_comment'
        db.delete_table('film_comment')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'object_name': 'Permission', 'unique_together': "(('content_type', 'codename'),)"},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'blank': 'True', 'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True', 'related_name': "'user_set'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True', 'related_name': "'user_set'"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'db_table': "'django_content_type'", 'object_name': 'ContentType', 'unique_together': "(('app_label', 'model'),)"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'film.film': {
            'Meta': {'object_name': 'Film', 'db_table': "'film'"},
            'film_award': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'film_country': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'}),
            'film_created_users': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'film_date_public': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 9, 2, 0, 0)'}),
            'film_image': ('django.db.models.fields.files.ImageField', [], {'blank': 'True', 'default': "'/media/filmImg/default.jpg'", 'max_length': '100'}),
            'film_is_moderator': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'film_like': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'default': '0', 'blank': 'True'}),
            'film_name': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'film_sided_id': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'film_sided_site': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'film_text': ('django.db.models.fields.TextField', [], {}),
            'film_user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'related_name': "'film'"}),
            'film_year': ('django.db.models.fields.IntegerField', [], {'default': '2014'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'film.film_comment': {
            'Meta': {'object_name': 'Film_comment', 'db_table': "'film_comment'"},
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