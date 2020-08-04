# test-system

For Viewing Purposes:
1. cd repository to git clone https://github.com/test-system/ticksys.git cd tictsys
2. Create a virtual environment for python, so that packages are not installed globally. python3 -m venv venv
3. Install dependencies, pip install -r requirements.txt

Database, possibly with docker:

docker run --rm --name rtask-db -e POSTGRES_PASSWORD=RobedCoder -e POSTGRES_DB=rtask -p5432:5432 -d postgres

Terminal command walkthrough:

docker run: tells docker to run an image
--rm: remove this container when it is stopped, so resources aren't held on to
--name ticksys-db: name this container 'ticksys-db'
-e POSTGRES_PASSWORD=... -e POSTGRES_DB=ticksys : environment variables set inside the container to have a database set up
-p5432:5432 : expose port 5432 from inside the container to port 5432 onto the host computer
postgres : the name of the docker image to run; this will run the latest stable version
Docker will pull up the image the first time if it's not already local to the environment
