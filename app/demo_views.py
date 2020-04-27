from app import app,db
from flask import request,jsonify,make_response,redirect, render_template,flash,url_for,session

from app.forms import RegistrationForm,LoginForm

from flask_login import current_user, login_user,logout_user,login_required
from app.database.models import User,UploadedVideo,MergedAdCategory,VideoAnalyticsFile
# from app.utils.ad_prediction import get_appropriate_adids
# from app.utils.dataUtilsCode import dynamicJsonFile
# from sqlalchemy import exists,or_
# from sqlalchemy import in_
from sqlalchemy.sql.expression import func

@app.route('/login', methods=["GET", "POST"])
def login():
	if current_user.is_authenticated:
		# return redirect(url_for('home'))
		return redirect(app.config["BASE_URL_WITH_PORT"]+"/home")

	form = LoginForm()
	if form.validate_on_submit():
		try:
			user = User.query.filter_by(email=form.email.data).first()
			if user is None or not user.check_password(form.password.data):
				flash('Invalid username or password')
				return redirect(url_for('login'))
			login_user(user, remember=True,duration=app.config["REMEMBER_COOKIE_DURATION"])
			# return redirect(url_for('home'))
			return redirect(app.config["BASE_URL_WITH_PORT"]+"/home")
		except Exception as err:
			# flash(err)
			flash("Problem while logging in.")
	return render_template('demo_views/login.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
	if current_user.is_authenticated:
		# return redirect(url_for('home'))
		return redirect(app.config["BASE_URL_WITH_PORT"]+"/home")
	form = RegistrationForm()

	if request.method=="GET":
		return render_template('demo_views/register.html', form=form)

	if request.method=="POST":
		if form.validate_on_submit():
			try:
				user = User(username=form.username.data, email=form.email.data)
				user.set_password(form.password.data)
				db.session.add(user)
				db.session.commit()
				flash('Congratulations, you are now a registered user!')
				return render_template('demo_views/register.html', form=form)
			except Exception as exp:
				flash('Problem while registering user!')
				return render_template('demo_views/register.html', form=form)
		else:
			flash('Problem while validating data!')
			return render_template('demo_views/register.html', form=form)


@app.route('/logout')
# @login_required
def logout():
	if current_user.is_authenticated:
	    logout_user()
	# return redirect(url_for('home'))
	return redirect(app.config["BASE_URL_WITH_PORT"]+"/login")

@app.route('/')
@app.route('/home')
# @login_required
def home():
	if current_user.is_authenticated:
		userid=current_user.id
	else:
		# return redirect(url_for('login'))
		return redirect(app.config["BASE_URL_WITH_PORT"]+"/login")

	try:
		c=db.session.query(UploadedVideo).order_by(UploadedVideo.videoid.desc()).limit(1)
		latestvideoid = c[0].videoid
	except:
		latestvideoid=-1
	view_video_url=str(app.config["BASE_URL_WITH_PORT"]+"/viewvideos")
	# print(view_video_url)
	return render_template('demo_views/home.html', view_video_url=view_video_url)

# @app.route('/viewRaghivvide')
# # @login_required
# def viewRaghivvide():
# 	return render_template('demo_views/viewvideo.html',main_video_url=main_video_url)

@app.route('/demoviewvideos')
# @login_required
def demoviewvideos():
	if not current_user.is_authenticated:
		# return redirect(url_for('login'))
		return redirect(app.config["BASE_URL_WITH_PORT"]+"/login")
	else:
		userid=current_user.id
	
	filename="20200229134607AngreziMediumLowerQuality.mp4"
	# main_video_url=request.url_root+str("static/video/uploaded/")+str(filename)
	main_video_url=app.config["BASE_URL_WITH_PORT"]+"/"+str("static/video/uploaded/")+str(filename)
	print(main_video_url)
	return render_template('demo_views/viewvideo.html',main_video_url=main_video_url)


def getLatestUploadedVideos(currentid,numberofvideos):
	latestvideolist = UploadedVideo.query.filter(UploadedVideo.videoid <= currentid).order_by(UploadedVideo.videoid.desc()).limit(numberofvideos)
	return latestvideolist

def getjsonfilename(associated_videoid):
	jsonFile = VideoAnalyticsFile.query.filter_by(video_id=associated_videoid).scalar()
	if jsonFile is None:
		return "FileNotFound"
	else:
		return app.config["BASE_URL_WITH_PORT"]+"/static/analyticsFolder/generated/"+jsonFile.filename

def getvideofilename(video_filename):
	if video_filename is None:
		return "FileNotFound"
	else:
		return app.config["BASE_URL_WITH_PORT"]+"/static/analyticsFolder/generated/"+video_filename

@app.route('/viewvideos')
# @login_required
def viewvideos_jabir():
	if not current_user.is_authenticated:
		# return redirect(url_for('login'))
		return redirect(app.config["BASE_URL_WITH_PORT"]+"/login")
	else:
		userid=current_user.id

	currentvideoid = request.args.get('videoid')
	
	if currentvideoid is None:
		# for only max-videoid
		max_video_id=db.session.query(func.max(UploadedVideo.videoid)).scalar()
	else:
		max_video_id=currentvideoid

	print("max_video_id is "+str(max_video_id))
	latestvideolist = getLatestUploadedVideos(max_video_id,6)
	
	# for the UploadedVideo object with max-videoid
	# latestvideo=UploadedVideo.query.order_by(UploadedVideo.videoid.desc()).limit(1)
	# print("The max videoid is "+str(max_video_id))
	# latestvideolist = getLatestUploadedVideos(latestvideo[0].videoid,6)

	pageinfojson=dict()
	side_playlist_info=[]
	count=1
	for eachvideo in latestvideolist:

		print("eachvideoid in list " + str(eachvideo.videoid))
		if count==1:
			current_video_info=dict()
			current_video_info["videoid"]=eachvideo.videoid
			current_video_info["videoname"]=(eachvideo.filename)[14:]
			current_video_info["source"]=getvideofilename(eachvideo.filename)
			#TODO:
			current_video_info["duration"]="2:20"
			current_video_info["thumbnailurl"]="https://lonelyplanetstatic.thumbnailurlix.net/op-vvideoideo-sync/images/production/p-5810396717001-brightcove-when-to-go-to-the-azores-20180726-050333.jpg?w=160&h=90&sharp=10&q=50"

			current_video_info["current_video_json"]=getjsonfilename(eachvideo.videoid)
		else:
			eachPlaylistVideo=dict()
			eachPlaylistVideo["videoid"]=eachvideo.videoid
			#ignoring the added number
			eachPlaylistVideo["videoname"]=eachvideo.filename[14:]
			eachPlaylistVideo["source"]=getvideofilename(eachvideo.filename)
			#TODO:
			eachPlaylistVideo["duration"]="2:20"
			eachPlaylistVideo["thumbnailurl"]="https://lonelyplanetstatic.thumbnailurlix.net/op-vvideoideo-sync/images/production/p-5810396717001-brightcove-when-to-go-to-the-azores-20180726-050333.jpg?w=160&h=90&sharp=10&q=50"

			eachPlaylistVideo["current_video_json"]=getjsonfilename(eachvideo.videoid)

			side_playlist_info.append(eachPlaylistVideo.copy())
		count=count+1
	
	pageinfojson["current_video_info"]=current_video_info
	pageinfojson["side_playlist_info"]=side_playlist_info

	print("The Page information Json is \n ")
	print(pageinfojson)

	# filename="20200229134607AngreziMediumLowerQuality.mp4"
	# # main_video_url=request.url_root+str("static/video/uploaded/")+str(filename)
	# main_video_url=app.config["BASE_URL_WITH_PORT"]+"/"+str("static/video/uploaded/")+str(filename)
	# print(main_video_url)
	return render_template('demo_views/viewvideos_jabir_integrated.html')


@app.route('/2d')
def view_2d():

	filename="20200229134607AngreziLowerQuality.mp4"
	# main_video_url=request.url_root+str("static/video/uploaded/")+str(filename)
	main_video_url=app.config["BASE_URL_WITH_PORT"]+"/"+str("static/video/uploaded/")+str(filename)
	print(main_video_url)
	return render_template('demo_views/2dview.html',main_video_url=main_video_url)

@app.route('/3d')
def view_3d():
	return render_template('demo_views/3dview.html')

import json
@app.route('/api/GetStaticJson',methods=['POST'])
def getstaticjson():

	# main_video_url=request.url_root+str("static/video/uploaded/")+str(filename)
	static_json="/home/ubuntu/workingDir/asmi-flask/app/static/analyticsFolder/generated/demo-raw1.json"
	data=dict()
	try:
		with open(static_json) as blog_file:
			data = json.load(blog_file)
	except Exception as err:
		return jsonify({"message":"Error","data":str(err)})

	return jsonify({"message":"Success","data":data})

@app.route('/uploaded')
# @login_required
def uploaded():
	if not current_user.is_authenticated:
		# return redirect(url_for('login'))
		return redirect(app.config["BASE_URL_WITH_PORT"]+"/login")
	latestvideoList=UploadedVideo.query.order_by(UploadedVideo.videoid.desc()).limit(15)
	if latestvideoList is None:
		latestvideoList=[]

	return render_template('demo_views/uploaded.html',latestvideoList=latestvideoList)


@app.route('/analytics')
# @login_required
def analytics():
	if not current_user.is_authenticated:
		# return redirect(url_for('login'))
		return redirect(app.config["BASE_URL_WITH_PORT"]+"/login")
	analyticsFileList=VideoAnalyticsFile.query.order_by(VideoAnalyticsFile.analyticsfileid.desc()).limit(15)
	if analyticsFileList is None:
		analyticsFileList=[]

	return render_template('demo_views/analytics.html',analyticsFileList=analyticsFileList)

