### To setup locally

Add a new conda environment (I had problems with py34 on heroku, so using py27):

    $ conda create -n env_name python=2.7

Edit `config.py` as appropriate (e.g. comment out `model_backend` to use default non-redis)
    
Install requirements with conda, and start app

    $ conda install --file conda-requirements.txt
    $ foreman start

### To setup on heroku

Configure heroku to use the conda buildpack and add your secret keys:

	$heroku config:add BUILDPACK_URL=https://github.com/ddollar/heroku-buildpack-multi.git

	$ heroku config:set BUILDPACK_URL=https://github.com/kennethreitz/conda-buildpack.git
    $ heroku config:set FLASK_SECRET_KEY='\xea\xe7l>uQ\xb0\x87\xd7\x1e\xc1\xd9O|\xc6\xf4\x02\xa2\x0cb6"zo'
    $ heroku config:set BOKEH_SECRET_KEY='\x95\xf3\xe1.x\x18\xc2\x83\x13\xaf&ZW\x03\x0f\xb7l\xbbZ"\xc4\xcf\xfc\xb3'

To run with redis, add the heroku add on rediscloud (the 25 level is free):

    $ heroku addons:add rediscloud:25 

Then, as normal, push to heroku to deploy
