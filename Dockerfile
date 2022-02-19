# Stage 1
# Installing base image
FROM python:3 
# Getting image updates
RUN apt-get update

# Stage 2
# Setting working directory
WORKDIR /usr/local/app
# Adding source code to WORKDIR
COPY /src /usr/local/app/

#Stage 3
# Installing necessary libraries
RUN pip install pygame

#Stage 4
# Running the game
CMD [ "python3", "/usr/local/app/main.py" ]
                                                     




