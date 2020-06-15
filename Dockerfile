from debian
RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get -y install python3
RUN apt-get -y install nano
RUN apt-get -y install  python3-pip python3-dev build-essential git
RUN pip3 install discord
RUN git clone git@github.com:computerdeath/jb-bot.git
COPY "TOKEN.key" "/"
ENTRYPOINT python3 /jb-bot/main.py