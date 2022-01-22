# Agnos-Backend-Interview-Assignment

<br>

<hr>
<b>How to deploy on local?</b>
<ul>
<li>Download Project or Clone Repository,extract zip and move inside project folder, and type the following commands.</li>
<li>Run Command "pip install -r requirement.txt"</li>
<li>Run Command "python manage.py runserver"</li>
</ul>
<hr>
<b>How to send API?</b>
<ul>
<li>Send request['GET'] to "127.0.0.1:8000/api/is_match" with the format:</li>
<li>{
	"message": "aaa",
	"pattern": "bbb"
}
</li>
</ul>
<hr>
<b>How to run unit test?</b>
<ul>
<li>While the server is running, open another command line, and type the following commands.</li>
<li>Run Command "python manage.py test api"</li>
</ul>
<hr>
