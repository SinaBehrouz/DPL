from benefactors import app, db
from benefactors.models import Post, PostComment, notificationTypeEnum, Notification, Dplstations, DPLNotification
import datetime



"""
    Notifies all users who have commented on the post

    :param post_id: the post in question (e.g was commented on, volunteered for, etc)
    :param notifier_user_id: id of user who did the action (e.g commented, volunteered, etc)
    :param notification_message: the notification message to be displayed
    :param type: the type of notification it is, helps prevent "duplicate" notifications as to not overload users with the same notification

"""
def notify_commenters(post_id, notifier_user_id,notification_message, type):
    unique_comments = db.session.query(PostComment).filter_by(post_id=post_id).distinct(PostComment.user_id)
    post = Post.query.get_or_404(post_id)
    for comment in unique_comments:
        # don't want to notify the person who made the comment, or the author (author will get notified later)
        if comment.user_id != notifier_user_id and comment.user_id != post.user_id :
            recipient = comment.user_id
            # should be unique combo of: recipient, notifier, post_id, is_read', type
            duplicate = Notification.query.filter_by(recipient=recipient, notifier=notifier_user_id, post_id=post_id, type=type).first()
            if duplicate:
                duplicate.is_read=False
                duplicate.date_created=datetime.datetime.now()
                db.session.commit()
            else:
                notification = Notification(recipient=recipient, notifier=notifier_user_id, post_id=post_id, notification_message=notification_message, is_read=0, type=type)
                db.session.add(notification)
                db.session.commit()


"""
    Notifies user who has volunteered for the post

    :param post_id: the post in question (e.g was commented on)
    :param notifier_user_id: id of user who did the action (e.g commented)
    :param notification_message: the notification message to be displayed
    :param type: the type of notification it is, helps prevent "duplicate" notifications as to not overload users with the same notification

"""
def notify_volunteer(post_id, notifier_user_id, notification_message, type):
    post = Post.query.get_or_404(post_id)
    if post.volunteer and notifier_user_id != post.volunteer:
        recipient = post.volunteer
        duplicate = Notification.query.filter_by(recipient=recipient, notifier=notifier_user_id, post_id=post_id, type=type).first()
        if duplicate:
            duplicate.is_read=False
            duplicate.date_created=datetime.datetime.now()
            db.session.commit()

        else:
            recipient = post.volunteer
            notification = Notification(recipient=recipient, notifier=notifier_user_id, post_id=post_id, notification_message=notification_message, is_read=0, type=type)
            db.session.add(notification)
            db.session.commit()

"""
    Notifies post owner

    :param post_id: the post in question (e.g was commented on)
    :param notifier_user_id: id of user who did the action (e.g commented, volunteered, etc)
    :param notification_message: the notification message to be displayed
    :param type: the type of notification it is, helps prevent "duplicate" notifications as to not overload users with the same notification

"""
def notify_post_owner(post_id, notifier_user_id, notification_message, type):
    post = Post.query.get_or_404(post_id)
    if notifier_user_id != post.user_id:
        recipient = post.user_id
        duplicate = Notification.query.filter_by(recipient=recipient, notifier=notifier_user_id, post_id=post_id, type=type).first()
        if duplicate:
            duplicate.is_read=False
            duplicate.date_created=datetime.datetime.now()
            db.session.commit()
        else:
            notification = Notification(recipient=recipient, notifier=notifier_user_id, post_id=post_id, notification_message=notification_message, is_read=0, type=type)
            db.session.add(notification)
            db.session.commit()
def notify_dpl_owner(notifier , station_id, notification_message, type=0):
    station = db.session.query(Dplstations).filter_by(station_id=station_id).first()
    owner_id = station.owner_id
    notification = DPLNotification(recipient=owner_id, notifier=notifier,notification_message=notification_message, is_read=0)
    db.session.add(notification)
    db.session.commit()
    return True
