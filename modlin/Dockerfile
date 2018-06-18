FROM ubuntu
RUN apt-get update && apt-get upgrade -y &&  apt-get install -y python3-pip vim && pip3 install conf pytelegrambotapi 
ADD sevens.py /opt/sevens.py
CMD ["sh","-c","cd . && python3 /opt/sevens.py"]
