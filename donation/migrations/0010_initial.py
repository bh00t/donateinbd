# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'UserProfile'
        db.create_table(u'donation_userprofile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('contact_no', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
            ('street_no', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
            ('street_address', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
            ('country', self.gf('django.db.models.fields.CharField')(default='Bangladesh', max_length=40, null=True, blank=True)),
            ('donor_donee_type', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('occupation', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
            ('website', self.gf('django.db.models.fields.CharField')(max_length=400, null=True, blank=True)),
            ('donation_make_count', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('donation_take_count', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'donation', ['UserProfile'])

        # Adding model 'Post'
        db.create_table(u'donation_post', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['donation.UserProfile'])),
            ('post_header', self.gf('django.db.models.fields.TextField')()),
            ('post_detail', self.gf('django.db.models.fields.TextField')()),
            ('post_date', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('post_type', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('post_amount', self.gf('django.db.models.fields.TextField')()),
            ('post_sector', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('post_donation_type', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('post_donation_method', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('post_rating', self.gf('django.db.models.fields.IntegerField')(default=5)),
            ('verified', self.gf('django.db.models.fields.CharField')(default='unverified', max_length=100)),
        ))
        db.send_create_signal(u'donation', ['Post'])

        # Adding model 'Message'
        db.create_table(u'donation_message', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sender', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('receiver', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('sender_full_name', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('event_time', self.gf('django.db.models.fields.TimeField')(auto_now=True, blank=True)),
            ('file', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True)),
        ))
        db.send_create_signal(u'donation', ['Message'])

        # Adding model 'ProfileFeedback'
        db.create_table(u'donation_profilefeedback', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('message', self.gf('django.db.models.fields.TextField')()),
            ('feedback_sender', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('event_time', self.gf('django.db.models.fields.TimeField')(auto_now=True, blank=True)),
            ('verified', self.gf('django.db.models.fields.CharField')(default='unverified', max_length=100)),
        ))
        db.send_create_signal(u'donation', ['ProfileFeedback'])

        # Adding model 'PostFeedback'
        db.create_table(u'donation_postfeedback', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('post', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['donation.Post'])),
            ('message', self.gf('django.db.models.fields.TextField')()),
            ('feedback_sender', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('event_time', self.gf('django.db.models.fields.TimeField')(auto_now=True, blank=True)),
            ('verified', self.gf('django.db.models.fields.CharField')(default='unverified', max_length=100)),
        ))
        db.send_create_signal(u'donation', ['PostFeedback'])

        # Adding model 'WorkingProject'
        db.create_table(u'donation_workingproject', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('post', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['donation.Post'])),
            ('status', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'donation', ['WorkingProject'])

        # Adding model 'Report'
        db.create_table(u'donation_report', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('working_project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['donation.Post'])),
            ('profile', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['donation.UserProfile'])),
            ('file', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('event_time', self.gf('django.db.models.fields.TimeField')(auto_now=True, blank=True)),
            ('header', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True)),
            ('additional_info', self.gf('django.db.models.fields.TextField')(null=True)),
        ))
        db.send_create_signal(u'donation', ['Report'])


    def backwards(self, orm):
        # Deleting model 'UserProfile'
        db.delete_table(u'donation_userprofile')

        # Deleting model 'Post'
        db.delete_table(u'donation_post')

        # Deleting model 'Message'
        db.delete_table(u'donation_message')

        # Deleting model 'ProfileFeedback'
        db.delete_table(u'donation_profilefeedback')

        # Deleting model 'PostFeedback'
        db.delete_table(u'donation_postfeedback')

        # Deleting model 'WorkingProject'
        db.delete_table(u'donation_workingproject')

        # Deleting model 'Report'
        db.delete_table(u'donation_report')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'donation.message': {
            'Meta': {'object_name': 'Message'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'event_time': ('django.db.models.fields.TimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'receiver': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'sender': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'sender_full_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        u'donation.post': {
            'Meta': {'object_name': 'Post'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'post_amount': ('django.db.models.fields.TextField', [], {}),
            'post_date': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'post_detail': ('django.db.models.fields.TextField', [], {}),
            'post_donation_method': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'post_donation_type': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'post_header': ('django.db.models.fields.TextField', [], {}),
            'post_rating': ('django.db.models.fields.IntegerField', [], {'default': '5'}),
            'post_sector': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'post_type': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['donation.UserProfile']"}),
            'verified': ('django.db.models.fields.CharField', [], {'default': "'unverified'", 'max_length': '100'})
        },
        u'donation.postfeedback': {
            'Meta': {'object_name': 'PostFeedback'},
            'event_time': ('django.db.models.fields.TimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'feedback_sender': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'post': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['donation.Post']"}),
            'verified': ('django.db.models.fields.CharField', [], {'default': "'unverified'", 'max_length': '100'})
        },
        u'donation.profilefeedback': {
            'Meta': {'object_name': 'ProfileFeedback'},
            'event_time': ('django.db.models.fields.TimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'feedback_sender': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'verified': ('django.db.models.fields.CharField', [], {'default': "'unverified'", 'max_length': '100'})
        },
        u'donation.report': {
            'Meta': {'object_name': 'Report'},
            'additional_info': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'event_time': ('django.db.models.fields.TimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True'}),
            'header': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'profile': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['donation.UserProfile']"}),
            'working_project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['donation.Post']"})
        },
        u'donation.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'contact_no': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'default': "'Bangladesh'", 'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'donation_make_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'donation_take_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'donor_donee_type': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'occupation': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'street_address': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'street_no': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'}),
            'website': ('django.db.models.fields.CharField', [], {'max_length': '400', 'null': 'True', 'blank': 'True'})
        },
        u'donation.workingproject': {
            'Meta': {'object_name': 'WorkingProject'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'post': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['donation.Post']"}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        }
    }

    complete_apps = ['donation']