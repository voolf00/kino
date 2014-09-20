# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Profession'
        db.create_table('profession', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('proffesion_name', self.gf('django.db.models.fields.CharField')(max_length=256)),
        ))
        db.send_create_signal('name', ['Profession'])

        # Adding model 'Name'
        db.create_table('name', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name_first', self.gf('django.db.models.fields.CharField')(blank=True, default='', max_length=256)),
            ('name_last', self.gf('django.db.models.fields.CharField')(blank=True, default='', max_length=256)),
            ('name_sex', self.gf('django.db.models.fields.IntegerField')(blank=True, default=0, max_length=1)),
            ('name_birthday', self.gf('django.db.models.fields.DateField')(blank=True, null=True)),
            ('name_mobile', self.gf('django.db.models.fields.IntegerField')(blank=True, null=True, max_length=30)),
            ('name_website', self.gf('django.db.models.fields.CharField')(blank=True, default='', null=True, max_length=256)),
            ('name_add_user_id', self.gf('django.db.models.fields.related.ForeignKey')(related_name='User', to=orm['auth.User'])),
            ('name_user_id', self.gf('django.db.models.fields.related.ForeignKey')(related_name='user', to=orm['auth.User'], blank=True, null=True)),
        ))
        db.send_create_signal('name', ['Name'])

        # Adding M2M table for field profession on 'Name'
        m2m_table_name = db.shorten_name('name_profession')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('name', models.ForeignKey(orm['name.name'], null=False)),
            ('profession', models.ForeignKey(orm['name.profession'], null=False))
        ))
        db.create_unique(m2m_table_name, ['name_id', 'profession_id'])

        # Adding M2M table for field name_works_id on 'Name'
        m2m_table_name = db.shorten_name('name_name_works_id')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('name', models.ForeignKey(orm['name.name'], null=False)),
            ('film', models.ForeignKey(orm['film.film'], null=False))
        ))
        db.create_unique(m2m_table_name, ['name_id', 'film_id'])


    def backwards(self, orm):
        # Deleting model 'Profession'
        db.delete_table('profession')

        # Deleting model 'Name'
        db.delete_table('name')

        # Removing M2M table for field profession on 'Name'
        db.delete_table(db.shorten_name('name_profession'))

        # Removing M2M table for field name_works_id on 'Name'
        db.delete_table(db.shorten_name('name_name_works_id'))


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'to': "orm['auth.Permission']", 'symmetrical': 'False'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'user_set'", 'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'user_set'", 'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'db_table': "'django_content_type'", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType'},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'film.film': {
            'Meta': {'db_table': "'film'", 'object_name': 'Film'},
            'film_award': ('django.db.models.fields.TextField', [], {'blank': 'True', 'default': "'-'"}),
            'film_country': ('django.db.models.fields.CharField', [], {'default': "'-'", 'max_length': '200'}),
            'film_date_public': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 9, 16, 0, 0)'}),
            'film_english_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '300'}),
            'film_image': ('django.db.models.fields.files.ImageField', [], {'blank': 'True', 'default': "'/media/filmImg/default.jpg'", 'max_length': '100'}),
            'film_is_moderator': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'film_jenres': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'film'", 'to': "orm['film.Jenre']", 'symmetrical': 'False'}),
            'film_like': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'default': '0', 'null': 'True'}),
            'film_money_create': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'default': '0'}),
            'film_name': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'film_sided_id': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'film_sided_site': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'film_status': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['film.Status']", 'default': '2'}),
            'film_text': ('django.db.models.fields.TextField', [], {}),
            'film_user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'film'", 'to': "orm['auth.User']"}),
            'film_year': ('django.db.models.fields.IntegerField', [], {'default': '2014'}),
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
        },
        'name.name': {
            'Meta': {'db_table': "'name'", 'object_name': 'Name'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_add_user_id': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'User'", 'to': "orm['auth.User']"}),
            'name_birthday': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'}),
            'name_first': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '256'}),
            'name_last': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '256'}),
            'name_mobile': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True', 'max_length': '30'}),
            'name_sex': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'default': '0', 'max_length': '1'}),
            'name_user_id': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'user'", 'to': "orm['auth.User']", 'blank': 'True', 'null': 'True'}),
            'name_website': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'null': 'True', 'max_length': '256'}),
            'name_works_id': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'film'", 'to': "orm['film.Film']", 'symmetrical': 'False'}),
            'profession': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'profession'", 'to': "orm['name.Profession']", 'default': "''", 'symmetrical': 'False', 'blank': 'True'})
        },
        'name.profession': {
            'Meta': {'db_table': "'profession'", 'object_name': 'Profession'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'proffesion_name': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        }
    }

    complete_apps = ['name']