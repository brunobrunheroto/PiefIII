# PIEF III
<p>This project was developed as a solution for facamp's third Integrated Engineering Project (PIEF III), which aims to build a project involving relational databases, a subject administered in the same semester. The Clinic+ group then proposed the development of a chatbot for scheduling appointments in a dental clinic in order to facilitate the scheduling process.</p>

## <ins>Goals</ins>
<p>This project was done with academic purposes. It aims to build a chatbot for a dental clinic and is prepared to deal with formal and informal language.</p>

## <ins>Technologies</ins>
- Rasa Chatbot: Open source framework that uses AI to give responses according to user input.
- Webchat: Open source contribution to the rasa framework, it offers a customizable widget.
- Python: This programming language was used to integrate Rasa and the database made in MySQL.
- MySQL: Relational database chosen to store user information and scheduled appointments.
The front-end of the site was made using Html and Css through Nicepage's software.

## <ins>How to use </ins>

- Download the project.
- Install Anaconda and import the virtual environment (venv.yml)
- Install MySQL and MySQL Workbench and create the database using the "PIEFIII.sql" script.
- Go to "actions\actions.py" path on the project and add your database password.
- Open up two anaconda terminals and use cd to go to the project path on both.
- Execute command on both terminals: "conda activate venv".
- On one of the terminals execute: "rasa run actions".
- On the other terminal run: "rasa run -m models --enable-api --cors "*" --debug".
After executing the commands above, run the index file.

## <ins>Execution of the program:</ins>
<p><ins>Site appearance</ins></p>

![site1](https://user-images.githubusercontent.com/67275098/176106627-f602a5e9-c378-4c42-9961-71ff7da10208.gif)

<p><ins>Frequent questions Session</ins></p>

![site2](https://user-images.githubusercontent.com/67275098/176106700-a2d6958a-855e-4db1-ad9b-a1eb9cbab86a.gif)

<p><ins>Chatbot being used</ins></p>

https://user-images.githubusercontent.com/67275098/176107085-53e3d8cc-247d-492d-a71d-20b0f0a91336.mp4

## <ins>Credits</ins>
<p> The ideia to work on this project and it's structure was shared by the teachers responsible for the PIEF III subject. </p>
<p>Other team members (Clinic+):</p>

- Fábio Seiji Sakai Iwashima
- Nicolas Raffi
- Gabriel Loewen Catarini
