# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Article'
        db.create_table('article', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('article_title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('article_text', self.gf('django.db.models.fields.TextField')()),
            ('article_likes', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('article_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('article_user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal('article', ['Article'])

        # Adding model 'Comments'
        db.create_table('comments', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('comments_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('comments_text', self.gf('django.db.models.fields.TextField')()),
            ('comments_article', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['article.Article'])),
            ('comments_user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal('article', ['Comments'])


    def backwards(self, orm):
        # Deleting model 'Article'
        db.delete_table('article')

        # Deleting model 'Comments'
        db.delete_table('comments')


    models = {
        'article.article': {
            'Meta': {'db_table': "'article'", 'object_name': 'Article'},
            'article_date': ('django.db.models.fields.DateTimeField', [], {}),
            'article_likes': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'article_text': ('django.db.models.fields.TextField', [], {}),
            'article_title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'article_user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'article.comments': {
            'Meta': {'db_table': "'comments'", 'object_name': 'Comments'},
            'comments_article': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['article.Article']"}),
            'comments_date': ('django.db.models.fields.DateTimeField', [], {}),
            'comments_text': ('django.db.models.fields.TextField', [], {}),
            'comments_user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'blank': 'True', 'symmetrical': 'False'})
        },
        'auth.permission': {
            'Meta': {'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission', 'ordering': "('content_type__app_label', 'content_type__model', 'codename')"},
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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'blank': 'True', 'symmetrical': 'False', 'related_name': "'user_set'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'blank': 'True', 'symmetrical': 'False', 'related_name': "'user_set'"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'db_table': "'django_content_type'", 'object_name': 'ContentType', 'ordering': "('name',)"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['article']