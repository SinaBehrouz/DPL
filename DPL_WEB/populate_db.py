from benefactors import db
from benefactors.models import User, Post, PostComment, ChatChannel, ChatMessages, notificationTypeEnum, Notification, Deliveries, Dplstations
import datetime
#will create a new site.db in .benefactors
db.drop_all()
db.create_all();

db.session.add(User(id=0, username="NULL", first_name="NULL", last_name="NULL", email="NULL", phone_number="NULL", postal_code="NULL", password="$2b$12$ppAg.mOnlIo15d0m7gPYr.1LZaUvuO29JVVBkv6bkQzQz6zK.f66y"))
db.session.add(User(id=1,username="SamSmith", first_name="Sam", last_name="Smith", email="samsmith@gmail.com", phone_number="7782234554", postal_code="V3E3B5", password="$2b$12$ppAg.mOnlIo15d0m7gPYr.1LZaUvuO29JVVBkv6bkQzQz6zK.f66y", user_image="b06567b4c614462ab0ec5283d9d8b206.jpg", owner=True))
db.session.add(User(id=2,username="Taylah", first_name="Taylah", last_name="Rosa", email="trosa@yahoo.com", phone_number="6043454565", postal_code="V3E3A7", password="$2b$12$ppAg.mOnlIo15d0m7gPYr.1LZaUvuO29JVVBkv6bkQzQz6zK.f66y", user_image="592d3d0ff7754784b50c7ed0f17dd499.jpg"))
db.session.add(User(id=3,username="Jezzie", first_name="Jess", last_name="Brown", email="jezzie@gmail.com", phone_number="6045557777", postal_code="V3H1L6", password="$2b$12$ppAg.mOnlIo15d0m7gPYr.1LZaUvuO29JVVBkv6bkQzQz6zK.f66y", user_image="ad2f902b324c4aca9284cc97baa73dfa.jpg"))
db.session.add(User(id=4,username="Jackie", first_name="Jacques", last_name="Tang", email="jjques@gmail.com", phone_number="7786562245", postal_code="V5K0A1", password="$2b$12$ppAg.mOnlIo15d0m7gPYr.1LZaUvuO29JVVBkv6bkQzQz6zK.f66y", user_image="744be000d8f94d5e8f44c0b0d83547ff.jpg"))
db.session.add(User(id=5,username="RL", first_name="Randall", last_name="Lowry", email="rrlowry@gmail.com", phone_number="6045001700", postal_code="V1M2R1", password="$2b$12$ppAg.mOnlIo15d0m7gPYr.1LZaUvuO29JVVBkv6bkQzQz6zK.f66y", user_image="afb14fd47ff846efb8b73179275cd531.jpg"))
db.session.add(User(id=6,username="EricH", first_name="Eric", last_name="Singh", email="erichsingh@gmail.com", phone_number="7788787799", postal_code="V3T2E4", password="$2b$12$ppAg.mOnlIo15d0m7gPYr.1LZaUvuO29JVVBkv6bkQzQz6zK.f66y", user_image="02173210948342908c4e4087551747e7.jpg"))
db.session.add(User(id=7, username="Arsalan", first_name="Arsalan", last_name="Mackie", email="1@1.com", phone_number="7786637867", postal_code="V6B0M3", password="$2b$12$ppAg.mOnlIo15d0m7gPYr.1LZaUvuO29JVVBkv6bkQzQz6zK.f66y"))
db.session.commit()


db.session.add(Dplstations(city="Coquitlam", address="1575 Warbler Lane", total_lockers=4, lockers_available=4, postal_code="V3E3B5", owner_id=1))
db.session.commit()

db.session.add(Deliveries(tracking_number="123123123", status=1, passcode="123456789", to_customer=7, title="Apple Air pods"))
db.session.add(Deliveries(tracking_number="123123124", status=1, passcode="123456789", to_customer=7, title="Ps5 from amazon"))
db.session.add(Deliveries(tracking_number="123123125", status=1, passcode="123456789", to_customer=7, title="mac book"))
db.session.add(Deliveries(tracking_number="123123126", status=1, passcode="123456789", to_customer=7, title="Janice's laptop"))

db.session.commit()


db.session.add(Post(title="A little help with Cleaning", category="CLEANING", status="OPEN", description="I will not be home next Saturday at August 17th, and I would really glad if someone could help clean my house interiors and take care of my two cute dogs for few hours. The task will mostly be vacuuming and sweeping the the living room, play with the dogs, and feed the dogs. It will be a fun experience, I promise you. For anyone who is interested or have any more questions, please message me.", user_id=3))
db.session.add(Post(title="Mount TV and Assemble Furniture", category="LABOUR", status="OPEN", description="Would really appreciate if someone can assist me in mounting up the TV and assemble a sofa-bed. I will have to prepare my open-house dinner and do not really have time to polish my living house because of the virus.", user_id=5))
db.session.add(Post(title="Bi-weekly Groceries Run", category="GROCERY", status="TAKEN", description="I would need someone to help me with my bi-weekly groceries to the nearest store. I would like to know where you live as well because I prefer someone who lives close to me. The groceries that I am buying are mostly food like canned food, meat, fresh vegetables, fruits, sometimes paper towel and toilet paper.  A little background on myself, I have grow old these last few days, and I am really scared of going out right now. I would appreciate if someone is kind enough and spend their time to help me with this simple task. Thank you to you all.", user_id=2, volunteer=6, date_posted=datetime.datetime(2020,7,31,10,0,0)))
db.session.add(Post(title="Need to Get My Medications A.S.A.P", category="MEDICATION", status="TAKEN", description="I'm in no condition to go out to my local pharmacy, and I would really appreciate if someone could buy them up for me. The medication I would like to buy are Tylenols, and maybe along with medical masks and hand sanitizers if they still exist on local store. I do really need them soon because I need to go work everyday using a bus, and I am risking myself everyday without mask and surgical mask.", user_id=2, volunteer=1))
db.session.add(Post(title="Need an extra hand or two to MOVE", category="MOVING", status="CLOSED", description="Hey it's the end of the month, and I am getting kicked out of my apartment. I would need someone that can drive a U-Haul truck to bring my furnitures, stuffs, and shoes. This is because I cannot drive and I have no money. Thank you for the help!", user_id=4, date_posted=datetime.datetime(2020,7,30,11,25,0)))
db.session.add(Post(title="Need Help Getting My Groceries", category="GROCERY", status="TAKEN", description="I am need in need of getting groceries this week. I am not feeling that great this week, and do not think I should be going into public spaces. I would really appreciate it if someone could help me out.", user_id=2, volunteer=3, date_posted=datetime.datetime(2020,7,31,10,0,0)))

db.session.commit()

db.session.add(PostComment(comment_desc="Hi I am interested in helping, and I have sent you a message regarding the details of the task", user_id=6, post_id=3, date_posted=datetime.datetime(2020,8,1,11,6,0)))
db.session.add(PostComment(comment_desc="Thanks everyone, but I've been helped. Closing this post soon", user_id=2, post_id=3, date_posted=datetime.datetime(2020,8,2,15,20,55)))
db.session.add(PostComment(comment_desc="Hi I just saw this post and see this post is still open, do you still need help?", user_id=7, post_id=3, date_posted=datetime.datetime(2020,8,9,22,25,30)))
db.session.add(PostComment(comment_desc="Closing this post as I used an uber driver to move instead, I needed to move on July 31st!!", user_id=4, post_id=5, date_posted=datetime.datetime(2020,8,1,22,44,45)))
db.session.add(PostComment(comment_desc="Hi, I'm interested in helping out! When do you need this done by?", user_id=1, post_id=1, date_posted=datetime.datetime(2020,8,9,22,25,30)))
db.session.add(PostComment(comment_desc="I work at a grocery store, and can for sure help get your groceries for you!", user_id=4, post_id=1, date_posted=datetime.datetime(2020,8,9,22,25,30)))
db.session.add(PostComment(comment_desc="I can help, I sent you a message about it!", user_id=5, post_id=1, date_posted=datetime.datetime(2020,8,9,22,25,30)))

db.session.commit()

db.session.add(Notification(recipient=3, notifier=1, post_id=1, notification_message="SamSmith commented on your post.", is_read=0, type=notificationTypeEnum.COMMENT))
db.session.add(Notification(recipient=3, notifier=4, post_id=1, notification_message="Jackie commented on your post.", is_read=0, type=notificationTypeEnum.COMMENT))
db.session.add(Notification(recipient=3, notifier=5, post_id=1, notification_message="RL commented on your post.", is_read=0, type=notificationTypeEnum.COMMENT))


db.session.add(ChatChannel(user1_id=2, user2_id=6, last_updated=datetime.datetime(2020,8,1,12,5,30)))
db.session.add(ChatChannel(user1_id=1, user2_id=3, last_updated=datetime.datetime(2020,8,11,19,35,22)))
db.session.add(ChatChannel(user1_id=2, user2_id=3, last_updated=datetime.datetime(2020,8,8,18,5,30)))

db.session.commit()

db.session.add(ChatMessages(sender_id=6, message_content="Hi Taylah, My name is Eric. I just check your post on bi-weekly groceries run, and I am willing to help. Where do you live?", channel_id=1, message_time=datetime.datetime(2020,8,1,11,5,30)))
db.session.add(ChatMessages(sender_id=2, message_content="Hi Eric, I live at apartment across from Langara Station, the nearest grocery is T&T or Safeway around Oakridge area.", channel_id=1, message_time=datetime.datetime(2020,8,1,12,6,21)))
db.session.add(ChatMessages(sender_id=6, message_content="Oh perfect!! I would probably go more often to Safeway if that's okay with you, but I can go to T&T as well. When do you want to start and what do you want to deliver?", channel_id=1, message_time=datetime.datetime(2020,8,1,12,25,45)))
db.session.add(ChatMessages(sender_id=2, message_content="For this week, I would like to get eggs, gluten-free bread (Please make sure it's gluten free), and 2% Milk. I will pay you for sure through interac. Can I get your email, please?", channel_id=1, message_time=datetime.datetime(2020,8,1,13,26,44)))
db.session.add(ChatMessages(sender_id=6, message_content="Great! I will deliver it to you tomorrow morning from Safeway, if that's okay. ", channel_id=1, message_time=datetime.datetime(2020,8,1,16,27,22)))
db.session.add(ChatMessages(sender_id=2, message_content="Sounds great, see you tomorrow morning" , channel_id=1, message_time=datetime.datetime(2020,8,1,16,45,11)))
db.session.add(ChatMessages(sender_id=6, message_content="Hi Taylah, am outside your apartment with your groceries. My email is My email is haymond@gmail.com. It is around 24.3, you can check the receipt later.", channel_id=1, message_time=datetime.datetime(2020,8,2,9,33,33)))
db.session.add(ChatMessages(sender_id=2, message_content="Already? Thank you so much, Eric. I am heading down right now" , channel_id=1, message_time=datetime.datetime(2020,8,2,9,35,22)))
db.session.add(ChatMessages(sender_id=1, message_content="Hi Ms. Brown. My name is Sam, I am interested and available to help you on the 17th." , channel_id=2, message_time=datetime.datetime(2020,8,10,8,15,22)))
db.session.add(ChatMessages(sender_id=3, message_content="Oh hey there! Yes please, I live around North Van near Lonsdale Quay terminal" , channel_id=2, message_time=datetime.datetime(2020,8,10,8,35,22)))
db.session.add(ChatMessages(sender_id=1, message_content="Sounds good what do I need to bring?" , channel_id=2, message_time=datetime.datetime(2020,8,10,9,15,22)))
db.session.add(ChatMessages(sender_id=3, message_content="Just a lot of patience, the dog can be woeful sometimes. Anyway, have fun! I will leave the door open as my neighbourhood is very safe anyway. My address is #### 6th Street East" , channel_id=2, message_time=datetime.datetime(2020,8,10,9,35,22)))
db.session.add(ChatMessages(sender_id=1, message_content="It seems like I will have a great time" , channel_id=2, message_time=datetime.datetime(2020,8,11,18,35,22)))
db.session.add(ChatMessages(sender_id=3, message_content="Thank you!" , channel_id=2, message_time=datetime.datetime(2020,8,11,19,35,22)))
db.session.add(ChatMessages(sender_id=3, message_content="Hi Taylah, how are you doing?" , channel_id=2, message_time=datetime.datetime(2020,8,8,18,5,30)))

db.session.commit()
