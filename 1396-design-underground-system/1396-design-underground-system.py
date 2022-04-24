class UndergroundSystem:

    def __init__(self):
        self.passengers = collections.defaultdict(list)
        self.stations = collections.defaultdict(list)
        
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.passengers[id].append((stationName, t))

    def checkOut(self, id: int, endStation: str, endTime: int) -> None:
        (startStation, startTime) = self.passengers[id][0]
        del self.passengers[id]
        totalTime = endTime - startTime
        flag = False
        endStations = self.stations[startStation]
        for i in range(len(endStations)):
             
            if endStations[i][0] == endStation:
                # update
                endStations[i] = (endStations[i][0], endStations[i][1] + totalTime, endStations[i][2] + 1)
                flag = True
             
        if not flag:
            self.stations[startStation].append((endStation, totalTime, 1))
            
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        endStations = self.stations[startStation]
        for i in range(len(endStations)):
            if endStations[i][0] == endStation:
                (_, totalTime, totalPassengers) = endStations[i]
        return totalTime / totalPassengers

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)