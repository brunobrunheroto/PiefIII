from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
import datetime as dt
import mysql.connector

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_show_time"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        operacao = tracker.get_slot("operacao")
        dia = tracker.get_slot("data")
        telefone = tracker.get_slot("telefone")
        nome = tracker.get_slot("name")
        horario = tracker.get_slot("horario")

        dispatcher.utter_message("Ok")

        #Connecting with the database and password
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            # Add your database password here
            passwd="",     
            database="pief"
        )
        mycursor = mydb.cursor()

        # processamento de dados
        mycursor.execute("SELECT * FROM pief.atende")
        linhas = mycursor.fetchall()

        isFound = False
        for row in linhas:
            i = 0
            crm = ""
            for column in row:
                if i == 0:
                    crm = column
                if i == 1:
                    especialidades = column.split(',')
                    print(especialidades)
                    for especialidade in especialidades:
                        if especialidade == operacao:
                            isFound = True
                            print(crm)
                i += 1

        if isFound == False:
            print("Desculpe-me, não oferecemos esta consulta/exame")

        horario += ":00"

        if int(dia) < 10:
            dia = '2021-11-0' + dia
        else:
            dia = '2021-11-' + dia


        print(crm," ", dia, " ", horario)

        mycursor.execute("SELECT * FROM pief.paciente WHERE telefone = '{}'".format(telefone))
        linhas = mycursor.fetchall()

        isRegistered = False
        for row in linhas:
            i = 0
            for column in row:
                if i == 0:
                    print("Paciente já registrado: ", column)
                    isRegistered =True
                i += 1

        if not isRegistered:
            #Registra um paciente novo
            mycursor.execute("INSERT INTO paciente (nome, telefone) VALUES ('{}', '{}')".format(nome, telefone))
            mydb.commit()
            print("Paciente foi registrado")

        #Verifica se consulta já foi marcada
        mycursor.execute("SELECT * FROM pief.consulta WHERE horario = '{}' AND dia = '{}' AND fk_Profissional_CRM = '{}' AND fk_Paciente_Telefone = '{}'".format(horario, dia, crm, telefone))
        linhas = mycursor.fetchall()

        isAlreadyScheduled = False
        for row in linhas:
            i = 0
            for column in row:
                if i == 2:
                    print("Horario está ocupado: ", column)
                    isAlreadyScheduled =True
                i += 1

        if not isAlreadyScheduled:
            # registra a consulta
            mycursor.execute("INSERT INTO consulta (Horario, Dia, fk_Profissional_CRM, fk_Paciente_Telefone) VALUES ('{}','{}','{}', '{}')".format(horario, dia, crm, telefone))
            mydb.commit()
            print("Consulta registrada!")

        return []

class ActionFeedbackSubmit(Action):

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "action_feedback_submit"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(template="utter_submit")

        return [SlotSet('feedback', tracker.latest_message['text'])]


class ActionFeedback(Action):

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "action_feedback"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(template="utter_feedback")

        return [SlotSet('lastN', tracker.latest_message['text'])]

class ActionFeedback(Action):

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "action_submit"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        """Video nao apresenta essa parte inteiramente, entao tive que improvisar"""
        dispatcher.utter_message(text="Your first name is {0}\n your last name is {1}\n your feedback is {0}"
                                 (tracker.get_slot("firstN"), tracker.get_slot("lastN"), tracker.get_slot("feedback")))

        return []