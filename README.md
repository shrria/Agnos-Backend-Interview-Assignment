# Agnos-Backend-Interview-Assignment

<br>
<b>How to deploy on local?</b>
<hr>
<ul>
<li>Download Project or Clone Repository,extract zip and move inside project folder, and type the following commands.</li>
<li>Run Command "pip install -r requirement.txt"</li>
<li>Run Command "python manage.py runserver"</li>
</ul>
<hr>
<ul>
<li>How to send API?</li>
<li>Send request['GET'] to "127.0.0.1:8000/api/is_match" with the format:</li>
<li>{
	"message": "aaa",
	"pattern": "bbb"
}
</li>
</ul>
<hr>
<ul>
<li>How to run unit test?</li>
<li>While the server is running, open another command line, and type the following commands.</li>
<li>Run Command "python manage.py test api"</li>
</ul>
