#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import memcache
from time import time
from datetime import datetime 
import csv

class DataManager(object):

    def __init__(self):
        """Set database link and set last week data into database"""
        self.db = memcache.Client(["127.0.0.1:11211"])
        self.db.set("graph", self.getLastWeekData())
        #TODO: utiliser un fonction pour récupérer chacun des état
        self.db.set("status", {"doorIsOpen": False})
        
    def updateGraph(self, value):
        time = int(time())
        self.updateGraphMC(value, time)
        self.updateGraphFile(value, time)

    def updateGraphMC(self, value, time):
        last6Days = self.db.get(key)[1:]
        # Append today
        last6Days.append([time, value])
        self.db.set("graph", last6Days)

    def updateGraphFile(self, value, time):
        with open("graph.csv", "a") as file:
            writer = csv.writer(file)
            writer.writerow([time, value])

    def tsToWeekday(self, timestamp):
        if timestamp == 0:
            return "None"
        weekdays = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]
        print(type(timestamp))
        nbOfWeekday = datetime.fromtimestamp(timestamp).isoweekday() - 1
        return weekdays[nbOfWeekday]

    def getLastWeekData(self):
        lastWeek = []

        try:
            with open("graph.csv", "r") as file:
                reader = csv.reader(file)
                allData = [ [int(ts), int(egg)] for ts, egg in reader]
                lastWeek.extend(allData[-7:])
        except FileNotFoundError:
            # Create file
            with open("graph.csv", "w") as file:
                file.write("0, 0")

        # if can't get last 7 days, fill with 0
        while len(lastWeek) < 7:
            lastWeek.insert(0, [0, 0])
        
        # Convert timestamp to weekday before return
        return [ [self.tsToWeekday(time), eggs] for time, eggs in lastWeek]


if __name__ == "__main__":
    graph = DataManager()
