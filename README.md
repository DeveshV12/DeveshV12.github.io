<!DOCTYPE html>
{% load static %}
<html>
<head>
	<title>home page</title>
	<link rel="stylesheet" type="text/css" href="{% static "css/mainapp/style.css" %}">
	<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
	
</head>
<body>
	<br>
	<div class="container">
		<div class="row">
			<div class="col-md-3">
				<div class="card card-body h-100" id="profile-wrapper">
					<img id="profile-pic" src="{% static "image/image.png" %}">
					<hr>
					<h4>Hi! I'm Devesh </h4>
					<h6><p>I love coding,and<br> I love to learn New Technologies.</p></h6>
				</div>
			</div>
			<div class="col-md-9">
				<div class="card card-body h-100">
				<h4>Technical Skills</h4>
				<hr>
				<p><b>JAVA</b><br>					
-Core JAVA(OPPS concepts,Multithreading,Exception Handeling,CollectionFrameWork.)
-Advanced JAVA,-J2EE (JDBC,SERVLETS,MVC)</p>
<p><b>PYTHON</b><br>
Special Datatypes,Collection ,Regular Expression,String,File Operations Exception Handling, Networking(Socket,Urllib),PDBC, Django</p>
<p><b>SQL</b><br> (ORACLE DATABASE,MySql)
</p>		
				<ul class="socialmidea">
					<li><img class="social" src="{% static "image/fb.png" %}"></li>
					<li><img class="social" src="{% static "image/insta.png" %}"></li>
				<li><img class="social" src="{% static "image/linkidin.png" %}"></li>
					<li><img class="social" src="{% static "image/youtube.png" %}"></li>
				</ul>
				</div>
			</div>			
		</div>
		<br>
		<div class="row">
			<div class="col-md-6">
				<div class="card card-body h-100">
					<h4>Area Of Intrest</h4>
					<hr>
					<ol>
						<dt>Internet Of Things</dt>
						<dt>Artificial Intelligence</dt>
						<dt>Machine Learning</dt>
						<dt>Web Development</dt>
					<dt>Mobile Applications</dt>
				</ol>
				</div>
			</div>
			<div class="col-md-6">
				<div class="card card-body h-100">
					<h4>Professional Skills</h4>
					<hr>					
						<dt>Leadership</dt>
						<dt>Smark Work</dt>
						<dt>Quick Learning</dt>
						<dt>Creativity</dt>				
				</div>				
			</div>			
		</div>
		<br>
		<div class="row">
			<div class="col-md-6">
				<div class="card card-body h-100">
					<h4>Hobbies</h4>
					<hr>
					<p>Playing Cricket,FootBall<br></p>
					<p>Listening Music<br></p>
					<p>Cooking<br></p>
					<p>Travelling<br></p>
				</div>
			</div>
			<div class="col-md-6">
				<div class="card card-body h-100">
					<h4>Click here To Check Proofs </h4>
					<hr>
				 <a class="btn btn-primary btn-lg" href="/personaldetails" role="button">Personal details here..</a><br>
					 <br>

 				 <a class="btn btn-primary btn-lg" href="/professionaldetails" role="button">Professional details here..</a>
				</div>
			</div>			
		</div>
		<br>
	</div>	
</body>
</html>
