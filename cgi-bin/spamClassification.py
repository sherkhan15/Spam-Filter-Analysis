import cgi
import classifier

form = cgi.FieldStorage()

mail = form.getvalue("text")

category = classifier.classify(mail)

if category[0] == "spam":
    spam = mail
    inbox = ""
elif category[0] == "ham":
    inbox = mail
    spam = ""

print("Content-type:text/html\r\n\r\n")
print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
    <link rel='stylesheet' href='../styles.css'>
</head>
<body>
<div class="container">
<h1>Message is {}</h1>

<ul class="nav nav-tabs" id="myTab" role="tablist">
  <li class="nav-item">
    <a class="nav-link active" id="home-tab" data-toggle="tab" href="#home" role="tab" aria-controls="home" aria-selected="true">Inbox</a>
  </li>
  <li class="nav-item">
    <a class="nav-link active" id="compose-tab" data-toggle="tab"
     href="#compose" role="tab" aria-controls="home" 
     aria-selected="true">Compose</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" id="profile-tab" data-toggle="tab" href="#profile" role="tab" aria-controls="profile" aria-selected="false">Spam</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" id="contact-tab" data-toggle="tab" href="#contact" role="tab" aria-controls="contact" aria-selected="false">Sent</a>
  </li>
</ul>
<div class="tab-content" id="myTabContent">
  <div class="tab-pane fade show active" id="home" role="tabpanel" aria-labelledby="home-tab"><h2>Inbox</h2>{}</div>
  <div class="tab-pane fade" id="compose" role="tabpanel"
   aria-labelledby="compose-tab"><h2>Send Mail</h2></div>
  <div class="tab-pane fade" id="profile" role="tabpanel" aria-labelledby="profile-tab"><h2>Spam</h2>{}</div>
  <div class="tab-pane fade" id="contact" role="tabpanel" aria-labelledby="contact-tab"><h2>Sent Mails</h2></div>
</div>

</div>

<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
<script src="../bootstrap.min.js"></script>
</body>
</html>
""".format(category[0], inbox, spam))