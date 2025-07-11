body,html{
	height: 100%;
	margin: 0;
	background: rgb(44, 47, 59);
   background: -webkit-linear-gradient(to right, rgb(40, 59, 34), rgb(54, 60, 70), rgb(32, 32, 43));
	background: linear-gradient(to right, rgb(38, 51, 61), rgb(50, 55, 65), rgb(33, 33, 78));
}

.chat{
	margin-top: auto;
	margin-bottom: auto;
}
.card{
	height: 500px;
	border-radius: 15px !important;
	background-color: rgba(0,0,0,0.4) !important;
}
.contacts_body{
	padding:  0.75rem 0 !important;
	overflow-y: auto;
	white-space: nowrap;
}
.msg_card_body{
	overflow-y: auto;
}
.card-header{
	border-radius: 15px 15px 0 0 !important;
	border-bottom: 0 !important;
}
.card-footer{
border-radius: 0 0 15px 15px !important;
	border-top: 0 !important;
}
.container{
	align-content: center;
}
.search{
	border-radius: 15px 0 0 15px !important;
	background-color: rgba(0,0,0,0.3) !important;
	border:0 !important;
	color:white !important;
}
.search:focus{
	 box-shadow:none !important;
   outline:0px !important;
}
.type_msg{
	background-color: rgba(0,0,0,0.3) !important;
	border:0 !important;
	color:white !important;
	height: 60px !important;
	overflow-y: auto;
}
	.type_msg:focus{
	 box-shadow:none !important;
   outline:0px !important;
}
.attach_btn{
	border-radius: 15px 0 0 15px !important;
	background-color: rgba(0,0,0,0.3) !important;
	border:0 !important;
	color: white !important;
	cursor: pointer;
}
.send_btn{
	border-radius: 0 15px 15px 0 !important;
	background-color: rgba(0,0,0,0.3) !important;
	border:0 !important;
	color: white !important;
	cursor: pointer;
}
.search_btn{
	border-radius: 0 15px 15px 0 !important;
	background-color: rgba(0,0,0,0.3) !important;
	border:0 !important;
	color: white !important;
	cursor: pointer;
}
.contacts{
	list-style: none;
	padding: 0;
}
.contacts li{
	width: 100% !important;
	padding: 5px 10px;
	margin-bottom: 15px !important;
}
.active{
	background-color: rgba(0,0,0,0.3);
}
.user_img{
	height: 70px;
	width: 70px;
	border:1.5px solid #f5f6fa;

}
.user_img_msg{
	height: 40px;
	width: 40px;
	border:1.5px solid #f5f6fa;

}
.img_cont{
	position: relative;
	height: 70px;
	width: 70px;
}
.img_cont_msg{
	height: 40px;
	width: 40px;
}
.online_icon{
	position: absolute;
	height: 15px;
	width:15px;
	background-color: #4cd137;
	border-radius: 50%;
	bottom: 0.2em;
	right: 0.4em;
	border:1.5px solid white;
}
.offline{
	background-color: #c23616 !important;
}
.user_info{
	margin-top: auto;
	margin-bottom: auto;
	margin-left: 15px;
}
.user_info span{
	font-size: 20px;
	color: white;
}
.user_info p{
	font-size: 10px;
	color: rgba(255,255,255,0.6);
}
.video_cam{
	margin-left: 50px;
	margin-top: 5px;
}
.video_cam span{
	color: white;
	font-size: 20px;
	cursor: pointer;
	margin-right: 20px;
}
.msg_cotainer{
	margin-top: auto;
	margin-bottom: auto;
	margin-left: 10px;
	border-radius: 25px;
	background-color: rgb(82, 172, 255);
	padding: 10px;
	position: relative;
}
.msg_cotainer_send{
	margin-top: auto;
	margin-bottom: auto;
	margin-right: 10px;
	border-radius: 25px;
	background-color: #58cc71;
	padding: 10px;
	position: relative;
}
.msg_time{
	position: absolute;
	left: 0;
	bottom: -15px;
	color: rgba(255,255,255,0.5);
	font-size: 10px;
}
.msg_time_send{
	position: absolute;
	right:0;
	bottom: -15px;
	color: rgba(255,255,255,0.5);
	font-size: 10px;
}
.msg_head{
	position: relative;
}
#action_menu_btn{
	position: absolute;
	right: 10px;
	top: 10px;
	color: white;
	cursor: pointer;
	font-size: 20px;
}
.action_menu{
	z-index: 1;
	position: absolute;
	padding: 15px 0;
	background-color: rgba(0,0,0,0.5);
	color: white;
	border-radius: 15px;
	top: 30px;
	right: 15px;
	display: none;
}
.action_menu ul{
	list-style: none;
	padding: 0;
	margin: 0;
}
.action_menu ul li{
	width: 100%;
	padding: 10px 15px;
	margin-bottom: 5px;
}
.action_menu ul li i{
	padding-right: 10px;
}
.action_menu ul li:hover{
	cursor: pointer;
	background-color: rgba(0,0,0,0.2);
}
@media(max-width: 576px){
	.contacts_card{
	margin-bottom: 15px !important;
}
}

<link href="//maxcdn.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css" rel="stylesheet" id="bootstrap-css">
<script src="//maxcdn.bootstrapcdn.com/bootstrap/4.1.1/js/bootstrap.min.js"></script>
<script src="//cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
<div class="box">
	<div class="person-a">
		<div class="icon">
		</div> <!-- icon-->
		<div class="message">
		Cat ipsum dolor sit amet, sit on human they not getting up ever and purr while eating. 
		</div><!-- message -->
	</div><!-- person a -->
	
		<div class="person-b">
	
		<div class="message">
	Lies down claw drapes jump off balcony
		</div><!-- message -->
	</div><!-- person b -->
	

		<div class="person-a">
		<div class="icon">
		</div> <!-- icon-->
		<div class="message">
		knock everything off the table
		</div><!-- message -->
	</div><!-- person a -->
	
		<div class="person-b">
		
		<div class="message">
intently stare at the same spot stand in doorway
		</div><!-- message -->
	</div><!-- person b -->
	
	<div class="person-a">
		<div class="icon">
		</div> <!-- icon-->
		<div class="message">
		Poop in the plant pot 
		</div><!-- message -->
	</div><!-- person a -->
	
			<div class="person-b">
	
		<div class="message">
always wanting food
		</div><!-- message -->
	</div><!-- person b -->
	
	<div class="person-a">
		<div class="icon">
		</div> <!-- icon-->
		<div class="message last">
		<svg  class="cat" viewBox="0 0 512 512">
<path style="fill:#FFC850;" d="M444.379,3.741c10.828-8.798,27.018-1.092,27.018,12.859v222.01l-182.26-107.699L444.379,3.741z"/>
<path style="fill:#EBAF4B;" d="M454.828,228.819l-110.973-65.574l92.462-104.241c6.465-7.288,18.511-2.716,18.511,7.027V228.819z"/>
<path style="fill:#FFC850;" d="M67.619,3.741C56.79-5.057,40.601,2.649,40.601,16.6v222.01l182.26-107.699L67.619,3.741z"/>
<path style="fill:#EBAF4B;" d="M57.17,228.819l110.973-65.574L75.681,59.004c-6.465-7.288-18.511-2.716-18.511,7.027
	C57.17,66.031,57.17,228.819,57.17,228.819z"/>
<ellipse style="fill:#FFDC64;" cx="255.999" cy="292.46" rx="231.97" ry="219.54"/>
<path style="fill:#FF8087;" d="M289.137,429.155v16.569c0,18.302-14.836,33.138-33.138,33.138l0,0
	c-18.302,0-33.138-14.836-33.138-33.138v-16.569l33.138-16.569L289.137,429.155z"/>
<path style="fill:#5D5360;" d="M274.293,343.862h-36.588c-7.899,0-12.273,9.157-7.307,15.3l18.295,22.634
	c3.76,4.651,10.852,4.651,14.613,0l18.295-22.634C286.566,353.019,282.193,343.862,274.293,343.862z"/>

	<path style="fill:#E1A546;" d="M479.673,437.439c-1.286,0-2.593-0.299-3.815-0.934c-50.092-26.047-128.491-41.524-129.28-41.678
		c-4.49-0.874-7.419-5.226-6.545-9.717c0.878-4.494,5.186-7.427,9.717-6.545c3.301,0.643,81.515,16.076,133.754,43.239
		c4.057,2.112,5.639,7.111,3.527,11.173C485.555,435.813,482.667,437.439,479.673,437.439z"/>
	<path style="fill:#E1A546;" d="M496.255,379.451c-0.712,0-1.436-0.093-2.156-0.287c-46.435-12.483-130.87-10.113-131.703-10.077
		c-4.652,0.134-8.398-3.459-8.531-8.03c-0.138-4.575,3.459-8.394,8.03-8.531c3.56-0.113,87.736-2.476,136.509,10.635
		c4.417,1.189,7.035,5.732,5.849,10.153C503.257,377.012,499.912,379.447,496.255,379.451z"/>

<path style="fill:#FFC850;" d="M313.991,495.431c-128.112,0-231.967-98.291-231.967-219.54c0-89.035,56.034-165.634,136.518-200.081
	C108.248,92.762,24.032,183.285,24.032,292.46C24.032,413.709,127.887,512,255.999,512c34.037,0,66.328-6.995,95.449-19.459
	C339.25,494.416,326.748,495.431,313.991,495.431z"/>

	<path style="fill:#E1A546;" d="M32.324,437.439c-2.993,0-5.882-1.622-7.358-4.462c-2.112-4.061-0.53-9.061,3.527-11.173
		c52.24-27.163,130.453-42.596,133.754-43.239c4.494-0.902,8.839,2.055,9.717,6.545c0.874,4.49-2.055,8.843-6.545,9.717
		c-0.789,0.154-79.189,15.631-129.28,41.678C34.917,437.14,33.611,437.439,32.324,437.439z"/>
	<path style="fill:#E1A546;" d="M15.743,379.451c-3.657,0-7.002-2.439-7.997-6.137c-1.185-4.421,1.432-8.964,5.849-10.153
		c48.777-13.115,132.941-10.736,136.509-10.635c4.571,0.138,8.167,3.956,8.03,8.531c-0.138,4.571-4.098,8.196-8.531,8.03
		c-0.849-0.028-85.297-2.407-131.703,10.077C17.179,379.358,16.455,379.451,15.743,379.451z"/>

<path style="fill:#4B3F4E;" d="M160.727,321.456L160.727,321.456c-15.948,0-28.996-13.048-28.996-28.996v-16.569
	c0-15.948,13.048-28.996,28.996-28.996l0,0c15.948,0,28.996,13.048,28.996,28.996v16.569
	C189.723,308.407,176.675,321.456,160.727,321.456z"/>
<path style="fill:#5D5360;" d="M160.727,246.895c-1.418,0-2.778,0.221-4.142,0.421v41.002c0,9.151,7.418,16.569,16.569,16.569
	s16.569-7.418,16.569-16.569v-12.427C189.723,259.943,176.674,246.895,160.727,246.895z"/>
<circle style="fill:#FFFFFF;" cx="160.729" cy="267.61" r="12.427"/>
<path style="fill:#4B3F4E;" d="M351.271,321.456L351.271,321.456c-15.948,0-28.996-13.048-28.996-28.996v-16.569
	c0-15.948,13.048-28.996,28.996-28.996l0,0c15.948,0,28.996,13.048,28.996,28.996v16.569
	C380.267,308.407,367.219,321.456,351.271,321.456z"/>
<path style="fill:#5D5360;" d="M351.271,246.895c-1.418,0-2.778,0.221-4.142,0.421v41.002c0,9.151,7.418,16.569,16.569,16.569
	s16.569-7.418,16.569-16.569v-12.427C380.267,259.943,367.219,246.895,351.271,246.895z"/>
<circle style="fill:#FFFFFF;" cx="351.269" cy="267.61" r="12.427"/>
<path style="fill:#4B3F4E;" d="M262.408,382.15l-18.295-36.215c-0.332-0.658-0.518-1.378-0.769-2.074h-5.639
	c-7.899,0-12.273,9.157-7.308,15.3l18.295,22.634c3.55,4.39,9.981,4.485,13.863,0.587
	C262.511,382.297,262.453,382.239,262.408,382.15z"/>
<path style="fill:#E6646E;" d="M255.999,412.586l-33.138,16.569v16.569c0,2.629,0.383,5.154,0.961,7.606
	c8.337-1.034,16.389-3.449,23.892-7.153v7.831c0,4.575,3.709,8.285,8.285,8.285c4.576,0,8.285-3.709,8.285-8.285v-7.83
	c7.504,3.704,15.556,6.119,23.892,7.152c0.578-2.452,0.961-4.978,0.961-7.606v-16.569L255.999,412.586z"/>
<path style="fill:#EBAF4B;" d="M297.422,437.439c-11.719,0-23.013-3.483-32.653-10.073c-5.162-3.527-12.374-3.527-17.544,0
	c-9.636,6.59-20.93,10.073-32.649,10.073c-14.259,0-27.993-5.275-38.672-14.85c-3.406-3.058-3.689-8.297-0.635-11.703
	s8.281-3.689,11.703-0.635c13.911,12.483,35.683,13.847,50.905,3.434c10.841-7.403,25.408-7.403,36.241,0
	c15.226,10.408,37.001,9.041,50.913-3.43c3.402-3.05,8.636-2.775,11.699,0.639c3.054,3.406,2.767,8.645-0.639,11.699
	C325.41,432.168,311.681,437.439,297.422,437.439z"/>

</svg>
		</div><!-- message -->
	</div><!-- person a -->
	
</div><!-- box -->
<!DOCTYPE html>
<html>
	<head>
		<title>Chatbot</title>
		<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
		<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.5.0/css/all.css" integrity="sha384-B4dIYHKNBt8Bc12p+WXckhzcICo0wtJAoU8YZTY5qE0Id1GSseTk6S+L3BlXeVIU" crossorigin="anonymous">
		<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
		<link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='style.css')}}"/>
	</head>
	
	
	<body>
		<div class="container-fluid h-100">
			<div class="row justify-content-center h-100">		
				<div class="col-md-8 col-xl-6 chat">
					<div class="card">
						<div class="card-header msg_head">
							<div class="d-flex bd-highlight">
								<div class="img_cont">
									<!-- <img src="https://i.ibb.co/fSNP7Rz/icons8-chatgpt-512.png" class="rounded-circle user_img"> -->
									<img src="https://www.prdistribution.com/spirit/uploads/pressreleases/2019/newsreleases/d83341deb75c4c4f6b113f27b1e42cd8-chatbot-florence-already-helps-thousands-of-patients-to-remember-their-medication.png" class="rounded-circle user_img">
									<span class="online_icon"></span>
								</div>
								<div class="user_info">
									<span>Medical Chatbot</span>
									<p>Ask me anything!</p>
								</div>
							</div>
						</div>
						<div id="messageFormeight" class="card-body msg_card_body">
							
							
						</div>
						<div class="card-footer">
							<form id="messageArea" class="input-group">
                                <input type="text" id="text" name="msg" placeholder="Type your message..." autocomplete="off" class="form-control type_msg" required/>
								<div class="input-group-append">
									<button type="submit" id="send" class="input-group-text send_btn"><i class="fas fa-location-arrow"></i></button>
								</div>
							</form>
						</div>
					</div>
				</div>
			</div>
		</div>
		
		<script>
			$(document).ready(function() {
				$("#messageArea").on("submit", function(event) {
					const date = new Date();
					const hour = date.getHours();
					const minute = date.getMinutes();
					const str_time = hour+":"+minute;
					var rawText = $("#text").val();

					var userHtml = '<div class="d-flex justify-content-end mb-4"><div class="msg_cotainer_send">' + rawText + '<span class="msg_time_send">'+ str_time + '</span></div><div class="img_cont_msg"><img src="https://i.ibb.co/d5b84Xw/Untitled-design.png" class="rounded-circle user_img_msg"></div></div>';
					
					$("#text").val("");
					$("#messageFormeight").append(userHtml);

					$.ajax({
						data: {
							msg: rawText,	
						},
						type: "POST",
						url: "/get",
					}).done(function(data) {
						var botHtml = '<div class="d-flex justify-content-start mb-4"><div class="img_cont_msg"><img src="https://www.prdistribution.com/spirit/uploads/pressreleases/2019/newsreleases/d83341deb75c4c4f6b113f27b1e42cd8-chatbot-florence-already-helps-thousands-of-patients-to-remember-their-medication.png" class="rounded-circle user_img_msg"></div><div class="msg_cotainer">' + data + '<span class="msg_time">' + str_time + '</span></div></div>';
						$("#messageFormeight").append($.parseHTML(botHtml));
					});
					event.preventDefault();
				});
			});
		</script>
        
    </body>
</html>